/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2011 Centre Tecnologic de Telecomunicacions de Catalunya (CTTC)
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
 * Author: Jaume Nin <jnin@cttc.cat>
 *         Nicola Baldo <nbaldo@cttc.cat>
 */


#include <ns3/tap-epc-enb-application.h>
#include <ns3/log.h>
#include <ns3/mac48-address.h>
#include <ns3/ipv4.h>
#include <ns3/inet-socket-address.h>
#include <ns3/uinteger.h>

#include <ns3/epc-gtpu-header.h>
#include <ns3/eps-bearer-tag.h>

namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("TapEpcEnbApplication");

TapEpcEnbApplication::EpsFlowId_t::EpsFlowId_t ()
{
}

TapEpcEnbApplication::EpsFlowId_t::EpsFlowId_t (const uint16_t a, const uint8_t b)
  : m_rnti (a),
    m_bid (b)
{
}

bool
operator == (const TapEpcEnbApplication::EpsFlowId_t &a, const TapEpcEnbApplication::EpsFlowId_t &b)
{
  return ( (a.m_rnti == b.m_rnti) && (a.m_bid == b.m_bid) );
}

bool
operator < (const TapEpcEnbApplication::EpsFlowId_t& a, const TapEpcEnbApplication::EpsFlowId_t& b)
{
  return ( (a.m_rnti < b.m_rnti) || ( (a.m_rnti == b.m_rnti) && (a.m_bid < b.m_bid) ) );
}

TypeId
TapEpcEnbApplication::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::TapEpcEnbApplication")
    .SetParent<Object> ();
  return tid;
}

void
TapEpcEnbApplication::DoDispose (void)
{
  NS_LOG_FUNCTION (this);
  m_lteSocket = 0;
  m_s1uSocket = 0;
  m_s1apSocket = 0;
  delete m_s1SapProvider;
  delete m_s1apSapEnb;
}

TapEpcEnbApplication::TapEpcEnbApplication (Ptr<Socket> lteSocket, Ptr<Socket> s1uSocket, Ptr<Socket> s1apSocket, Ipv4Address enbS1uAddress, Ipv4Address sgwS1uAddress, uint16_t cellId)
  : m_lteSocket (lteSocket),
    m_s1uSocket (s1uSocket),
    m_s1apSocket (s1apSocket),
    m_enbS1uAddress (enbS1uAddress),
    m_sgwS1uAddress (sgwS1uAddress),
    m_gtpuUdpPort (2152), // fixed by the standard
    m_s1SapUser (0),
    m_cellId (cellId)
{
  NS_LOG_FUNCTION (this << lteSocket << s1uSocket << sgwS1uAddress);
  m_s1uSocket->SetRecvCallback (MakeCallback (&TapEpcEnbApplication::RecvFromS1uSocket, this));
  m_lteSocket->SetRecvCallback (MakeCallback (&TapEpcEnbApplication::RecvFromLteSocket, this));
  m_s1apSocket->SetRecvCallback (MakeCallback (&TapEpcEnbApplication::RecvFromS1apSocket, this));
  m_s1SapProvider = new MemberEpcEnbS1SapProvider<TapEpcEnbApplication> (this);
  m_s1apSapEnb = new MemberEpcS1apSapEnb<TapEpcEnbApplication> (this);
}

TapEpcEnbApplication::~TapEpcEnbApplication (void)
{
  NS_LOG_FUNCTION (this);
}

void 
TapEpcEnbApplication::SetS1SapUser (EpcEnbS1SapUser * s)
{
  m_s1SapUser = s;
}

EpcEnbS1SapProvider* 
TapEpcEnbApplication::GetS1SapProvider ()
{
  return m_s1SapProvider;
}

EpcS1apSapEnb* 
TapEpcEnbApplication::GetS1apSapEnb ()
{
  return m_s1apSapEnb;
}

void 
TapEpcEnbApplication::DoInitialUeMessage (uint64_t imsi, uint16_t rnti)
{
  NS_LOG_FUNCTION (this);
  // side effect: create entry if not exist
  m_imsiRntiMap[imsi] = rnti;
  
  EpcS1apHeader epcS1apHeader;
  epcS1apHeader.SetProcedureCode (EpcS1apHeader::InitialUeMessage);
  epcS1apHeader.SetTypeOfMessage (EpcS1apHeader::InitiatingMessage);
  
  InitialUeRequestHeader initialUeRequestHeader;
  initialUeRequestHeader.SetMmeUeS1Id (imsi);
  initialUeRequestHeader.SetEnbUeS1Id (rnti);
  initialUeRequestHeader.SetStmsi (imsi);
  initialUeRequestHeader.SetEcgi (m_cellId);
  
  Ptr<Packet> packet = Create<Packet> ();
  packet->AddHeader (initialUeRequestHeader);
  packet->AddHeader (epcS1apHeader);
  SendToS1apSocket (packet);
}

