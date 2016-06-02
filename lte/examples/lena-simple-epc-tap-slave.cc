/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2011, 2013 Centre Tecnologic de Telecomunicacions de Catalunya (CTTC)
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Author: Jaume Nin <jaume.nin@cttc.cat>
 *         Nicola Baldo <nbaldo@cttc.cat>
 */

#include "ns3/lte-helper.h"
#include "ns3/epc-helper.h"
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/ipv4-global-routing-helper.h"
#include "ns3/internet-module.h"
#include "ns3/mobility-module.h"
#include "ns3/lte-module.h"
#include "ns3/applications-module.h"
#include "ns3/point-to-point-helper.h"
#include "ns3/config-store-module.h"
#include "ns3/tap-fd-net-device-helper.h"
#include "ns3/tap-bridge-module.h"
#include "ns3/lte-time-dilation-factor.h"

using namespace ns3;

/*
 * Simple simulation program using the emulated EPC.
 * For the LTE radio part, it simulates a simple linear topology with
 * a fixed number of eNBs spaced at equal distance, and a fixed number
 * of UEs per each eNB, located at the same position of the eNB. 
 * For the EPC, it uses TapEpcHelper to realize the S1-U connection
 * via a real link. 
 */

NS_LOG_COMPONENT_DEFINE ("EpcTapExample");

int
main (int argc, char *argv[])
{
  uint16_t nEnbs = 1;
  uint16_t nUesPerEnb = 1;
  double simTime = 3600.1;
  double distance = 1000.0;
  uint16_t imsiBase = 0;
  uint16_t cellIdBase = 0;

  // Command line arguments
  CommandLine cmd;
  cmd.AddValue("nEnbs", "Number of eNBs", nEnbs);
  cmd.AddValue("nUesPerEnb", "Number of UEs per eNB", nUesPerEnb);
  cmd.AddValue("simTime", "Total duration of the simulation [s]", simTime);
  cmd.AddValue("distance", "Distance between eNBs [m]", distance);
  cmd.AddValue("imsiBase", "Base number of IMSI", imsiBase);
  cmd.AddValue("cellIdBase", "Base number of CellId", cellIdBase);
  cmd.Parse(argc, argv);

  // let's go in real time
  // NOTE: if you go in real time I strongly advise to use
  // --ns3::RealtimeSimulatorImpl::SynchronizationMode=HardLimit
  // I've seen that if BestEffort is used things can break
  // (even simple stuff such as ARP)
  GlobalValue::Bind ("SimulatorImplementationType", StringValue ("ns3::RealtimeSimulatorImpl"));
  GlobalValue::Bind ("ChecksumEnabled", BooleanValue (true));

  // let's speed things up, we don't need these details for this scenario
  Config::SetDefault ("ns3::LteSpectrumPhy::CtrlErrorModelEnabled", BooleanValue (false));
  Config::SetDefault ("ns3::LteSpectrumPhy::DataErrorModelEnabled", BooleanValue (false));

  LteTimeDilationFactor::SetTimeDilationFactor (100);

  ConfigStore inputConfig;
  inputConfig.ConfigureDefaults();

  // parse again so you can override default values from the command line
  cmd.Parse(argc, argv);

  Ptr<LteHelper> lteHelper = CreateObject<LteHelper> ();
  lteHelper->SetImsiCounter (imsiBase);
  lteHelper->SetCellIdCounter (cellIdBase);
  
  Ptr<TapEpcHelper> epcHelper = CreateObject<TapEpcHelper> ();
  lteHelper->SetEpcHelper (epcHelper);
  epcHelper->Initialize ();

  Ptr<Node> pgw = epcHelper->GetPgwNode ();

  NodeContainer ueNodes;
  NodeContainer enbNodes;
  enbNodes.Create(nEnbs);
  ueNodes.Create(nEnbs*nUesPerEnb);

  // Install Mobility Model
  Ptr<ListPositionAllocator> positionAlloc = CreateObject<ListPositionAllocator> ();
  for (uint16_t i = 0; i < nEnbs; i++)
    {
      positionAlloc->Add (Vector(distance * i, 0, 0));
    }
  MobilityHelper mobility;
  mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
  mobility.SetPositionAllocator(positionAlloc);
  mobility.Install(enbNodes);
  mobility.Install(ueNodes);

  // Install LTE Devices to the nodes
  NetDeviceContainer enbLteDevs = lteHelper->InstallEnbDevice (enbNodes);
  NetDeviceContainer ueLteDevs = lteHelper->InstallUeDevice (ueNodes);

  // Install the IP stack on the UEs
  InternetStackHelper internet;
  internet.SetIpv6StackInstall (false);
  internet.Install (ueNodes);

  // Assign IP address to UEs, and install applications
  Ipv4InterfaceContainer ueIpIface;
  ueIpIface = epcHelper->AssignUeIpv4Address (NetDeviceContainer (ueLteDevs));

  // lteHelper->Attach (ueLteDevs);
  Simulator::Schedule (Seconds ((nEnbs * nUesPerEnb + nEnbs) * 0.1), static_cast<void (LteHelper::*)(NetDeviceContainer)>(&LteHelper::Attach), lteHelper, ueLteDevs);
  // side effects: 1) use idle mode cell selection, 2) activate default EPS bearer

  // Add TapBridge on UE
  TapBridgeHelper tapBridge;
  tapBridge.SetAttribute ("Mode", StringValue ("ConfigureLocal"));
  for (uint32_t u = 0; u < ueLteDevs.GetN (); ++u)
    {
      std::ostringstream oss;
      oss << "h" << u + 1 + imsiBase << "-eth0";
      tapBridge.SetAttribute ("DeviceName", StringValue (oss.str ()));
      Address macAddress = Mac48Address::Allocate ();
      tapBridge.SetAttribute ("MacAddress", Mac48AddressValue (Mac48Address::ConvertFrom (macAddress)));
      NS_LOG_LOGIC ("TapBridge DeviceName: " << oss.str ());
      tapBridge.Install (ueNodes.Get (u), ueLteDevs.Get (u));

      Ptr<NetDevice> netDev = ueLteDevs.Get (u);
      Ptr<LteUeNetDevice> dev = netDev->GetObject<LteUeNetDevice> ();
      dev->SetMacAddress (macAddress);
      dev->SetGatewayMacAddress (epcHelper->GetUeDefaultGatewayMacAddress ());
    }
    
  Simulator::Stop(Seconds(simTime));
  Simulator::Run();

  Simulator::Destroy();
  return 0;
}

