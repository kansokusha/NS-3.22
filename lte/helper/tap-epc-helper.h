/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2011-2013 Centre Tecnologic de Telecomunicacions de Catalunya (CTTC)
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
 * Author: Jaume Nin <jnin@cttc.es>
 *         Nicola Baldo <nbaldo@cttc.es>
 *         Manuel Requena <manuel.requena@cttc.es>
 */

#ifndef TAP_EPC_HELPER_H
#define TAP_EPC_HELPER_H

#include <ns3/object.h>
#include <ns3/ipv4-address-helper.h>
#include <ns3/data-rate.h>
#include <ns3/epc-tft.h>
#include <ns3/eps-bearer.h>
#include <ns3/epc-helper.h>
#include <ns3/emu-epc-helper.h>
#include <ns3/header.h>
#include <ns3/system-condition.h>

namespace ns3 {

class Node;
class NetDevice;
class VirtualNetDevice;
class EpcSgwPgwApplication;
class EpcX2;
class TapEpcMme;

/**
 * \ingroup lte
 *
 * \brief Create an EPC network using TapFdNetDevice 
 *
 * This Helper will create an EPC network topology comprising of a
 * single node that implements both the SGW and PGW functionality, and
 * an MME node. The S1-U, X2-U and X2-C interfaces are realized using
 * TapFdNetDevice; in particular, one device is used to send all the
 * traffic related to these interfaces. 
 */
class TapEpcHelper : public EpcHelper
{
public:
  
  /** 
   * Constructor
   */
  TapEpcHelper ();

  /** 
   * Destructor
   */  
  virtual ~TapEpcHelper ();
  
  // inherited from Object
  /**
   *  Register this type.
   *  \return The object TypeId.
   */
  static TypeId GetTypeId (void);
  virtual void DoInitialize ();
  virtual void DoDispose ();

  // inherited from EpcHelper
  virtual void AddEnb (Ptr<Node> enbNode, Ptr<NetDevice> lteEnbNetDevice, uint16_t cellId);
  virtual void AddUe (Ptr<NetDevice> ueLteDevice, uint64_t imsi);
  virtual void AddX2Interface (Ptr<Node> enbNode1, Ptr<Node> enbNode2);
  virtual uint8_t ActivateEpsBearer (Ptr<NetDevice> ueLteDevice, uint64_t imsi, Ptr<EpcTft> tft, EpsBearer bearer);
  virtual Ptr<Node> GetPgwNode ();
  virtual Ipv4InterfaceContainer AssignUeIpv4Address (NetDeviceContainer ueDevices);
  virtual Ipv4Address GetUeDefaultGatewayAddress ();
  virtual Mac48Address GetUeDefaultGatewayMacAddress ();
  
  enum Mode
  {
    Master,
    Slave
  };
  
  void SetMode (TapEpcHelper::Mode mode);

private:

  void HandleS1apConnection (Ptr<Socket> socket, const Address &addr);
  void HandleEpcMasterConnection (Ptr<Socket> socket, const Address &addr);
  
  void RecvFromS1apSocket (Ptr<Socket> socket);
  void RecvFromEpcMasterSocket (Ptr<Socket> socket);
  void RecvFromEpcSlaveSocket (Ptr<Socket> socket);
  
  void HandleEpcMasterPacket (Ptr<Socket> socket, Ptr<Packet> packet);
  
  void MasterInitialize ();
  void SlaveInitialize ();
  
  Mac48Address AllocateMac48Address ();

  /** 
   * helper to assign addresses to UE devices as well as to the TUN device of the SGW/PGW
   */
  Ipv4AddressHelper m_ueAddressHelper; 

  /**
   * SGW-PGW network element
   */  
  Ptr<Node> m_sgwPgw;
  
  Ptr<Node> m_mmeNode;
  
  Ptr<Node> m_epcMaster;
  
  Ptr<Node> m_epcSlave;

  /**
   * SGW-PGW application
   */
  Ptr<EpcSgwPgwApplication> m_sgwPgwApp;

  /**
   * TUN device implementing tunneling of user data over GTP-U/UDP/IP
   */
  Ptr<VirtualNetDevice> m_tunDevice;

  /**
   * MME network element
   */
  Ptr<TapEpcMme> m_mme;
  
  Ptr<Socket> m_epcSlaveSocket;

  /** 
   * helper to assign addresses to S1-U NetDevices 
   */
  Ipv4AddressHelper m_epcIpv4AddressHelper; 

  /**
   * UDP port where the GTP-U Socket is bound, fixed by the standard as 2152
   */
  uint16_t m_gtpuUdpPort;
  
  uint16_t m_s1apTcpPort;
  
  uint16_t m_epcMasterTcpPort;

  /**
   * Map storing for each IMSI the corresponding eNB NetDevice
   * 
   */
  std::map<uint64_t, Ptr<NetDevice> > m_imsiEnbDeviceMap;
  
  Ipv4Address m_sgwIpv4Address;
  Ipv4Address m_mmeIpv4Address;
  Ipv4Address m_epcMasterIpv4Address;
  Ipv4Address m_epcSlaveIpv4Address;

  /**
   * The name of the device used for the S1-U interface of the SGW
   */
  std::string m_sgwDeviceName;

  /**
   * The name of the device used for the S1-U interface of the eNB
   */
  std::string m_enbDeviceName;
  
  std::string m_mmeDeviceName;
  std::string m_epcMasterDeviceName;
  std::string m_epcSlaveDeviceName;

  /**
   * The count of eNB
   */
  uint16_t m_enbCount;
  
  std::string m_masterUeIpAddressBase;
  std::string m_slaveUeIpAddressBase;
  
  std::string m_masterIpAddressBase;
  std::string m_slaveIpAddressBase;
  
  uint64_t m_mac48AddressBase;
  
  Mode m_mode;

  Address m_ueDefaultGatewayMacAddress;
  Ipv4Address m_ueDefaultGatewayAddress;

  // SystemCondition m_epcSlaveSocketCondition;
  
  std::vector<EpcTft> tftContainer;
};

} // namespace ns3

#endif // TAP_EPC_HELPER_H