void 
TapEpcEnbApplication::DoPathSwitchRequest (EpcEnbS1SapProvider::PathSwitchRequestParameters params)
{
  NS_LOG_FUNCTION (this);
  uint16_t enbUeS1Id = params.rnti;  
  uint64_t mmeUeS1Id = params.mmeUeS1Id;
  uint64_t imsi = mmeUeS1Id;
  // side effect: create entry if not exist
  m_imsiRntiMap[imsi] = params.rnti;

  uint16_t cgi = params.cellId;
  std::list<EpcS1apSapMme::ErabSwitchedInDownlinkItem> erabToBeSwitchedInDownlinkList;
  for (std::list<EpcEnbS1SapProvider::BearerToBeSwitched>::iterator bit = params.bearersToBeSwitched.begin ();
       bit != params.bearersToBeSwitched.end ();
       ++bit)
    {
      EpsFlowId_t flowId;
      flowId.m_rnti = params.rnti;
      flowId.m_bid = bit->epsBearerId;
      uint32_t teid = bit->teid;
      
      EpsFlowId_t rbid (params.rnti, bit->epsBearerId);
      // side effect: create entries if not exist
      m_rbidTeidMap[params.rnti][bit->epsBearerId] = teid;
      m_teidRbidMap[teid] = rbid;

      EpcS1apSapMme::ErabSwitchedInDownlinkItem erab;
      erab.erabId = bit->epsBearerId;
      erab.enbTransportLayerAddress = m_enbS1uAddress;
      erab.enbTeid = bit->teid;

      erabToBeSwitchedInDownlinkList.push_back (erab);
    }
    
  EpcS1apHeader epcS1apHeader;
  epcS1apHeader.SetProcedureCode (EpcS1apHeader::PathSwitchRequest);
  epcS1apHeader.SetTypeOfMessage (EpcS1apHeader::InitiatingMessage);
  
  PathSwitchRequestHeader pathSwitchRequestHeader;
  pathSwitchRequestHeader.SetMmeUeS1Id (mmeUeS1Id);
  pathSwitchRequestHeader.SetEnbUeS1Id (enbUeS1Id);
  pathSwitchRequestHeader.SetCgi (cgi);
  pathSwitchRequestHeader.SetErabToBeSwitchedInDownlinkList (erabToBeSwitchedInDownlinkList);
  
  Ptr<Packet> packet = Create<Packet> ();
  packet->AddHeader (pathSwitchRequestHeader);
  packet->AddHeader (epcS1apHeader);
  SendToS1apSocket (packet);
}

void 
TapEpcEnbApplication::DoUeContextRelease (uint16_t rnti)
{
  NS_LOG_FUNCTION (this << rnti);
  std::map<uint16_t, std::map<uint8_t, uint32_t> >::iterator rntiIt = m_rbidTeidMap.find (rnti);
  if (rntiIt != m_rbidTeidMap.end ())
    {
      for (std::map<uint8_t, uint32_t>::iterator bidIt = rntiIt->second.begin ();
           bidIt != rntiIt->second.end ();
           ++bidIt)
        {
          uint32_t teid = bidIt->second;
          m_teidRbidMap.erase (teid);
        }
      m_rbidTeidMap.erase (rntiIt);
    }
}

void 
TapEpcEnbApplication::DoInitialContextSetupRequest (uint64_t mmeUeS1Id, uint16_t enbUeS1Id, std::list<EpcS1apSapEnb::ErabToBeSetupItem> erabToBeSetupList)
{
  NS_LOG_FUNCTION (this);
  
  for (std::list<EpcS1apSapEnb::ErabToBeSetupItem>::iterator erabIt = erabToBeSetupList.begin ();
       erabIt != erabToBeSetupList.end ();
       ++erabIt)
    {
      // request the RRC to setup a radio bearer

      uint64_t imsi = mmeUeS1Id;
      std::map<uint64_t, uint16_t>::iterator imsiIt = m_imsiRntiMap.find (imsi);
      NS_ASSERT_MSG (imsiIt != m_imsiRntiMap.end (), "unknown IMSI");
      uint16_t rnti = imsiIt->second;
      
      struct EpcEnbS1SapUser::DataRadioBearerSetupRequestParameters params;
      params.rnti = rnti;
      params.bearer = erabIt->erabLevelQosParameters;
      params.bearerId = erabIt->erabId;
      params.gtpTeid = erabIt->sgwTeid;
      m_s1SapUser->DataRadioBearerSetupRequest (params);

      EpsFlowId_t rbid (rnti, erabIt->erabId);
      // side effect: create entries if not exist
      m_rbidTeidMap[rnti][erabIt->erabId] = params.gtpTeid;
      m_teidRbidMap[params.gtpTeid] = rbid;
    }
}

void 
TapEpcEnbApplication::DoPathSwitchRequestAcknowledge (uint64_t enbUeS1Id, uint64_t mmeUeS1Id, uint16_t cgi, std::list<EpcS1apSapEnb::ErabSwitchedInUplinkItem> erabToBeSwitchedInUplinkList)
{
  NS_LOG_FUNCTION (this);

  uint64_t imsi = mmeUeS1Id;
  std::map<uint64_t, uint16_t>::iterator imsiIt = m_imsiRntiMap.find (imsi);
  NS_ASSERT_MSG (imsiIt != m_imsiRntiMap.end (), "unknown IMSI");
  uint16_t rnti = imsiIt->second;
  EpcEnbS1SapUser::PathSwitchRequestAcknowledgeParameters params;
  params.rnti = rnti;
  
  m_s1SapUser->PathSwitchRequestAcknowledge (params);
}

void 
TapEpcEnbApplication::RecvFromLteSocket (Ptr<Socket> socket)
{
  NS_LOG_FUNCTION (this);  
  NS_ASSERT (socket == m_lteSocket);
  Ptr<Packet> packet = socket->Recv ();

  /// \internal
  /// Workaround for \bugid{231}
  SocketAddressTag satag;
  packet->RemovePacketTag (satag);

  EpsBearerTag tag;
  bool found = packet->RemovePacketTag (tag);
  NS_ASSERT (found);
  uint16_t rnti = tag.GetRnti ();
  uint8_t bid = tag.GetBid ();
  NS_LOG_LOGIC ("received packet with RNTI=" << (uint32_t) rnti << ", BID=" << (uint32_t)  bid);
  std::map<uint16_t, std::map<uint8_t, uint32_t> >::iterator rntiIt = m_rbidTeidMap.find (rnti);
  if (rntiIt == m_rbidTeidMap.end ())
    {
      NS_LOG_WARN ("UE context not found, discarding packet");
    }
  else
    {
      std::map<uint8_t, uint32_t>::iterator bidIt = rntiIt->second.find (bid);
      NS_ASSERT (bidIt != rntiIt->second.end ());
      uint32_t teid = bidIt->second;
      SendToS1uSocket (packet, teid);
    }
}

void 
TapEpcEnbApplication::RecvFromS1uSocket (Ptr<Socket> socket)
{
  NS_LOG_FUNCTION (this << socket);  
  NS_ASSERT (socket == m_s1uSocket);
  Ptr<Packet> packet = socket->Recv ();
  GtpuHeader gtpu;
  packet->RemoveHeader (gtpu);
  uint32_t teid = gtpu.GetTeid ();
  std::map<uint32_t, EpsFlowId_t>::iterator it = m_teidRbidMap.find (teid);
  NS_ASSERT (it != m_teidRbidMap.end ());

  /// \internal
  /// Workaround for \bugid{231}
  SocketAddressTag tag;
  packet->RemovePacketTag (tag);
  
  SendToLteSocket (packet, it->second.m_rnti, it->second.m_bid);
}

void
TapEpcEnbApplication::RecvFromS1apSocket (Ptr<Socket> socket)
{
  NS_LOG_FUNCTION (this);
  NS_ASSERT (socket == m_s1apSocket);
  Ptr<Packet> packet = socket->Recv ();
  NS_LOG_LOGIC ("Packet size = " << packet->GetSize ());
  HandleS1apPacket (socket, packet);
}

void
TapEpcEnbApplication::HandleS1apPacket (Ptr<Socket> socket, Ptr<Packet> packet)
{
  EpcS1apHeader epcS1apHeader;
  packet->RemoveHeader (epcS1apHeader);
  
  uint8_t procedureCode = epcS1apHeader.GetProcedureCode ();
  uint8_t typeOfMessage = epcS1apHeader.GetTypeOfMessage ();
  
  if (procedureCode == EpcS1apHeader::InitialContextSetup)
    {
      if (typeOfMessage == EpcS1apHeader::InitiatingMessage)
        {
          NS_LOG_LOGIC ("InitialContextSetup");
          InitialContextSetupRequestHeader initialContextSetupRequestHeader;
          packet->RemoveHeader (initialContextSetupRequestHeader);
          
          uint64_t mmeUeS1Id = initialContextSetupRequestHeader.GetMmeUeS1Id ();
          uint16_t enbUeS1Id = initialContextSetupRequestHeader.GetEnbUeS1Id ();
          std::list<EpcS1apSapEnb::ErabToBeSetupItem> erabToBeSetupList;
          erabToBeSetupList = initialContextSetupRequestHeader.GetErabToBeSetupList ();
          DoInitialContextSetupRequest (mmeUeS1Id, enbUeS1Id, erabToBeSetupList);
        }
    }
  else if (procedureCode == EpcS1apHeader::PathSwitchRequest)
    {
      if (typeOfMessage == EpcS1apHeader::SuccessfulOutcome)
        {
          NS_LOG_LOGIC ("PathSwitchRequest");
          PathSwitchRequestAcknowledgeHeader pathSwitchRequestAcknowledgeHeader;
          packet->RemoveHeader (pathSwitchRequestAcknowledgeHeader);
          
          uint64_t mmeUeS1Id = pathSwitchRequestAcknowledgeHeader.GetMmeUeS1Id ();
          uint16_t enbUeS1Id = pathSwitchRequestAcknowledgeHeader.GetEnbUeS1Id ();
          uint16_t cgi = pathSwitchRequestAcknowledgeHeader.GetCgi ();
          std::list<EpcS1apSapEnb::ErabSwitchedInUplinkItem> erabToBeSwitchedInUplinkList;
          erabToBeSwitchedInUplinkList = pathSwitchRequestAcknowledgeHeader.GetErabToBeSwitchedInUplinkList ();
          
          DoPathSwitchRequestAcknowledge (enbUeS1Id, mmeUeS1Id, cgi, erabToBeSwitchedInUplinkList);
        }
    }
    
  if (packet->GetSize () != 0)
    {
      HandleS1apPacket (socket, packet);
    }
}

void 
TapEpcEnbApplication::SendToLteSocket (Ptr<Packet> packet, uint16_t rnti, uint8_t bid)
{
  NS_LOG_FUNCTION (this << packet << rnti << (uint16_t) bid << packet->GetSize ());  
  EpsBearerTag tag (rnti, bid);
  packet->AddPacketTag (tag);
  int sentBytes = m_lteSocket->Send (packet);
  NS_ASSERT (sentBytes > 0);
}

void 
TapEpcEnbApplication::SendToS1uSocket (Ptr<Packet> packet, uint32_t teid)
{
  NS_LOG_FUNCTION (this << packet << teid <<  packet->GetSize ());  
  GtpuHeader gtpu;
  gtpu.SetTeid (teid);
  // From 3GPP TS 29.281 v10.0.0 Section 5.1
  // Length of the payload + the non obligatory GTP-U header
  gtpu.SetLength (packet->GetSize () + gtpu.GetSerializedSize () - 8);  
  packet->AddHeader (gtpu);
  uint32_t flags = 0;
  m_s1uSocket->SendTo (packet, flags, InetSocketAddress (m_sgwS1uAddress, m_gtpuUdpPort));
}

void
TapEpcEnbApplication::SendToS1apSocket (Ptr<Packet> packet)
{
  NS_LOG_FUNCTION (this);
  m_s1apSocket->Send (packet);
}

void
TapEpcEnbApplication::DoReleaseIndication (uint64_t imsi, uint16_t rnti, uint8_t bearerId)
{
  NS_LOG_FUNCTION (this << bearerId );
  std::list<EpcS1apSapMme::ErabToBeReleasedIndication> erabToBeReleaseIndication;
  EpcS1apSapMme::ErabToBeReleasedIndication erab;
  erab.erabId = bearerId;
  erabToBeReleaseIndication.push_back (erab);
  //From 3GPP TS 23401-950 Section 5.4.4.2, enB sends EPS bearer Identity in Bearer Release Indication message to MME

  EpcS1apHeader epcS1apHeader;
  epcS1apHeader.SetProcedureCode (EpcS1apHeader::ErabRelease);
  epcS1apHeader.SetTypeOfMessage (EpcS1apHeader::InitiatingMessage);
  
  ErabReleaseIndicationHeader erabReleaseIndicationHeader;
  erabReleaseIndicationHeader.SetMmeUeS1Id (imsi);
  erabReleaseIndicationHeader.SetEnbUeS1Id (rnti);
  erabReleaseIndicationHeader.SetErabToBeReleaseIndication (erabToBeReleaseIndication);
  
  Ptr<Packet> packet = Create<Packet> ();
  packet->AddHeader (erabReleaseIndicationHeader);
  packet->AddHeader (epcS1apHeader);
  SendToS1apSocket (packet);
}

}  // namespace ns3
