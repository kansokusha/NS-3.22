from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('ns.netanim', cpp_namespace='::ns3')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    ## ff-mac-common.h (module 'lte'): ns3::Result_e [enumeration]
    module.add_enum('Result_e', ['SUCCESS', 'FAILURE'], import_from_module='ns.lte')
    ## log.h (module 'core'): ns3::LogLevel [enumeration]
    module.add_enum('LogLevel', ['LOG_NONE', 'LOG_ERROR', 'LOG_LEVEL_ERROR', 'LOG_WARN', 'LOG_LEVEL_WARN', 'LOG_DEBUG', 'LOG_LEVEL_DEBUG', 'LOG_INFO', 'LOG_LEVEL_INFO', 'LOG_FUNCTION', 'LOG_LEVEL_FUNCTION', 'LOG_LOGIC', 'LOG_LEVEL_LOGIC', 'LOG_ALL', 'LOG_LEVEL_ALL', 'LOG_PREFIX_FUNC', 'LOG_PREFIX_TIME', 'LOG_PREFIX_NODE', 'LOG_PREFIX_LEVEL', 'LOG_PREFIX_ALL'], import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::SetupRelease_e [enumeration]
    module.add_enum('SetupRelease_e', ['setup', 'release'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::CeBitmap_e [enumeration]
    module.add_enum('CeBitmap_e', ['TA', 'DRX', 'CR'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::NormalExtended_e [enumeration]
    module.add_enum('NormalExtended_e', ['normal', 'extended'], import_from_module='ns.lte')
    ## address.h (module 'network'): ns3::Address [class]
    module.add_class('Address', import_from_module='ns.network')
    ## address.h (module 'network'): ns3::Address::MaxSize_e [enumeration]
    module.add_enum('MaxSize_e', ['MAX_SIZE'], outer_class=root_module['ns3::Address'], import_from_module='ns.network')
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority [struct]
    module.add_class('AllocationRetentionPriority', import_from_module='ns.lte')
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface [class]
    module.add_class('AnimationInterface')
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface::CounterType [enumeration]
    module.add_enum('CounterType', ['UINT32_COUNTER', 'DOUBLE_COUNTER'], outer_class=root_module['ns3::AnimationInterface'])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList [class]
    module.add_class('AttributeConstructionList', import_from_module='ns.core')
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item [struct]
    module.add_class('Item', import_from_module='ns.core', outer_class=root_module['ns3::AttributeConstructionList'])
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo [struct]
    module.add_class('BandInfo', import_from_module='ns.spectrum')
    ## buffer.h (module 'network'): ns3::Buffer [class]
    module.add_class('Buffer', import_from_module='ns.network')
    ## buffer.h (module 'network'): ns3::Buffer::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::Buffer'])
    ## lte-common.h (module 'lte'): ns3::BufferSizeLevelBsr [class]
    module.add_class('BufferSizeLevelBsr', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s [struct]
    module.add_class('BuildBroadcastListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::Type_e [enumeration]
    module.add_enum('Type_e', ['BCCH', 'PCCH'], outer_class=root_module['ns3::BuildBroadcastListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s [struct]
    module.add_class('BuildDataListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s [struct]
    module.add_class('BuildRarListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s [struct]
    module.add_class('BwPart_s', import_from_module='ns.lte')
    ## packet.h (module 'network'): ns3::ByteTagIterator [class]
    module.add_class('ByteTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagIterator'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList [class]
    module.add_class('ByteTagList', import_from_module='ns.network')
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList::Iterator'])
    ## callback.h (module 'core'): ns3::CallbackBase [class]
    module.add_class('CallbackBase', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s [struct]
    module.add_class('CqiConfig_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s [struct]
    module.add_class('CqiListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::CqiType_e [enumeration]
    module.add_enum('CqiType_e', ['P10', 'P11', 'P20', 'P21', 'A12', 'A22', 'A20', 'A30', 'A31'], outer_class=root_module['ns3::CqiListElement_s'], import_from_module='ns.lte')
    ## data-rate.h (module 'network'): ns3::DataRate [class]
    module.add_class('DataRate', import_from_module='ns.network')
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s [struct]
    module.add_class('DlDciListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::Format_e [enumeration]
    module.add_enum('Format_e', ['ONE', 'ONE_A', 'ONE_B', 'ONE_C', 'ONE_D', 'TWO', 'TWO_A', 'TWO_B'], outer_class=root_module['ns3::DlDciListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::VrbFormat_e [enumeration]
    module.add_enum('VrbFormat_e', ['VRB_DISTRIBUTED', 'VRB_LOCALIZED'], outer_class=root_module['ns3::DlDciListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::Ngap_e [enumeration]
    module.add_enum('Ngap_e', ['GAP1', 'GAP2'], outer_class=root_module['ns3::DlDciListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s [struct]
    module.add_class('DlInfoListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::HarqStatus_e [enumeration]
    module.add_enum('HarqStatus_e', ['ACK', 'NACK', 'DTX'], outer_class=root_module['ns3::DlInfoListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s [struct]
    module.add_class('DrxConfig_s', import_from_module='ns.lte')
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer [struct]
    module.add_class('EpsBearer', import_from_module='ns.lte')
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::Qci [enumeration]
    module.add_enum('Qci', ['GBR_CONV_VOICE', 'GBR_CONV_VIDEO', 'GBR_GAMING', 'GBR_NON_CONV_VIDEO', 'NGBR_IMS', 'NGBR_VIDEO_TCP_OPERATOR', 'NGBR_VOICE_VIDEO_GAMING', 'NGBR_VIDEO_TCP_PREMIUM', 'NGBR_VIDEO_TCP_DEFAULT'], outer_class=root_module['ns3::EpsBearer'], import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::EutranMeasurementMapping [class]
    module.add_class('EutranMeasurementMapping', import_from_module='ns.lte')
    ## event-id.h (module 'core'): ns3::EventId [class]
    module.add_class('EventId', import_from_module='ns.core')
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation [struct]
    module.add_class('GbrQosInformation', import_from_module='ns.lte')
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t [struct]
    module.add_class('HarqProcessInfoElement_t', import_from_module='ns.lte')
    ## hash.h (module 'core'): ns3::Hasher [class]
    module.add_class('Hasher', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::HigherLayerSelected_s [struct]
    module.add_class('HigherLayerSelected_s', import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t [struct]
    module.add_class('ImsiLcidPair_t', import_from_module='ns.lte')
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress [class]
    module.add_class('Inet6SocketAddress', import_from_module='ns.network')
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress [class]
    root_module['ns3::Inet6SocketAddress'].implicitly_converts_to(root_module['ns3::Address'])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress [class]
    module.add_class('InetSocketAddress', import_from_module='ns.network')
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress [class]
    root_module['ns3::InetSocketAddress'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    module.add_class('Ipv4Address', import_from_module='ns.network')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    root_module['ns3::Ipv4Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress [class]
    module.add_class('Ipv4InterfaceAddress', import_from_module='ns.internet')
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e [enumeration]
    module.add_enum('InterfaceAddressScope_e', ['HOST', 'LINK', 'GLOBAL'], outer_class=root_module['ns3::Ipv4InterfaceAddress'], import_from_module='ns.internet')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask [class]
    module.add_class('Ipv4Mask', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    module.add_class('Ipv6Address', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    root_module['ns3::Ipv6Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix [class]
    module.add_class('Ipv6Prefix', import_from_module='ns.network')
    ## log.h (module 'core'): ns3::LogComponent [class]
    module.add_class('LogComponent', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s [struct]
    module.add_class('LogicalChannelConfigListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::Direction_e [enumeration]
    module.add_enum('Direction_e', ['DIR_UL', 'DIR_DL', 'DIR_BOTH'], outer_class=root_module['ns3::LogicalChannelConfigListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::QosBearerType_e [enumeration]
    module.add_enum('QosBearerType_e', ['QBT_NON_GBR', 'QBT_GBR'], outer_class=root_module['ns3::LogicalChannelConfigListElement_s'], import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::LteFfConverter [class]
    module.add_class('LteFfConverter', import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t [struct]
    module.add_class('LteFlowId_t', import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap [class]
    module.add_class('LteRrcSap', import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestablishmentCause [enumeration]
    module.add_enum('ReestablishmentCause', ['RECONFIGURATION_FAILURE', 'HANDOVER_FAILURE', 'OTHER_FAILURE'], outer_class=root_module['ns3::LteRrcSap'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AntennaInfoDedicated [struct]
    module.add_class('AntennaInfoDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig [struct]
    module.add_class('AsConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::BlackCellsToAddMod [struct]
    module.add_class('BlackCellsToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierBandwidthEutra [struct]
    module.add_class('CarrierBandwidthEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierFreqEutra [struct]
    module.add_class('CarrierFreqEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo [struct]
    module.add_class('CellAccessRelatedInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellSelectionInfo [struct]
    module.add_class('CellSelectionInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod [struct]
    module.add_class('CellsToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo [struct]
    module.add_class('CgiInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod [struct]
    module.add_class('DrbToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::FreqInfo [struct]
    module.add_class('FreqInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::HandoverPreparationInfo [struct]
    module.add_class('HandoverPreparationInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig [struct]
    module.add_class('LogicalChannelConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock [struct]
    module.add_class('MasterInformationBlock', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig [struct]
    module.add_class('MeasConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig [struct]
    module.add_class('MeasGapConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig [enumeration]
    module.add_enum('', ['SETUP', 'RESET'], outer_class=root_module['ns3::LteRrcSap::MeasGapConfig'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig [enumeration]
    module.add_enum('', ['GP0', 'GP1'], outer_class=root_module['ns3::LteRrcSap::MeasGapConfig'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod [struct]
    module.add_class('MeasIdToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra [struct]
    module.add_class('MeasObjectEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectToAddMod [struct]
    module.add_class('MeasObjectToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra [struct]
    module.add_class('MeasResultEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults [struct]
    module.add_class('MeasResults', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasurementReport [struct]
    module.add_class('MeasurementReport', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo [struct]
    module.add_class('MobilityControlInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters [struct]
    module.add_class('MobilityStateParameters', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigCommon [struct]
    module.add_class('PdschConfigCommon', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigDedicated [struct]
    module.add_class('PdschConfigDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigDedicated [enumeration]
    module.add_enum('', ['dB_6', 'dB_4dot77', 'dB_3', 'dB_1dot77', 'dB0', 'dB1', 'dB2', 'dB3'], outer_class=root_module['ns3::LteRrcSap::PdschConfigDedicated'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange [struct]
    module.add_class('PhysCellIdRange', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated [struct]
    module.add_class('PhysicalConfigDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PlmnIdentityInfo [struct]
    module.add_class('PlmnIdentityInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PreambleInfo [struct]
    module.add_class('PreambleInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::QuantityConfig [struct]
    module.add_class('QuantityConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RaSupervisionInfo [struct]
    module.add_class('RaSupervisionInfo', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigCommon [struct]
    module.add_class('RachConfigCommon', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigDedicated [struct]
    module.add_class('RachConfigDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommon [struct]
    module.add_class('RadioResourceConfigCommon', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommonSib [struct]
    module.add_class('RadioResourceConfigCommonSib', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated [struct]
    module.add_class('RadioResourceConfigDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestabUeIdentity [struct]
    module.add_class('ReestabUeIdentity', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [struct]
    module.add_class('ReportConfigEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['EVENT', 'PERIODICAL'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['EVENT_A1', 'EVENT_A2', 'EVENT_A3', 'EVENT_A4', 'EVENT_A5'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['REPORT_STRONGEST_CELLS', 'REPORT_CGI'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['RSRP', 'RSRQ'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['SAME_AS_TRIGGER_QUANTITY', 'BOTH'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra [enumeration]
    module.add_enum('', ['MS120', 'MS240', 'MS480', 'MS640', 'MS1024', 'MS2048', 'MS5120', 'MS10240', 'MIN1', 'MIN6', 'MIN12', 'MIN30', 'MIN60', 'SPARE3', 'SPARE2', 'SPARE1'], outer_class=root_module['ns3::LteRrcSap::ReportConfigEutra'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigToAddMod [struct]
    module.add_class('ReportConfigToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RlcConfig [struct]
    module.add_class('RlcConfig', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RlcConfig [enumeration]
    module.add_enum('', ['AM', 'UM_BI_DIRECTIONAL', 'UM_UNI_DIRECTIONAL_UL', 'UM_UNI_DIRECTIONAL_DL'], outer_class=root_module['ns3::LteRrcSap::RlcConfig'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration [struct]
    module.add_class('RrcConnectionReconfiguration', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfigurationCompleted [struct]
    module.add_class('RrcConnectionReconfigurationCompleted', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishment [struct]
    module.add_class('RrcConnectionReestablishment', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentComplete [struct]
    module.add_class('RrcConnectionReestablishmentComplete', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentReject [struct]
    module.add_class('RrcConnectionReestablishmentReject', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentRequest [struct]
    module.add_class('RrcConnectionReestablishmentRequest', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReject [struct]
    module.add_class('RrcConnectionReject', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRelease [struct]
    module.add_class('RrcConnectionRelease', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRequest [struct]
    module.add_class('RrcConnectionRequest', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetup [struct]
    module.add_class('RrcConnectionSetup', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetupCompleted [struct]
    module.add_class('RrcConnectionSetupCompleted', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon [struct]
    module.add_class('SoundingRsUlConfigCommon', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon [enumeration]
    module.add_enum('', ['SETUP', 'RESET'], outer_class=root_module['ns3::LteRrcSap::SoundingRsUlConfigCommon'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated [struct]
    module.add_class('SoundingRsUlConfigDedicated', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated [enumeration]
    module.add_enum('', ['SETUP', 'RESET'], outer_class=root_module['ns3::LteRrcSap::SoundingRsUlConfigDedicated'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars [struct]
    module.add_class('SpeedStatePars', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars [enumeration]
    module.add_enum('', ['SETUP', 'RESET'], outer_class=root_module['ns3::LteRrcSap::SpeedStatePars'], import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStateScaleFactors [struct]
    module.add_class('SpeedStateScaleFactors', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SrbToAddMod [struct]
    module.add_class('SrbToAddMod', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformation [struct]
    module.add_class('SystemInformation', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1 [struct]
    module.add_class('SystemInformationBlockType1', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType2 [struct]
    module.add_class('SystemInformationBlockType2', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ThresholdEutra [struct]
    module.add_class('ThresholdEutra', import_from_module='ns.lte', outer_class=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ThresholdEutra [enumeration]
    module.add_enum('', ['THRESHOLD_RSRP', 'THRESHOLD_RSRQ'], outer_class=root_module['ns3::LteRrcSap::ThresholdEutra'], import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t [struct]
    module.add_class('LteUeConfig_t', import_from_module='ns.lte')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider [class]
    module.add_class('LteUeRrcSapProvider', import_from_module='ns.lte', parent=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::CompleteSetupParameters [struct]
    module.add_class('CompleteSetupParameters', import_from_module='ns.lte', outer_class=root_module['ns3::LteUeRrcSapProvider'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser [class]
    module.add_class('LteUeRrcSapUser', import_from_module='ns.lte', parent=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::SetupParameters [struct]
    module.add_class('SetupParameters', import_from_module='ns.lte', outer_class=root_module['ns3::LteUeRrcSapUser'])
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    module.add_class('Mac48Address', import_from_module='ns.network')
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    root_module['ns3::Mac48Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s [struct]
    module.add_class('MacCeListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::MacCeType_e [enumeration]
    module.add_enum('MacCeType_e', ['BSR', 'PHR', 'CRNTI'], outer_class=root_module['ns3::MacCeListElement_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u [struct]
    module.add_class('MacCeValue_u', import_from_module='ns.lte')
    ## node-container.h (module 'network'): ns3::NodeContainer [class]
    module.add_class('NodeContainer', import_from_module='ns.network')
    ## node-list.h (module 'network'): ns3::NodeList [class]
    module.add_class('NodeList', import_from_module='ns.network')
    ## object-base.h (module 'core'): ns3::ObjectBase [class]
    module.add_class('ObjectBase', allow_subclassing=True, import_from_module='ns.core')
    ## object.h (module 'core'): ns3::ObjectDeleter [struct]
    module.add_class('ObjectDeleter', import_from_module='ns.core')
    ## object-factory.h (module 'core'): ns3::ObjectFactory [class]
    module.add_class('ObjectFactory', import_from_module='ns.core')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata [class]
    module.add_class('PacketMetadata', import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item [enumeration]
    module.add_enum('', ['PAYLOAD', 'HEADER', 'TRAILER'], outer_class=root_module['ns3::PacketMetadata::Item'], import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator [class]
    module.add_class('ItemIterator', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## packet.h (module 'network'): ns3::PacketTagIterator [class]
    module.add_class('PacketTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagIterator'])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList [class]
    module.add_class('PacketTagList', import_from_module='ns.network')
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData [struct]
    module.add_class('TagData', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagList'])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData_e [enumeration]
    module.add_enum('TagData_e', ['MAX_SIZE'], outer_class=root_module['ns3::PacketTagList::TagData'], import_from_module='ns.network')
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s [struct]
    module.add_class('PagingInfoListElement_s', import_from_module='ns.lte')
    ## log.h (module 'core'): ns3::ParameterLogger [class]
    module.add_class('ParameterLogger', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s [struct]
    module.add_class('PhichListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s::Phich_e [enumeration]
    module.add_enum('Phich_e', ['ACK', 'NACK'], outer_class=root_module['ns3::PhichListElement_s'], import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters [struct]
    module.add_class('PhyReceptionStatParameters', import_from_module='ns.lte')
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters [struct]
    module.add_class('PhyTransmissionStatParameters', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::RachListElement_s [struct]
    module.add_class('RachListElement_s', import_from_module='ns.lte')
    ## rectangle.h (module 'mobility'): ns3::Rectangle [class]
    module.add_class('Rectangle', import_from_module='ns.mobility')
    ## rectangle.h (module 'mobility'): ns3::Rectangle::Side [enumeration]
    module.add_enum('Side', ['RIGHT', 'LEFT', 'TOP', 'BOTTOM'], outer_class=root_module['ns3::Rectangle'], import_from_module='ns.mobility')
    ## ff-mac-common.h (module 'lte'): ns3::RlcPduListElement_s [struct]
    module.add_class('RlcPduListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s [struct]
    module.add_class('SbMeasResult_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s [struct]
    module.add_class('SiConfiguration_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::SiMessageListElement_s [struct]
    module.add_class('SiMessageListElement_s', import_from_module='ns.lte')
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Object', 'ns3::ObjectBase', 'ns3::ObjectDeleter'], parent=root_module['ns3::ObjectBase'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simulator.h (module 'core'): ns3::Simulator [class]
    module.add_class('Simulator', destructor_visibility='private', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s [struct]
    module.add_class('SpsConfig_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s [struct]
    module.add_class('SrConfig_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::SrListElement_s [struct]
    module.add_class('SrListElement_s', import_from_module='ns.lte')
    ## tag.h (module 'network'): ns3::Tag [class]
    module.add_class('Tag', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer [class]
    module.add_class('TagBuffer', import_from_module='ns.network')
    ## uan-prop-model.h (module 'uan'): ns3::Tap [class]
    module.add_class('Tap', import_from_module='ns.uan')
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t [struct]
    module.add_class('TbId_t', import_from_module='ns.lte')
    ## nstime.h (module 'core'): ns3::TimeWithUnit [class]
    module.add_class('TimeWithUnit', import_from_module='ns.core')
    ## lte-common.h (module 'lte'): ns3::TransmissionModesLayers [class]
    module.add_class('TransmissionModesLayers', import_from_module='ns.lte')
    ## type-id.h (module 'core'): ns3::TypeId [class]
    module.add_class('TypeId', import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeFlag [enumeration]
    module.add_enum('AttributeFlag', ['ATTR_GET', 'ATTR_SET', 'ATTR_CONSTRUCT', 'ATTR_SGC'], outer_class=root_module['ns3::TypeId'], import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation [struct]
    module.add_class('AttributeInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation [struct]
    module.add_class('TraceSourceInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesList [class]
    module.add_class('UanModesList', import_from_module='ns.uan')
    ## uan-transducer.h (module 'uan'): ns3::UanPacketArrival [class]
    module.add_class('UanPacketArrival', import_from_module='ns.uan')
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp [class]
    module.add_class('UanPdp', import_from_module='ns.uan')
    ## uan-phy.h (module 'uan'): ns3::UanPhyListener [class]
    module.add_class('UanPhyListener', allow_subclassing=True, import_from_module='ns.uan')
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxMode [class]
    module.add_class('UanTxMode', import_from_module='ns.uan')
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxMode::ModulationType [enumeration]
    module.add_enum('ModulationType', ['PSK', 'QAM', 'FSK', 'OTHER'], outer_class=root_module['ns3::UanTxMode'], import_from_module='ns.uan')
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxModeFactory [class]
    module.add_class('UanTxModeFactory', import_from_module='ns.uan')
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s [struct]
    module.add_class('UeCapabilities_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s [struct]
    module.add_class('UeSelected_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s [struct]
    module.add_class('UlCqi_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s::Type_e [enumeration]
    module.add_enum('Type_e', ['SRS', 'PUSCH', 'PUCCH_1', 'PUCCH_2', 'PRACH'], outer_class=root_module['ns3::UlCqi_s'], import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s [struct]
    module.add_class('UlDciListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s [struct]
    module.add_class('UlGrant_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s [struct]
    module.add_class('UlInfoListElement_s', import_from_module='ns.lte')
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::ReceptionStatus_e [enumeration]
    module.add_enum('ReceptionStatus_e', ['Ok', 'NotOk', 'NotValid'], outer_class=root_module['ns3::UlInfoListElement_s'], import_from_module='ns.lte')
    ## vector.h (module 'core'): ns3::Vector2D [class]
    module.add_class('Vector2D', import_from_module='ns.core')
    ## vector.h (module 'core'): ns3::Vector3D [class]
    module.add_class('Vector3D', import_from_module='ns.core')
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s [struct]
    module.add_class('VendorSpecificListElement_s', import_from_module='ns.lte')
    ## empty.h (module 'core'): ns3::empty [class]
    module.add_class('empty', import_from_module='ns.core')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t [class]
    module.add_class('int64x64_t', import_from_module='ns.core')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::impl_type [enumeration]
    module.add_enum('impl_type', ['int128_impl', 'cairo_impl', 'ld_impl'], outer_class=root_module['ns3::int64x64_t'], import_from_module='ns.core')
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t [struct]
    module.add_class('tbInfo_t', import_from_module='ns.lte')
    ## animation-interface.h (module 'netanim'): ns3::AnimByteTag [class]
    module.add_class('AnimByteTag', parent=root_module['ns3::Tag'])
    ## chunk.h (module 'network'): ns3::Chunk [class]
    module.add_class('Chunk', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## header.h (module 'network'): ns3::Header [class]
    module.add_class('Header', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header [class]
    module.add_class('Ipv4Header', import_from_module='ns.internet', parent=root_module['ns3::Header'])
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::DscpType [enumeration]
    module.add_enum('DscpType', ['DscpDefault', 'DSCP_CS1', 'DSCP_AF11', 'DSCP_AF12', 'DSCP_AF13', 'DSCP_CS2', 'DSCP_AF21', 'DSCP_AF22', 'DSCP_AF23', 'DSCP_CS3', 'DSCP_AF31', 'DSCP_AF32', 'DSCP_AF33', 'DSCP_CS4', 'DSCP_AF41', 'DSCP_AF42', 'DSCP_AF43', 'DSCP_CS5', 'DSCP_EF', 'DSCP_CS6', 'DSCP_CS7'], outer_class=root_module['ns3::Ipv4Header'], import_from_module='ns.internet')
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::EcnType [enumeration]
    module.add_enum('EcnType', ['ECN_NotECT', 'ECN_ECT1', 'ECN_ECT0', 'ECN_CE'], outer_class=root_module['ns3::Ipv4Header'], import_from_module='ns.internet')
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider [class]
    module.add_class('LteEnbRrcSapProvider', import_from_module='ns.lte', parent=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters [struct]
    module.add_class('CompleteSetupUeParameters', import_from_module='ns.lte', outer_class=root_module['ns3::LteEnbRrcSapProvider'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser [class]
    module.add_class('LteEnbRrcSapUser', import_from_module='ns.lte', parent=root_module['ns3::LteRrcSap'])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::SetupUeParameters [struct]
    module.add_class('SetupUeParameters', import_from_module='ns.lte', outer_class=root_module['ns3::LteEnbRrcSapUser'])
    ## object.h (module 'core'): ns3::Object [class]
    module.add_class('Object', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    ## object.h (module 'core'): ns3::Object::AggregateIterator [class]
    module.add_class('AggregateIterator', import_from_module='ns.core', outer_class=root_module['ns3::Object'])
    ## packet-burst.h (module 'network'): ns3::PacketBurst [class]
    module.add_class('PacketBurst', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream [class]
    module.add_class('RandomVariableStream', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable [class]
    module.add_class('SequentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeChecker', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeChecker>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::CallbackImplBase', 'ns3::empty', 'ns3::DefaultDeleter<ns3::CallbackImplBase>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::EventImpl', 'ns3::empty', 'ns3::DefaultDeleter<ns3::EventImpl>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Hash::Implementation', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Hash::Implementation>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Ipv4MulticastRoute', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Ipv4MulticastRoute>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Ipv4Route', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Ipv4Route>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::LteControlMessage', 'ns3::empty', 'ns3::DefaultDeleter<ns3::LteControlMessage>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::LteHarqPhy', 'ns3::empty', 'ns3::DefaultDeleter<ns3::LteHarqPhy>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::NixVector', 'ns3::empty', 'ns3::DefaultDeleter<ns3::NixVector>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::OutputStreamWrapper', 'ns3::empty', 'ns3::DefaultDeleter<ns3::OutputStreamWrapper>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Packet', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Packet>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumModel', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumModel>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumSignalParameters', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumSignalParameters>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SpectrumValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SpectrumValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::TraceSourceAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::TraceSourceAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::VendorSpecificValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::VendorSpecificValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## socket.h (module 'network'): ns3::Socket [class]
    module.add_class('Socket', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## socket.h (module 'network'): ns3::Socket::SocketErrno [enumeration]
    module.add_enum('SocketErrno', ['ERROR_NOTERROR', 'ERROR_ISCONN', 'ERROR_NOTCONN', 'ERROR_MSGSIZE', 'ERROR_AGAIN', 'ERROR_SHUTDOWN', 'ERROR_OPNOTSUPP', 'ERROR_AFNOSUPPORT', 'ERROR_INVAL', 'ERROR_BADF', 'ERROR_NOROUTETOHOST', 'ERROR_NODEV', 'ERROR_ADDRNOTAVAIL', 'ERROR_ADDRINUSE', 'SOCKET_ERRNO_LAST'], outer_class=root_module['ns3::Socket'], import_from_module='ns.network')
    ## socket.h (module 'network'): ns3::Socket::SocketType [enumeration]
    module.add_enum('SocketType', ['NS3_SOCK_STREAM', 'NS3_SOCK_SEQPACKET', 'NS3_SOCK_DGRAM', 'NS3_SOCK_RAW'], outer_class=root_module['ns3::Socket'], import_from_module='ns.network')
    ## socket.h (module 'network'): ns3::SocketAddressTag [class]
    module.add_class('SocketAddressTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## socket.h (module 'network'): ns3::SocketIpTosTag [class]
    module.add_class('SocketIpTosTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## socket.h (module 'network'): ns3::SocketIpTtlTag [class]
    module.add_class('SocketIpTtlTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## socket.h (module 'network'): ns3::SocketIpv6HopLimitTag [class]
    module.add_class('SocketIpv6HopLimitTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## socket.h (module 'network'): ns3::SocketIpv6TclassTag [class]
    module.add_class('SocketIpv6TclassTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## socket.h (module 'network'): ns3::SocketSetDontFragmentTag [class]
    module.add_class('SocketSetDontFragmentTag', import_from_module='ns.network', parent=root_module['ns3::Tag'])
    ## spectrum-interference.h (module 'spectrum'): ns3::SpectrumInterference [class]
    module.add_class('SpectrumInterference', import_from_module='ns.spectrum', parent=root_module['ns3::Object'])
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel [class]
    module.add_class('SpectrumModel', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >'])
    ## spectrum-phy.h (module 'spectrum'): ns3::SpectrumPhy [class]
    module.add_class('SpectrumPhy', import_from_module='ns.spectrum', parent=root_module['ns3::Object'])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters [struct]
    module.add_class('SpectrumSignalParameters', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >'])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue [class]
    module.add_class('SpectrumValue', import_from_module='ns.spectrum', parent=root_module['ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >'])
    ## nstime.h (module 'core'): ns3::Time [class]
    module.add_class('Time', import_from_module='ns.core')
    ## nstime.h (module 'core'): ns3::Time::Unit [enumeration]
    module.add_enum('Unit', ['Y', 'D', 'H', 'MIN', 'S', 'MS', 'US', 'NS', 'PS', 'FS', 'LAST'], outer_class=root_module['ns3::Time'], import_from_module='ns.core')
    ## nstime.h (module 'core'): ns3::Time [class]
    root_module['ns3::Time'].implicitly_converts_to(root_module['ns3::int64x64_t'])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor [class]
    module.add_class('TraceSourceAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    ## trailer.h (module 'network'): ns3::Trailer [class]
    module.add_class('Trailer', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable [class]
    module.add_class('TriangularRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## uan-mac.h (module 'uan'): ns3::UanMac [class]
    module.add_class('UanMac', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-phy.h (module 'uan'): ns3::UanPhy [class]
    module.add_class('UanPhy', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-phy.h (module 'uan'): ns3::UanPhy::State [enumeration]
    module.add_enum('State', ['IDLE', 'CCABUSY', 'RX', 'TX', 'SLEEP'], outer_class=root_module['ns3::UanPhy'], import_from_module='ns.uan')
    ## uan-phy.h (module 'uan'): ns3::UanPhyCalcSinr [class]
    module.add_class('UanPhyCalcSinr', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrDefault [class]
    module.add_class('UanPhyCalcSinrDefault', import_from_module='ns.uan', parent=root_module['ns3::UanPhyCalcSinr'])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrFhFsk [class]
    module.add_class('UanPhyCalcSinrFhFsk', import_from_module='ns.uan', parent=root_module['ns3::UanPhyCalcSinr'])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyGen [class]
    module.add_class('UanPhyGen', import_from_module='ns.uan', parent=root_module['ns3::UanPhy'])
    ## uan-phy.h (module 'uan'): ns3::UanPhyPer [class]
    module.add_class('UanPhyPer', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerGenDefault [class]
    module.add_class('UanPhyPerGenDefault', import_from_module='ns.uan', parent=root_module['ns3::UanPhyPer'])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerUmodem [class]
    module.add_class('UanPhyPerUmodem', import_from_module='ns.uan', parent=root_module['ns3::UanPhyPer'])
    ## uan-prop-model.h (module 'uan'): ns3::UanPropModel [class]
    module.add_class('UanPropModel', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-transducer.h (module 'uan'): ns3::UanTransducer [class]
    module.add_class('UanTransducer', import_from_module='ns.uan', parent=root_module['ns3::Object'])
    ## uan-transducer.h (module 'uan'): ns3::UanTransducer::State [enumeration]
    module.add_enum('State', ['TX', 'RX'], outer_class=root_module['ns3::UanTransducer'], import_from_module='ns.uan')
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable [class]
    module.add_class('UniformRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificValue [struct]
    module.add_class('VendorSpecificValue', import_from_module='ns.lte', parent=root_module['ns3::SimpleRefCount< ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> >'])
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable [class]
    module.add_class('WeibullRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable [class]
    module.add_class('ZetaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable [class]
    module.add_class('ZipfRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## attribute.h (module 'core'): ns3::AttributeAccessor [class]
    module.add_class('AttributeAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    ## attribute.h (module 'core'): ns3::AttributeChecker [class]
    module.add_class('AttributeChecker', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    ## attribute.h (module 'core'): ns3::AttributeValue [class]
    module.add_class('AttributeValue', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    ## callback.h (module 'core'): ns3::CallbackChecker [class]
    module.add_class('CallbackChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## callback.h (module 'core'): ns3::CallbackImplBase [class]
    module.add_class('CallbackImplBase', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    ## callback.h (module 'core'): ns3::CallbackValue [class]
    module.add_class('CallbackValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## channel.h (module 'network'): ns3::Channel [class]
    module.add_class('Channel', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable [class]
    module.add_class('ConstantRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## data-rate.h (module 'network'): ns3::DataRateChecker [class]
    module.add_class('DataRateChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## data-rate.h (module 'network'): ns3::DataRateValue [class]
    module.add_class('DataRateValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable [class]
    module.add_class('DeterministicRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel [class]
    module.add_class('DeviceEnergyModel', import_from_module='ns.energy', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable [class]
    module.add_class('EmpiricalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue [class]
    module.add_class('EmptyAttributeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable [class]
    module.add_class('ErlangRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## event-impl.h (module 'core'): ns3::EventImpl [class]
    module.add_class('EventImpl', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable [class]
    module.add_class('ExponentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable [class]
    module.add_class('GammaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## ipv4.h (module 'internet'): ns3::Ipv4 [class]
    module.add_class('Ipv4', import_from_module='ns.internet', parent=root_module['ns3::Object'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker [class]
    module.add_class('Ipv4AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue [class]
    module.add_class('Ipv4AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4L3Protocol [class]
    module.add_class('Ipv4L3Protocol', import_from_module='ns.internet', parent=root_module['ns3::Ipv4'])
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4L3Protocol::DropReason [enumeration]
    module.add_enum('DropReason', ['DROP_TTL_EXPIRED', 'DROP_NO_ROUTE', 'DROP_BAD_CHECKSUM', 'DROP_INTERFACE_DOWN', 'DROP_ROUTE_ERROR', 'DROP_FRAGMENT_TIMEOUT'], outer_class=root_module['ns3::Ipv4L3Protocol'], import_from_module='ns.internet')
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker [class]
    module.add_class('Ipv4MaskChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue [class]
    module.add_class('Ipv4MaskValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4MulticastRoute [class]
    module.add_class('Ipv4MulticastRoute', import_from_module='ns.internet', parent=root_module['ns3::SimpleRefCount< ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> >'])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Route [class]
    module.add_class('Ipv4Route', import_from_module='ns.internet', parent=root_module['ns3::SimpleRefCount< ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> >'])
    ## ipv4-routing-protocol.h (module 'internet'): ns3::Ipv4RoutingProtocol [class]
    module.add_class('Ipv4RoutingProtocol', import_from_module='ns.internet', parent=root_module['ns3::Object'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker [class]
    module.add_class('Ipv6AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue [class]
    module.add_class('Ipv6AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker [class]
    module.add_class('Ipv6PrefixChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue [class]
    module.add_class('Ipv6PrefixValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable [class]
    module.add_class('LogNormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## lte-control-messages.h (module 'lte'): ns3::LteControlMessage [class]
    module.add_class('LteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::SimpleRefCount< ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> >'])
    ## lte-control-messages.h (module 'lte'): ns3::LteControlMessage::MessageType [enumeration]
    module.add_enum('MessageType', ['DL_DCI', 'UL_DCI', 'DL_CQI', 'UL_CQI', 'BSR', 'DL_HARQ', 'RACH_PREAMBLE', 'RAR', 'MIB', 'SIB1'], outer_class=root_module['ns3::LteControlMessage'], import_from_module='ns.lte')
    ## lte-harq-phy.h (module 'lte'): ns3::LteHarqPhy [class]
    module.add_class('LteHarqPhy', import_from_module='ns.lte', parent=root_module['ns3::SimpleRefCount< ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> >'])
    ## lte-interference.h (module 'lte'): ns3::LteInterference [class]
    module.add_class('LteInterference', import_from_module='ns.lte', parent=root_module['ns3::Object'])
    ## lte-phy.h (module 'lte'): ns3::LtePhy [class]
    module.add_class('LtePhy', import_from_module='ns.lte', parent=root_module['ns3::Object'])
    ## lte-spectrum-phy.h (module 'lte'): ns3::LteSpectrumPhy [class]
    module.add_class('LteSpectrumPhy', import_from_module='ns.lte', parent=root_module['ns3::SpectrumPhy'])
    ## lte-spectrum-phy.h (module 'lte'): ns3::LteSpectrumPhy::State [enumeration]
    module.add_enum('State', ['IDLE', 'TX', 'RX_DATA', 'RX_CTRL'], outer_class=root_module['ns3::LteSpectrumPhy'], import_from_module='ns.lte')
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker [class]
    module.add_class('Mac48AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue [class]
    module.add_class('Mac48AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## lte-control-messages.h (module 'lte'): ns3::MibLteControlMessage [class]
    module.add_class('MibLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel [class]
    module.add_class('MobilityModel', import_from_module='ns.mobility', parent=root_module['ns3::Object'])
    ## net-device.h (module 'network'): ns3::NetDevice [class]
    module.add_class('NetDevice', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## net-device.h (module 'network'): ns3::NetDevice::PacketType [enumeration]
    module.add_enum('PacketType', ['PACKET_HOST', 'NS3_PACKET_HOST', 'PACKET_BROADCAST', 'NS3_PACKET_BROADCAST', 'PACKET_MULTICAST', 'NS3_PACKET_MULTICAST', 'PACKET_OTHERHOST', 'NS3_PACKET_OTHERHOST'], outer_class=root_module['ns3::NetDevice'], import_from_module='ns.network')
    ## nix-vector.h (module 'network'): ns3::NixVector [class]
    module.add_class('NixVector', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    ## node.h (module 'network'): ns3::Node [class]
    module.add_class('Node', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable [class]
    module.add_class('NormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker [class]
    module.add_class('ObjectFactoryChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue [class]
    module.add_class('ObjectFactoryValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper [class]
    module.add_class('OutputStreamWrapper', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    ## packet.h (module 'network'): ns3::Packet [class]
    module.add_class('Packet', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable [class]
    module.add_class('ParetoRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## lte-control-messages.h (module 'lte'): ns3::RachPreambleLteControlMessage [class]
    module.add_class('RachPreambleLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage [class]
    module.add_class('RarLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::Rar [struct]
    module.add_class('Rar', import_from_module='ns.lte', outer_class=root_module['ns3::RarLteControlMessage'])
    ## rectangle.h (module 'mobility'): ns3::RectangleChecker [class]
    module.add_class('RectangleChecker', import_from_module='ns.mobility', parent=root_module['ns3::AttributeChecker'])
    ## rectangle.h (module 'mobility'): ns3::RectangleValue [class]
    module.add_class('RectangleValue', import_from_module='ns.mobility', parent=root_module['ns3::AttributeValue'])
    ## lte-control-messages.h (module 'lte'): ns3::Sib1LteControlMessage [class]
    module.add_class('Sib1LteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel [class]
    module.add_class('SpectrumChannel', import_from_module='ns.spectrum', parent=root_module['ns3::Channel'])
    ## nstime.h (module 'core'): ns3::TimeValue [class]
    module.add_class('TimeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## type-id.h (module 'core'): ns3::TypeIdChecker [class]
    module.add_class('TypeIdChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## type-id.h (module 'core'): ns3::TypeIdValue [class]
    module.add_class('TypeIdValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListChecker [class]
    module.add_class('UanModesListChecker', import_from_module='ns.uan', parent=root_module['ns3::AttributeChecker'])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListValue [class]
    module.add_class('UanModesListValue', import_from_module='ns.uan', parent=root_module['ns3::AttributeValue'])
    ## uinteger.h (module 'core'): ns3::UintegerValue [class]
    module.add_class('UintegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## lte-control-messages.h (module 'lte'): ns3::UlDciLteControlMessage [class]
    module.add_class('UlDciLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## vector.h (module 'core'): ns3::Vector2DChecker [class]
    module.add_class('Vector2DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector2DValue [class]
    module.add_class('Vector2DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vector.h (module 'core'): ns3::Vector3DChecker [class]
    module.add_class('Vector3DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector3DValue [class]
    module.add_class('Vector3DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## address.h (module 'network'): ns3::AddressChecker [class]
    module.add_class('AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## address.h (module 'network'): ns3::AddressValue [class]
    module.add_class('AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## lte-control-messages.h (module 'lte'): ns3::BsrLteControlMessage [class]
    module.add_class('BsrLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-control-messages.h (module 'lte'): ns3::DlCqiLteControlMessage [class]
    module.add_class('DlCqiLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-control-messages.h (module 'lte'): ns3::DlDciLteControlMessage [class]
    module.add_class('DlDciLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-control-messages.h (module 'lte'): ns3::DlHarqFeedbackLteControlMessage [class]
    module.add_class('DlHarqFeedbackLteControlMessage', import_from_module='ns.lte', parent=root_module['ns3::LteControlMessage'])
    ## lte-net-device.h (module 'lte'): ns3::LteNetDevice [class]
    module.add_class('LteNetDevice', import_from_module='ns.lte', parent=root_module['ns3::NetDevice'])
    ## lte-ue-net-device.h (module 'lte'): ns3::LteUeNetDevice [class]
    module.add_class('LteUeNetDevice', import_from_module='ns.lte', parent=root_module['ns3::LteNetDevice'])
    ## lte-enb-net-device.h (module 'lte'): ns3::LteEnbNetDevice [class]
    module.add_class('LteEnbNetDevice', import_from_module='ns.lte', parent=root_module['ns3::LteNetDevice'])
    module.add_container('std::vector< ns3::CeBitmap_e >', 'ns3::CeBitmap_e', container_type=u'vector')
    module.add_container('std::vector< std::vector< ns3::RlcPduListElement_s > >', 'std::vector< ns3::RlcPduListElement_s >', container_type=u'vector')
    module.add_container('std::vector< unsigned char >', 'unsigned char', container_type=u'vector')
    module.add_container('std::vector< unsigned short >', 'short unsigned int', container_type=u'vector')
    module.add_container('std::vector< ns3::DlInfoListElement_s::HarqStatus_e >', 'ns3::DlInfoListElement_s::HarqStatus_e', container_type=u'vector')
    module.add_container('std::map< std::string, ns3::LogComponent * >', ('std::string', 'ns3::LogComponent *'), container_type=u'map')
    module.add_container('std::list< ns3::LteRrcSap::SrbToAddMod >', 'ns3::LteRrcSap::SrbToAddMod', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::DrbToAddMod >', 'ns3::LteRrcSap::DrbToAddMod', container_type=u'list')
    module.add_container('std::list< unsigned char >', 'unsigned char', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::CellsToAddMod >', 'ns3::LteRrcSap::CellsToAddMod', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::BlackCellsToAddMod >', 'ns3::LteRrcSap::BlackCellsToAddMod', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::MeasObjectToAddMod >', 'ns3::LteRrcSap::MeasObjectToAddMod', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::ReportConfigToAddMod >', 'ns3::LteRrcSap::ReportConfigToAddMod', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::MeasIdToAddMod >', 'ns3::LteRrcSap::MeasIdToAddMod', container_type=u'list')
    module.add_container('std::list< unsigned int >', 'unsigned int', container_type=u'list')
    module.add_container('std::list< ns3::LteRrcSap::MeasResultEutra >', 'ns3::LteRrcSap::MeasResultEutra', container_type=u'list')
    module.add_container('std::vector< ns3::HigherLayerSelected_s >', 'ns3::HigherLayerSelected_s', container_type=u'vector')
    module.add_container('std::vector< ns3::SiMessageListElement_s >', 'ns3::SiMessageListElement_s', container_type=u'vector')
    module.add_container('std::vector< ns3::Tap >', 'ns3::Tap', container_type=u'vector')
    module.add_container('std::vector< std::complex< double > >', 'std::complex< double >', container_type=u'vector')
    module.add_container('std::vector< double >', 'double', container_type=u'vector')
    module.add_container('std::vector< int >', 'int', container_type=u'vector')
    module.add_container('std::list< ns3::Ptr< ns3::Packet > >', 'ns3::Ptr< ns3::Packet >', container_type=u'list')
    module.add_container('ns3::Bands', 'ns3::BandInfo', container_type=u'vector')
    module.add_container('std::list< ns3::UanPacketArrival >', 'ns3::UanPacketArrival', container_type=u'list')
    module.add_container('std::list< ns3::Ptr< ns3::UanPhy > >', 'ns3::Ptr< ns3::UanPhy >', container_type=u'list')
    module.add_container('std::map< unsigned int, unsigned int >', ('unsigned int', 'unsigned int'), container_type=u'map')
    module.add_container('ns3::HarqProcessInfoList_t', 'ns3::HarqProcessInfoElement_t', container_type=u'vector')
    module.add_container('std::list< ns3::Ptr< ns3::LteControlMessage > >', 'ns3::Ptr< ns3::LteControlMessage >', container_type=u'list')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyTxEndCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyTxEndCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyTxEndCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, unsigned short, ns3::Ptr< ns3::SpectrumValue >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyRxPssCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, unsigned short, ns3::Ptr< ns3::SpectrumValue >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyRxPssCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, unsigned short, ns3::Ptr< ns3::SpectrumValue >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyRxPssCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyTxEndCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyTxEndCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyTxEndCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *', u'ns3::LogNodePrinter')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) **', u'ns3::LogNodePrinter*')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *&', u'ns3::LogNodePrinter&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxStartCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxStartCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxStartCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyRxDataEndOkCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyRxDataEndOkCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyRxDataEndOkCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyRxDataEndErrorCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyRxDataEndErrorCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyRxDataEndErrorCallback&')
    typehandlers.add_type_alias(u'std::vector< ns3::HarqProcessInfoElement_t, std::allocator< ns3::HarqProcessInfoElement_t > >', u'ns3::HarqProcessInfoList_t')
    typehandlers.add_type_alias(u'std::vector< ns3::HarqProcessInfoElement_t, std::allocator< ns3::HarqProcessInfoElement_t > >*', u'ns3::HarqProcessInfoList_t*')
    typehandlers.add_type_alias(u'std::vector< ns3::HarqProcessInfoElement_t, std::allocator< ns3::HarqProcessInfoElement_t > >&', u'ns3::HarqProcessInfoList_t&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyRxCtrlEndErrorCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyRxCtrlEndErrorCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyRxCtrlEndErrorCallback&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxEndErrorCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxEndErrorCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxEndErrorCallback&')
    typehandlers.add_type_alias(u'std::vector< double, std::allocator< double > >', u'ns3::Values')
    typehandlers.add_type_alias(u'std::vector< double, std::allocator< double > >*', u'ns3::Values*')
    typehandlers.add_type_alias(u'std::vector< double, std::allocator< double > >&', u'ns3::Values&')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo, std::allocator< ns3::BandInfo > >', u'ns3::Bands')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo, std::allocator< ns3::BandInfo > >*', u'ns3::Bands*')
    typehandlers.add_type_alias(u'std::vector< ns3::BandInfo, std::allocator< ns3::BandInfo > >&', u'ns3::Bands&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::DlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyDlHarqFeedbackCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::DlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyDlHarqFeedbackCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::DlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyDlHarqFeedbackCallback&')
    typehandlers.add_type_alias(u'ns3::Vector3D', u'ns3::Vector')
    typehandlers.add_type_alias(u'ns3::Vector3D*', u'ns3::Vector*')
    typehandlers.add_type_alias(u'ns3::Vector3D&', u'ns3::Vector&')
    module.add_typedef(root_module['ns3::Vector3D'], 'Vector')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyTxStartCallback')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyTxStartCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< bool, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyTxStartCallback&')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *', u'ns3::LogTimePrinter')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) **', u'ns3::LogTimePrinter*')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *&', u'ns3::LogTimePrinter&')
    typehandlers.add_type_alias(u'ns3::Vector3DValue', u'ns3::VectorValue')
    typehandlers.add_type_alias(u'ns3::Vector3DValue*', u'ns3::VectorValue*')
    typehandlers.add_type_alias(u'ns3::Vector3DValue&', u'ns3::VectorValue&')
    module.add_typedef(root_module['ns3::Vector3DValue'], 'VectorValue')
    typehandlers.add_type_alias(u'ns3::Callback< void, std::list< ns3::Ptr< ns3::LteControlMessage >, std::allocator< ns3::Ptr< ns3::LteControlMessage > > >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyRxCtrlEndOkCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, std::list< ns3::Ptr< ns3::LteControlMessage >, std::allocator< ns3::Ptr< ns3::LteControlMessage > > >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyRxCtrlEndOkCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, std::list< ns3::Ptr< ns3::LteControlMessage >, std::allocator< ns3::Ptr< ns3::LteControlMessage > > >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyRxCtrlEndOkCallback&')
    typehandlers.add_type_alias(u'uint32_t', u'ns3::SpectrumModelUid_t')
    typehandlers.add_type_alias(u'uint32_t*', u'ns3::SpectrumModelUid_t*')
    typehandlers.add_type_alias(u'uint32_t&', u'ns3::SpectrumModelUid_t&')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker', u'ns3::VectorChecker')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker*', u'ns3::VectorChecker*')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker&', u'ns3::VectorChecker&')
    module.add_typedef(root_module['ns3::Vector3DChecker'], 'VectorChecker')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::UlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::LtePhyUlHarqFeedbackCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::UlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::LtePhyUlHarqFeedbackCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::UlInfoListElement_s, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::LtePhyUlHarqFeedbackCallback&')
    typehandlers.add_type_alias(u'std::map< ns3::TbId_t, ns3::tbInfo_t, std::less< ns3::TbId_t >, std::allocator< std::pair< ns3::TbId_t const, ns3::tbInfo_t > > >', u'ns3::expectedTbs_t')
    typehandlers.add_type_alias(u'std::map< ns3::TbId_t, ns3::tbInfo_t, std::less< ns3::TbId_t >, std::allocator< std::pair< ns3::TbId_t const, ns3::tbInfo_t > > >*', u'ns3::expectedTbs_t*')
    typehandlers.add_type_alias(u'std::map< ns3::TbId_t, ns3::tbInfo_t, std::less< ns3::TbId_t >, std::allocator< std::pair< ns3::TbId_t const, ns3::tbInfo_t > > >&', u'ns3::expectedTbs_t&')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', u'ns3::GenericPhyRxEndOkCallback')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >*', u'ns3::GenericPhyRxEndOkCallback*')
    typehandlers.add_type_alias(u'ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >&', u'ns3::GenericPhyRxEndOkCallback&')
    
    ## Register a nested module for the namespace Config
    
    nested_module = module.add_cpp_namespace('Config')
    register_types_ns3_Config(nested_module)
    
    
    ## Register a nested module for the namespace FatalImpl
    
    nested_module = module.add_cpp_namespace('FatalImpl')
    register_types_ns3_FatalImpl(nested_module)
    
    
    ## Register a nested module for the namespace Hash
    
    nested_module = module.add_cpp_namespace('Hash')
    register_types_ns3_Hash(nested_module)
    
    
    ## Register a nested module for the namespace internal
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    

def register_types_ns3_Config(module):
    root_module = module.get_root()
    
    ## config.h (module 'core'): ns3::Config::MatchContainer [class]
    module.add_class('MatchContainer', import_from_module='ns.core')
    module.add_container('std::vector< ns3::Ptr< ns3::Object > >', 'ns3::Ptr< ns3::Object >', container_type=u'vector')
    module.add_container('std::vector< std::string >', 'std::string', container_type=u'vector')

def register_types_ns3_FatalImpl(module):
    root_module = module.get_root()
    

def register_types_ns3_Hash(module):
    root_module = module.get_root()
    
    ## hash-function.h (module 'core'): ns3::Hash::Implementation [class]
    module.add_class('Implementation', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) *', u'ns3::Hash::Hash64Function_ptr')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) **', u'ns3::Hash::Hash64Function_ptr*')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) *&', u'ns3::Hash::Hash64Function_ptr&')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) *', u'ns3::Hash::Hash32Function_ptr')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) **', u'ns3::Hash::Hash32Function_ptr*')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) *&', u'ns3::Hash::Hash32Function_ptr&')
    
    ## Register a nested module for the namespace Function
    
    nested_module = module.add_cpp_namespace('Function')
    register_types_ns3_Hash_Function(nested_module)
    

def register_types_ns3_Hash_Function(module):
    root_module = module.get_root()
    
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a [class]
    module.add_class('Fnv1a', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32 [class]
    module.add_class('Hash32', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64 [class]
    module.add_class('Hash64', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3 [class]
    module.add_class('Murmur3', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3Address_methods(root_module, root_module['ns3::Address'])
    register_Ns3AllocationRetentionPriority_methods(root_module, root_module['ns3::AllocationRetentionPriority'])
    register_Ns3AnimationInterface_methods(root_module, root_module['ns3::AnimationInterface'])
    register_Ns3AttributeConstructionList_methods(root_module, root_module['ns3::AttributeConstructionList'])
    register_Ns3AttributeConstructionListItem_methods(root_module, root_module['ns3::AttributeConstructionList::Item'])
    register_Ns3BandInfo_methods(root_module, root_module['ns3::BandInfo'])
    register_Ns3Buffer_methods(root_module, root_module['ns3::Buffer'])
    register_Ns3BufferIterator_methods(root_module, root_module['ns3::Buffer::Iterator'])
    register_Ns3BufferSizeLevelBsr_methods(root_module, root_module['ns3::BufferSizeLevelBsr'])
    register_Ns3BuildBroadcastListElement_s_methods(root_module, root_module['ns3::BuildBroadcastListElement_s'])
    register_Ns3BuildDataListElement_s_methods(root_module, root_module['ns3::BuildDataListElement_s'])
    register_Ns3BuildRarListElement_s_methods(root_module, root_module['ns3::BuildRarListElement_s'])
    register_Ns3BwPart_s_methods(root_module, root_module['ns3::BwPart_s'])
    register_Ns3ByteTagIterator_methods(root_module, root_module['ns3::ByteTagIterator'])
    register_Ns3ByteTagIteratorItem_methods(root_module, root_module['ns3::ByteTagIterator::Item'])
    register_Ns3ByteTagList_methods(root_module, root_module['ns3::ByteTagList'])
    register_Ns3ByteTagListIterator_methods(root_module, root_module['ns3::ByteTagList::Iterator'])
    register_Ns3ByteTagListIteratorItem_methods(root_module, root_module['ns3::ByteTagList::Iterator::Item'])
    register_Ns3CallbackBase_methods(root_module, root_module['ns3::CallbackBase'])
    register_Ns3CqiConfig_s_methods(root_module, root_module['ns3::CqiConfig_s'])
    register_Ns3CqiListElement_s_methods(root_module, root_module['ns3::CqiListElement_s'])
    register_Ns3DataRate_methods(root_module, root_module['ns3::DataRate'])
    register_Ns3DlDciListElement_s_methods(root_module, root_module['ns3::DlDciListElement_s'])
    register_Ns3DlInfoListElement_s_methods(root_module, root_module['ns3::DlInfoListElement_s'])
    register_Ns3DrxConfig_s_methods(root_module, root_module['ns3::DrxConfig_s'])
    register_Ns3EpsBearer_methods(root_module, root_module['ns3::EpsBearer'])
    register_Ns3EutranMeasurementMapping_methods(root_module, root_module['ns3::EutranMeasurementMapping'])
    register_Ns3EventId_methods(root_module, root_module['ns3::EventId'])
    register_Ns3GbrQosInformation_methods(root_module, root_module['ns3::GbrQosInformation'])
    register_Ns3HarqProcessInfoElement_t_methods(root_module, root_module['ns3::HarqProcessInfoElement_t'])
    register_Ns3Hasher_methods(root_module, root_module['ns3::Hasher'])
    register_Ns3HigherLayerSelected_s_methods(root_module, root_module['ns3::HigherLayerSelected_s'])
    register_Ns3ImsiLcidPair_t_methods(root_module, root_module['ns3::ImsiLcidPair_t'])
    register_Ns3Inet6SocketAddress_methods(root_module, root_module['ns3::Inet6SocketAddress'])
    register_Ns3InetSocketAddress_methods(root_module, root_module['ns3::InetSocketAddress'])
    register_Ns3Ipv4Address_methods(root_module, root_module['ns3::Ipv4Address'])
    register_Ns3Ipv4InterfaceAddress_methods(root_module, root_module['ns3::Ipv4InterfaceAddress'])
    register_Ns3Ipv4Mask_methods(root_module, root_module['ns3::Ipv4Mask'])
    register_Ns3Ipv6Address_methods(root_module, root_module['ns3::Ipv6Address'])
    register_Ns3Ipv6Prefix_methods(root_module, root_module['ns3::Ipv6Prefix'])
    register_Ns3LogComponent_methods(root_module, root_module['ns3::LogComponent'])
    register_Ns3LogicalChannelConfigListElement_s_methods(root_module, root_module['ns3::LogicalChannelConfigListElement_s'])
    register_Ns3LteFfConverter_methods(root_module, root_module['ns3::LteFfConverter'])
    register_Ns3LteFlowId_t_methods(root_module, root_module['ns3::LteFlowId_t'])
    register_Ns3LteRrcSap_methods(root_module, root_module['ns3::LteRrcSap'])
    register_Ns3LteRrcSapAntennaInfoDedicated_methods(root_module, root_module['ns3::LteRrcSap::AntennaInfoDedicated'])
    register_Ns3LteRrcSapAsConfig_methods(root_module, root_module['ns3::LteRrcSap::AsConfig'])
    register_Ns3LteRrcSapBlackCellsToAddMod_methods(root_module, root_module['ns3::LteRrcSap::BlackCellsToAddMod'])
    register_Ns3LteRrcSapCarrierBandwidthEutra_methods(root_module, root_module['ns3::LteRrcSap::CarrierBandwidthEutra'])
    register_Ns3LteRrcSapCarrierFreqEutra_methods(root_module, root_module['ns3::LteRrcSap::CarrierFreqEutra'])
    register_Ns3LteRrcSapCellAccessRelatedInfo_methods(root_module, root_module['ns3::LteRrcSap::CellAccessRelatedInfo'])
    register_Ns3LteRrcSapCellSelectionInfo_methods(root_module, root_module['ns3::LteRrcSap::CellSelectionInfo'])
    register_Ns3LteRrcSapCellsToAddMod_methods(root_module, root_module['ns3::LteRrcSap::CellsToAddMod'])
    register_Ns3LteRrcSapCgiInfo_methods(root_module, root_module['ns3::LteRrcSap::CgiInfo'])
    register_Ns3LteRrcSapDrbToAddMod_methods(root_module, root_module['ns3::LteRrcSap::DrbToAddMod'])
    register_Ns3LteRrcSapFreqInfo_methods(root_module, root_module['ns3::LteRrcSap::FreqInfo'])
    register_Ns3LteRrcSapHandoverPreparationInfo_methods(root_module, root_module['ns3::LteRrcSap::HandoverPreparationInfo'])
    register_Ns3LteRrcSapLogicalChannelConfig_methods(root_module, root_module['ns3::LteRrcSap::LogicalChannelConfig'])
    register_Ns3LteRrcSapMasterInformationBlock_methods(root_module, root_module['ns3::LteRrcSap::MasterInformationBlock'])
    register_Ns3LteRrcSapMeasConfig_methods(root_module, root_module['ns3::LteRrcSap::MeasConfig'])
    register_Ns3LteRrcSapMeasGapConfig_methods(root_module, root_module['ns3::LteRrcSap::MeasGapConfig'])
    register_Ns3LteRrcSapMeasIdToAddMod_methods(root_module, root_module['ns3::LteRrcSap::MeasIdToAddMod'])
    register_Ns3LteRrcSapMeasObjectEutra_methods(root_module, root_module['ns3::LteRrcSap::MeasObjectEutra'])
    register_Ns3LteRrcSapMeasObjectToAddMod_methods(root_module, root_module['ns3::LteRrcSap::MeasObjectToAddMod'])
    register_Ns3LteRrcSapMeasResultEutra_methods(root_module, root_module['ns3::LteRrcSap::MeasResultEutra'])
    register_Ns3LteRrcSapMeasResults_methods(root_module, root_module['ns3::LteRrcSap::MeasResults'])
    register_Ns3LteRrcSapMeasurementReport_methods(root_module, root_module['ns3::LteRrcSap::MeasurementReport'])
    register_Ns3LteRrcSapMobilityControlInfo_methods(root_module, root_module['ns3::LteRrcSap::MobilityControlInfo'])
    register_Ns3LteRrcSapMobilityStateParameters_methods(root_module, root_module['ns3::LteRrcSap::MobilityStateParameters'])
    register_Ns3LteRrcSapPdschConfigCommon_methods(root_module, root_module['ns3::LteRrcSap::PdschConfigCommon'])
    register_Ns3LteRrcSapPdschConfigDedicated_methods(root_module, root_module['ns3::LteRrcSap::PdschConfigDedicated'])
    register_Ns3LteRrcSapPhysCellIdRange_methods(root_module, root_module['ns3::LteRrcSap::PhysCellIdRange'])
    register_Ns3LteRrcSapPhysicalConfigDedicated_methods(root_module, root_module['ns3::LteRrcSap::PhysicalConfigDedicated'])
    register_Ns3LteRrcSapPlmnIdentityInfo_methods(root_module, root_module['ns3::LteRrcSap::PlmnIdentityInfo'])
    register_Ns3LteRrcSapPreambleInfo_methods(root_module, root_module['ns3::LteRrcSap::PreambleInfo'])
    register_Ns3LteRrcSapQuantityConfig_methods(root_module, root_module['ns3::LteRrcSap::QuantityConfig'])
    register_Ns3LteRrcSapRaSupervisionInfo_methods(root_module, root_module['ns3::LteRrcSap::RaSupervisionInfo'])
    register_Ns3LteRrcSapRachConfigCommon_methods(root_module, root_module['ns3::LteRrcSap::RachConfigCommon'])
    register_Ns3LteRrcSapRachConfigDedicated_methods(root_module, root_module['ns3::LteRrcSap::RachConfigDedicated'])
    register_Ns3LteRrcSapRadioResourceConfigCommon_methods(root_module, root_module['ns3::LteRrcSap::RadioResourceConfigCommon'])
    register_Ns3LteRrcSapRadioResourceConfigCommonSib_methods(root_module, root_module['ns3::LteRrcSap::RadioResourceConfigCommonSib'])
    register_Ns3LteRrcSapRadioResourceConfigDedicated_methods(root_module, root_module['ns3::LteRrcSap::RadioResourceConfigDedicated'])
    register_Ns3LteRrcSapReestabUeIdentity_methods(root_module, root_module['ns3::LteRrcSap::ReestabUeIdentity'])
    register_Ns3LteRrcSapReportConfigEutra_methods(root_module, root_module['ns3::LteRrcSap::ReportConfigEutra'])
    register_Ns3LteRrcSapReportConfigToAddMod_methods(root_module, root_module['ns3::LteRrcSap::ReportConfigToAddMod'])
    register_Ns3LteRrcSapRlcConfig_methods(root_module, root_module['ns3::LteRrcSap::RlcConfig'])
    register_Ns3LteRrcSapRrcConnectionReconfiguration_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReconfiguration'])
    register_Ns3LteRrcSapRrcConnectionReconfigurationCompleted_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReconfigurationCompleted'])
    register_Ns3LteRrcSapRrcConnectionReestablishment_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReestablishment'])
    register_Ns3LteRrcSapRrcConnectionReestablishmentComplete_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReestablishmentComplete'])
    register_Ns3LteRrcSapRrcConnectionReestablishmentReject_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReestablishmentReject'])
    register_Ns3LteRrcSapRrcConnectionReestablishmentRequest_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReestablishmentRequest'])
    register_Ns3LteRrcSapRrcConnectionReject_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionReject'])
    register_Ns3LteRrcSapRrcConnectionRelease_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionRelease'])
    register_Ns3LteRrcSapRrcConnectionRequest_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionRequest'])
    register_Ns3LteRrcSapRrcConnectionSetup_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionSetup'])
    register_Ns3LteRrcSapRrcConnectionSetupCompleted_methods(root_module, root_module['ns3::LteRrcSap::RrcConnectionSetupCompleted'])
    register_Ns3LteRrcSapSoundingRsUlConfigCommon_methods(root_module, root_module['ns3::LteRrcSap::SoundingRsUlConfigCommon'])
    register_Ns3LteRrcSapSoundingRsUlConfigDedicated_methods(root_module, root_module['ns3::LteRrcSap::SoundingRsUlConfigDedicated'])
    register_Ns3LteRrcSapSpeedStatePars_methods(root_module, root_module['ns3::LteRrcSap::SpeedStatePars'])
    register_Ns3LteRrcSapSpeedStateScaleFactors_methods(root_module, root_module['ns3::LteRrcSap::SpeedStateScaleFactors'])
    register_Ns3LteRrcSapSrbToAddMod_methods(root_module, root_module['ns3::LteRrcSap::SrbToAddMod'])
    register_Ns3LteRrcSapSystemInformation_methods(root_module, root_module['ns3::LteRrcSap::SystemInformation'])
    register_Ns3LteRrcSapSystemInformationBlockType1_methods(root_module, root_module['ns3::LteRrcSap::SystemInformationBlockType1'])
    register_Ns3LteRrcSapSystemInformationBlockType2_methods(root_module, root_module['ns3::LteRrcSap::SystemInformationBlockType2'])
    register_Ns3LteRrcSapThresholdEutra_methods(root_module, root_module['ns3::LteRrcSap::ThresholdEutra'])
    register_Ns3LteUeConfig_t_methods(root_module, root_module['ns3::LteUeConfig_t'])
    register_Ns3LteUeRrcSapProvider_methods(root_module, root_module['ns3::LteUeRrcSapProvider'])
    register_Ns3LteUeRrcSapProviderCompleteSetupParameters_methods(root_module, root_module['ns3::LteUeRrcSapProvider::CompleteSetupParameters'])
    register_Ns3LteUeRrcSapUser_methods(root_module, root_module['ns3::LteUeRrcSapUser'])
    register_Ns3LteUeRrcSapUserSetupParameters_methods(root_module, root_module['ns3::LteUeRrcSapUser::SetupParameters'])
    register_Ns3Mac48Address_methods(root_module, root_module['ns3::Mac48Address'])
    register_Ns3MacCeListElement_s_methods(root_module, root_module['ns3::MacCeListElement_s'])
    register_Ns3MacCeValue_u_methods(root_module, root_module['ns3::MacCeValue_u'])
    register_Ns3NodeContainer_methods(root_module, root_module['ns3::NodeContainer'])
    register_Ns3NodeList_methods(root_module, root_module['ns3::NodeList'])
    register_Ns3ObjectBase_methods(root_module, root_module['ns3::ObjectBase'])
    register_Ns3ObjectDeleter_methods(root_module, root_module['ns3::ObjectDeleter'])
    register_Ns3ObjectFactory_methods(root_module, root_module['ns3::ObjectFactory'])
    register_Ns3PacketMetadata_methods(root_module, root_module['ns3::PacketMetadata'])
    register_Ns3PacketMetadataItem_methods(root_module, root_module['ns3::PacketMetadata::Item'])
    register_Ns3PacketMetadataItemIterator_methods(root_module, root_module['ns3::PacketMetadata::ItemIterator'])
    register_Ns3PacketTagIterator_methods(root_module, root_module['ns3::PacketTagIterator'])
    register_Ns3PacketTagIteratorItem_methods(root_module, root_module['ns3::PacketTagIterator::Item'])
    register_Ns3PacketTagList_methods(root_module, root_module['ns3::PacketTagList'])
    register_Ns3PacketTagListTagData_methods(root_module, root_module['ns3::PacketTagList::TagData'])
    register_Ns3PagingInfoListElement_s_methods(root_module, root_module['ns3::PagingInfoListElement_s'])
    register_Ns3ParameterLogger_methods(root_module, root_module['ns3::ParameterLogger'])
    register_Ns3PhichListElement_s_methods(root_module, root_module['ns3::PhichListElement_s'])
    register_Ns3PhyReceptionStatParameters_methods(root_module, root_module['ns3::PhyReceptionStatParameters'])
    register_Ns3PhyTransmissionStatParameters_methods(root_module, root_module['ns3::PhyTransmissionStatParameters'])
    register_Ns3RachListElement_s_methods(root_module, root_module['ns3::RachListElement_s'])
    register_Ns3Rectangle_methods(root_module, root_module['ns3::Rectangle'])
    register_Ns3RlcPduListElement_s_methods(root_module, root_module['ns3::RlcPduListElement_s'])
    register_Ns3SbMeasResult_s_methods(root_module, root_module['ns3::SbMeasResult_s'])
    register_Ns3SiConfiguration_s_methods(root_module, root_module['ns3::SiConfiguration_s'])
    register_Ns3SiMessageListElement_s_methods(root_module, root_module['ns3::SiMessageListElement_s'])
    register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    register_Ns3Simulator_methods(root_module, root_module['ns3::Simulator'])
    register_Ns3SpsConfig_s_methods(root_module, root_module['ns3::SpsConfig_s'])
    register_Ns3SrConfig_s_methods(root_module, root_module['ns3::SrConfig_s'])
    register_Ns3SrListElement_s_methods(root_module, root_module['ns3::SrListElement_s'])
    register_Ns3Tag_methods(root_module, root_module['ns3::Tag'])
    register_Ns3TagBuffer_methods(root_module, root_module['ns3::TagBuffer'])
    register_Ns3Tap_methods(root_module, root_module['ns3::Tap'])
    register_Ns3TbId_t_methods(root_module, root_module['ns3::TbId_t'])
    register_Ns3TimeWithUnit_methods(root_module, root_module['ns3::TimeWithUnit'])
    register_Ns3TransmissionModesLayers_methods(root_module, root_module['ns3::TransmissionModesLayers'])
    register_Ns3TypeId_methods(root_module, root_module['ns3::TypeId'])
    register_Ns3TypeIdAttributeInformation_methods(root_module, root_module['ns3::TypeId::AttributeInformation'])
    register_Ns3TypeIdTraceSourceInformation_methods(root_module, root_module['ns3::TypeId::TraceSourceInformation'])
    register_Ns3UanModesList_methods(root_module, root_module['ns3::UanModesList'])
    register_Ns3UanPacketArrival_methods(root_module, root_module['ns3::UanPacketArrival'])
    register_Ns3UanPdp_methods(root_module, root_module['ns3::UanPdp'])
    register_Ns3UanPhyListener_methods(root_module, root_module['ns3::UanPhyListener'])
    register_Ns3UanTxMode_methods(root_module, root_module['ns3::UanTxMode'])
    register_Ns3UanTxModeFactory_methods(root_module, root_module['ns3::UanTxModeFactory'])
    register_Ns3UeCapabilities_s_methods(root_module, root_module['ns3::UeCapabilities_s'])
    register_Ns3UeSelected_s_methods(root_module, root_module['ns3::UeSelected_s'])
    register_Ns3UlCqi_s_methods(root_module, root_module['ns3::UlCqi_s'])
    register_Ns3UlDciListElement_s_methods(root_module, root_module['ns3::UlDciListElement_s'])
    register_Ns3UlGrant_s_methods(root_module, root_module['ns3::UlGrant_s'])
    register_Ns3UlInfoListElement_s_methods(root_module, root_module['ns3::UlInfoListElement_s'])
    register_Ns3Vector2D_methods(root_module, root_module['ns3::Vector2D'])
    register_Ns3Vector3D_methods(root_module, root_module['ns3::Vector3D'])
    register_Ns3VendorSpecificListElement_s_methods(root_module, root_module['ns3::VendorSpecificListElement_s'])
    register_Ns3Empty_methods(root_module, root_module['ns3::empty'])
    register_Ns3Int64x64_t_methods(root_module, root_module['ns3::int64x64_t'])
    register_Ns3TbInfo_t_methods(root_module, root_module['ns3::tbInfo_t'])
    register_Ns3AnimByteTag_methods(root_module, root_module['ns3::AnimByteTag'])
    register_Ns3Chunk_methods(root_module, root_module['ns3::Chunk'])
    register_Ns3Header_methods(root_module, root_module['ns3::Header'])
    register_Ns3Ipv4Header_methods(root_module, root_module['ns3::Ipv4Header'])
    register_Ns3LteEnbRrcSapProvider_methods(root_module, root_module['ns3::LteEnbRrcSapProvider'])
    register_Ns3LteEnbRrcSapProviderCompleteSetupUeParameters_methods(root_module, root_module['ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters'])
    register_Ns3LteEnbRrcSapUser_methods(root_module, root_module['ns3::LteEnbRrcSapUser'])
    register_Ns3LteEnbRrcSapUserSetupUeParameters_methods(root_module, root_module['ns3::LteEnbRrcSapUser::SetupUeParameters'])
    register_Ns3Object_methods(root_module, root_module['ns3::Object'])
    register_Ns3ObjectAggregateIterator_methods(root_module, root_module['ns3::Object::AggregateIterator'])
    register_Ns3PacketBurst_methods(root_module, root_module['ns3::PacketBurst'])
    register_Ns3RandomVariableStream_methods(root_module, root_module['ns3::RandomVariableStream'])
    register_Ns3SequentialRandomVariable_methods(root_module, root_module['ns3::SequentialRandomVariable'])
    register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    register_Ns3SimpleRefCount__Ns3Ipv4MulticastRoute_Ns3Empty_Ns3DefaultDeleter__lt__ns3Ipv4MulticastRoute__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> >'])
    register_Ns3SimpleRefCount__Ns3Ipv4Route_Ns3Empty_Ns3DefaultDeleter__lt__ns3Ipv4Route__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> >'])
    register_Ns3SimpleRefCount__Ns3LteControlMessage_Ns3Empty_Ns3DefaultDeleter__lt__ns3LteControlMessage__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> >'])
    register_Ns3SimpleRefCount__Ns3LteHarqPhy_Ns3Empty_Ns3DefaultDeleter__lt__ns3LteHarqPhy__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> >'])
    register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >'])
    register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumModel_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumModel__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumSignalParameters_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumSignalParameters__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >'])
    register_Ns3SimpleRefCount__Ns3SpectrumValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >'])
    register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    register_Ns3SimpleRefCount__Ns3VendorSpecificValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3VendorSpecificValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> >'])
    register_Ns3Socket_methods(root_module, root_module['ns3::Socket'])
    register_Ns3SocketAddressTag_methods(root_module, root_module['ns3::SocketAddressTag'])
    register_Ns3SocketIpTosTag_methods(root_module, root_module['ns3::SocketIpTosTag'])
    register_Ns3SocketIpTtlTag_methods(root_module, root_module['ns3::SocketIpTtlTag'])
    register_Ns3SocketIpv6HopLimitTag_methods(root_module, root_module['ns3::SocketIpv6HopLimitTag'])
    register_Ns3SocketIpv6TclassTag_methods(root_module, root_module['ns3::SocketIpv6TclassTag'])
    register_Ns3SocketSetDontFragmentTag_methods(root_module, root_module['ns3::SocketSetDontFragmentTag'])
    register_Ns3SpectrumInterference_methods(root_module, root_module['ns3::SpectrumInterference'])
    register_Ns3SpectrumModel_methods(root_module, root_module['ns3::SpectrumModel'])
    register_Ns3SpectrumPhy_methods(root_module, root_module['ns3::SpectrumPhy'])
    register_Ns3SpectrumSignalParameters_methods(root_module, root_module['ns3::SpectrumSignalParameters'])
    register_Ns3SpectrumValue_methods(root_module, root_module['ns3::SpectrumValue'])
    register_Ns3Time_methods(root_module, root_module['ns3::Time'])
    register_Ns3TraceSourceAccessor_methods(root_module, root_module['ns3::TraceSourceAccessor'])
    register_Ns3Trailer_methods(root_module, root_module['ns3::Trailer'])
    register_Ns3TriangularRandomVariable_methods(root_module, root_module['ns3::TriangularRandomVariable'])
    register_Ns3UanMac_methods(root_module, root_module['ns3::UanMac'])
    register_Ns3UanPhy_methods(root_module, root_module['ns3::UanPhy'])
    register_Ns3UanPhyCalcSinr_methods(root_module, root_module['ns3::UanPhyCalcSinr'])
    register_Ns3UanPhyCalcSinrDefault_methods(root_module, root_module['ns3::UanPhyCalcSinrDefault'])
    register_Ns3UanPhyCalcSinrFhFsk_methods(root_module, root_module['ns3::UanPhyCalcSinrFhFsk'])
    register_Ns3UanPhyGen_methods(root_module, root_module['ns3::UanPhyGen'])
    register_Ns3UanPhyPer_methods(root_module, root_module['ns3::UanPhyPer'])
    register_Ns3UanPhyPerGenDefault_methods(root_module, root_module['ns3::UanPhyPerGenDefault'])
    register_Ns3UanPhyPerUmodem_methods(root_module, root_module['ns3::UanPhyPerUmodem'])
    register_Ns3UanPropModel_methods(root_module, root_module['ns3::UanPropModel'])
    register_Ns3UanTransducer_methods(root_module, root_module['ns3::UanTransducer'])
    register_Ns3UniformRandomVariable_methods(root_module, root_module['ns3::UniformRandomVariable'])
    register_Ns3VendorSpecificValue_methods(root_module, root_module['ns3::VendorSpecificValue'])
    register_Ns3WeibullRandomVariable_methods(root_module, root_module['ns3::WeibullRandomVariable'])
    register_Ns3ZetaRandomVariable_methods(root_module, root_module['ns3::ZetaRandomVariable'])
    register_Ns3ZipfRandomVariable_methods(root_module, root_module['ns3::ZipfRandomVariable'])
    register_Ns3AttributeAccessor_methods(root_module, root_module['ns3::AttributeAccessor'])
    register_Ns3AttributeChecker_methods(root_module, root_module['ns3::AttributeChecker'])
    register_Ns3AttributeValue_methods(root_module, root_module['ns3::AttributeValue'])
    register_Ns3CallbackChecker_methods(root_module, root_module['ns3::CallbackChecker'])
    register_Ns3CallbackImplBase_methods(root_module, root_module['ns3::CallbackImplBase'])
    register_Ns3CallbackValue_methods(root_module, root_module['ns3::CallbackValue'])
    register_Ns3Channel_methods(root_module, root_module['ns3::Channel'])
    register_Ns3ConstantRandomVariable_methods(root_module, root_module['ns3::ConstantRandomVariable'])
    register_Ns3DataRateChecker_methods(root_module, root_module['ns3::DataRateChecker'])
    register_Ns3DataRateValue_methods(root_module, root_module['ns3::DataRateValue'])
    register_Ns3DeterministicRandomVariable_methods(root_module, root_module['ns3::DeterministicRandomVariable'])
    register_Ns3DeviceEnergyModel_methods(root_module, root_module['ns3::DeviceEnergyModel'])
    register_Ns3EmpiricalRandomVariable_methods(root_module, root_module['ns3::EmpiricalRandomVariable'])
    register_Ns3EmptyAttributeValue_methods(root_module, root_module['ns3::EmptyAttributeValue'])
    register_Ns3ErlangRandomVariable_methods(root_module, root_module['ns3::ErlangRandomVariable'])
    register_Ns3EventImpl_methods(root_module, root_module['ns3::EventImpl'])
    register_Ns3ExponentialRandomVariable_methods(root_module, root_module['ns3::ExponentialRandomVariable'])
    register_Ns3GammaRandomVariable_methods(root_module, root_module['ns3::GammaRandomVariable'])
    register_Ns3Ipv4_methods(root_module, root_module['ns3::Ipv4'])
    register_Ns3Ipv4AddressChecker_methods(root_module, root_module['ns3::Ipv4AddressChecker'])
    register_Ns3Ipv4AddressValue_methods(root_module, root_module['ns3::Ipv4AddressValue'])
    register_Ns3Ipv4L3Protocol_methods(root_module, root_module['ns3::Ipv4L3Protocol'])
    register_Ns3Ipv4MaskChecker_methods(root_module, root_module['ns3::Ipv4MaskChecker'])
    register_Ns3Ipv4MaskValue_methods(root_module, root_module['ns3::Ipv4MaskValue'])
    register_Ns3Ipv4MulticastRoute_methods(root_module, root_module['ns3::Ipv4MulticastRoute'])
    register_Ns3Ipv4Route_methods(root_module, root_module['ns3::Ipv4Route'])
    register_Ns3Ipv4RoutingProtocol_methods(root_module, root_module['ns3::Ipv4RoutingProtocol'])
    register_Ns3Ipv6AddressChecker_methods(root_module, root_module['ns3::Ipv6AddressChecker'])
    register_Ns3Ipv6AddressValue_methods(root_module, root_module['ns3::Ipv6AddressValue'])
    register_Ns3Ipv6PrefixChecker_methods(root_module, root_module['ns3::Ipv6PrefixChecker'])
    register_Ns3Ipv6PrefixValue_methods(root_module, root_module['ns3::Ipv6PrefixValue'])
    register_Ns3LogNormalRandomVariable_methods(root_module, root_module['ns3::LogNormalRandomVariable'])
    register_Ns3LteControlMessage_methods(root_module, root_module['ns3::LteControlMessage'])
    register_Ns3LteHarqPhy_methods(root_module, root_module['ns3::LteHarqPhy'])
    register_Ns3LteInterference_methods(root_module, root_module['ns3::LteInterference'])
    register_Ns3LtePhy_methods(root_module, root_module['ns3::LtePhy'])
    register_Ns3LteSpectrumPhy_methods(root_module, root_module['ns3::LteSpectrumPhy'])
    register_Ns3Mac48AddressChecker_methods(root_module, root_module['ns3::Mac48AddressChecker'])
    register_Ns3Mac48AddressValue_methods(root_module, root_module['ns3::Mac48AddressValue'])
    register_Ns3MibLteControlMessage_methods(root_module, root_module['ns3::MibLteControlMessage'])
    register_Ns3MobilityModel_methods(root_module, root_module['ns3::MobilityModel'])
    register_Ns3NetDevice_methods(root_module, root_module['ns3::NetDevice'])
    register_Ns3NixVector_methods(root_module, root_module['ns3::NixVector'])
    register_Ns3Node_methods(root_module, root_module['ns3::Node'])
    register_Ns3NormalRandomVariable_methods(root_module, root_module['ns3::NormalRandomVariable'])
    register_Ns3ObjectFactoryChecker_methods(root_module, root_module['ns3::ObjectFactoryChecker'])
    register_Ns3ObjectFactoryValue_methods(root_module, root_module['ns3::ObjectFactoryValue'])
    register_Ns3OutputStreamWrapper_methods(root_module, root_module['ns3::OutputStreamWrapper'])
    register_Ns3Packet_methods(root_module, root_module['ns3::Packet'])
    register_Ns3ParetoRandomVariable_methods(root_module, root_module['ns3::ParetoRandomVariable'])
    register_Ns3RachPreambleLteControlMessage_methods(root_module, root_module['ns3::RachPreambleLteControlMessage'])
    register_Ns3RarLteControlMessage_methods(root_module, root_module['ns3::RarLteControlMessage'])
    register_Ns3RarLteControlMessageRar_methods(root_module, root_module['ns3::RarLteControlMessage::Rar'])
    register_Ns3RectangleChecker_methods(root_module, root_module['ns3::RectangleChecker'])
    register_Ns3RectangleValue_methods(root_module, root_module['ns3::RectangleValue'])
    register_Ns3Sib1LteControlMessage_methods(root_module, root_module['ns3::Sib1LteControlMessage'])
    register_Ns3SpectrumChannel_methods(root_module, root_module['ns3::SpectrumChannel'])
    register_Ns3TimeValue_methods(root_module, root_module['ns3::TimeValue'])
    register_Ns3TypeIdChecker_methods(root_module, root_module['ns3::TypeIdChecker'])
    register_Ns3TypeIdValue_methods(root_module, root_module['ns3::TypeIdValue'])
    register_Ns3UanModesListChecker_methods(root_module, root_module['ns3::UanModesListChecker'])
    register_Ns3UanModesListValue_methods(root_module, root_module['ns3::UanModesListValue'])
    register_Ns3UintegerValue_methods(root_module, root_module['ns3::UintegerValue'])
    register_Ns3UlDciLteControlMessage_methods(root_module, root_module['ns3::UlDciLteControlMessage'])
    register_Ns3Vector2DChecker_methods(root_module, root_module['ns3::Vector2DChecker'])
    register_Ns3Vector2DValue_methods(root_module, root_module['ns3::Vector2DValue'])
    register_Ns3Vector3DChecker_methods(root_module, root_module['ns3::Vector3DChecker'])
    register_Ns3Vector3DValue_methods(root_module, root_module['ns3::Vector3DValue'])
    register_Ns3AddressChecker_methods(root_module, root_module['ns3::AddressChecker'])
    register_Ns3AddressValue_methods(root_module, root_module['ns3::AddressValue'])
    register_Ns3BsrLteControlMessage_methods(root_module, root_module['ns3::BsrLteControlMessage'])
    register_Ns3DlCqiLteControlMessage_methods(root_module, root_module['ns3::DlCqiLteControlMessage'])
    register_Ns3DlDciLteControlMessage_methods(root_module, root_module['ns3::DlDciLteControlMessage'])
    register_Ns3DlHarqFeedbackLteControlMessage_methods(root_module, root_module['ns3::DlHarqFeedbackLteControlMessage'])
    register_Ns3LteNetDevice_methods(root_module, root_module['ns3::LteNetDevice'])
    register_Ns3LteUeNetDevice_methods(root_module, root_module['ns3::LteUeNetDevice'])
    register_Ns3LteEnbNetDevice_methods(root_module, root_module['ns3::LteEnbNetDevice'])
    register_Ns3ConfigMatchContainer_methods(root_module, root_module['ns3::Config::MatchContainer'])
    register_Ns3HashImplementation_methods(root_module, root_module['ns3::Hash::Implementation'])
    register_Ns3HashFunctionFnv1a_methods(root_module, root_module['ns3::Hash::Function::Fnv1a'])
    register_Ns3HashFunctionHash32_methods(root_module, root_module['ns3::Hash::Function::Hash32'])
    register_Ns3HashFunctionHash64_methods(root_module, root_module['ns3::Hash::Function::Hash64'])
    register_Ns3HashFunctionMurmur3_methods(root_module, root_module['ns3::Hash::Function::Murmur3'])
    return

def register_Ns3Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## address.h (module 'network'): ns3::Address::Address() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::Address::Address(uint8_t type, uint8_t const * buffer, uint8_t len) [constructor]
    cls.add_constructor([param('uint8_t', 'type'), param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): ns3::Address::Address(ns3::Address const & address) [copy constructor]
    cls.add_constructor([param('ns3::Address const &', 'address')])
    ## address.h (module 'network'): bool ns3::Address::CheckCompatible(uint8_t type, uint8_t len) const [member function]
    cls.add_method('CheckCompatible', 
                   'bool', 
                   [param('uint8_t', 'type'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyAllFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllTo(uint8_t * buffer, uint8_t len) const [member function]
    cls.add_method('CopyAllTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## address.h (module 'network'): void ns3::Address::Deserialize(ns3::TagBuffer buffer) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')])
    ## address.h (module 'network'): uint8_t ns3::Address::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsInvalid() const [member function]
    cls.add_method('IsInvalid', 
                   'bool', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsMatchingType(uint8_t type) const [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('uint8_t', 'type')], 
                   is_const=True)
    ## address.h (module 'network'): static uint8_t ns3::Address::Register() [member function]
    cls.add_method('Register', 
                   'uint8_t', 
                   [], 
                   is_static=True)
    ## address.h (module 'network'): void ns3::Address::Serialize(ns3::TagBuffer buffer) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')], 
                   is_const=True)
    return

def register_Ns3AllocationRetentionPriority_methods(root_module, cls):
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority::AllocationRetentionPriority(ns3::AllocationRetentionPriority const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AllocationRetentionPriority const &', 'arg0')])
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority::AllocationRetentionPriority() [constructor]
    cls.add_constructor([])
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority::preemptionCapability [variable]
    cls.add_instance_attribute('preemptionCapability', 'bool', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority::preemptionVulnerability [variable]
    cls.add_instance_attribute('preemptionVulnerability', 'bool', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::AllocationRetentionPriority::priorityLevel [variable]
    cls.add_instance_attribute('priorityLevel', 'uint8_t', is_const=False)
    return

def register_Ns3AnimationInterface_methods(root_module, cls):
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface::AnimationInterface(ns3::AnimationInterface const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AnimationInterface const &', 'arg0')])
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface::AnimationInterface(std::string const filename) [constructor]
    cls.add_constructor([param('std::string const', 'filename')])
    ## animation-interface.h (module 'netanim'): uint32_t ns3::AnimationInterface::AddNodeCounter(std::string counterName, ns3::AnimationInterface::CounterType counterType) [member function]
    cls.add_method('AddNodeCounter', 
                   'uint32_t', 
                   [param('std::string', 'counterName'), param('ns3::AnimationInterface::CounterType', 'counterType')])
    ## animation-interface.h (module 'netanim'): uint32_t ns3::AnimationInterface::AddResource(std::string resourcePath) [member function]
    cls.add_method('AddResource', 
                   'uint32_t', 
                   [param('std::string', 'resourcePath')])
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface & ns3::AnimationInterface::AddSourceDestination(uint32_t fromNodeId, std::string destinationIpv4Address) [member function]
    cls.add_method('AddSourceDestination', 
                   'ns3::AnimationInterface &', 
                   [param('uint32_t', 'fromNodeId'), param('std::string', 'destinationIpv4Address')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::EnableIpv4L3ProtocolCounters(ns3::Time startTime, ns3::Time stopTime, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableIpv4L3ProtocolCounters', 
                   'void', 
                   [param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface & ns3::AnimationInterface::EnableIpv4RouteTracking(std::string fileName, ns3::Time startTime, ns3::Time stopTime, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableIpv4RouteTracking', 
                   'ns3::AnimationInterface &', 
                   [param('std::string', 'fileName'), param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): ns3::AnimationInterface & ns3::AnimationInterface::EnableIpv4RouteTracking(std::string fileName, ns3::Time startTime, ns3::Time stopTime, ns3::NodeContainer nc, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableIpv4RouteTracking', 
                   'ns3::AnimationInterface &', 
                   [param('std::string', 'fileName'), param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::NodeContainer', 'nc'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::EnablePacketMetadata(bool enable=true) [member function]
    cls.add_method('EnablePacketMetadata', 
                   'void', 
                   [param('bool', 'enable', default_value='true')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::EnableQueueCounters(ns3::Time startTime, ns3::Time stopTime, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableQueueCounters', 
                   'void', 
                   [param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::EnableWifiMacCounters(ns3::Time startTime, ns3::Time stopTime, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableWifiMacCounters', 
                   'void', 
                   [param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::EnableWifiPhyCounters(ns3::Time startTime, ns3::Time stopTime, ns3::Time pollInterval=ns3::Seconds( )) [member function]
    cls.add_method('EnableWifiPhyCounters', 
                   'void', 
                   [param('ns3::Time', 'startTime'), param('ns3::Time', 'stopTime'), param('ns3::Time', 'pollInterval', default_value='ns3::Seconds(0)')])
    ## animation-interface.h (module 'netanim'): double ns3::AnimationInterface::GetNodeEnergyFraction(ns3::Ptr<const ns3::Node> node) const [member function]
    cls.add_method('GetNodeEnergyFraction', 
                   'double', 
                   [param('ns3::Ptr< ns3::Node const >', 'node')], 
                   is_const=True)
    ## animation-interface.h (module 'netanim'): uint64_t ns3::AnimationInterface::GetTracePktCount() [member function]
    cls.add_method('GetTracePktCount', 
                   'uint64_t', 
                   [])
    ## animation-interface.h (module 'netanim'): static bool ns3::AnimationInterface::IsInitialized() [member function]
    cls.add_method('IsInitialized', 
                   'bool', 
                   [], 
                   is_static=True)
    ## animation-interface.h (module 'netanim'): bool ns3::AnimationInterface::IsStarted() [member function]
    cls.add_method('IsStarted', 
                   'bool', 
                   [])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::ResetAnimWriteCallback() [member function]
    cls.add_method('ResetAnimWriteCallback', 
                   'void', 
                   [])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetAnimWriteCallback(void (*)( char const * ) * cb) [member function]
    cls.add_method('SetAnimWriteCallback', 
                   'void', 
                   [param('void ( * ) ( char const * ) *', 'cb')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetBackgroundImage(std::string fileName, double x, double y, double scaleX, double scaleY, double opacity) [member function]
    cls.add_method('SetBackgroundImage', 
                   'void', 
                   [param('std::string', 'fileName'), param('double', 'x'), param('double', 'y'), param('double', 'scaleX'), param('double', 'scaleY'), param('double', 'opacity')])
    ## animation-interface.h (module 'netanim'): static void ns3::AnimationInterface::SetConstantPosition(ns3::Ptr<ns3::Node> n, double x, double y, double z=0) [member function]
    cls.add_method('SetConstantPosition', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'n'), param('double', 'x'), param('double', 'y'), param('double', 'z', default_value='0')], 
                   is_static=True)
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetMaxPktsPerTraceFile(uint64_t maxPktsPerFile) [member function]
    cls.add_method('SetMaxPktsPerTraceFile', 
                   'void', 
                   [param('uint64_t', 'maxPktsPerFile')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetMobilityPollInterval(ns3::Time t) [member function]
    cls.add_method('SetMobilityPollInterval', 
                   'void', 
                   [param('ns3::Time', 't')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetStartTime(ns3::Time t) [member function]
    cls.add_method('SetStartTime', 
                   'void', 
                   [param('ns3::Time', 't')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SetStopTime(ns3::Time t) [member function]
    cls.add_method('SetStopTime', 
                   'void', 
                   [param('ns3::Time', 't')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::SkipPacketTracing() [member function]
    cls.add_method('SkipPacketTracing', 
                   'void', 
                   [])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateLinkDescription(uint32_t fromNode, uint32_t toNode, std::string linkDescription) [member function]
    cls.add_method('UpdateLinkDescription', 
                   'void', 
                   [param('uint32_t', 'fromNode'), param('uint32_t', 'toNode'), param('std::string', 'linkDescription')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateLinkDescription(ns3::Ptr<ns3::Node> fromNode, ns3::Ptr<ns3::Node> toNode, std::string linkDescription) [member function]
    cls.add_method('UpdateLinkDescription', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'fromNode'), param('ns3::Ptr< ns3::Node >', 'toNode'), param('std::string', 'linkDescription')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeColor(ns3::Ptr<ns3::Node> n, uint8_t r, uint8_t g, uint8_t b) [member function]
    cls.add_method('UpdateNodeColor', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'n'), param('uint8_t', 'r'), param('uint8_t', 'g'), param('uint8_t', 'b')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeColor(uint32_t nodeId, uint8_t r, uint8_t g, uint8_t b) [member function]
    cls.add_method('UpdateNodeColor', 
                   'void', 
                   [param('uint32_t', 'nodeId'), param('uint8_t', 'r'), param('uint8_t', 'g'), param('uint8_t', 'b')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeCounter(uint32_t nodeCounterId, uint32_t nodeId, double counter) [member function]
    cls.add_method('UpdateNodeCounter', 
                   'void', 
                   [param('uint32_t', 'nodeCounterId'), param('uint32_t', 'nodeId'), param('double', 'counter')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeDescription(ns3::Ptr<ns3::Node> n, std::string descr) [member function]
    cls.add_method('UpdateNodeDescription', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'n'), param('std::string', 'descr')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeDescription(uint32_t nodeId, std::string descr) [member function]
    cls.add_method('UpdateNodeDescription', 
                   'void', 
                   [param('uint32_t', 'nodeId'), param('std::string', 'descr')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeImage(uint32_t nodeId, uint32_t resourceId) [member function]
    cls.add_method('UpdateNodeImage', 
                   'void', 
                   [param('uint32_t', 'nodeId'), param('uint32_t', 'resourceId')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimationInterface::UpdateNodeSize(uint32_t nodeId, double width, double height) [member function]
    cls.add_method('UpdateNodeSize', 
                   'void', 
                   [param('uint32_t', 'nodeId'), param('double', 'width'), param('double', 'height')])
    return

def register_Ns3AttributeConstructionList_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList(ns3::AttributeConstructionList const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): void ns3::AttributeConstructionList::Add(std::string name, ns3::Ptr<ns3::AttributeChecker const> checker, ns3::Ptr<ns3::AttributeValue> value) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::Ptr< ns3::AttributeValue >', 'value')])
    ## attribute-construction-list.h (module 'core'): std::_List_const_iterator<ns3::AttributeConstructionList::Item> ns3::AttributeConstructionList::Begin() const [member function]
    cls.add_method('Begin', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): std::_List_const_iterator<ns3::AttributeConstructionList::Item> ns3::AttributeConstructionList::End() const [member function]
    cls.add_method('End', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeConstructionList::Find(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('Find', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True)
    return

def register_Ns3AttributeConstructionListItem_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item(ns3::AttributeConstructionList::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList::Item const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::value [variable]
    cls.add_instance_attribute('value', 'ns3::Ptr< ns3::AttributeValue >', is_const=False)
    return

def register_Ns3BandInfo_methods(root_module, cls):
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::BandInfo() [constructor]
    cls.add_constructor([])
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::BandInfo(ns3::BandInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BandInfo const &', 'arg0')])
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fc [variable]
    cls.add_instance_attribute('fc', 'double', is_const=False)
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fh [variable]
    cls.add_instance_attribute('fh', 'double', is_const=False)
    ## spectrum-model.h (module 'spectrum'): ns3::BandInfo::fl [variable]
    cls.add_instance_attribute('fl', 'double', is_const=False)
    return

def register_Ns3Buffer_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Buffer() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize, bool initialize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize'), param('bool', 'initialize')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(ns3::Buffer const & o) [copy constructor]
    cls.add_constructor([param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): bool ns3::Buffer::AddAtEnd(uint32_t end) [member function]
    cls.add_method('AddAtEnd', 
                   'bool', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtEnd(ns3::Buffer const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): bool ns3::Buffer::AddAtStart(uint32_t start) [member function]
    cls.add_method('AddAtStart', 
                   'bool', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): ns3::Buffer ns3::Buffer::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Buffer', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## buffer.h (module 'network'): ns3::Buffer ns3::Buffer::CreateFullCopy() const [member function]
    cls.add_method('CreateFullCopy', 
                   'ns3::Buffer', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::End() const [member function]
    cls.add_method('End', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): int32_t ns3::Buffer::GetCurrentEndOffset() const [member function]
    cls.add_method('GetCurrentEndOffset', 
                   'int32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): int32_t ns3::Buffer::GetCurrentStartOffset() const [member function]
    cls.add_method('GetCurrentStartOffset', 
                   'int32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint8_t const * ns3::Buffer::PeekData() const [member function]
    cls.add_method('PeekData', 
                   'uint8_t const *', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3BufferIterator_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator(ns3::Buffer::Iterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Buffer::Iterator const &', 'arg0')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size, uint32_t initialChecksum) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size'), param('uint32_t', 'initialChecksum')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetDistanceFrom(ns3::Buffer::Iterator const & o) const [member function]
    cls.add_method('GetDistanceFrom', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator const &', 'o')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsEnd() const [member function]
    cls.add_method('IsEnd', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsStart() const [member function]
    cls.add_method('IsStart', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next(uint32_t delta) [member function]
    cls.add_method('Next', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::PeekU8() [member function]
    cls.add_method('PeekU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev() [member function]
    cls.add_method('Prev', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev(uint32_t delta) [member function]
    cls.add_method('Prev', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(ns3::Buffer::Iterator start, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadLsbtohU16() [member function]
    cls.add_method('ReadLsbtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadLsbtohU32() [member function]
    cls.add_method('ReadLsbtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadLsbtohU64() [member function]
    cls.add_method('ReadLsbtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadNtohU16() [member function]
    cls.add_method('ReadNtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadNtohU32() [member function]
    cls.add_method('ReadNtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadNtohU64() [member function]
    cls.add_method('ReadNtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(ns3::Buffer::Iterator start, ns3::Buffer::Iterator end) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU16(uint16_t data) [member function]
    cls.add_method('WriteHtolsbU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU32(uint32_t data) [member function]
    cls.add_method('WriteHtolsbU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU64(uint64_t data) [member function]
    cls.add_method('WriteHtolsbU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU16(uint16_t data) [member function]
    cls.add_method('WriteHtonU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU32(uint32_t data) [member function]
    cls.add_method('WriteHtonU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU64(uint64_t data) [member function]
    cls.add_method('WriteHtonU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU16(uint16_t data) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU32(uint32_t data) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU64(uint64_t data) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data, uint32_t len) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data'), param('uint32_t', 'len')])
    return

def register_Ns3BufferSizeLevelBsr_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::BufferSizeLevelBsr::BufferSizeLevelBsr() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::BufferSizeLevelBsr::BufferSizeLevelBsr(ns3::BufferSizeLevelBsr const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BufferSizeLevelBsr const &', 'arg0')])
    ## lte-common.h (module 'lte'): static uint32_t ns3::BufferSizeLevelBsr::BsrId2BufferSize(uint8_t val) [member function]
    cls.add_method('BsrId2BufferSize', 
                   'uint32_t', 
                   [param('uint8_t', 'val')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static uint8_t ns3::BufferSizeLevelBsr::BufferSize2BsrId(uint32_t val) [member function]
    cls.add_method('BufferSize2BsrId', 
                   'uint8_t', 
                   [param('uint32_t', 'val')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): ns3::BufferSizeLevelBsr::m_bufferSizeLevelBsr [variable]
    cls.add_static_attribute('m_bufferSizeLevelBsr', 'int [ 64 ]', is_const=False)
    return

def register_Ns3BuildBroadcastListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::BuildBroadcastListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::BuildBroadcastListElement_s(ns3::BuildBroadcastListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BuildBroadcastListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::m_dci [variable]
    cls.add_instance_attribute('m_dci', 'ns3::DlDciListElement_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::m_index [variable]
    cls.add_instance_attribute('m_index', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildBroadcastListElement_s::m_type [variable]
    cls.add_instance_attribute('m_type', 'ns3::BuildBroadcastListElement_s::Type_e', is_const=False)
    return

def register_Ns3BuildDataListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::BuildDataListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::BuildDataListElement_s(ns3::BuildDataListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BuildDataListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::m_ceBitmap [variable]
    cls.add_instance_attribute('m_ceBitmap', 'std::vector< ns3::CeBitmap_e >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::m_dci [variable]
    cls.add_instance_attribute('m_dci', 'ns3::DlDciListElement_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::m_rlcPduList [variable]
    cls.add_instance_attribute('m_rlcPduList', 'std::vector< std::vector< ns3::RlcPduListElement_s > >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildDataListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3BuildRarListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s::BuildRarListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s::BuildRarListElement_s(ns3::BuildRarListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BuildRarListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s::m_dci [variable]
    cls.add_instance_attribute('m_dci', 'ns3::DlDciListElement_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s::m_grant [variable]
    cls.add_instance_attribute('m_grant', 'ns3::UlGrant_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BuildRarListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3BwPart_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s::BwPart_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s::BwPart_s(ns3::BwPart_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BwPart_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s::m_bwPartIndex [variable]
    cls.add_instance_attribute('m_bwPartIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s::m_cqi [variable]
    cls.add_instance_attribute('m_cqi', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::BwPart_s::m_sb [variable]
    cls.add_instance_attribute('m_sb', 'uint8_t', is_const=False)
    return

def register_Ns3ByteTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::ByteTagIterator(ns3::ByteTagIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::ByteTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item ns3::ByteTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagIterator::Item', 
                   [])
    return

def register_Ns3ByteTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item::Item(ns3::ByteTagIterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetEnd() const [member function]
    cls.add_method('GetEnd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetStart() const [member function]
    cls.add_method('GetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::ByteTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::ByteTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3ByteTagList_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList() [constructor]
    cls.add_constructor([])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList(ns3::ByteTagList const & o) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): ns3::TagBuffer ns3::ByteTagList::Add(ns3::TypeId tid, uint32_t bufferSize, int32_t start, int32_t end) [member function]
    cls.add_method('Add', 
                   'ns3::TagBuffer', 
                   [param('ns3::TypeId', 'tid'), param('uint32_t', 'bufferSize'), param('int32_t', 'start'), param('int32_t', 'end')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::Add(ns3::ByteTagList const & o) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtEnd(int32_t adjustment, int32_t appendOffset) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('int32_t', 'adjustment'), param('int32_t', 'appendOffset')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtStart(int32_t adjustment, int32_t prependOffset) [member function]
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('int32_t', 'adjustment'), param('int32_t', 'prependOffset')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator ns3::ByteTagList::Begin(int32_t offsetStart, int32_t offsetEnd) const [member function]
    cls.add_method('Begin', 
                   'ns3::ByteTagList::Iterator', 
                   [param('int32_t', 'offsetStart'), param('int32_t', 'offsetEnd')], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    return

def register_Ns3ByteTagListIterator_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Iterator(ns3::ByteTagList::Iterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): uint32_t ns3::ByteTagList::Iterator::GetOffsetStart() const [member function]
    cls.add_method('GetOffsetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): bool ns3::ByteTagList::Iterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item ns3::ByteTagList::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagList::Iterator::Item', 
                   [])
    return

def register_Ns3ByteTagListIteratorItem_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::ByteTagList::Iterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator::Item const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::TagBuffer buf) [constructor]
    cls.add_constructor([param('ns3::TagBuffer', 'buf')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::buf [variable]
    cls.add_instance_attribute('buf', 'ns3::TagBuffer', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::end [variable]
    cls.add_instance_attribute('end', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::size [variable]
    cls.add_instance_attribute('size', 'uint32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::start [variable]
    cls.add_instance_attribute('start', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3CallbackBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::CallbackBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::Ptr<ns3::CallbackImplBase> ns3::CallbackBase::GetImpl() const [member function]
    cls.add_method('GetImpl', 
                   'ns3::Ptr< ns3::CallbackImplBase >', 
                   [], 
                   is_const=True)
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::Ptr<ns3::CallbackImplBase> impl) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::CallbackImplBase >', 'impl')], 
                        visibility='protected')
    ## callback.h (module 'core'): static std::string ns3::CallbackBase::Demangle(std::string const & mangled) [member function]
    cls.add_method('Demangle', 
                   'std::string', 
                   [param('std::string const &', 'mangled')], 
                   is_static=True, visibility='protected')
    return

def register_Ns3CqiConfig_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s::CqiConfig_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s::CqiConfig_s(ns3::CqiConfig_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CqiConfig_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s::m_action [variable]
    cls.add_instance_attribute('m_action', 'ns3::SetupRelease_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s::m_cqiSchedInterval [variable]
    cls.add_instance_attribute('m_cqiSchedInterval', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiConfig_s::m_riSchedInterval [variable]
    cls.add_instance_attribute('m_riSchedInterval', 'uint8_t', is_const=False)
    return

def register_Ns3CqiListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::CqiListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::CqiListElement_s(ns3::CqiListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CqiListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_cqiType [variable]
    cls.add_instance_attribute('m_cqiType', 'ns3::CqiListElement_s::CqiType_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_ri [variable]
    cls.add_instance_attribute('m_ri', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_sbMeasResult [variable]
    cls.add_instance_attribute('m_sbMeasResult', 'ns3::SbMeasResult_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_wbCqi [variable]
    cls.add_instance_attribute('m_wbCqi', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::CqiListElement_s::m_wbPmi [variable]
    cls.add_instance_attribute('m_wbPmi', 'uint8_t', is_const=False)
    return

def register_Ns3DataRate_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>')
    cls.add_binary_comparison_operator('>=')
    ## data-rate.h (module 'network'): ns3::DataRate::DataRate(ns3::DataRate const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DataRate const &', 'arg0')])
    ## data-rate.h (module 'network'): ns3::DataRate::DataRate() [constructor]
    cls.add_constructor([])
    ## data-rate.h (module 'network'): ns3::DataRate::DataRate(uint64_t bps) [constructor]
    cls.add_constructor([param('uint64_t', 'bps')])
    ## data-rate.h (module 'network'): ns3::DataRate::DataRate(std::string rate) [constructor]
    cls.add_constructor([param('std::string', 'rate')])
    ## data-rate.h (module 'network'): double ns3::DataRate::CalculateTxTime(uint32_t bytes) const [member function]
    cls.add_method('CalculateTxTime', 
                   'double', 
                   [param('uint32_t', 'bytes')], 
                   is_const=True)
    ## data-rate.h (module 'network'): uint64_t ns3::DataRate::GetBitRate() const [member function]
    cls.add_method('GetBitRate', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3DlDciListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::DlDciListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::DlDciListElement_s(ns3::DlDciListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DlDciListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_aggrLevel [variable]
    cls.add_instance_attribute('m_aggrLevel', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_cceIndex [variable]
    cls.add_instance_attribute('m_cceIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_dai [variable]
    cls.add_instance_attribute('m_dai', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_dlPowerOffset [variable]
    cls.add_instance_attribute('m_dlPowerOffset', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_format [variable]
    cls.add_instance_attribute('m_format', 'ns3::DlDciListElement_s::Format_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_harqProcess [variable]
    cls.add_instance_attribute('m_harqProcess', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_mcs [variable]
    cls.add_instance_attribute('m_mcs', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_nGap [variable]
    cls.add_instance_attribute('m_nGap', 'ns3::DlDciListElement_s::Ngap_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_ndi [variable]
    cls.add_instance_attribute('m_ndi', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_pdcchOrder [variable]
    cls.add_instance_attribute('m_pdcchOrder', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_pdcchPowerOffset [variable]
    cls.add_instance_attribute('m_pdcchPowerOffset', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_prachMaskIndex [variable]
    cls.add_instance_attribute('m_prachMaskIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_preambleIndex [variable]
    cls.add_instance_attribute('m_preambleIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_precodingInfo [variable]
    cls.add_instance_attribute('m_precodingInfo', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_rbBitmap [variable]
    cls.add_instance_attribute('m_rbBitmap', 'uint32_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_rbShift [variable]
    cls.add_instance_attribute('m_rbShift', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_resAlloc [variable]
    cls.add_instance_attribute('m_resAlloc', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_rv [variable]
    cls.add_instance_attribute('m_rv', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_spsRelease [variable]
    cls.add_instance_attribute('m_spsRelease', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_tbSwap [variable]
    cls.add_instance_attribute('m_tbSwap', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_tbsIdx [variable]
    cls.add_instance_attribute('m_tbsIdx', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_tbsSize [variable]
    cls.add_instance_attribute('m_tbsSize', 'std::vector< unsigned short >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_tpc [variable]
    cls.add_instance_attribute('m_tpc', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlDciListElement_s::m_vrbFormat [variable]
    cls.add_instance_attribute('m_vrbFormat', 'ns3::DlDciListElement_s::VrbFormat_e', is_const=False)
    return

def register_Ns3DlInfoListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::DlInfoListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::DlInfoListElement_s(ns3::DlInfoListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DlInfoListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::m_harqProcessId [variable]
    cls.add_instance_attribute('m_harqProcessId', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::m_harqStatus [variable]
    cls.add_instance_attribute('m_harqStatus', 'std::vector< ns3::DlInfoListElement_s::HarqStatus_e >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DlInfoListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3DrxConfig_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::DrxConfig_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::DrxConfig_s(ns3::DrxConfig_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DrxConfig_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_drxInactivityTimer [variable]
    cls.add_instance_attribute('m_drxInactivityTimer', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_drxRetransmissionTimer [variable]
    cls.add_instance_attribute('m_drxRetransmissionTimer', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_drxShortCycleTimer [variable]
    cls.add_instance_attribute('m_drxShortCycleTimer', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_longDrxCycle [variable]
    cls.add_instance_attribute('m_longDrxCycle', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_longDrxCycleStartOffset [variable]
    cls.add_instance_attribute('m_longDrxCycleStartOffset', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_onDurationTimer [variable]
    cls.add_instance_attribute('m_onDurationTimer', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::DrxConfig_s::m_shortDrxCycle [variable]
    cls.add_instance_attribute('m_shortDrxCycle', 'uint16_t', is_const=False)
    return

def register_Ns3EpsBearer_methods(root_module, cls):
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::EpsBearer(ns3::EpsBearer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EpsBearer const &', 'arg0')])
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::EpsBearer() [constructor]
    cls.add_constructor([])
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::EpsBearer(ns3::EpsBearer::Qci x) [constructor]
    cls.add_constructor([param('ns3::EpsBearer::Qci', 'x')])
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::EpsBearer(ns3::EpsBearer::Qci x, ns3::GbrQosInformation y) [constructor]
    cls.add_constructor([param('ns3::EpsBearer::Qci', 'x'), param('ns3::GbrQosInformation', 'y')])
    ## eps-bearer.h (module 'lte'): uint16_t ns3::EpsBearer::GetPacketDelayBudgetMs() const [member function]
    cls.add_method('GetPacketDelayBudgetMs', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## eps-bearer.h (module 'lte'): double ns3::EpsBearer::GetPacketErrorLossRate() const [member function]
    cls.add_method('GetPacketErrorLossRate', 
                   'double', 
                   [], 
                   is_const=True)
    ## eps-bearer.h (module 'lte'): uint8_t ns3::EpsBearer::GetPriority() const [member function]
    cls.add_method('GetPriority', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## eps-bearer.h (module 'lte'): bool ns3::EpsBearer::IsGbr() const [member function]
    cls.add_method('IsGbr', 
                   'bool', 
                   [], 
                   is_const=True)
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::arp [variable]
    cls.add_instance_attribute('arp', 'ns3::AllocationRetentionPriority', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::gbrQosInfo [variable]
    cls.add_instance_attribute('gbrQosInfo', 'ns3::GbrQosInformation', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::EpsBearer::qci [variable]
    cls.add_instance_attribute('qci', 'ns3::EpsBearer::Qci', is_const=False)
    return

def register_Ns3EutranMeasurementMapping_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::EutranMeasurementMapping::EutranMeasurementMapping() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::EutranMeasurementMapping::EutranMeasurementMapping(ns3::EutranMeasurementMapping const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EutranMeasurementMapping const &', 'arg0')])
    ## lte-common.h (module 'lte'): static int8_t ns3::EutranMeasurementMapping::ActualA3Offset2IeValue(double a3OffsetDb) [member function]
    cls.add_method('ActualA3Offset2IeValue', 
                   'int8_t', 
                   [param('double', 'a3OffsetDb')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static uint8_t ns3::EutranMeasurementMapping::ActualHysteresis2IeValue(double hysteresisDb) [member function]
    cls.add_method('ActualHysteresis2IeValue', 
                   'uint8_t', 
                   [param('double', 'hysteresisDb')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static uint8_t ns3::EutranMeasurementMapping::Db2RsrqRange(double db) [member function]
    cls.add_method('Db2RsrqRange', 
                   'uint8_t', 
                   [param('double', 'db')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static uint8_t ns3::EutranMeasurementMapping::Dbm2RsrpRange(double dbm) [member function]
    cls.add_method('Dbm2RsrpRange', 
                   'uint8_t', 
                   [param('double', 'dbm')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::IeValue2ActualA3Offset(int8_t a3OffsetIeValue) [member function]
    cls.add_method('IeValue2ActualA3Offset', 
                   'double', 
                   [param('int8_t', 'a3OffsetIeValue')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::IeValue2ActualHysteresis(uint8_t hysteresisIeValue) [member function]
    cls.add_method('IeValue2ActualHysteresis', 
                   'double', 
                   [param('uint8_t', 'hysteresisIeValue')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::IeValue2ActualQQualMin(int8_t qQualMinIeValue) [member function]
    cls.add_method('IeValue2ActualQQualMin', 
                   'double', 
                   [param('int8_t', 'qQualMinIeValue')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::IeValue2ActualQRxLevMin(int8_t qRxLevMinIeValue) [member function]
    cls.add_method('IeValue2ActualQRxLevMin', 
                   'double', 
                   [param('int8_t', 'qRxLevMinIeValue')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::QuantizeRsrp(double v) [member function]
    cls.add_method('QuantizeRsrp', 
                   'double', 
                   [param('double', 'v')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::QuantizeRsrq(double v) [member function]
    cls.add_method('QuantizeRsrq', 
                   'double', 
                   [param('double', 'v')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::RsrpRange2Dbm(uint8_t range) [member function]
    cls.add_method('RsrpRange2Dbm', 
                   'double', 
                   [param('uint8_t', 'range')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::EutranMeasurementMapping::RsrqRange2Db(uint8_t range) [member function]
    cls.add_method('RsrqRange2Db', 
                   'double', 
                   [param('uint8_t', 'range')], 
                   is_static=True)
    return

def register_Ns3EventId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('==')
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::EventId const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EventId const &', 'arg0')])
    ## event-id.h (module 'core'): ns3::EventId::EventId() [constructor]
    cls.add_constructor([])
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::Ptr<ns3::EventImpl> const & impl, uint64_t ts, uint32_t context, uint32_t uid) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::EventImpl > const &', 'impl'), param('uint64_t', 'ts'), param('uint32_t', 'context'), param('uint32_t', 'uid')])
    ## event-id.h (module 'core'): void ns3::EventId::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint64_t ns3::EventId::GetTs() const [member function]
    cls.add_method('GetTs', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsExpired() const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsRunning() const [member function]
    cls.add_method('IsRunning', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): ns3::EventImpl * ns3::EventId::PeekEventImpl() const [member function]
    cls.add_method('PeekEventImpl', 
                   'ns3::EventImpl *', 
                   [], 
                   is_const=True)
    return

def register_Ns3GbrQosInformation_methods(root_module, cls):
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::GbrQosInformation(ns3::GbrQosInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::GbrQosInformation const &', 'arg0')])
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::GbrQosInformation() [constructor]
    cls.add_constructor([])
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::gbrDl [variable]
    cls.add_instance_attribute('gbrDl', 'uint64_t', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::gbrUl [variable]
    cls.add_instance_attribute('gbrUl', 'uint64_t', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::mbrDl [variable]
    cls.add_instance_attribute('mbrDl', 'uint64_t', is_const=False)
    ## eps-bearer.h (module 'lte'): ns3::GbrQosInformation::mbrUl [variable]
    cls.add_instance_attribute('mbrUl', 'uint64_t', is_const=False)
    return

def register_Ns3HarqProcessInfoElement_t_methods(root_module, cls):
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::HarqProcessInfoElement_t() [constructor]
    cls.add_constructor([])
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::HarqProcessInfoElement_t(ns3::HarqProcessInfoElement_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HarqProcessInfoElement_t const &', 'arg0')])
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::m_codeBits [variable]
    cls.add_instance_attribute('m_codeBits', 'uint16_t', is_const=False)
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::m_infoBits [variable]
    cls.add_instance_attribute('m_infoBits', 'uint16_t', is_const=False)
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::m_mi [variable]
    cls.add_instance_attribute('m_mi', 'double', is_const=False)
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoElement_t::m_rv [variable]
    cls.add_instance_attribute('m_rv', 'uint8_t', is_const=False)
    return

def register_Ns3Hasher_methods(root_module, cls):
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Hasher const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hasher const &', 'arg0')])
    ## hash.h (module 'core'): ns3::Hasher::Hasher() [constructor]
    cls.add_constructor([])
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Ptr<ns3::Hash::Implementation> hp) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Hash::Implementation >', 'hp')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(std::string const s) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(std::string const s) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): ns3::Hasher & ns3::Hasher::clear() [member function]
    cls.add_method('clear', 
                   'ns3::Hasher &', 
                   [])
    return

def register_Ns3HigherLayerSelected_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::HigherLayerSelected_s::HigherLayerSelected_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::HigherLayerSelected_s::HigherLayerSelected_s(ns3::HigherLayerSelected_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HigherLayerSelected_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::HigherLayerSelected_s::m_sbCqi [variable]
    cls.add_instance_attribute('m_sbCqi', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::HigherLayerSelected_s::m_sbPmi [variable]
    cls.add_instance_attribute('m_sbPmi', 'uint8_t', is_const=False)
    return

def register_Ns3ImsiLcidPair_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t::ImsiLcidPair_t(ns3::ImsiLcidPair_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ImsiLcidPair_t const &', 'arg0')])
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t::ImsiLcidPair_t() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t::ImsiLcidPair_t(uint64_t const a, uint8_t const b) [constructor]
    cls.add_constructor([param('uint64_t const', 'a'), param('uint8_t const', 'b')])
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t::m_imsi [variable]
    cls.add_instance_attribute('m_imsi', 'uint64_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::ImsiLcidPair_t::m_lcId [variable]
    cls.add_instance_attribute('m_lcId', 'uint8_t', is_const=False)
    return

def register_Ns3Inet6SocketAddress_methods(root_module, cls):
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(ns3::Inet6SocketAddress const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Inet6SocketAddress const &', 'arg0')])
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(ns3::Ipv6Address ipv6, uint16_t port) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address', 'ipv6'), param('uint16_t', 'port')])
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(ns3::Ipv6Address ipv6) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address', 'ipv6')])
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(uint16_t port) [constructor]
    cls.add_constructor([param('uint16_t', 'port')])
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(char const * ipv6, uint16_t port) [constructor]
    cls.add_constructor([param('char const *', 'ipv6'), param('uint16_t', 'port')])
    ## inet6-socket-address.h (module 'network'): ns3::Inet6SocketAddress::Inet6SocketAddress(char const * ipv6) [constructor]
    cls.add_constructor([param('char const *', 'ipv6')])
    ## inet6-socket-address.h (module 'network'): static ns3::Inet6SocketAddress ns3::Inet6SocketAddress::ConvertFrom(ns3::Address const & addr) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Inet6SocketAddress', 
                   [param('ns3::Address const &', 'addr')], 
                   is_static=True)
    ## inet6-socket-address.h (module 'network'): ns3::Ipv6Address ns3::Inet6SocketAddress::GetIpv6() const [member function]
    cls.add_method('GetIpv6', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## inet6-socket-address.h (module 'network'): uint16_t ns3::Inet6SocketAddress::GetPort() const [member function]
    cls.add_method('GetPort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## inet6-socket-address.h (module 'network'): static bool ns3::Inet6SocketAddress::IsMatchingType(ns3::Address const & addr) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'addr')], 
                   is_static=True)
    ## inet6-socket-address.h (module 'network'): void ns3::Inet6SocketAddress::SetIpv6(ns3::Ipv6Address ipv6) [member function]
    cls.add_method('SetIpv6', 
                   'void', 
                   [param('ns3::Ipv6Address', 'ipv6')])
    ## inet6-socket-address.h (module 'network'): void ns3::Inet6SocketAddress::SetPort(uint16_t port) [member function]
    cls.add_method('SetPort', 
                   'void', 
                   [param('uint16_t', 'port')])
    return

def register_Ns3InetSocketAddress_methods(root_module, cls):
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(ns3::InetSocketAddress const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::InetSocketAddress const &', 'arg0')])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(ns3::Ipv4Address ipv4, uint16_t port) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address', 'ipv4'), param('uint16_t', 'port')])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(ns3::Ipv4Address ipv4) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address', 'ipv4')])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(uint16_t port) [constructor]
    cls.add_constructor([param('uint16_t', 'port')])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(char const * ipv4, uint16_t port) [constructor]
    cls.add_constructor([param('char const *', 'ipv4'), param('uint16_t', 'port')])
    ## inet-socket-address.h (module 'network'): ns3::InetSocketAddress::InetSocketAddress(char const * ipv4) [constructor]
    cls.add_constructor([param('char const *', 'ipv4')])
    ## inet-socket-address.h (module 'network'): static ns3::InetSocketAddress ns3::InetSocketAddress::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::InetSocketAddress', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## inet-socket-address.h (module 'network'): ns3::Ipv4Address ns3::InetSocketAddress::GetIpv4() const [member function]
    cls.add_method('GetIpv4', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## inet-socket-address.h (module 'network'): uint16_t ns3::InetSocketAddress::GetPort() const [member function]
    cls.add_method('GetPort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## inet-socket-address.h (module 'network'): static bool ns3::InetSocketAddress::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## inet-socket-address.h (module 'network'): void ns3::InetSocketAddress::SetIpv4(ns3::Ipv4Address address) [member function]
    cls.add_method('SetIpv4', 
                   'void', 
                   [param('ns3::Ipv4Address', 'address')])
    ## inet-socket-address.h (module 'network'): void ns3::InetSocketAddress::SetPort(uint16_t port) [member function]
    cls.add_method('SetPort', 
                   'void', 
                   [param('uint16_t', 'port')])
    return

def register_Ns3Ipv4Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(ns3::Ipv4Address const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(uint32_t address) [constructor]
    cls.add_constructor([param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::CombineMask(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('CombineMask', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv4Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Address::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::GetSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('GetSubnetDirectedBroadcast', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsEqual(ns3::Ipv4Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Address const &', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsLocalMulticast() const [member function]
    cls.add_method('IsLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static bool ns3::Ipv4Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('IsSubnetDirectedBroadcast', 
                   'bool', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(uint32_t address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    return

def register_Ns3Ipv4InterfaceAddress_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress::Ipv4InterfaceAddress() [constructor]
    cls.add_constructor([])
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress::Ipv4InterfaceAddress(ns3::Ipv4Address local, ns3::Ipv4Mask mask) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address', 'local'), param('ns3::Ipv4Mask', 'mask')])
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress::Ipv4InterfaceAddress(ns3::Ipv4InterfaceAddress const & o) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4InterfaceAddress const &', 'o')])
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4InterfaceAddress::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4InterfaceAddress::GetLocal() const [member function]
    cls.add_method('GetLocal', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4Mask ns3::Ipv4InterfaceAddress::GetMask() const [member function]
    cls.add_method('GetMask', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_const=True)
    ## ipv4-interface-address.h (module 'internet'): ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e ns3::Ipv4InterfaceAddress::GetScope() const [member function]
    cls.add_method('GetScope', 
                   'ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e', 
                   [], 
                   is_const=True)
    ## ipv4-interface-address.h (module 'internet'): bool ns3::Ipv4InterfaceAddress::IsSecondary() const [member function]
    cls.add_method('IsSecondary', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetBroadcast(ns3::Ipv4Address broadcast) [member function]
    cls.add_method('SetBroadcast', 
                   'void', 
                   [param('ns3::Ipv4Address', 'broadcast')])
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetLocal(ns3::Ipv4Address local) [member function]
    cls.add_method('SetLocal', 
                   'void', 
                   [param('ns3::Ipv4Address', 'local')])
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetMask(ns3::Ipv4Mask mask) [member function]
    cls.add_method('SetMask', 
                   'void', 
                   [param('ns3::Ipv4Mask', 'mask')])
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetPrimary() [member function]
    cls.add_method('SetPrimary', 
                   'void', 
                   [])
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetScope(ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e scope) [member function]
    cls.add_method('SetScope', 
                   'void', 
                   [param('ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e', 'scope')])
    ## ipv4-interface-address.h (module 'internet'): void ns3::Ipv4InterfaceAddress::SetSecondary() [member function]
    cls.add_method('SetSecondary', 
                   'void', 
                   [])
    return

def register_Ns3Ipv4Mask_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(ns3::Ipv4Mask const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(uint32_t mask) [constructor]
    cls.add_constructor([param('uint32_t', 'mask')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(char const * mask) [constructor]
    cls.add_constructor([param('char const *', 'mask')])
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::GetInverse() const [member function]
    cls.add_method('GetInverse', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint16_t ns3::Ipv4Mask::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsEqual(ns3::Ipv4Mask other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Mask', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsMatch(ns3::Ipv4Address a, ns3::Ipv4Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'a'), param('ns3::Ipv4Address', 'b')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Set(uint32_t mask) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'mask')])
    return

def register_Ns3Ipv6Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(uint8_t * address) [constructor]
    cls.add_constructor([param('uint8_t *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const & addr) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const * addr) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const *', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6Address::CombinePrefix(ns3::Ipv6Prefix const & prefix) [member function]
    cls.add_method('CombinePrefix', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv6Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllHostsMulticast() [member function]
    cls.add_method('GetAllHostsMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllNodesMulticast() [member function]
    cls.add_method('GetAllNodesMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllRoutersMulticast() [member function]
    cls.add_method('GetAllRoutersMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv6Address::GetIpv4MappedAddress() const [member function]
    cls.add_method('GetIpv4MappedAddress', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllHostsMulticast() const [member function]
    cls.add_method('IsAllHostsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllNodesMulticast() const [member function]
    cls.add_method('IsAllNodesMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllRoutersMulticast() const [member function]
    cls.add_method('IsAllRoutersMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAny() const [member function]
    cls.add_method('IsAny', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsDocumentation() const [member function]
    cls.add_method('IsDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsEqual(ns3::Ipv6Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Address const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsIpv4MappedAddress() const [member function]
    cls.add_method('IsIpv4MappedAddress', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocal() const [member function]
    cls.add_method('IsLinkLocal', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocalMulticast() const [member function]
    cls.add_method('IsLinkLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLocalhost() const [member function]
    cls.add_method('IsLocalhost', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static bool ns3::Ipv6Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsSolicitedMulticast() const [member function]
    cls.add_method('IsSolicitedMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac16Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac48Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac64Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac16Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac48Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac64Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeIpv4MappedAddress(ns3::Ipv4Address addr) [member function]
    cls.add_method('MakeIpv4MappedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeSolicitedAddress(ns3::Ipv6Address addr) [member function]
    cls.add_method('MakeSolicitedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(uint8_t * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint8_t *', 'address')])
    return

def register_Ns3Ipv6Prefix_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t * prefix) [constructor]
    cls.add_constructor([param('uint8_t *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(char const * prefix) [constructor]
    cls.add_constructor([param('char const *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t prefix) [constructor]
    cls.add_constructor([param('uint8_t', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const & prefix) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const * prefix) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const *', 'prefix')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): uint8_t ns3::Ipv6Prefix::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsEqual(ns3::Ipv6Prefix const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Prefix const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsMatch(ns3::Ipv6Address a, ns3::Ipv6Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv6Address', 'a'), param('ns3::Ipv6Address', 'b')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    return

def register_Ns3LogComponent_methods(root_module, cls):
    ## log.h (module 'core'): ns3::LogComponent::LogComponent(ns3::LogComponent const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LogComponent const &', 'arg0')])
    ## log.h (module 'core'): ns3::LogComponent::LogComponent(std::string const & name, std::string const & file, ns3::LogLevel const mask=::ns3::LOG_NONE) [constructor]
    cls.add_constructor([param('std::string const &', 'name'), param('std::string const &', 'file'), param('ns3::LogLevel const', 'mask', default_value='::ns3::LOG_NONE')])
    ## log.h (module 'core'): void ns3::LogComponent::Disable(ns3::LogLevel const level) [member function]
    cls.add_method('Disable', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    ## log.h (module 'core'): void ns3::LogComponent::Enable(ns3::LogLevel const level) [member function]
    cls.add_method('Enable', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    ## log.h (module 'core'): std::string ns3::LogComponent::File() const [member function]
    cls.add_method('File', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): static std::map<std::basic_string<char, std::char_traits<char>, std::allocator<char> >,ns3::LogComponent*,std::less<std::basic_string<char, std::char_traits<char>, std::allocator<char> > >,std::allocator<std::pair<const std::basic_string<char, std::char_traits<char>, std::allocator<char> >, ns3::LogComponent*> > > * ns3::LogComponent::GetComponentList() [member function]
    cls.add_method('GetComponentList', 
                   'std::map< std::string, ns3::LogComponent * > *', 
                   [], 
                   is_static=True)
    ## log.h (module 'core'): static std::string ns3::LogComponent::GetLevelLabel(ns3::LogLevel const level) [member function]
    cls.add_method('GetLevelLabel', 
                   'std::string', 
                   [param('ns3::LogLevel const', 'level')], 
                   is_static=True)
    ## log.h (module 'core'): bool ns3::LogComponent::IsEnabled(ns3::LogLevel const level) const [member function]
    cls.add_method('IsEnabled', 
                   'bool', 
                   [param('ns3::LogLevel const', 'level')], 
                   is_const=True)
    ## log.h (module 'core'): bool ns3::LogComponent::IsNoneEnabled() const [member function]
    cls.add_method('IsNoneEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): char const * ns3::LogComponent::Name() const [member function]
    cls.add_method('Name', 
                   'char const *', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): void ns3::LogComponent::SetMask(ns3::LogLevel const level) [member function]
    cls.add_method('SetMask', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    return

def register_Ns3LogicalChannelConfigListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::LogicalChannelConfigListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::LogicalChannelConfigListElement_s(ns3::LogicalChannelConfigListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LogicalChannelConfigListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_direction [variable]
    cls.add_instance_attribute('m_direction', 'ns3::LogicalChannelConfigListElement_s::Direction_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_eRabGuaranteedBitrateDl [variable]
    cls.add_instance_attribute('m_eRabGuaranteedBitrateDl', 'uint64_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_eRabGuaranteedBitrateUl [variable]
    cls.add_instance_attribute('m_eRabGuaranteedBitrateUl', 'uint64_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_eRabMaximulBitrateDl [variable]
    cls.add_instance_attribute('m_eRabMaximulBitrateDl', 'uint64_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_eRabMaximulBitrateUl [variable]
    cls.add_instance_attribute('m_eRabMaximulBitrateUl', 'uint64_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_logicalChannelGroup [variable]
    cls.add_instance_attribute('m_logicalChannelGroup', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_logicalChannelIdentity [variable]
    cls.add_instance_attribute('m_logicalChannelIdentity', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_qci [variable]
    cls.add_instance_attribute('m_qci', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::LogicalChannelConfigListElement_s::m_qosBearerType [variable]
    cls.add_instance_attribute('m_qosBearerType', 'ns3::LogicalChannelConfigListElement_s::QosBearerType_e', is_const=False)
    return

def register_Ns3LteFfConverter_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::LteFfConverter::LteFfConverter() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::LteFfConverter::LteFfConverter(ns3::LteFfConverter const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteFfConverter const &', 'arg0')])
    ## lte-common.h (module 'lte'): static uint16_t ns3::LteFfConverter::double2fpS11dot3(double val) [member function]
    cls.add_method('double2fpS11dot3', 
                   'uint16_t', 
                   [param('double', 'val')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::LteFfConverter::fpS11dot3toDouble(uint16_t val) [member function]
    cls.add_method('fpS11dot3toDouble', 
                   'double', 
                   [param('uint16_t', 'val')], 
                   is_static=True)
    ## lte-common.h (module 'lte'): static double ns3::LteFfConverter::getMinFpS11dot3Value() [member function]
    cls.add_method('getMinFpS11dot3Value', 
                   'double', 
                   [], 
                   is_static=True)
    return

def register_Ns3LteFlowId_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t::LteFlowId_t(ns3::LteFlowId_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteFlowId_t const &', 'arg0')])
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t::LteFlowId_t() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t::LteFlowId_t(uint16_t const a, uint8_t const b) [constructor]
    cls.add_constructor([param('uint16_t const', 'a'), param('uint8_t const', 'b')])
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t::m_lcId [variable]
    cls.add_instance_attribute('m_lcId', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::LteFlowId_t::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSap_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LteRrcSap() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LteRrcSap(ns3::LteRrcSap const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): static double ns3::LteRrcSap::ConvertPdschConfigDedicated2Double(ns3::LteRrcSap::PdschConfigDedicated pdschConfigDedicated) [member function]
    cls.add_method('ConvertPdschConfigDedicated2Double', 
                   'double', 
                   [param('ns3::LteRrcSap::PdschConfigDedicated', 'pdschConfigDedicated')], 
                   is_static=True)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MaxReportCells [variable]
    cls.add_static_attribute('MaxReportCells', 'uint8_t const', is_const=True)
    return

def register_Ns3LteRrcSapAntennaInfoDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AntennaInfoDedicated::AntennaInfoDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AntennaInfoDedicated::AntennaInfoDedicated(ns3::LteRrcSap::AntennaInfoDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::AntennaInfoDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AntennaInfoDedicated::transmissionMode [variable]
    cls.add_instance_attribute('transmissionMode', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapAsConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::AsConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::AsConfig(ns3::LteRrcSap::AsConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::AsConfig const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceDlCarrierFreq [variable]
    cls.add_instance_attribute('sourceDlCarrierFreq', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceMasterInformationBlock [variable]
    cls.add_instance_attribute('sourceMasterInformationBlock', 'ns3::LteRrcSap::MasterInformationBlock', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceMeasConfig [variable]
    cls.add_instance_attribute('sourceMeasConfig', 'ns3::LteRrcSap::MeasConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceRadioResourceConfig [variable]
    cls.add_instance_attribute('sourceRadioResourceConfig', 'ns3::LteRrcSap::RadioResourceConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceSystemInformationBlockType1 [variable]
    cls.add_instance_attribute('sourceSystemInformationBlockType1', 'ns3::LteRrcSap::SystemInformationBlockType1', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceSystemInformationBlockType2 [variable]
    cls.add_instance_attribute('sourceSystemInformationBlockType2', 'ns3::LteRrcSap::SystemInformationBlockType2', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::AsConfig::sourceUeIdentity [variable]
    cls.add_instance_attribute('sourceUeIdentity', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapBlackCellsToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::BlackCellsToAddMod::BlackCellsToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::BlackCellsToAddMod::BlackCellsToAddMod(ns3::LteRrcSap::BlackCellsToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::BlackCellsToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::BlackCellsToAddMod::cellIndex [variable]
    cls.add_instance_attribute('cellIndex', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::BlackCellsToAddMod::physCellIdRange [variable]
    cls.add_instance_attribute('physCellIdRange', 'ns3::LteRrcSap::PhysCellIdRange', is_const=False)
    return

def register_Ns3LteRrcSapCarrierBandwidthEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierBandwidthEutra::CarrierBandwidthEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierBandwidthEutra::CarrierBandwidthEutra(ns3::LteRrcSap::CarrierBandwidthEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CarrierBandwidthEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierBandwidthEutra::dlBandwidth [variable]
    cls.add_instance_attribute('dlBandwidth', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierBandwidthEutra::ulBandwidth [variable]
    cls.add_instance_attribute('ulBandwidth', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapCarrierFreqEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierFreqEutra::CarrierFreqEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierFreqEutra::CarrierFreqEutra(ns3::LteRrcSap::CarrierFreqEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CarrierFreqEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierFreqEutra::dlCarrierFreq [variable]
    cls.add_instance_attribute('dlCarrierFreq', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CarrierFreqEutra::ulCarrierFreq [variable]
    cls.add_instance_attribute('ulCarrierFreq', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapCellAccessRelatedInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::CellAccessRelatedInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::CellAccessRelatedInfo(ns3::LteRrcSap::CellAccessRelatedInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CellAccessRelatedInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::cellIdentity [variable]
    cls.add_instance_attribute('cellIdentity', 'uint32_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::csgIdentity [variable]
    cls.add_instance_attribute('csgIdentity', 'uint32_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::csgIndication [variable]
    cls.add_instance_attribute('csgIndication', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellAccessRelatedInfo::plmnIdentityInfo [variable]
    cls.add_instance_attribute('plmnIdentityInfo', 'ns3::LteRrcSap::PlmnIdentityInfo', is_const=False)
    return

def register_Ns3LteRrcSapCellSelectionInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellSelectionInfo::CellSelectionInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellSelectionInfo::CellSelectionInfo(ns3::LteRrcSap::CellSelectionInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CellSelectionInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellSelectionInfo::qQualMin [variable]
    cls.add_instance_attribute('qQualMin', 'int8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellSelectionInfo::qRxLevMin [variable]
    cls.add_instance_attribute('qRxLevMin', 'int8_t', is_const=False)
    return

def register_Ns3LteRrcSapCellsToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod::CellsToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod::CellsToAddMod(ns3::LteRrcSap::CellsToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CellsToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod::cellIndex [variable]
    cls.add_instance_attribute('cellIndex', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod::cellIndividualOffset [variable]
    cls.add_instance_attribute('cellIndividualOffset', 'int8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CellsToAddMod::physCellId [variable]
    cls.add_instance_attribute('physCellId', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapCgiInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::CgiInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::CgiInfo(ns3::LteRrcSap::CgiInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::CgiInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::cellIdentity [variable]
    cls.add_instance_attribute('cellIdentity', 'uint32_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::plmnIdentity [variable]
    cls.add_instance_attribute('plmnIdentity', 'uint32_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::plmnIdentityList [variable]
    cls.add_instance_attribute('plmnIdentityList', 'std::list< unsigned int >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::CgiInfo::trackingAreaCode [variable]
    cls.add_instance_attribute('trackingAreaCode', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapDrbToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::DrbToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::DrbToAddMod(ns3::LteRrcSap::DrbToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::DrbToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::drbIdentity [variable]
    cls.add_instance_attribute('drbIdentity', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::epsBearerIdentity [variable]
    cls.add_instance_attribute('epsBearerIdentity', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::logicalChannelConfig [variable]
    cls.add_instance_attribute('logicalChannelConfig', 'ns3::LteRrcSap::LogicalChannelConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::logicalChannelIdentity [variable]
    cls.add_instance_attribute('logicalChannelIdentity', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::DrbToAddMod::rlcConfig [variable]
    cls.add_instance_attribute('rlcConfig', 'ns3::LteRrcSap::RlcConfig', is_const=False)
    return

def register_Ns3LteRrcSapFreqInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::FreqInfo::FreqInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::FreqInfo::FreqInfo(ns3::LteRrcSap::FreqInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::FreqInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::FreqInfo::ulBandwidth [variable]
    cls.add_instance_attribute('ulBandwidth', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::FreqInfo::ulCarrierFreq [variable]
    cls.add_instance_attribute('ulCarrierFreq', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapHandoverPreparationInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::HandoverPreparationInfo::HandoverPreparationInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::HandoverPreparationInfo::HandoverPreparationInfo(ns3::LteRrcSap::HandoverPreparationInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::HandoverPreparationInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::HandoverPreparationInfo::asConfig [variable]
    cls.add_instance_attribute('asConfig', 'ns3::LteRrcSap::AsConfig', is_const=False)
    return

def register_Ns3LteRrcSapLogicalChannelConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::LogicalChannelConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::LogicalChannelConfig(ns3::LteRrcSap::LogicalChannelConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::LogicalChannelConfig const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::bucketSizeDurationMs [variable]
    cls.add_instance_attribute('bucketSizeDurationMs', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::logicalChannelGroup [variable]
    cls.add_instance_attribute('logicalChannelGroup', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::prioritizedBitRateKbps [variable]
    cls.add_instance_attribute('prioritizedBitRateKbps', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::LogicalChannelConfig::priority [variable]
    cls.add_instance_attribute('priority', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMasterInformationBlock_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock::MasterInformationBlock() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock::MasterInformationBlock(ns3::LteRrcSap::MasterInformationBlock const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MasterInformationBlock const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock::dlBandwidth [variable]
    cls.add_instance_attribute('dlBandwidth', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock::systemFrameNumber [variable]
    cls.add_instance_attribute('systemFrameNumber', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::MeasConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::MeasConfig(ns3::LteRrcSap::MeasConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasConfig const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::haveMeasGapConfig [variable]
    cls.add_instance_attribute('haveMeasGapConfig', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::haveQuantityConfig [variable]
    cls.add_instance_attribute('haveQuantityConfig', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::haveSmeasure [variable]
    cls.add_instance_attribute('haveSmeasure', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::haveSpeedStatePars [variable]
    cls.add_instance_attribute('haveSpeedStatePars', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::measGapConfig [variable]
    cls.add_instance_attribute('measGapConfig', 'ns3::LteRrcSap::MeasGapConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::measIdToAddModList [variable]
    cls.add_instance_attribute('measIdToAddModList', 'std::list< ns3::LteRrcSap::MeasIdToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::measIdToRemoveList [variable]
    cls.add_instance_attribute('measIdToRemoveList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::measObjectToAddModList [variable]
    cls.add_instance_attribute('measObjectToAddModList', 'std::list< ns3::LteRrcSap::MeasObjectToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::measObjectToRemoveList [variable]
    cls.add_instance_attribute('measObjectToRemoveList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::quantityConfig [variable]
    cls.add_instance_attribute('quantityConfig', 'ns3::LteRrcSap::QuantityConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::reportConfigToAddModList [variable]
    cls.add_instance_attribute('reportConfigToAddModList', 'std::list< ns3::LteRrcSap::ReportConfigToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::reportConfigToRemoveList [variable]
    cls.add_instance_attribute('reportConfigToRemoveList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::sMeasure [variable]
    cls.add_instance_attribute('sMeasure', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasConfig::speedStatePars [variable]
    cls.add_instance_attribute('speedStatePars', 'ns3::LteRrcSap::SpeedStatePars', is_const=False)
    return

def register_Ns3LteRrcSapMeasGapConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig::MeasGapConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig::MeasGapConfig(ns3::LteRrcSap::MeasGapConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasGapConfig const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasGapConfig::gapOffsetValue [variable]
    cls.add_instance_attribute('gapOffsetValue', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasIdToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod::MeasIdToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod::MeasIdToAddMod(ns3::LteRrcSap::MeasIdToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasIdToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod::measId [variable]
    cls.add_instance_attribute('measId', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod::measObjectId [variable]
    cls.add_instance_attribute('measObjectId', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasIdToAddMod::reportConfigId [variable]
    cls.add_instance_attribute('reportConfigId', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasObjectEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::MeasObjectEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::MeasObjectEutra(ns3::LteRrcSap::MeasObjectEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasObjectEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::allowedMeasBandwidth [variable]
    cls.add_instance_attribute('allowedMeasBandwidth', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::blackCellsToAddModList [variable]
    cls.add_instance_attribute('blackCellsToAddModList', 'std::list< ns3::LteRrcSap::BlackCellsToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::blackCellsToRemoveList [variable]
    cls.add_instance_attribute('blackCellsToRemoveList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::carrierFreq [variable]
    cls.add_instance_attribute('carrierFreq', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::cellForWhichToReportCGI [variable]
    cls.add_instance_attribute('cellForWhichToReportCGI', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::cellsToAddModList [variable]
    cls.add_instance_attribute('cellsToAddModList', 'std::list< ns3::LteRrcSap::CellsToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::cellsToRemoveList [variable]
    cls.add_instance_attribute('cellsToRemoveList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::haveCellForWhichToReportCGI [variable]
    cls.add_instance_attribute('haveCellForWhichToReportCGI', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::neighCellConfig [variable]
    cls.add_instance_attribute('neighCellConfig', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::offsetFreq [variable]
    cls.add_instance_attribute('offsetFreq', 'int8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectEutra::presenceAntennaPort1 [variable]
    cls.add_instance_attribute('presenceAntennaPort1', 'bool', is_const=False)
    return

def register_Ns3LteRrcSapMeasObjectToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectToAddMod::MeasObjectToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectToAddMod::MeasObjectToAddMod(ns3::LteRrcSap::MeasObjectToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasObjectToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectToAddMod::measObjectEutra [variable]
    cls.add_instance_attribute('measObjectEutra', 'ns3::LteRrcSap::MeasObjectEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasObjectToAddMod::measObjectId [variable]
    cls.add_instance_attribute('measObjectId', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasResultEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::MeasResultEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::MeasResultEutra(ns3::LteRrcSap::MeasResultEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasResultEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::cgiInfo [variable]
    cls.add_instance_attribute('cgiInfo', 'ns3::LteRrcSap::CgiInfo', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::haveCgiInfo [variable]
    cls.add_instance_attribute('haveCgiInfo', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::haveRsrpResult [variable]
    cls.add_instance_attribute('haveRsrpResult', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::haveRsrqResult [variable]
    cls.add_instance_attribute('haveRsrqResult', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::physCellId [variable]
    cls.add_instance_attribute('physCellId', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::rsrpResult [variable]
    cls.add_instance_attribute('rsrpResult', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResultEutra::rsrqResult [variable]
    cls.add_instance_attribute('rsrqResult', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasResults_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::MeasResults() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::MeasResults(ns3::LteRrcSap::MeasResults const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasResults const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::haveMeasResultNeighCells [variable]
    cls.add_instance_attribute('haveMeasResultNeighCells', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::measId [variable]
    cls.add_instance_attribute('measId', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::measResultListEutra [variable]
    cls.add_instance_attribute('measResultListEutra', 'std::list< ns3::LteRrcSap::MeasResultEutra >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::rsrpResult [variable]
    cls.add_instance_attribute('rsrpResult', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasResults::rsrqResult [variable]
    cls.add_instance_attribute('rsrqResult', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapMeasurementReport_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasurementReport::MeasurementReport() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasurementReport::MeasurementReport(ns3::LteRrcSap::MeasurementReport const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MeasurementReport const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MeasurementReport::measResults [variable]
    cls.add_instance_attribute('measResults', 'ns3::LteRrcSap::MeasResults', is_const=False)
    return

def register_Ns3LteRrcSapMobilityControlInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::MobilityControlInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::MobilityControlInfo(ns3::LteRrcSap::MobilityControlInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MobilityControlInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::carrierBandwidth [variable]
    cls.add_instance_attribute('carrierBandwidth', 'ns3::LteRrcSap::CarrierBandwidthEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::carrierFreq [variable]
    cls.add_instance_attribute('carrierFreq', 'ns3::LteRrcSap::CarrierFreqEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::haveCarrierBandwidth [variable]
    cls.add_instance_attribute('haveCarrierBandwidth', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::haveCarrierFreq [variable]
    cls.add_instance_attribute('haveCarrierFreq', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::haveRachConfigDedicated [variable]
    cls.add_instance_attribute('haveRachConfigDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::newUeIdentity [variable]
    cls.add_instance_attribute('newUeIdentity', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::rachConfigDedicated [variable]
    cls.add_instance_attribute('rachConfigDedicated', 'ns3::LteRrcSap::RachConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::radioResourceConfigCommon [variable]
    cls.add_instance_attribute('radioResourceConfigCommon', 'ns3::LteRrcSap::RadioResourceConfigCommon', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityControlInfo::targetPhysCellId [variable]
    cls.add_instance_attribute('targetPhysCellId', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapMobilityStateParameters_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::MobilityStateParameters() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::MobilityStateParameters(ns3::LteRrcSap::MobilityStateParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::MobilityStateParameters const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::nCellChangeHigh [variable]
    cls.add_instance_attribute('nCellChangeHigh', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::nCellChangeMedium [variable]
    cls.add_instance_attribute('nCellChangeMedium', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::tEvaluation [variable]
    cls.add_instance_attribute('tEvaluation', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::MobilityStateParameters::tHystNormal [variable]
    cls.add_instance_attribute('tHystNormal', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapPdschConfigCommon_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigCommon::PdschConfigCommon() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigCommon::PdschConfigCommon(ns3::LteRrcSap::PdschConfigCommon const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PdschConfigCommon const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigCommon::pb [variable]
    cls.add_instance_attribute('pb', 'int8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigCommon::referenceSignalPower [variable]
    cls.add_instance_attribute('referenceSignalPower', 'int8_t', is_const=False)
    return

def register_Ns3LteRrcSapPdschConfigDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigDedicated::PdschConfigDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigDedicated::PdschConfigDedicated(ns3::LteRrcSap::PdschConfigDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PdschConfigDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PdschConfigDedicated::pa [variable]
    cls.add_instance_attribute('pa', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapPhysCellIdRange_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange::PhysCellIdRange() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange::PhysCellIdRange(ns3::LteRrcSap::PhysCellIdRange const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PhysCellIdRange const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange::haveRange [variable]
    cls.add_instance_attribute('haveRange', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange::range [variable]
    cls.add_instance_attribute('range', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysCellIdRange::start [variable]
    cls.add_instance_attribute('start', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapPhysicalConfigDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::PhysicalConfigDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::PhysicalConfigDedicated(ns3::LteRrcSap::PhysicalConfigDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PhysicalConfigDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::antennaInfo [variable]
    cls.add_instance_attribute('antennaInfo', 'ns3::LteRrcSap::AntennaInfoDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::haveAntennaInfoDedicated [variable]
    cls.add_instance_attribute('haveAntennaInfoDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::havePdschConfigDedicated [variable]
    cls.add_instance_attribute('havePdschConfigDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::haveSoundingRsUlConfigDedicated [variable]
    cls.add_instance_attribute('haveSoundingRsUlConfigDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::pdschConfigDedicated [variable]
    cls.add_instance_attribute('pdschConfigDedicated', 'ns3::LteRrcSap::PdschConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PhysicalConfigDedicated::soundingRsUlConfigDedicated [variable]
    cls.add_instance_attribute('soundingRsUlConfigDedicated', 'ns3::LteRrcSap::SoundingRsUlConfigDedicated', is_const=False)
    return

def register_Ns3LteRrcSapPlmnIdentityInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PlmnIdentityInfo::PlmnIdentityInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PlmnIdentityInfo::PlmnIdentityInfo(ns3::LteRrcSap::PlmnIdentityInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PlmnIdentityInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PlmnIdentityInfo::plmnIdentity [variable]
    cls.add_instance_attribute('plmnIdentity', 'uint32_t', is_const=False)
    return

def register_Ns3LteRrcSapPreambleInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PreambleInfo::PreambleInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PreambleInfo::PreambleInfo(ns3::LteRrcSap::PreambleInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::PreambleInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::PreambleInfo::numberOfRaPreambles [variable]
    cls.add_instance_attribute('numberOfRaPreambles', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapQuantityConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::QuantityConfig::QuantityConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::QuantityConfig::QuantityConfig(ns3::LteRrcSap::QuantityConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::QuantityConfig const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::QuantityConfig::filterCoefficientRSRP [variable]
    cls.add_instance_attribute('filterCoefficientRSRP', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::QuantityConfig::filterCoefficientRSRQ [variable]
    cls.add_instance_attribute('filterCoefficientRSRQ', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRaSupervisionInfo_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RaSupervisionInfo::RaSupervisionInfo() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RaSupervisionInfo::RaSupervisionInfo(ns3::LteRrcSap::RaSupervisionInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RaSupervisionInfo const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RaSupervisionInfo::preambleTransMax [variable]
    cls.add_instance_attribute('preambleTransMax', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RaSupervisionInfo::raResponseWindowSize [variable]
    cls.add_instance_attribute('raResponseWindowSize', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRachConfigCommon_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigCommon::RachConfigCommon() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigCommon::RachConfigCommon(ns3::LteRrcSap::RachConfigCommon const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RachConfigCommon const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigCommon::preambleInfo [variable]
    cls.add_instance_attribute('preambleInfo', 'ns3::LteRrcSap::PreambleInfo', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigCommon::raSupervisionInfo [variable]
    cls.add_instance_attribute('raSupervisionInfo', 'ns3::LteRrcSap::RaSupervisionInfo', is_const=False)
    return

def register_Ns3LteRrcSapRachConfigDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigDedicated::RachConfigDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigDedicated::RachConfigDedicated(ns3::LteRrcSap::RachConfigDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RachConfigDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigDedicated::raPrachMaskIndex [variable]
    cls.add_instance_attribute('raPrachMaskIndex', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RachConfigDedicated::raPreambleIndex [variable]
    cls.add_instance_attribute('raPreambleIndex', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRadioResourceConfigCommon_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommon::RadioResourceConfigCommon() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommon::RadioResourceConfigCommon(ns3::LteRrcSap::RadioResourceConfigCommon const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RadioResourceConfigCommon const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommon::rachConfigCommon [variable]
    cls.add_instance_attribute('rachConfigCommon', 'ns3::LteRrcSap::RachConfigCommon', is_const=False)
    return

def register_Ns3LteRrcSapRadioResourceConfigCommonSib_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommonSib::RadioResourceConfigCommonSib() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommonSib::RadioResourceConfigCommonSib(ns3::LteRrcSap::RadioResourceConfigCommonSib const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RadioResourceConfigCommonSib const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommonSib::pdschConfigCommon [variable]
    cls.add_instance_attribute('pdschConfigCommon', 'ns3::LteRrcSap::PdschConfigCommon', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigCommonSib::rachConfigCommon [variable]
    cls.add_instance_attribute('rachConfigCommon', 'ns3::LteRrcSap::RachConfigCommon', is_const=False)
    return

def register_Ns3LteRrcSapRadioResourceConfigDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::RadioResourceConfigDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::RadioResourceConfigDedicated(ns3::LteRrcSap::RadioResourceConfigDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RadioResourceConfigDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::drbToAddModList [variable]
    cls.add_instance_attribute('drbToAddModList', 'std::list< ns3::LteRrcSap::DrbToAddMod >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::drbToReleaseList [variable]
    cls.add_instance_attribute('drbToReleaseList', 'std::list< unsigned char >', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::havePhysicalConfigDedicated [variable]
    cls.add_instance_attribute('havePhysicalConfigDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::physicalConfigDedicated [variable]
    cls.add_instance_attribute('physicalConfigDedicated', 'ns3::LteRrcSap::PhysicalConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RadioResourceConfigDedicated::srbToAddModList [variable]
    cls.add_instance_attribute('srbToAddModList', 'std::list< ns3::LteRrcSap::SrbToAddMod >', is_const=False)
    return

def register_Ns3LteRrcSapReestabUeIdentity_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestabUeIdentity::ReestabUeIdentity() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestabUeIdentity::ReestabUeIdentity(ns3::LteRrcSap::ReestabUeIdentity const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::ReestabUeIdentity const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestabUeIdentity::cRnti [variable]
    cls.add_instance_attribute('cRnti', 'uint16_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReestabUeIdentity::physCellId [variable]
    cls.add_instance_attribute('physCellId', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapReportConfigEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::ReportConfigEutra(ns3::LteRrcSap::ReportConfigEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::ReportConfigEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::ReportConfigEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::a3Offset [variable]
    cls.add_instance_attribute('a3Offset', 'int8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::hysteresis [variable]
    cls.add_instance_attribute('hysteresis', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::maxReportCells [variable]
    cls.add_instance_attribute('maxReportCells', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::reportAmount [variable]
    cls.add_instance_attribute('reportAmount', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::reportOnLeave [variable]
    cls.add_instance_attribute('reportOnLeave', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::threshold1 [variable]
    cls.add_instance_attribute('threshold1', 'ns3::LteRrcSap::ThresholdEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::threshold2 [variable]
    cls.add_instance_attribute('threshold2', 'ns3::LteRrcSap::ThresholdEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigEutra::timeToTrigger [variable]
    cls.add_instance_attribute('timeToTrigger', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapReportConfigToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigToAddMod::ReportConfigToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigToAddMod::ReportConfigToAddMod(ns3::LteRrcSap::ReportConfigToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::ReportConfigToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigToAddMod::reportConfigEutra [variable]
    cls.add_instance_attribute('reportConfigEutra', 'ns3::LteRrcSap::ReportConfigEutra', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ReportConfigToAddMod::reportConfigId [variable]
    cls.add_instance_attribute('reportConfigId', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRlcConfig_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RlcConfig::RlcConfig() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RlcConfig::RlcConfig(ns3::LteRrcSap::RlcConfig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RlcConfig const &', 'arg0')])
    return

def register_Ns3LteRrcSapRrcConnectionReconfiguration_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::RrcConnectionReconfiguration() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::RrcConnectionReconfiguration(ns3::LteRrcSap::RrcConnectionReconfiguration const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReconfiguration const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::haveMeasConfig [variable]
    cls.add_instance_attribute('haveMeasConfig', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::haveMobilityControlInfo [variable]
    cls.add_instance_attribute('haveMobilityControlInfo', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::haveRadioResourceConfigDedicated [variable]
    cls.add_instance_attribute('haveRadioResourceConfigDedicated', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::measConfig [variable]
    cls.add_instance_attribute('measConfig', 'ns3::LteRrcSap::MeasConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::mobilityControlInfo [variable]
    cls.add_instance_attribute('mobilityControlInfo', 'ns3::LteRrcSap::MobilityControlInfo', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::radioResourceConfigDedicated [variable]
    cls.add_instance_attribute('radioResourceConfigDedicated', 'ns3::LteRrcSap::RadioResourceConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionReconfigurationCompleted_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfigurationCompleted::RrcConnectionReconfigurationCompleted() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfigurationCompleted::RrcConnectionReconfigurationCompleted(ns3::LteRrcSap::RrcConnectionReconfigurationCompleted const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReconfigurationCompleted const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfigurationCompleted::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionReestablishment_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishment::RrcConnectionReestablishment() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishment::RrcConnectionReestablishment(ns3::LteRrcSap::RrcConnectionReestablishment const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReestablishment const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishment::radioResourceConfigDedicated [variable]
    cls.add_instance_attribute('radioResourceConfigDedicated', 'ns3::LteRrcSap::RadioResourceConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishment::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionReestablishmentComplete_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentComplete::RrcConnectionReestablishmentComplete() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentComplete::RrcConnectionReestablishmentComplete(ns3::LteRrcSap::RrcConnectionReestablishmentComplete const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReestablishmentComplete const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentComplete::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionReestablishmentReject_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentReject::RrcConnectionReestablishmentReject() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentReject::RrcConnectionReestablishmentReject(ns3::LteRrcSap::RrcConnectionReestablishmentReject const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReestablishmentReject const &', 'arg0')])
    return

def register_Ns3LteRrcSapRrcConnectionReestablishmentRequest_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentRequest::RrcConnectionReestablishmentRequest() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentRequest::RrcConnectionReestablishmentRequest(ns3::LteRrcSap::RrcConnectionReestablishmentRequest const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReestablishmentRequest const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentRequest::reestablishmentCause [variable]
    cls.add_instance_attribute('reestablishmentCause', 'ns3::LteRrcSap::ReestablishmentCause', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReestablishmentRequest::ueIdentity [variable]
    cls.add_instance_attribute('ueIdentity', 'ns3::LteRrcSap::ReestabUeIdentity', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionReject_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReject::RrcConnectionReject() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReject::RrcConnectionReject(ns3::LteRrcSap::RrcConnectionReject const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionReject const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReject::waitTime [variable]
    cls.add_instance_attribute('waitTime', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionRelease_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRelease::RrcConnectionRelease() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRelease::RrcConnectionRelease(ns3::LteRrcSap::RrcConnectionRelease const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionRelease const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRelease::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionRequest_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRequest::RrcConnectionRequest() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRequest::RrcConnectionRequest(ns3::LteRrcSap::RrcConnectionRequest const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionRequest const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionRequest::ueIdentity [variable]
    cls.add_instance_attribute('ueIdentity', 'uint64_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionSetup_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetup::RrcConnectionSetup() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetup::RrcConnectionSetup(ns3::LteRrcSap::RrcConnectionSetup const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionSetup const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetup::radioResourceConfigDedicated [variable]
    cls.add_instance_attribute('radioResourceConfigDedicated', 'ns3::LteRrcSap::RadioResourceConfigDedicated', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetup::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapRrcConnectionSetupCompleted_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetupCompleted::RrcConnectionSetupCompleted() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetupCompleted::RrcConnectionSetupCompleted(ns3::LteRrcSap::RrcConnectionSetupCompleted const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::RrcConnectionSetupCompleted const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionSetupCompleted::rrcTransactionIdentifier [variable]
    cls.add_instance_attribute('rrcTransactionIdentifier', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapSoundingRsUlConfigCommon_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon::SoundingRsUlConfigCommon() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon::SoundingRsUlConfigCommon(ns3::LteRrcSap::SoundingRsUlConfigCommon const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SoundingRsUlConfigCommon const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon::srsBandwidthConfig [variable]
    cls.add_instance_attribute('srsBandwidthConfig', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigCommon::srsSubframeConfig [variable]
    cls.add_instance_attribute('srsSubframeConfig', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapSoundingRsUlConfigDedicated_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated::SoundingRsUlConfigDedicated() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated::SoundingRsUlConfigDedicated(ns3::LteRrcSap::SoundingRsUlConfigDedicated const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SoundingRsUlConfigDedicated const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated::srsBandwidth [variable]
    cls.add_instance_attribute('srsBandwidth', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SoundingRsUlConfigDedicated::srsConfigIndex [variable]
    cls.add_instance_attribute('srsConfigIndex', 'uint16_t', is_const=False)
    return

def register_Ns3LteRrcSapSpeedStatePars_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars::SpeedStatePars() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars::SpeedStatePars(ns3::LteRrcSap::SpeedStatePars const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SpeedStatePars const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars::mobilityStateParameters [variable]
    cls.add_instance_attribute('mobilityStateParameters', 'ns3::LteRrcSap::MobilityStateParameters', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStatePars::timeToTriggerSf [variable]
    cls.add_instance_attribute('timeToTriggerSf', 'ns3::LteRrcSap::SpeedStateScaleFactors', is_const=False)
    return

def register_Ns3LteRrcSapSpeedStateScaleFactors_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStateScaleFactors::SpeedStateScaleFactors() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStateScaleFactors::SpeedStateScaleFactors(ns3::LteRrcSap::SpeedStateScaleFactors const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SpeedStateScaleFactors const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStateScaleFactors::sfHigh [variable]
    cls.add_instance_attribute('sfHigh', 'uint8_t', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SpeedStateScaleFactors::sfMedium [variable]
    cls.add_instance_attribute('sfMedium', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapSrbToAddMod_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SrbToAddMod::SrbToAddMod() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SrbToAddMod::SrbToAddMod(ns3::LteRrcSap::SrbToAddMod const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SrbToAddMod const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SrbToAddMod::logicalChannelConfig [variable]
    cls.add_instance_attribute('logicalChannelConfig', 'ns3::LteRrcSap::LogicalChannelConfig', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SrbToAddMod::srbIdentity [variable]
    cls.add_instance_attribute('srbIdentity', 'uint8_t', is_const=False)
    return

def register_Ns3LteRrcSapSystemInformation_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformation::SystemInformation() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformation::SystemInformation(ns3::LteRrcSap::SystemInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SystemInformation const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformation::haveSib2 [variable]
    cls.add_instance_attribute('haveSib2', 'bool', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformation::sib2 [variable]
    cls.add_instance_attribute('sib2', 'ns3::LteRrcSap::SystemInformationBlockType2', is_const=False)
    return

def register_Ns3LteRrcSapSystemInformationBlockType1_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1::SystemInformationBlockType1() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1::SystemInformationBlockType1(ns3::LteRrcSap::SystemInformationBlockType1 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SystemInformationBlockType1 const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1::cellAccessRelatedInfo [variable]
    cls.add_instance_attribute('cellAccessRelatedInfo', 'ns3::LteRrcSap::CellAccessRelatedInfo', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1::cellSelectionInfo [variable]
    cls.add_instance_attribute('cellSelectionInfo', 'ns3::LteRrcSap::CellSelectionInfo', is_const=False)
    return

def register_Ns3LteRrcSapSystemInformationBlockType2_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType2::SystemInformationBlockType2() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType2::SystemInformationBlockType2(ns3::LteRrcSap::SystemInformationBlockType2 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::SystemInformationBlockType2 const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType2::freqInfo [variable]
    cls.add_instance_attribute('freqInfo', 'ns3::LteRrcSap::FreqInfo', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType2::radioResourceConfigCommon [variable]
    cls.add_instance_attribute('radioResourceConfigCommon', 'ns3::LteRrcSap::RadioResourceConfigCommonSib', is_const=False)
    return

def register_Ns3LteRrcSapThresholdEutra_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ThresholdEutra::ThresholdEutra() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ThresholdEutra::ThresholdEutra(ns3::LteRrcSap::ThresholdEutra const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteRrcSap::ThresholdEutra const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::ThresholdEutra::range [variable]
    cls.add_instance_attribute('range', 'uint8_t', is_const=False)
    return

def register_Ns3LteUeConfig_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::LteUeConfig_t(ns3::LteUeConfig_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteUeConfig_t const &', 'arg0')])
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::LteUeConfig_t() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::m_reconfigureFlag [variable]
    cls.add_instance_attribute('m_reconfigureFlag', 'bool', is_const=False)
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::m_srsConfigurationIndex [variable]
    cls.add_instance_attribute('m_srsConfigurationIndex', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::LteUeConfig_t::m_transmissionMode [variable]
    cls.add_instance_attribute('m_transmissionMode', 'uint8_t', is_const=False)
    return

def register_Ns3LteUeRrcSapProvider_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::LteUeRrcSapProvider() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::LteUeRrcSapProvider(ns3::LteUeRrcSapProvider const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteUeRrcSapProvider const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::CompleteSetup(ns3::LteUeRrcSapProvider::CompleteSetupParameters params) [member function]
    cls.add_method('CompleteSetup', 
                   'void', 
                   [param('ns3::LteUeRrcSapProvider::CompleteSetupParameters', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionReconfiguration(ns3::LteRrcSap::RrcConnectionReconfiguration msg) [member function]
    cls.add_method('RecvRrcConnectionReconfiguration', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReconfiguration', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionReestablishment(ns3::LteRrcSap::RrcConnectionReestablishment msg) [member function]
    cls.add_method('RecvRrcConnectionReestablishment', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReestablishment', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionReestablishmentReject(ns3::LteRrcSap::RrcConnectionReestablishmentReject msg) [member function]
    cls.add_method('RecvRrcConnectionReestablishmentReject', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReestablishmentReject', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionReject(ns3::LteRrcSap::RrcConnectionReject msg) [member function]
    cls.add_method('RecvRrcConnectionReject', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReject', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionRelease(ns3::LteRrcSap::RrcConnectionRelease msg) [member function]
    cls.add_method('RecvRrcConnectionRelease', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionRelease', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvRrcConnectionSetup(ns3::LteRrcSap::RrcConnectionSetup msg) [member function]
    cls.add_method('RecvRrcConnectionSetup', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionSetup', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapProvider::RecvSystemInformation(ns3::LteRrcSap::SystemInformation msg) [member function]
    cls.add_method('RecvSystemInformation', 
                   'void', 
                   [param('ns3::LteRrcSap::SystemInformation', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3LteUeRrcSapProviderCompleteSetupParameters_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::CompleteSetupParameters::CompleteSetupParameters() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::CompleteSetupParameters::CompleteSetupParameters(ns3::LteUeRrcSapProvider::CompleteSetupParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteUeRrcSapProvider::CompleteSetupParameters const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::CompleteSetupParameters::srb0SapUser [variable]
    cls.add_instance_attribute('srb0SapUser', 'ns3::LteRlcSapUser *', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapProvider::CompleteSetupParameters::srb1SapUser [variable]
    cls.add_instance_attribute('srb1SapUser', 'ns3::LtePdcpSapUser *', is_const=False)
    return

def register_Ns3LteUeRrcSapUser_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::LteUeRrcSapUser() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::LteUeRrcSapUser(ns3::LteUeRrcSapUser const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteUeRrcSapUser const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendMeasurementReport(ns3::LteRrcSap::MeasurementReport msg) [member function]
    cls.add_method('SendMeasurementReport', 
                   'void', 
                   [param('ns3::LteRrcSap::MeasurementReport', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendRrcConnectionReconfigurationCompleted(ns3::LteRrcSap::RrcConnectionReconfigurationCompleted msg) [member function]
    cls.add_method('SendRrcConnectionReconfigurationCompleted', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReconfigurationCompleted', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendRrcConnectionReestablishmentComplete(ns3::LteRrcSap::RrcConnectionReestablishmentComplete msg) [member function]
    cls.add_method('SendRrcConnectionReestablishmentComplete', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReestablishmentComplete', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendRrcConnectionReestablishmentRequest(ns3::LteRrcSap::RrcConnectionReestablishmentRequest msg) [member function]
    cls.add_method('SendRrcConnectionReestablishmentRequest', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionReestablishmentRequest', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendRrcConnectionRequest(ns3::LteRrcSap::RrcConnectionRequest msg) [member function]
    cls.add_method('SendRrcConnectionRequest', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionRequest', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::SendRrcConnectionSetupCompleted(ns3::LteRrcSap::RrcConnectionSetupCompleted msg) [member function]
    cls.add_method('SendRrcConnectionSetupCompleted', 
                   'void', 
                   [param('ns3::LteRrcSap::RrcConnectionSetupCompleted', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteUeRrcSapUser::Setup(ns3::LteUeRrcSapUser::SetupParameters params) [member function]
    cls.add_method('Setup', 
                   'void', 
                   [param('ns3::LteUeRrcSapUser::SetupParameters', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3LteUeRrcSapUserSetupParameters_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::SetupParameters::SetupParameters() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::SetupParameters::SetupParameters(ns3::LteUeRrcSapUser::SetupParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteUeRrcSapUser::SetupParameters const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::SetupParameters::srb0SapProvider [variable]
    cls.add_instance_attribute('srb0SapProvider', 'ns3::LteRlcSapProvider *', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteUeRrcSapUser::SetupParameters::srb1SapProvider [variable]
    cls.add_instance_attribute('srb1SapProvider', 'ns3::LtePdcpSapProvider *', is_const=False)
    return

def register_Ns3Mac48Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(ns3::Mac48Address const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(char const * str) [constructor]
    cls.add_constructor([param('char const *', 'str')])
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Mac48Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyFrom(uint8_t const * buffer) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'buffer')])
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv4Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv6Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv6Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast6Prefix() [member function]
    cls.add_method('GetMulticast6Prefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticastPrefix() [member function]
    cls.add_method('GetMulticastPrefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsGroup() const [member function]
    cls.add_method('IsGroup', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static bool ns3::Mac48Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3MacCeListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::MacCeListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::MacCeListElement_s(ns3::MacCeListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacCeListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::m_macCeType [variable]
    cls.add_instance_attribute('m_macCeType', 'ns3::MacCeListElement_s::MacCeType_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::m_macCeValue [variable]
    cls.add_instance_attribute('m_macCeValue', 'ns3::MacCeValue_u', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::MacCeListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3MacCeValue_u_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u::MacCeValue_u() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u::MacCeValue_u(ns3::MacCeValue_u const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MacCeValue_u const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u::m_bufferStatus [variable]
    cls.add_instance_attribute('m_bufferStatus', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u::m_crnti [variable]
    cls.add_instance_attribute('m_crnti', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::MacCeValue_u::m_phr [variable]
    cls.add_instance_attribute('m_phr', 'uint8_t', is_const=False)
    return

def register_Ns3NodeContainer_methods(root_module, cls):
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'arg0')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer() [constructor]
    cls.add_constructor([])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::Ptr<ns3::Node> node) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(std::string nodeName) [constructor]
    cls.add_constructor([param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d, ns3::NodeContainer const & e) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd'), param('ns3::NodeContainer const &', 'e')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::NodeContainer other) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NodeContainer', 'other')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(std::string nodeName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n, uint32_t systemId) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n'), param('uint32_t', 'systemId')])
    ## node-container.h (module 'network'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeContainer::End() const [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NodeContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Node >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## node-container.h (module 'network'): static ns3::NodeContainer ns3::NodeContainer::GetGlobal() [member function]
    cls.add_method('GetGlobal', 
                   'ns3::NodeContainer', 
                   [], 
                   is_static=True)
    ## node-container.h (module 'network'): uint32_t ns3::NodeContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3NodeList_methods(root_module, cls):
    ## node-list.h (module 'network'): ns3::NodeList::NodeList() [constructor]
    cls.add_constructor([])
    ## node-list.h (module 'network'): ns3::NodeList::NodeList(ns3::NodeList const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::NodeList const &', 'arg0')])
    ## node-list.h (module 'network'): static uint32_t ns3::NodeList::Add(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('Add', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_static=True)
    ## node-list.h (module 'network'): static __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeList::Begin() [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_static=True)
    ## node-list.h (module 'network'): static __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeList::End() [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_static=True)
    ## node-list.h (module 'network'): static uint32_t ns3::NodeList::GetNNodes() [member function]
    cls.add_method('GetNNodes', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## node-list.h (module 'network'): static ns3::Ptr<ns3::Node> ns3::NodeList::GetNode(uint32_t n) [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [param('uint32_t', 'n')], 
                   is_static=True)
    return

def register_Ns3ObjectBase_methods(root_module, cls):
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase() [constructor]
    cls.add_constructor([])
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase(ns3::ObjectBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectBase const &', 'arg0')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::GetAttribute(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): bool ns3::ObjectBase::GetAttributeFailSafe(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): ns3::TypeId ns3::ObjectBase::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## object-base.h (module 'core'): static ns3::TypeId ns3::ObjectBase::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object-base.h (module 'core'): void ns3::ObjectBase::SetAttribute(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::SetAttributeFailSafe(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::ConstructSelf(ns3::AttributeConstructionList const & attributes) [member function]
    cls.add_method('ConstructSelf', 
                   'void', 
                   [param('ns3::AttributeConstructionList const &', 'attributes')], 
                   visibility='protected')
    ## object-base.h (module 'core'): void ns3::ObjectBase::NotifyConstructionCompleted() [member function]
    cls.add_method('NotifyConstructionCompleted', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectDeleter_methods(root_module, cls):
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter(ns3::ObjectDeleter const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectDeleter const &', 'arg0')])
    ## object.h (module 'core'): static void ns3::ObjectDeleter::Delete(ns3::Object * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Object *', 'object')], 
                   is_static=True)
    return

def register_Ns3ObjectFactory_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(ns3::ObjectFactory const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(std::string typeId) [constructor]
    cls.add_constructor([param('std::string', 'typeId')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::Object> ns3::ObjectFactory::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): ns3::TypeId ns3::ObjectFactory::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::Set(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(ns3::TypeId tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('ns3::TypeId', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(char const * tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('char const *', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(std::string tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('std::string', 'tid')])
    return

def register_Ns3PacketMetadata_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(uint64_t uid, uint32_t size) [constructor]
    cls.add_constructor([param('uint64_t', 'uid'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(ns3::PacketMetadata const & o) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddAtEnd(ns3::PacketMetadata const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddPaddingAtEnd(uint32_t end) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::PacketMetadata::BeginItem(ns3::Buffer buffer) const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [param('ns3::Buffer', 'buffer')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata ns3::PacketMetadata::CreateFragment(uint32_t start, uint32_t end) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::PacketMetadata', 
                   [param('uint32_t', 'start'), param('uint32_t', 'end')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::Enable() [member function]
    cls.add_method('Enable', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint64_t ns3::PacketMetadata::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('RemoveHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('RemoveTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3PacketMetadataItem_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item() [constructor]
    cls.add_constructor([])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item(ns3::PacketMetadata::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata::Item const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::current [variable]
    cls.add_instance_attribute('current', 'ns3::Buffer::Iterator', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentSize [variable]
    cls.add_instance_attribute('currentSize', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromEnd [variable]
    cls.add_instance_attribute('currentTrimedFromEnd', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromStart [variable]
    cls.add_instance_attribute('currentTrimedFromStart', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::isFragment [variable]
    cls.add_instance_attribute('isFragment', 'bool', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PacketMetadataItemIterator_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata::ItemIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata::ItemIterator const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata const * metadata, ns3::Buffer buffer) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata const *', 'metadata'), param('ns3::Buffer', 'buffer')])
    ## packet-metadata.h (module 'network'): bool ns3::PacketMetadata::ItemIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item ns3::PacketMetadata::ItemIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketMetadata::Item', 
                   [])
    return

def register_Ns3PacketTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::PacketTagIterator(ns3::PacketTagIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::PacketTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item ns3::PacketTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketTagIterator::Item', 
                   [])
    return

def register_Ns3PacketTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item::Item(ns3::PacketTagIterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): void ns3::PacketTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::PacketTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3PacketTagList_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList(ns3::PacketTagList const & o) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagList const &', 'o')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::Add(ns3::Tag const & tag) const [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData const * ns3::PacketTagList::Head() const [member function]
    cls.add_method('Head', 
                   'ns3::PacketTagList::TagData const *', 
                   [], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Peek(ns3::Tag & tag) const [member function]
    cls.add_method('Peek', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Remove(ns3::Tag & tag) [member function]
    cls.add_method('Remove', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Replace(ns3::Tag & tag) [member function]
    cls.add_method('Replace', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    return

def register_Ns3PacketTagListTagData_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData(ns3::PacketTagList::TagData const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagList::TagData const &', 'arg0')])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::count [variable]
    cls.add_instance_attribute('count', 'uint32_t', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::data [variable]
    cls.add_instance_attribute('data', 'uint8_t [ 20 ]', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::next [variable]
    cls.add_instance_attribute('next', 'ns3::PacketTagList::TagData *', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PagingInfoListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s::PagingInfoListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s::PagingInfoListElement_s(ns3::PagingInfoListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PagingInfoListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s::m_pagingIndex [variable]
    cls.add_instance_attribute('m_pagingIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s::m_pagingMessageSize [variable]
    cls.add_instance_attribute('m_pagingMessageSize', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::PagingInfoListElement_s::m_pagingSubframe [variable]
    cls.add_instance_attribute('m_pagingSubframe', 'uint8_t', is_const=False)
    return

def register_Ns3ParameterLogger_methods(root_module, cls):
    ## log.h (module 'core'): ns3::ParameterLogger::ParameterLogger(ns3::ParameterLogger const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ParameterLogger const &', 'arg0')])
    ## log.h (module 'core'): ns3::ParameterLogger::ParameterLogger(std::ostream & os) [constructor]
    cls.add_constructor([param('std::ostream &', 'os')])
    return

def register_Ns3PhichListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s::PhichListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s::PhichListElement_s(ns3::PhichListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PhichListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s::m_phich [variable]
    cls.add_instance_attribute('m_phich', 'ns3::PhichListElement_s::Phich_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::PhichListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3PhyReceptionStatParameters_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::PhyReceptionStatParameters() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::PhyReceptionStatParameters(ns3::PhyReceptionStatParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PhyReceptionStatParameters const &', 'arg0')])
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_cellId [variable]
    cls.add_instance_attribute('m_cellId', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_correctness [variable]
    cls.add_instance_attribute('m_correctness', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_imsi [variable]
    cls.add_instance_attribute('m_imsi', 'uint64_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_layer [variable]
    cls.add_instance_attribute('m_layer', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_mcs [variable]
    cls.add_instance_attribute('m_mcs', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_ndi [variable]
    cls.add_instance_attribute('m_ndi', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_rv [variable]
    cls.add_instance_attribute('m_rv', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_size [variable]
    cls.add_instance_attribute('m_size', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_timestamp [variable]
    cls.add_instance_attribute('m_timestamp', 'int64_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyReceptionStatParameters::m_txMode [variable]
    cls.add_instance_attribute('m_txMode', 'uint8_t', is_const=False)
    return

def register_Ns3PhyTransmissionStatParameters_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::PhyTransmissionStatParameters() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::PhyTransmissionStatParameters(ns3::PhyTransmissionStatParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PhyTransmissionStatParameters const &', 'arg0')])
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_cellId [variable]
    cls.add_instance_attribute('m_cellId', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_imsi [variable]
    cls.add_instance_attribute('m_imsi', 'uint64_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_layer [variable]
    cls.add_instance_attribute('m_layer', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_mcs [variable]
    cls.add_instance_attribute('m_mcs', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_ndi [variable]
    cls.add_instance_attribute('m_ndi', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_rv [variable]
    cls.add_instance_attribute('m_rv', 'uint8_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_size [variable]
    cls.add_instance_attribute('m_size', 'uint16_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_timestamp [variable]
    cls.add_instance_attribute('m_timestamp', 'int64_t', is_const=False)
    ## lte-common.h (module 'lte'): ns3::PhyTransmissionStatParameters::m_txMode [variable]
    cls.add_instance_attribute('m_txMode', 'uint8_t', is_const=False)
    return

def register_Ns3RachListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::RachListElement_s::RachListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::RachListElement_s::RachListElement_s(ns3::RachListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RachListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::RachListElement_s::m_estimatedSize [variable]
    cls.add_instance_attribute('m_estimatedSize', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::RachListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3Rectangle_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## rectangle.h (module 'mobility'): ns3::Rectangle::Rectangle(ns3::Rectangle const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Rectangle const &', 'arg0')])
    ## rectangle.h (module 'mobility'): ns3::Rectangle::Rectangle(double _xMin, double _xMax, double _yMin, double _yMax) [constructor]
    cls.add_constructor([param('double', '_xMin'), param('double', '_xMax'), param('double', '_yMin'), param('double', '_yMax')])
    ## rectangle.h (module 'mobility'): ns3::Rectangle::Rectangle() [constructor]
    cls.add_constructor([])
    ## rectangle.h (module 'mobility'): ns3::Vector ns3::Rectangle::CalculateIntersection(ns3::Vector const & current, ns3::Vector const & speed) const [member function]
    cls.add_method('CalculateIntersection', 
                   'ns3::Vector', 
                   [param('ns3::Vector const &', 'current'), param('ns3::Vector const &', 'speed')], 
                   is_const=True)
    ## rectangle.h (module 'mobility'): ns3::Rectangle::Side ns3::Rectangle::GetClosestSide(ns3::Vector const & position) const [member function]
    cls.add_method('GetClosestSide', 
                   'ns3::Rectangle::Side', 
                   [param('ns3::Vector const &', 'position')], 
                   is_const=True)
    ## rectangle.h (module 'mobility'): bool ns3::Rectangle::IsInside(ns3::Vector const & position) const [member function]
    cls.add_method('IsInside', 
                   'bool', 
                   [param('ns3::Vector const &', 'position')], 
                   is_const=True)
    ## rectangle.h (module 'mobility'): ns3::Rectangle::xMax [variable]
    cls.add_instance_attribute('xMax', 'double', is_const=False)
    ## rectangle.h (module 'mobility'): ns3::Rectangle::xMin [variable]
    cls.add_instance_attribute('xMin', 'double', is_const=False)
    ## rectangle.h (module 'mobility'): ns3::Rectangle::yMax [variable]
    cls.add_instance_attribute('yMax', 'double', is_const=False)
    ## rectangle.h (module 'mobility'): ns3::Rectangle::yMin [variable]
    cls.add_instance_attribute('yMin', 'double', is_const=False)
    return

def register_Ns3RlcPduListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::RlcPduListElement_s::RlcPduListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::RlcPduListElement_s::RlcPduListElement_s(ns3::RlcPduListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RlcPduListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::RlcPduListElement_s::m_logicalChannelIdentity [variable]
    cls.add_instance_attribute('m_logicalChannelIdentity', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::RlcPduListElement_s::m_size [variable]
    cls.add_instance_attribute('m_size', 'uint16_t', is_const=False)
    return

def register_Ns3SbMeasResult_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s::SbMeasResult_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s::SbMeasResult_s(ns3::SbMeasResult_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SbMeasResult_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s::m_bwPart [variable]
    cls.add_instance_attribute('m_bwPart', 'ns3::BwPart_s', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s::m_higherLayerSelected [variable]
    cls.add_instance_attribute('m_higherLayerSelected', 'std::vector< ns3::HigherLayerSelected_s >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SbMeasResult_s::m_ueSelected [variable]
    cls.add_instance_attribute('m_ueSelected', 'ns3::UeSelected_s', is_const=False)
    return

def register_Ns3SiConfiguration_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::SiConfiguration_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::SiConfiguration_s(ns3::SiConfiguration_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SiConfiguration_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::m_sfn [variable]
    cls.add_instance_attribute('m_sfn', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::m_siMessageList [variable]
    cls.add_instance_attribute('m_siMessageList', 'std::vector< ns3::SiMessageListElement_s >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::m_siWindowLength [variable]
    cls.add_instance_attribute('m_siWindowLength', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SiConfiguration_s::m_sib1Length [variable]
    cls.add_instance_attribute('m_sib1Length', 'uint16_t', is_const=False)
    return

def register_Ns3SiMessageListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SiMessageListElement_s::SiMessageListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SiMessageListElement_s::SiMessageListElement_s(ns3::SiMessageListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SiMessageListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SiMessageListElement_s::m_length [variable]
    cls.add_instance_attribute('m_length', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SiMessageListElement_s::m_periodicity [variable]
    cls.add_instance_attribute('m_periodicity', 'uint16_t', is_const=False)
    return

def register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount(ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3Simulator_methods(root_module, cls):
    ## simulator.h (module 'core'): ns3::Simulator::Simulator(ns3::Simulator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Simulator const &', 'arg0')])
    ## simulator.h (module 'core'): static void ns3::Simulator::Cancel(ns3::EventId const & id) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetContext() [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetDelayLeft(ns3::EventId const & id) [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Ptr<ns3::SimulatorImpl> ns3::Simulator::GetImplementation() [member function]
    cls.add_method('GetImplementation', 
                   'ns3::Ptr< ns3::SimulatorImpl >', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetMaximumSimulationTime() [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetSystemId() [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsExpired(ns3::EventId const & id) [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsFinished() [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::Now() [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Remove(ns3::EventId const & id) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetImplementation(ns3::Ptr<ns3::SimulatorImpl> impl) [member function]
    cls.add_method('SetImplementation', 
                   'void', 
                   [param('ns3::Ptr< ns3::SimulatorImpl >', 'impl')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop(ns3::Time const & time) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'time')], 
                   is_static=True)
    return

def register_Ns3SpsConfig_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::SpsConfig_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::SpsConfig_s(ns3::SpsConfig_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpsConfig_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_implicitReleaseAfter [variable]
    cls.add_instance_attribute('m_implicitReleaseAfter', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_n1PucchAnPersistentList [variable]
    cls.add_instance_attribute('m_n1PucchAnPersistentList', 'std::vector< unsigned short >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_n1PucchAnPersistentListSize [variable]
    cls.add_instance_attribute('m_n1PucchAnPersistentListSize', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_numberOfConfSpsProcesses [variable]
    cls.add_instance_attribute('m_numberOfConfSpsProcesses', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_semiPersistSchedIntervalDl [variable]
    cls.add_instance_attribute('m_semiPersistSchedIntervalDl', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SpsConfig_s::m_semiPersistSchedIntervalUl [variable]
    cls.add_instance_attribute('m_semiPersistSchedIntervalUl', 'uint16_t', is_const=False)
    return

def register_Ns3SrConfig_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s::SrConfig_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s::SrConfig_s(ns3::SrConfig_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SrConfig_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s::m_action [variable]
    cls.add_instance_attribute('m_action', 'ns3::SetupRelease_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s::m_dsrTransMax [variable]
    cls.add_instance_attribute('m_dsrTransMax', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::SrConfig_s::m_schedInterval [variable]
    cls.add_instance_attribute('m_schedInterval', 'uint8_t', is_const=False)
    return

def register_Ns3SrListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::SrListElement_s::SrListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::SrListElement_s::SrListElement_s(ns3::SrListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SrListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::SrListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3Tag_methods(root_module, cls):
    ## tag.h (module 'network'): ns3::Tag::Tag() [constructor]
    cls.add_constructor([])
    ## tag.h (module 'network'): ns3::Tag::Tag(ns3::Tag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Tag const &', 'arg0')])
    ## tag.h (module 'network'): void ns3::Tag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_virtual=True)
    ## tag.h (module 'network'): uint32_t ns3::Tag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): static ns3::TypeId ns3::Tag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## tag.h (module 'network'): void ns3::Tag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): void ns3::Tag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TagBuffer_methods(root_module, cls):
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(ns3::TagBuffer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TagBuffer const &', 'arg0')])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(uint8_t * start, uint8_t * end) [constructor]
    cls.add_constructor([param('uint8_t *', 'start'), param('uint8_t *', 'end')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::CopyFrom(ns3::TagBuffer o) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('ns3::TagBuffer', 'o')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): double ns3::TagBuffer::ReadDouble() [member function]
    cls.add_method('ReadDouble', 
                   'double', 
                   [])
    ## tag-buffer.h (module 'network'): uint16_t ns3::TagBuffer::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint32_t ns3::TagBuffer::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint64_t ns3::TagBuffer::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint8_t ns3::TagBuffer::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::TrimAtEnd(uint32_t trim) [member function]
    cls.add_method('TrimAtEnd', 
                   'void', 
                   [param('uint32_t', 'trim')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteDouble(double v) [member function]
    cls.add_method('WriteDouble', 
                   'void', 
                   [param('double', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU16(uint16_t data) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU32(uint32_t data) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU64(uint64_t v) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU8(uint8_t v) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'v')])
    return

def register_Ns3Tap_methods(root_module, cls):
    ## uan-prop-model.h (module 'uan'): ns3::Tap::Tap(ns3::Tap const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Tap const &', 'arg0')])
    ## uan-prop-model.h (module 'uan'): ns3::Tap::Tap() [constructor]
    cls.add_constructor([])
    ## uan-prop-model.h (module 'uan'): ns3::Tap::Tap(ns3::Time delay, std::complex<double> amp) [constructor]
    cls.add_constructor([param('ns3::Time', 'delay'), param('std::complex< double >', 'amp')])
    ## uan-prop-model.h (module 'uan'): std::complex<double> ns3::Tap::GetAmp() const [member function]
    cls.add_method('GetAmp', 
                   'std::complex< double >', 
                   [], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): ns3::Time ns3::Tap::GetDelay() const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    return

def register_Ns3TbId_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t::TbId_t(ns3::TbId_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TbId_t const &', 'arg0')])
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t::TbId_t() [constructor]
    cls.add_constructor([])
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t::TbId_t(uint16_t const a, uint8_t const b) [constructor]
    cls.add_constructor([param('uint16_t const', 'a'), param('uint8_t const', 'b')])
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t::m_layer [variable]
    cls.add_instance_attribute('m_layer', 'uint8_t', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::TbId_t::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    return

def register_Ns3TimeWithUnit_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::TimeWithUnit const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TimeWithUnit const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::Time const time, ns3::Time::Unit const unit) [constructor]
    cls.add_constructor([param('ns3::Time const', 'time'), param('ns3::Time::Unit const', 'unit')])
    return

def register_Ns3TransmissionModesLayers_methods(root_module, cls):
    ## lte-common.h (module 'lte'): ns3::TransmissionModesLayers::TransmissionModesLayers() [constructor]
    cls.add_constructor([])
    ## lte-common.h (module 'lte'): ns3::TransmissionModesLayers::TransmissionModesLayers(ns3::TransmissionModesLayers const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TransmissionModesLayers const &', 'arg0')])
    ## lte-common.h (module 'lte'): static uint8_t ns3::TransmissionModesLayers::TxMode2LayerNum(uint8_t txMode) [member function]
    cls.add_method('TxMode2LayerNum', 
                   'uint8_t', 
                   [param('uint8_t', 'txMode')], 
                   is_static=True)
    return

def register_Ns3TypeId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(char const * name) [constructor]
    cls.add_constructor([param('char const *', 'name')])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(ns3::TypeId const & o) [copy constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'o')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, ns3::AttributeValue const & initialValue, ns3::Ptr<ns3::AttributeAccessor const> accessor, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, uint32_t flags, ns3::AttributeValue const & initialValue, ns3::Ptr<ns3::AttributeAccessor const> accessor, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('uint32_t', 'flags'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<ns3::TraceSourceAccessor const> accessor) [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor')], 
                   deprecated=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<ns3::TraceSourceAccessor const> accessor, std::string callback) [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor'), param('std::string', 'callback')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation ns3::TypeId::GetAttribute(uint32_t i) const [member function]
    cls.add_method('GetAttribute', 
                   'ns3::TypeId::AttributeInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetAttributeFullName(uint32_t i) const [member function]
    cls.add_method('GetAttributeFullName', 
                   'std::string', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetAttributeN() const [member function]
    cls.add_method('GetAttributeN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::Callback<ns3::ObjectBase*,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> ns3::TypeId::GetConstructor() const [member function]
    cls.add_method('GetConstructor', 
                   'ns3::Callback< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetGroupName() const [member function]
    cls.add_method('GetGroupName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetHash() const [member function]
    cls.add_method('GetHash', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::GetParent() const [member function]
    cls.add_method('GetParent', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::GetRegistered(uint32_t i) [member function]
    cls.add_method('GetRegistered', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'i')], 
                   is_static=True)
    ## type-id.h (module 'core'): static uint32_t ns3::TypeId::GetRegisteredN() [member function]
    cls.add_method('GetRegisteredN', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## type-id.h (module 'core'): std::size_t ns3::TypeId::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'std::size_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation ns3::TypeId::GetTraceSource(uint32_t i) const [member function]
    cls.add_method('GetTraceSource', 
                   'ns3::TypeId::TraceSourceInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetTraceSourceN() const [member function]
    cls.add_method('GetTraceSourceN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): uint16_t ns3::TypeId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasConstructor() const [member function]
    cls.add_method('HasConstructor', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasParent() const [member function]
    cls.add_method('HasParent', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::HideFromDocumentation() [member function]
    cls.add_method('HideFromDocumentation', 
                   'ns3::TypeId', 
                   [])
    ## type-id.h (module 'core'): bool ns3::TypeId::IsChildOf(ns3::TypeId other) const [member function]
    cls.add_method('IsChildOf', 
                   'bool', 
                   [param('ns3::TypeId', 'other')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::LookupAttributeByName(std::string name, ns3::TypeId::AttributeInformation * info) const [member function]
    cls.add_method('LookupAttributeByName', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::TypeId::AttributeInformation *', 'info', transfer_ownership=False)], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByHash(uint32_t hash) [member function]
    cls.add_method('LookupByHash', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'hash')], 
                   is_static=True)
    ## type-id.h (module 'core'): static bool ns3::TypeId::LookupByHashFailSafe(uint32_t hash, ns3::TypeId * tid) [member function]
    cls.add_method('LookupByHashFailSafe', 
                   'bool', 
                   [param('uint32_t', 'hash'), param('ns3::TypeId *', 'tid')], 
                   is_static=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByName(std::string name) [member function]
    cls.add_method('LookupByName', 
                   'ns3::TypeId', 
                   [param('std::string', 'name')], 
                   is_static=True)
    ## type-id.h (module 'core'): ns3::Ptr<ns3::TraceSourceAccessor const> ns3::TypeId::LookupTraceSourceByName(std::string name) const [member function]
    cls.add_method('LookupTraceSourceByName', 
                   'ns3::Ptr< ns3::TraceSourceAccessor const >', 
                   [param('std::string', 'name')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::MustHideFromDocumentation() const [member function]
    cls.add_method('MustHideFromDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::SetAttributeInitialValue(uint32_t i, ns3::Ptr<ns3::AttributeValue const> initialValue) [member function]
    cls.add_method('SetAttributeInitialValue', 
                   'bool', 
                   [param('uint32_t', 'i'), param('ns3::Ptr< ns3::AttributeValue const >', 'initialValue')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetGroupName(std::string groupName) [member function]
    cls.add_method('SetGroupName', 
                   'ns3::TypeId', 
                   [param('std::string', 'groupName')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetParent(ns3::TypeId tid) [member function]
    cls.add_method('SetParent', 
                   'ns3::TypeId', 
                   [param('ns3::TypeId', 'tid')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetSize(std::size_t size) [member function]
    cls.add_method('SetSize', 
                   'ns3::TypeId', 
                   [param('std::size_t', 'size')])
    ## type-id.h (module 'core'): void ns3::TypeId::SetUid(uint16_t tid) [member function]
    cls.add_method('SetUid', 
                   'void', 
                   [param('uint16_t', 'tid')])
    return

def register_Ns3TypeIdAttributeInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation(ns3::TypeId::AttributeInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeId::AttributeInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::AttributeAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::flags [variable]
    cls.add_instance_attribute('flags', 'uint32_t', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::initialValue [variable]
    cls.add_instance_attribute('initialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::originalInitialValue [variable]
    cls.add_instance_attribute('originalInitialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    return

def register_Ns3TypeIdTraceSourceInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation(ns3::TypeId::TraceSourceInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeId::TraceSourceInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::TraceSourceAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::callback [variable]
    cls.add_instance_attribute('callback', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    return

def register_Ns3UanModesList_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesList::UanModesList(ns3::UanModesList const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanModesList const &', 'arg0')])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesList::UanModesList() [constructor]
    cls.add_constructor([])
    ## uan-tx-mode.h (module 'uan'): void ns3::UanModesList::AppendMode(ns3::UanTxMode mode) [member function]
    cls.add_method('AppendMode', 
                   'void', 
                   [param('ns3::UanTxMode', 'mode')])
    ## uan-tx-mode.h (module 'uan'): void ns3::UanModesList::DeleteMode(uint32_t num) [member function]
    cls.add_method('DeleteMode', 
                   'void', 
                   [param('uint32_t', 'num')])
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanModesList::GetNModes() const [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3UanPacketArrival_methods(root_module, cls):
    ## uan-transducer.h (module 'uan'): ns3::UanPacketArrival::UanPacketArrival(ns3::UanPacketArrival const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPacketArrival const &', 'arg0')])
    ## uan-transducer.h (module 'uan'): ns3::UanPacketArrival::UanPacketArrival() [constructor]
    cls.add_constructor([])
    ## uan-transducer.h (module 'uan'): ns3::UanPacketArrival::UanPacketArrival(ns3::Ptr<ns3::Packet> packet, double rxPowerDb, ns3::UanTxMode txMode, ns3::UanPdp pdp, ns3::Time arrTime) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'rxPowerDb'), param('ns3::UanTxMode', 'txMode'), param('ns3::UanPdp', 'pdp'), param('ns3::Time', 'arrTime')])
    ## uan-transducer.h (module 'uan'): ns3::Time ns3::UanPacketArrival::GetArrivalTime() const [member function]
    cls.add_method('GetArrivalTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## uan-transducer.h (module 'uan'): ns3::Ptr<ns3::Packet> ns3::UanPacketArrival::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## uan-transducer.h (module 'uan'): ns3::UanPdp ns3::UanPacketArrival::GetPdp() const [member function]
    cls.add_method('GetPdp', 
                   'ns3::UanPdp', 
                   [], 
                   is_const=True)
    ## uan-transducer.h (module 'uan'): double ns3::UanPacketArrival::GetRxPowerDb() const [member function]
    cls.add_method('GetRxPowerDb', 
                   'double', 
                   [], 
                   is_const=True)
    ## uan-transducer.h (module 'uan'): ns3::UanTxMode const & ns3::UanPacketArrival::GetTxMode() const [member function]
    cls.add_method('GetTxMode', 
                   'ns3::UanTxMode const &', 
                   [], 
                   is_const=True)
    return

def register_Ns3UanPdp_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp::UanPdp(ns3::UanPdp const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPdp const &', 'arg0')])
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp::UanPdp() [constructor]
    cls.add_constructor([])
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp::UanPdp(std::vector<ns3::Tap, std::allocator<ns3::Tap> > taps, ns3::Time resolution) [constructor]
    cls.add_constructor([param('std::vector< ns3::Tap >', 'taps'), param('ns3::Time', 'resolution')])
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp::UanPdp(std::vector<std::complex<double>,std::allocator<std::complex<double> > > arrivals, ns3::Time resolution) [constructor]
    cls.add_constructor([param('std::vector< std::complex< double > >', 'arrivals'), param('ns3::Time', 'resolution')])
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp::UanPdp(std::vector<double, std::allocator<double> > arrivals, ns3::Time resolution) [constructor]
    cls.add_constructor([param('std::vector< double >', 'arrivals'), param('ns3::Time', 'resolution')])
    ## uan-prop-model.h (module 'uan'): static ns3::UanPdp ns3::UanPdp::CreateImpulsePdp() [member function]
    cls.add_method('CreateImpulsePdp', 
                   'ns3::UanPdp', 
                   [], 
                   is_static=True)
    ## uan-prop-model.h (module 'uan'): __gnu_cxx::__normal_iterator<const ns3::Tap*,std::vector<ns3::Tap, std::allocator<ns3::Tap> > > ns3::UanPdp::GetBegin() const [member function]
    cls.add_method('GetBegin', 
                   '__gnu_cxx::__normal_iterator< ns3::Tap const *, std::vector< ns3::Tap > >', 
                   [], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): __gnu_cxx::__normal_iterator<const ns3::Tap*,std::vector<ns3::Tap, std::allocator<ns3::Tap> > > ns3::UanPdp::GetEnd() const [member function]
    cls.add_method('GetEnd', 
                   '__gnu_cxx::__normal_iterator< ns3::Tap const *, std::vector< ns3::Tap > >', 
                   [], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): uint32_t ns3::UanPdp::GetNTaps() const [member function]
    cls.add_method('GetNTaps', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): ns3::Time ns3::UanPdp::GetResolution() const [member function]
    cls.add_method('GetResolution', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): ns3::Tap const & ns3::UanPdp::GetTap(uint32_t i) const [member function]
    cls.add_method('GetTap', 
                   'ns3::Tap const &', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): void ns3::UanPdp::SetNTaps(uint32_t nTaps) [member function]
    cls.add_method('SetNTaps', 
                   'void', 
                   [param('uint32_t', 'nTaps')])
    ## uan-prop-model.h (module 'uan'): void ns3::UanPdp::SetResolution(ns3::Time resolution) [member function]
    cls.add_method('SetResolution', 
                   'void', 
                   [param('ns3::Time', 'resolution')])
    ## uan-prop-model.h (module 'uan'): void ns3::UanPdp::SetTap(std::complex<double> arrival, uint32_t index) [member function]
    cls.add_method('SetTap', 
                   'void', 
                   [param('std::complex< double >', 'arrival'), param('uint32_t', 'index')])
    ## uan-prop-model.h (module 'uan'): std::complex<double> ns3::UanPdp::SumTapsC(ns3::Time begin, ns3::Time end) const [member function]
    cls.add_method('SumTapsC', 
                   'std::complex< double >', 
                   [param('ns3::Time', 'begin'), param('ns3::Time', 'end')], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): std::complex<double> ns3::UanPdp::SumTapsFromMaxC(ns3::Time delay, ns3::Time duration) const [member function]
    cls.add_method('SumTapsFromMaxC', 
                   'std::complex< double >', 
                   [param('ns3::Time', 'delay'), param('ns3::Time', 'duration')], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): double ns3::UanPdp::SumTapsFromMaxNc(ns3::Time delay, ns3::Time duration) const [member function]
    cls.add_method('SumTapsFromMaxNc', 
                   'double', 
                   [param('ns3::Time', 'delay'), param('ns3::Time', 'duration')], 
                   is_const=True)
    ## uan-prop-model.h (module 'uan'): double ns3::UanPdp::SumTapsNc(ns3::Time begin, ns3::Time end) const [member function]
    cls.add_method('SumTapsNc', 
                   'double', 
                   [param('ns3::Time', 'begin'), param('ns3::Time', 'end')], 
                   is_const=True)
    return

def register_Ns3UanPhyListener_methods(root_module, cls):
    ## uan-phy.h (module 'uan'): ns3::UanPhyListener::UanPhyListener() [constructor]
    cls.add_constructor([])
    ## uan-phy.h (module 'uan'): ns3::UanPhyListener::UanPhyListener(ns3::UanPhyListener const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyListener const &', 'arg0')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyCcaEnd() [member function]
    cls.add_method('NotifyCcaEnd', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyCcaStart() [member function]
    cls.add_method('NotifyCcaStart', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyRxEndError() [member function]
    cls.add_method('NotifyRxEndError', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyRxEndOk() [member function]
    cls.add_method('NotifyRxEndOk', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyRxStart() [member function]
    cls.add_method('NotifyRxStart', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyListener::NotifyTxStart(ns3::Time duration) [member function]
    cls.add_method('NotifyTxStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3UanTxMode_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxMode::UanTxMode(ns3::UanTxMode const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanTxMode const &', 'arg0')])
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxMode::UanTxMode() [constructor]
    cls.add_constructor([])
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetBandwidthHz() const [member function]
    cls.add_method('GetBandwidthHz', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetCenterFreqHz() const [member function]
    cls.add_method('GetCenterFreqHz', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetConstellationSize() const [member function]
    cls.add_method('GetConstellationSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetDataRateBps() const [member function]
    cls.add_method('GetDataRateBps', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxMode::ModulationType ns3::UanTxMode::GetModType() const [member function]
    cls.add_method('GetModType', 
                   'ns3::UanTxMode::ModulationType', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): std::string ns3::UanTxMode::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetPhyRateSps() const [member function]
    cls.add_method('GetPhyRateSps', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): uint32_t ns3::UanTxMode::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3UanTxModeFactory_methods(root_module, cls):
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxModeFactory::UanTxModeFactory(ns3::UanTxModeFactory const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanTxModeFactory const &', 'arg0')])
    ## uan-tx-mode.h (module 'uan'): ns3::UanTxModeFactory::UanTxModeFactory() [constructor]
    cls.add_constructor([])
    ## uan-tx-mode.h (module 'uan'): static ns3::UanTxMode ns3::UanTxModeFactory::CreateMode(ns3::UanTxMode::ModulationType type, uint32_t dataRateBps, uint32_t phyRateSps, uint32_t cfHz, uint32_t bwHz, uint32_t constSize, std::string name) [member function]
    cls.add_method('CreateMode', 
                   'ns3::UanTxMode', 
                   [param('ns3::UanTxMode::ModulationType', 'type'), param('uint32_t', 'dataRateBps'), param('uint32_t', 'phyRateSps'), param('uint32_t', 'cfHz'), param('uint32_t', 'bwHz'), param('uint32_t', 'constSize'), param('std::string', 'name')], 
                   is_static=True)
    ## uan-tx-mode.h (module 'uan'): static ns3::UanTxMode ns3::UanTxModeFactory::GetMode(std::string name) [member function]
    cls.add_method('GetMode', 
                   'ns3::UanTxMode', 
                   [param('std::string', 'name')], 
                   is_static=True)
    ## uan-tx-mode.h (module 'uan'): static ns3::UanTxMode ns3::UanTxModeFactory::GetMode(uint32_t uid) [member function]
    cls.add_method('GetMode', 
                   'ns3::UanTxMode', 
                   [param('uint32_t', 'uid')], 
                   is_static=True)
    return

def register_Ns3UeCapabilities_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::UeCapabilities_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::UeCapabilities_s(ns3::UeCapabilities_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UeCapabilities_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::m_halfDuplex [variable]
    cls.add_instance_attribute('m_halfDuplex', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::m_intraSfHopping [variable]
    cls.add_instance_attribute('m_intraSfHopping', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::m_resAllocType1 [variable]
    cls.add_instance_attribute('m_resAllocType1', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::m_type2Sb1 [variable]
    cls.add_instance_attribute('m_type2Sb1', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeCapabilities_s::m_ueCategory [variable]
    cls.add_instance_attribute('m_ueCategory', 'uint8_t', is_const=False)
    return

def register_Ns3UeSelected_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s::UeSelected_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s::UeSelected_s(ns3::UeSelected_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UeSelected_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s::m_sbCqi [variable]
    cls.add_instance_attribute('m_sbCqi', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s::m_sbList [variable]
    cls.add_instance_attribute('m_sbList', 'std::vector< unsigned char >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UeSelected_s::m_sbPmi [variable]
    cls.add_instance_attribute('m_sbPmi', 'uint8_t', is_const=False)
    return

def register_Ns3UlCqi_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s::UlCqi_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s::UlCqi_s(ns3::UlCqi_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UlCqi_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s::m_sinr [variable]
    cls.add_instance_attribute('m_sinr', 'std::vector< unsigned short >', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlCqi_s::m_type [variable]
    cls.add_instance_attribute('m_type', 'ns3::UlCqi_s::Type_e', is_const=False)
    return

def register_Ns3UlDciListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::UlDciListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::UlDciListElement_s(ns3::UlDciListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UlDciListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_aggrLevel [variable]
    cls.add_instance_attribute('m_aggrLevel', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_cceIndex [variable]
    cls.add_instance_attribute('m_cceIndex', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_cqiRequest [variable]
    cls.add_instance_attribute('m_cqiRequest', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_dai [variable]
    cls.add_instance_attribute('m_dai', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_freqHopping [variable]
    cls.add_instance_attribute('m_freqHopping', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_hopping [variable]
    cls.add_instance_attribute('m_hopping', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_mcs [variable]
    cls.add_instance_attribute('m_mcs', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_n2Dmrs [variable]
    cls.add_instance_attribute('m_n2Dmrs', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_ndi [variable]
    cls.add_instance_attribute('m_ndi', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_pdcchPowerOffset [variable]
    cls.add_instance_attribute('m_pdcchPowerOffset', 'int8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_rbLen [variable]
    cls.add_instance_attribute('m_rbLen', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_rbStart [variable]
    cls.add_instance_attribute('m_rbStart', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_tbSize [variable]
    cls.add_instance_attribute('m_tbSize', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_tpc [variable]
    cls.add_instance_attribute('m_tpc', 'int8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_ueTxAntennaSelection [variable]
    cls.add_instance_attribute('m_ueTxAntennaSelection', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlDciListElement_s::m_ulIndex [variable]
    cls.add_instance_attribute('m_ulIndex', 'uint8_t', is_const=False)
    return

def register_Ns3UlGrant_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::UlGrant_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::UlGrant_s(ns3::UlGrant_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UlGrant_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_cqiRequest [variable]
    cls.add_instance_attribute('m_cqiRequest', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_hopping [variable]
    cls.add_instance_attribute('m_hopping', 'bool', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_mcs [variable]
    cls.add_instance_attribute('m_mcs', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_rbLen [variable]
    cls.add_instance_attribute('m_rbLen', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_rbStart [variable]
    cls.add_instance_attribute('m_rbStart', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_tbSize [variable]
    cls.add_instance_attribute('m_tbSize', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_tpc [variable]
    cls.add_instance_attribute('m_tpc', 'int8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlGrant_s::m_ulDelay [variable]
    cls.add_instance_attribute('m_ulDelay', 'bool', is_const=False)
    return

def register_Ns3UlInfoListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::UlInfoListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::UlInfoListElement_s(ns3::UlInfoListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UlInfoListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::m_receptionStatus [variable]
    cls.add_instance_attribute('m_receptionStatus', 'ns3::UlInfoListElement_s::ReceptionStatus_e', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::m_rnti [variable]
    cls.add_instance_attribute('m_rnti', 'uint16_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::m_tpc [variable]
    cls.add_instance_attribute('m_tpc', 'uint8_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::UlInfoListElement_s::m_ulReception [variable]
    cls.add_instance_attribute('m_ulReception', 'std::vector< unsigned short >', is_const=False)
    return

def register_Ns3Vector2D_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(ns3::Vector2D const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(double _x, double _y) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector2D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    return

def register_Ns3Vector3D_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(ns3::Vector3D const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(double _x, double _y, double _z) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y'), param('double', '_z')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::z [variable]
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_Ns3VendorSpecificListElement_s_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s::VendorSpecificListElement_s() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s::VendorSpecificListElement_s(ns3::VendorSpecificListElement_s const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::VendorSpecificListElement_s const &', 'arg0')])
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s::m_length [variable]
    cls.add_instance_attribute('m_length', 'uint32_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s::m_type [variable]
    cls.add_instance_attribute('m_type', 'uint32_t', is_const=False)
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificListElement_s::m_value [variable]
    cls.add_instance_attribute('m_value', 'ns3::Ptr< ns3::VendorSpecificValue >', is_const=False)
    return

def register_Ns3Empty_methods(root_module, cls):
    ## empty.h (module 'core'): ns3::empty::empty() [constructor]
    cls.add_constructor([])
    ## empty.h (module 'core'): ns3::empty::empty(ns3::empty const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::empty const &', 'arg0')])
    return

def register_Ns3Int64x64_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_unary_numeric_operator('-')
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('*=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::int64x64_t const &', u'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t() [constructor]
    cls.add_constructor([])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(double v) [constructor]
    cls.add_constructor([param('double', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long double v) [constructor]
    cls.add_constructor([param('long double', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(int v) [constructor]
    cls.add_constructor([param('int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long int v) [constructor]
    cls.add_constructor([param('long int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long long int v) [constructor]
    cls.add_constructor([param('long long int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(unsigned int v) [constructor]
    cls.add_constructor([param('unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long unsigned int v) [constructor]
    cls.add_constructor([param('long unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long long unsigned int v) [constructor]
    cls.add_constructor([param('long long unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(int64_t hi, uint64_t lo) [constructor]
    cls.add_constructor([param('int64_t', 'hi'), param('uint64_t', 'lo')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(ns3::int64x64_t const & o) [copy constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'o')])
    ## int64x64-double.h (module 'core'): double ns3::int64x64_t::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): int64_t ns3::int64x64_t::GetHigh() const [member function]
    cls.add_method('GetHigh', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): uint64_t ns3::int64x64_t::GetLow() const [member function]
    cls.add_method('GetLow', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): static ns3::int64x64_t ns3::int64x64_t::Invert(uint64_t v) [member function]
    cls.add_method('Invert', 
                   'ns3::int64x64_t', 
                   [param('uint64_t', 'v')], 
                   is_static=True)
    ## int64x64-double.h (module 'core'): void ns3::int64x64_t::MulByInvert(ns3::int64x64_t const & o) [member function]
    cls.add_method('MulByInvert', 
                   'void', 
                   [param('ns3::int64x64_t const &', 'o')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::implementation [variable]
    cls.add_static_attribute('implementation', 'ns3::int64x64_t::impl_type const', is_const=True)
    return

def register_Ns3TbInfo_t_methods(root_module, cls):
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::tbInfo_t() [constructor]
    cls.add_constructor([])
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::tbInfo_t(ns3::tbInfo_t const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::tbInfo_t const &', 'arg0')])
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::corrupt [variable]
    cls.add_instance_attribute('corrupt', 'bool', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::downlink [variable]
    cls.add_instance_attribute('downlink', 'bool', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::harqFeedbackSent [variable]
    cls.add_instance_attribute('harqFeedbackSent', 'bool', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::harqProcessId [variable]
    cls.add_instance_attribute('harqProcessId', 'uint8_t', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::mcs [variable]
    cls.add_instance_attribute('mcs', 'uint8_t', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::mi [variable]
    cls.add_instance_attribute('mi', 'double', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::ndi [variable]
    cls.add_instance_attribute('ndi', 'uint8_t', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::rbBitmap [variable]
    cls.add_instance_attribute('rbBitmap', 'std::vector< int >', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::rv [variable]
    cls.add_instance_attribute('rv', 'uint8_t', is_const=False)
    ## lte-spectrum-phy.h (module 'lte'): ns3::tbInfo_t::size [variable]
    cls.add_instance_attribute('size', 'uint16_t', is_const=False)
    return

def register_Ns3AnimByteTag_methods(root_module, cls):
    ## animation-interface.h (module 'netanim'): ns3::AnimByteTag::AnimByteTag() [constructor]
    cls.add_constructor([])
    ## animation-interface.h (module 'netanim'): ns3::AnimByteTag::AnimByteTag(ns3::AnimByteTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AnimByteTag const &', 'arg0')])
    ## animation-interface.h (module 'netanim'): void ns3::AnimByteTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## animation-interface.h (module 'netanim'): uint64_t ns3::AnimByteTag::Get() const [member function]
    cls.add_method('Get', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## animation-interface.h (module 'netanim'): ns3::TypeId ns3::AnimByteTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## animation-interface.h (module 'netanim'): uint32_t ns3::AnimByteTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## animation-interface.h (module 'netanim'): static ns3::TypeId ns3::AnimByteTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## animation-interface.h (module 'netanim'): void ns3::AnimByteTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## animation-interface.h (module 'netanim'): void ns3::AnimByteTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## animation-interface.h (module 'netanim'): void ns3::AnimByteTag::Set(uint64_t AnimUid) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint64_t', 'AnimUid')])
    return

def register_Ns3Chunk_methods(root_module, cls):
    ## chunk.h (module 'network'): ns3::Chunk::Chunk() [constructor]
    cls.add_constructor([])
    ## chunk.h (module 'network'): ns3::Chunk::Chunk(ns3::Chunk const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Chunk const &', 'arg0')])
    ## chunk.h (module 'network'): uint32_t ns3::Chunk::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## chunk.h (module 'network'): static ns3::TypeId ns3::Chunk::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## chunk.h (module 'network'): void ns3::Chunk::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Header_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## header.h (module 'network'): ns3::Header::Header() [constructor]
    cls.add_constructor([])
    ## header.h (module 'network'): ns3::Header::Header(ns3::Header const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Header const &', 'arg0')])
    ## header.h (module 'network'): uint32_t ns3::Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## header.h (module 'network'): uint32_t ns3::Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): static ns3::TypeId ns3::Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## header.h (module 'network'): void ns3::Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): void ns3::Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Ipv4Header_methods(root_module, cls):
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::Ipv4Header(ns3::Ipv4Header const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Header const &', 'arg0')])
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::Ipv4Header() [constructor]
    cls.add_constructor([])
    ## ipv4-header.h (module 'internet'): uint32_t ns3::Ipv4Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## ipv4-header.h (module 'internet'): std::string ns3::Ipv4Header::DscpTypeToString(ns3::Ipv4Header::DscpType dscp) const [member function]
    cls.add_method('DscpTypeToString', 
                   'std::string', 
                   [param('ns3::Ipv4Header::DscpType', 'dscp')], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): std::string ns3::Ipv4Header::EcnTypeToString(ns3::Ipv4Header::EcnType ecn) const [member function]
    cls.add_method('EcnTypeToString', 
                   'std::string', 
                   [param('ns3::Ipv4Header::EcnType', 'ecn')], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::EnableChecksum() [member function]
    cls.add_method('EnableChecksum', 
                   'void', 
                   [])
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4Header::GetDestination() const [member function]
    cls.add_method('GetDestination', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::DscpType ns3::Ipv4Header::GetDscp() const [member function]
    cls.add_method('GetDscp', 
                   'ns3::Ipv4Header::DscpType', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Header::EcnType ns3::Ipv4Header::GetEcn() const [member function]
    cls.add_method('GetEcn', 
                   'ns3::Ipv4Header::EcnType', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint16_t ns3::Ipv4Header::GetFragmentOffset() const [member function]
    cls.add_method('GetFragmentOffset', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint16_t ns3::Ipv4Header::GetIdentification() const [member function]
    cls.add_method('GetIdentification', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): ns3::TypeId ns3::Ipv4Header::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-header.h (module 'internet'): uint16_t ns3::Ipv4Header::GetPayloadSize() const [member function]
    cls.add_method('GetPayloadSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint8_t ns3::Ipv4Header::GetProtocol() const [member function]
    cls.add_method('GetProtocol', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint32_t ns3::Ipv4Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-header.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4Header::GetSource() const [member function]
    cls.add_method('GetSource', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint8_t ns3::Ipv4Header::GetTos() const [member function]
    cls.add_method('GetTos', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): uint8_t ns3::Ipv4Header::GetTtl() const [member function]
    cls.add_method('GetTtl', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): static ns3::TypeId ns3::Ipv4Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4-header.h (module 'internet'): bool ns3::Ipv4Header::IsChecksumOk() const [member function]
    cls.add_method('IsChecksumOk', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): bool ns3::Ipv4Header::IsDontFragment() const [member function]
    cls.add_method('IsDontFragment', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): bool ns3::Ipv4Header::IsLastFragment() const [member function]
    cls.add_method('IsLastFragment', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetDestination(ns3::Ipv4Address destination) [member function]
    cls.add_method('SetDestination', 
                   'void', 
                   [param('ns3::Ipv4Address', 'destination')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetDontFragment() [member function]
    cls.add_method('SetDontFragment', 
                   'void', 
                   [])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetDscp(ns3::Ipv4Header::DscpType dscp) [member function]
    cls.add_method('SetDscp', 
                   'void', 
                   [param('ns3::Ipv4Header::DscpType', 'dscp')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetEcn(ns3::Ipv4Header::EcnType ecn) [member function]
    cls.add_method('SetEcn', 
                   'void', 
                   [param('ns3::Ipv4Header::EcnType', 'ecn')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetFragmentOffset(uint16_t offsetBytes) [member function]
    cls.add_method('SetFragmentOffset', 
                   'void', 
                   [param('uint16_t', 'offsetBytes')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetIdentification(uint16_t identification) [member function]
    cls.add_method('SetIdentification', 
                   'void', 
                   [param('uint16_t', 'identification')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetLastFragment() [member function]
    cls.add_method('SetLastFragment', 
                   'void', 
                   [])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetMayFragment() [member function]
    cls.add_method('SetMayFragment', 
                   'void', 
                   [])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetMoreFragments() [member function]
    cls.add_method('SetMoreFragments', 
                   'void', 
                   [])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetPayloadSize(uint16_t size) [member function]
    cls.add_method('SetPayloadSize', 
                   'void', 
                   [param('uint16_t', 'size')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetProtocol(uint8_t num) [member function]
    cls.add_method('SetProtocol', 
                   'void', 
                   [param('uint8_t', 'num')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetSource(ns3::Ipv4Address source) [member function]
    cls.add_method('SetSource', 
                   'void', 
                   [param('ns3::Ipv4Address', 'source')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetTos(uint8_t tos) [member function]
    cls.add_method('SetTos', 
                   'void', 
                   [param('uint8_t', 'tos')])
    ## ipv4-header.h (module 'internet'): void ns3::Ipv4Header::SetTtl(uint8_t ttl) [member function]
    cls.add_method('SetTtl', 
                   'void', 
                   [param('uint8_t', 'ttl')])
    return

def register_Ns3LteEnbRrcSapProvider_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::LteEnbRrcSapProvider() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::LteEnbRrcSapProvider(ns3::LteEnbRrcSapProvider const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteEnbRrcSapProvider const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::CompleteSetupUe(uint16_t rnti, ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters params) [member function]
    cls.add_method('CompleteSetupUe', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvMeasurementReport(uint16_t rnti, ns3::LteRrcSap::MeasurementReport msg) [member function]
    cls.add_method('RecvMeasurementReport', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::MeasurementReport', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvRrcConnectionReconfigurationCompleted(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReconfigurationCompleted msg) [member function]
    cls.add_method('RecvRrcConnectionReconfigurationCompleted', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReconfigurationCompleted', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvRrcConnectionReestablishmentComplete(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReestablishmentComplete msg) [member function]
    cls.add_method('RecvRrcConnectionReestablishmentComplete', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReestablishmentComplete', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvRrcConnectionReestablishmentRequest(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReestablishmentRequest msg) [member function]
    cls.add_method('RecvRrcConnectionReestablishmentRequest', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReestablishmentRequest', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvRrcConnectionRequest(uint16_t rnti, ns3::LteRrcSap::RrcConnectionRequest msg) [member function]
    cls.add_method('RecvRrcConnectionRequest', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionRequest', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapProvider::RecvRrcConnectionSetupCompleted(uint16_t rnti, ns3::LteRrcSap::RrcConnectionSetupCompleted msg) [member function]
    cls.add_method('RecvRrcConnectionSetupCompleted', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionSetupCompleted', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3LteEnbRrcSapProviderCompleteSetupUeParameters_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters::CompleteSetupUeParameters() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters::CompleteSetupUeParameters(ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters::srb0SapUser [variable]
    cls.add_instance_attribute('srb0SapUser', 'ns3::LteRlcSapUser *', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapProvider::CompleteSetupUeParameters::srb1SapUser [variable]
    cls.add_instance_attribute('srb1SapUser', 'ns3::LtePdcpSapUser *', is_const=False)
    return

def register_Ns3LteEnbRrcSapUser_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::LteEnbRrcSapUser() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::LteEnbRrcSapUser(ns3::LteEnbRrcSapUser const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteEnbRrcSapUser const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::RrcConnectionReconfiguration ns3::LteEnbRrcSapUser::DecodeHandoverCommand(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('DecodeHandoverCommand', 
                   'ns3::LteRrcSap::RrcConnectionReconfiguration', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteRrcSap::HandoverPreparationInfo ns3::LteEnbRrcSapUser::DecodeHandoverPreparationInformation(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('DecodeHandoverPreparationInformation', 
                   'ns3::LteRrcSap::HandoverPreparationInfo', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): ns3::Ptr<ns3::Packet> ns3::LteEnbRrcSapUser::EncodeHandoverCommand(ns3::LteRrcSap::RrcConnectionReconfiguration msg) [member function]
    cls.add_method('EncodeHandoverCommand', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::LteRrcSap::RrcConnectionReconfiguration', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): ns3::Ptr<ns3::Packet> ns3::LteEnbRrcSapUser::EncodeHandoverPreparationInformation(ns3::LteRrcSap::HandoverPreparationInfo msg) [member function]
    cls.add_method('EncodeHandoverPreparationInformation', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::LteRrcSap::HandoverPreparationInfo', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::RemoveUe(uint16_t rnti) [member function]
    cls.add_method('RemoveUe', 
                   'void', 
                   [param('uint16_t', 'rnti')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionReconfiguration(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReconfiguration msg) [member function]
    cls.add_method('SendRrcConnectionReconfiguration', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReconfiguration', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionReestablishment(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReestablishment msg) [member function]
    cls.add_method('SendRrcConnectionReestablishment', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReestablishment', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionReestablishmentReject(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReestablishmentReject msg) [member function]
    cls.add_method('SendRrcConnectionReestablishmentReject', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReestablishmentReject', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionReject(uint16_t rnti, ns3::LteRrcSap::RrcConnectionReject msg) [member function]
    cls.add_method('SendRrcConnectionReject', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionReject', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionRelease(uint16_t rnti, ns3::LteRrcSap::RrcConnectionRelease msg) [member function]
    cls.add_method('SendRrcConnectionRelease', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionRelease', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendRrcConnectionSetup(uint16_t rnti, ns3::LteRrcSap::RrcConnectionSetup msg) [member function]
    cls.add_method('SendRrcConnectionSetup', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteRrcSap::RrcConnectionSetup', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SendSystemInformation(ns3::LteRrcSap::SystemInformation msg) [member function]
    cls.add_method('SendSystemInformation', 
                   'void', 
                   [param('ns3::LteRrcSap::SystemInformation', 'msg')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-rrc-sap.h (module 'lte'): void ns3::LteEnbRrcSapUser::SetupUe(uint16_t rnti, ns3::LteEnbRrcSapUser::SetupUeParameters params) [member function]
    cls.add_method('SetupUe', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('ns3::LteEnbRrcSapUser::SetupUeParameters', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3LteEnbRrcSapUserSetupUeParameters_methods(root_module, cls):
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::SetupUeParameters::SetupUeParameters() [constructor]
    cls.add_constructor([])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::SetupUeParameters::SetupUeParameters(ns3::LteEnbRrcSapUser::SetupUeParameters const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteEnbRrcSapUser::SetupUeParameters const &', 'arg0')])
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::SetupUeParameters::srb0SapProvider [variable]
    cls.add_instance_attribute('srb0SapProvider', 'ns3::LteRlcSapProvider *', is_const=False)
    ## lte-rrc-sap.h (module 'lte'): ns3::LteEnbRrcSapUser::SetupUeParameters::srb1SapProvider [variable]
    cls.add_instance_attribute('srb1SapProvider', 'ns3::LtePdcpSapProvider *', is_const=False)
    return

def register_Ns3Object_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::Object() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): void ns3::Object::AggregateObject(ns3::Ptr<ns3::Object> other) [member function]
    cls.add_method('AggregateObject', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'other')])
    ## object.h (module 'core'): void ns3::Object::Dispose() [member function]
    cls.add_method('Dispose', 
                   'void', 
                   [])
    ## object.h (module 'core'): ns3::Object::AggregateIterator ns3::Object::GetAggregateIterator() const [member function]
    cls.add_method('GetAggregateIterator', 
                   'ns3::Object::AggregateIterator', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::TypeId ns3::Object::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object.h (module 'core'): static ns3::TypeId ns3::Object::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object.h (module 'core'): void ns3::Object::Initialize() [member function]
    cls.add_method('Initialize', 
                   'void', 
                   [])
    ## object.h (module 'core'): ns3::Object::Object(ns3::Object const & o) [copy constructor]
    cls.add_constructor([param('ns3::Object const &', 'o')], 
                        visibility='protected')
    ## object.h (module 'core'): void ns3::Object::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectAggregateIterator_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator(ns3::Object::AggregateIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Object::AggregateIterator const &', 'arg0')])
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): bool ns3::Object::AggregateIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::Ptr<ns3::Object const> ns3::Object::AggregateIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::Ptr< ns3::Object const >', 
                   [])
    return

def register_Ns3PacketBurst_methods(root_module, cls):
    ## packet-burst.h (module 'network'): ns3::PacketBurst::PacketBurst(ns3::PacketBurst const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketBurst const &', 'arg0')])
    ## packet-burst.h (module 'network'): ns3::PacketBurst::PacketBurst() [constructor]
    cls.add_constructor([])
    ## packet-burst.h (module 'network'): void ns3::PacketBurst::AddPacket(ns3::Ptr<ns3::Packet> packet) [member function]
    cls.add_method('AddPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    ## packet-burst.h (module 'network'): std::_List_const_iterator<ns3::Ptr<ns3::Packet> > ns3::PacketBurst::Begin() const [member function]
    cls.add_method('Begin', 
                   'std::_List_const_iterator< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): ns3::Ptr<ns3::PacketBurst> ns3::PacketBurst::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): std::_List_const_iterator<ns3::Ptr<ns3::Packet> > ns3::PacketBurst::End() const [member function]
    cls.add_method('End', 
                   'std::_List_const_iterator< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): uint32_t ns3::PacketBurst::GetNPackets() const [member function]
    cls.add_method('GetNPackets', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): std::list<ns3::Ptr<ns3::Packet>, std::allocator<ns3::Ptr<ns3::Packet> > > ns3::PacketBurst::GetPackets() const [member function]
    cls.add_method('GetPackets', 
                   'std::list< ns3::Ptr< ns3::Packet > >', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): uint32_t ns3::PacketBurst::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet-burst.h (module 'network'): static ns3::TypeId ns3::PacketBurst::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## packet-burst.h (module 'network'): void ns3::PacketBurst::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3RandomVariableStream_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::RandomVariableStream::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream::RandomVariableStream() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetStream(int64_t stream) [member function]
    cls.add_method('SetStream', 
                   'void', 
                   [param('int64_t', 'stream')])
    ## random-variable-stream.h (module 'core'): int64_t ns3::RandomVariableStream::GetStream() const [member function]
    cls.add_method('GetStream', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetAntithetic(bool isAntithetic) [member function]
    cls.add_method('SetAntithetic', 
                   'void', 
                   [param('bool', 'isAntithetic')])
    ## random-variable-stream.h (module 'core'): bool ns3::RandomVariableStream::IsAntithetic() const [member function]
    cls.add_method('IsAntithetic', 
                   'bool', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::RandomVariableStream::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::RandomVariableStream::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): ns3::RngStream * ns3::RandomVariableStream::Peek() const [member function]
    cls.add_method('Peek', 
                   'ns3::RngStream *', 
                   [], 
                   is_const=True, visibility='protected')
    return

def register_Ns3SequentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::SequentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable::SequentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): ns3::Ptr<ns3::RandomVariableStream> ns3::SequentialRandomVariable::GetIncrement() const [member function]
    cls.add_method('GetIncrement', 
                   'ns3::Ptr< ns3::RandomVariableStream >', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetConsecutive() const [member function]
    cls.add_method('GetConsecutive', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter< ns3::AttributeAccessor > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter< ns3::AttributeChecker > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter< ns3::AttributeValue > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount(ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter< ns3::CallbackImplBase > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount(ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter< ns3::EventImpl > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter< ns3::Hash::Implementation > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3Ipv4MulticastRoute_Ns3Empty_Ns3DefaultDeleter__lt__ns3Ipv4MulticastRoute__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter< ns3::Ipv4MulticastRoute > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Ipv4MulticastRoute, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4MulticastRoute> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3Ipv4Route_Ns3Empty_Ns3DefaultDeleter__lt__ns3Ipv4Route__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter< ns3::Ipv4Route > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Ipv4Route, ns3::empty, ns3::DefaultDeleter<ns3::Ipv4Route> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3LteControlMessage_Ns3Empty_Ns3DefaultDeleter__lt__ns3LteControlMessage__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> >::SimpleRefCount(ns3::SimpleRefCount<ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter< ns3::LteControlMessage > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::LteControlMessage, ns3::empty, ns3::DefaultDeleter<ns3::LteControlMessage> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3LteHarqPhy_Ns3Empty_Ns3DefaultDeleter__lt__ns3LteHarqPhy__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> >::SimpleRefCount(ns3::SimpleRefCount<ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter< ns3::LteHarqPhy > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::LteHarqPhy, ns3::empty, ns3::DefaultDeleter<ns3::LteHarqPhy> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount(ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter< ns3::NixVector > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3OutputStreamWrapper_Ns3Empty_Ns3DefaultDeleter__lt__ns3OutputStreamWrapper__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >::SimpleRefCount(ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter< ns3::OutputStreamWrapper > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::OutputStreamWrapper, ns3::empty, ns3::DefaultDeleter<ns3::OutputStreamWrapper> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter< ns3::Packet > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3SpectrumModel_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumModel__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumModel > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::SpectrumModel, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumModel> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3SpectrumSignalParameters_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumSignalParameters__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumSignalParameters > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::SpectrumSignalParameters, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumSignalParameters> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3SpectrumValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3SpectrumValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter< ns3::SpectrumValue > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::SpectrumValue, ns3::empty, ns3::DefaultDeleter<ns3::SpectrumValue> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter< ns3::TraceSourceAccessor > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3VendorSpecificValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3VendorSpecificValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter< ns3::VendorSpecificValue > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::VendorSpecificValue, ns3::empty, ns3::DefaultDeleter<ns3::VendorSpecificValue> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3Socket_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::Socket::Socket(ns3::Socket const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Socket const &', 'arg0')])
    ## socket.h (module 'network'): ns3::Socket::Socket() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): int ns3::Socket::Bind(ns3::Address const & address) [member function]
    cls.add_method('Bind', 
                   'int', 
                   [param('ns3::Address const &', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::Bind() [member function]
    cls.add_method('Bind', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::Bind6() [member function]
    cls.add_method('Bind6', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::Socket::BindToNetDevice(ns3::Ptr<ns3::NetDevice> netdevice) [member function]
    cls.add_method('BindToNetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'netdevice')], 
                   is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::Close() [member function]
    cls.add_method('Close', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::Connect(ns3::Address const & address) [member function]
    cls.add_method('Connect', 
                   'int', 
                   [param('ns3::Address const &', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): static ns3::Ptr<ns3::Socket> ns3::Socket::CreateSocket(ns3::Ptr<ns3::Node> node, ns3::TypeId tid) [member function]
    cls.add_method('CreateSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::TypeId', 'tid')], 
                   is_static=True)
    ## socket.h (module 'network'): bool ns3::Socket::GetAllowBroadcast() const [member function]
    cls.add_method('GetAllowBroadcast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Socket::GetBoundNetDevice() [member function]
    cls.add_method('GetBoundNetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [])
    ## socket.h (module 'network'): ns3::Socket::SocketErrno ns3::Socket::GetErrno() const [member function]
    cls.add_method('GetErrno', 
                   'ns3::Socket::SocketErrno', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::Socket::GetIpTos() const [member function]
    cls.add_method('GetIpTos', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): uint8_t ns3::Socket::GetIpTtl() const [member function]
    cls.add_method('GetIpTtl', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::Socket::GetIpv6HopLimit() const [member function]
    cls.add_method('GetIpv6HopLimit', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::Socket::GetIpv6Tclass() const [member function]
    cls.add_method('GetIpv6Tclass', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): ns3::Ptr<ns3::Node> ns3::Socket::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::Socket::GetRxAvailable() const [member function]
    cls.add_method('GetRxAvailable', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::GetSockName(ns3::Address & address) const [member function]
    cls.add_method('GetSockName', 
                   'int', 
                   [param('ns3::Address &', 'address')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): ns3::Socket::SocketType ns3::Socket::GetSocketType() const [member function]
    cls.add_method('GetSocketType', 
                   'ns3::Socket::SocketType', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::Socket::GetTxAvailable() const [member function]
    cls.add_method('GetTxAvailable', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::Socket::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsIpRecvTos() const [member function]
    cls.add_method('IsIpRecvTos', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsIpRecvTtl() const [member function]
    cls.add_method('IsIpRecvTtl', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsIpv6RecvHopLimit() const [member function]
    cls.add_method('IsIpv6RecvHopLimit', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsIpv6RecvTclass() const [member function]
    cls.add_method('IsIpv6RecvTclass', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsRecvPktInfo() const [member function]
    cls.add_method('IsRecvPktInfo', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): int ns3::Socket::Listen() [member function]
    cls.add_method('Listen', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Socket::Recv(uint32_t maxSize, uint32_t flags) [member function]
    cls.add_method('Recv', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'maxSize'), param('uint32_t', 'flags')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Socket::Recv() [member function]
    cls.add_method('Recv', 
                   'ns3::Ptr< ns3::Packet >', 
                   [])
    ## socket.h (module 'network'): int ns3::Socket::Recv(uint8_t * buf, uint32_t size, uint32_t flags) [member function]
    cls.add_method('Recv', 
                   'int', 
                   [param('uint8_t *', 'buf'), param('uint32_t', 'size'), param('uint32_t', 'flags')])
    ## socket.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Socket::RecvFrom(uint32_t maxSize, uint32_t flags, ns3::Address & fromAddress) [member function]
    cls.add_method('RecvFrom', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'maxSize'), param('uint32_t', 'flags'), param('ns3::Address &', 'fromAddress')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Socket::RecvFrom(ns3::Address & fromAddress) [member function]
    cls.add_method('RecvFrom', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::Address &', 'fromAddress')])
    ## socket.h (module 'network'): int ns3::Socket::RecvFrom(uint8_t * buf, uint32_t size, uint32_t flags, ns3::Address & fromAddress) [member function]
    cls.add_method('RecvFrom', 
                   'int', 
                   [param('uint8_t *', 'buf'), param('uint32_t', 'size'), param('uint32_t', 'flags'), param('ns3::Address &', 'fromAddress')])
    ## socket.h (module 'network'): int ns3::Socket::Send(ns3::Ptr<ns3::Packet> p, uint32_t flags) [member function]
    cls.add_method('Send', 
                   'int', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('uint32_t', 'flags')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::Send(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('Send', 
                   'int', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    ## socket.h (module 'network'): int ns3::Socket::Send(uint8_t const * buf, uint32_t size, uint32_t flags) [member function]
    cls.add_method('Send', 
                   'int', 
                   [param('uint8_t const *', 'buf'), param('uint32_t', 'size'), param('uint32_t', 'flags')])
    ## socket.h (module 'network'): int ns3::Socket::SendTo(ns3::Ptr<ns3::Packet> p, uint32_t flags, ns3::Address const & toAddress) [member function]
    cls.add_method('SendTo', 
                   'int', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('uint32_t', 'flags'), param('ns3::Address const &', 'toAddress')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::SendTo(uint8_t const * buf, uint32_t size, uint32_t flags, ns3::Address const & address) [member function]
    cls.add_method('SendTo', 
                   'int', 
                   [param('uint8_t const *', 'buf'), param('uint32_t', 'size'), param('uint32_t', 'flags'), param('ns3::Address const &', 'address')])
    ## socket.h (module 'network'): void ns3::Socket::SetAcceptCallback(ns3::Callback<bool, ns3::Ptr<ns3::Socket>, ns3::Address const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> connectionRequest, ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::Address const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> newConnectionCreated) [member function]
    cls.add_method('SetAcceptCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::Socket >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'connectionRequest'), param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'newConnectionCreated')])
    ## socket.h (module 'network'): bool ns3::Socket::SetAllowBroadcast(bool allowBroadcast) [member function]
    cls.add_method('SetAllowBroadcast', 
                   'bool', 
                   [param('bool', 'allowBroadcast')], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::Socket::SetCloseCallbacks(ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> normalClose, ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> errorClose) [member function]
    cls.add_method('SetCloseCallbacks', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'normalClose'), param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'errorClose')])
    ## socket.h (module 'network'): void ns3::Socket::SetConnectCallback(ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> connectionSucceeded, ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> connectionFailed) [member function]
    cls.add_method('SetConnectCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'connectionSucceeded'), param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'connectionFailed')])
    ## socket.h (module 'network'): void ns3::Socket::SetDataSentCallback(ns3::Callback<void, ns3::Ptr<ns3::Socket>, unsigned int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> dataSent) [member function]
    cls.add_method('SetDataSentCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, unsigned int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'dataSent')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpRecvTos(bool ipv4RecvTos) [member function]
    cls.add_method('SetIpRecvTos', 
                   'void', 
                   [param('bool', 'ipv4RecvTos')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpRecvTtl(bool ipv4RecvTtl) [member function]
    cls.add_method('SetIpRecvTtl', 
                   'void', 
                   [param('bool', 'ipv4RecvTtl')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpTos(uint8_t ipTos) [member function]
    cls.add_method('SetIpTos', 
                   'void', 
                   [param('uint8_t', 'ipTos')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpTtl(uint8_t ipTtl) [member function]
    cls.add_method('SetIpTtl', 
                   'void', 
                   [param('uint8_t', 'ipTtl')], 
                   is_virtual=True)
    ## socket.h (module 'network'): void ns3::Socket::SetIpv6HopLimit(uint8_t ipHopLimit) [member function]
    cls.add_method('SetIpv6HopLimit', 
                   'void', 
                   [param('uint8_t', 'ipHopLimit')], 
                   is_virtual=True)
    ## socket.h (module 'network'): void ns3::Socket::SetIpv6RecvHopLimit(bool ipv6RecvHopLimit) [member function]
    cls.add_method('SetIpv6RecvHopLimit', 
                   'void', 
                   [param('bool', 'ipv6RecvHopLimit')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpv6RecvTclass(bool ipv6RecvTclass) [member function]
    cls.add_method('SetIpv6RecvTclass', 
                   'void', 
                   [param('bool', 'ipv6RecvTclass')])
    ## socket.h (module 'network'): void ns3::Socket::SetIpv6Tclass(int ipTclass) [member function]
    cls.add_method('SetIpv6Tclass', 
                   'void', 
                   [param('int', 'ipTclass')])
    ## socket.h (module 'network'): void ns3::Socket::SetRecvCallback(ns3::Callback<void, ns3::Ptr<ns3::Socket>, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> arg0) [member function]
    cls.add_method('SetRecvCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'arg0')])
    ## socket.h (module 'network'): void ns3::Socket::SetRecvPktInfo(bool flag) [member function]
    cls.add_method('SetRecvPktInfo', 
                   'void', 
                   [param('bool', 'flag')])
    ## socket.h (module 'network'): void ns3::Socket::SetSendCallback(ns3::Callback<void, ns3::Ptr<ns3::Socket>, unsigned int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> sendCb) [member function]
    cls.add_method('SetSendCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Socket >, unsigned int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'sendCb')])
    ## socket.h (module 'network'): int ns3::Socket::ShutdownRecv() [member function]
    cls.add_method('ShutdownRecv', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): int ns3::Socket::ShutdownSend() [member function]
    cls.add_method('ShutdownSend', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::Socket::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## socket.h (module 'network'): bool ns3::Socket::IsManualIpTos() const [member function]
    cls.add_method('IsManualIpTos', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## socket.h (module 'network'): bool ns3::Socket::IsManualIpTtl() const [member function]
    cls.add_method('IsManualIpTtl', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## socket.h (module 'network'): bool ns3::Socket::IsManualIpv6HopLimit() const [member function]
    cls.add_method('IsManualIpv6HopLimit', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## socket.h (module 'network'): bool ns3::Socket::IsManualIpv6Tclass() const [member function]
    cls.add_method('IsManualIpv6Tclass', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyConnectionFailed() [member function]
    cls.add_method('NotifyConnectionFailed', 
                   'void', 
                   [], 
                   visibility='protected')
    ## socket.h (module 'network'): bool ns3::Socket::NotifyConnectionRequest(ns3::Address const & from) [member function]
    cls.add_method('NotifyConnectionRequest', 
                   'bool', 
                   [param('ns3::Address const &', 'from')], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyConnectionSucceeded() [member function]
    cls.add_method('NotifyConnectionSucceeded', 
                   'void', 
                   [], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyDataRecv() [member function]
    cls.add_method('NotifyDataRecv', 
                   'void', 
                   [], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyDataSent(uint32_t size) [member function]
    cls.add_method('NotifyDataSent', 
                   'void', 
                   [param('uint32_t', 'size')], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyErrorClose() [member function]
    cls.add_method('NotifyErrorClose', 
                   'void', 
                   [], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyNewConnectionCreated(ns3::Ptr<ns3::Socket> socket, ns3::Address const & from) [member function]
    cls.add_method('NotifyNewConnectionCreated', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket'), param('ns3::Address const &', 'from')], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifyNormalClose() [member function]
    cls.add_method('NotifyNormalClose', 
                   'void', 
                   [], 
                   visibility='protected')
    ## socket.h (module 'network'): void ns3::Socket::NotifySend(uint32_t spaceAvailable) [member function]
    cls.add_method('NotifySend', 
                   'void', 
                   [param('uint32_t', 'spaceAvailable')], 
                   visibility='protected')
    return

def register_Ns3SocketAddressTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketAddressTag::SocketAddressTag(ns3::SocketAddressTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketAddressTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketAddressTag::SocketAddressTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketAddressTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): ns3::Address ns3::SocketAddressTag::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketAddressTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketAddressTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketAddressTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): void ns3::SocketAddressTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketAddressTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketAddressTag::SetAddress(ns3::Address addr) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'addr')])
    return

def register_Ns3SocketIpTosTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketIpTosTag::SocketIpTosTag(ns3::SocketIpTosTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketIpTosTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketIpTosTag::SocketIpTosTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketIpTosTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketIpTosTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketIpTosTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::SocketIpTosTag::GetTos() const [member function]
    cls.add_method('GetTos', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketIpTosTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): void ns3::SocketIpTosTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpTosTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpTosTag::SetTos(uint8_t tos) [member function]
    cls.add_method('SetTos', 
                   'void', 
                   [param('uint8_t', 'tos')])
    return

def register_Ns3SocketIpTtlTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketIpTtlTag::SocketIpTtlTag(ns3::SocketIpTtlTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketIpTtlTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketIpTtlTag::SocketIpTtlTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketIpTtlTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketIpTtlTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketIpTtlTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::SocketIpTtlTag::GetTtl() const [member function]
    cls.add_method('GetTtl', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketIpTtlTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): void ns3::SocketIpTtlTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpTtlTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpTtlTag::SetTtl(uint8_t ttl) [member function]
    cls.add_method('SetTtl', 
                   'void', 
                   [param('uint8_t', 'ttl')])
    return

def register_Ns3SocketIpv6HopLimitTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketIpv6HopLimitTag::SocketIpv6HopLimitTag(ns3::SocketIpv6HopLimitTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketIpv6HopLimitTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketIpv6HopLimitTag::SocketIpv6HopLimitTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketIpv6HopLimitTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::SocketIpv6HopLimitTag::GetHopLimit() const [member function]
    cls.add_method('GetHopLimit', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketIpv6HopLimitTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketIpv6HopLimitTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketIpv6HopLimitTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6HopLimitTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6HopLimitTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6HopLimitTag::SetHopLimit(uint8_t hopLimit) [member function]
    cls.add_method('SetHopLimit', 
                   'void', 
                   [param('uint8_t', 'hopLimit')])
    return

def register_Ns3SocketIpv6TclassTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketIpv6TclassTag::SocketIpv6TclassTag(ns3::SocketIpv6TclassTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketIpv6TclassTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketIpv6TclassTag::SocketIpv6TclassTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketIpv6TclassTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketIpv6TclassTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketIpv6TclassTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint8_t ns3::SocketIpv6TclassTag::GetTclass() const [member function]
    cls.add_method('GetTclass', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketIpv6TclassTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6TclassTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6TclassTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketIpv6TclassTag::SetTclass(uint8_t tclass) [member function]
    cls.add_method('SetTclass', 
                   'void', 
                   [param('uint8_t', 'tclass')])
    return

def register_Ns3SocketSetDontFragmentTag_methods(root_module, cls):
    ## socket.h (module 'network'): ns3::SocketSetDontFragmentTag::SocketSetDontFragmentTag(ns3::SocketSetDontFragmentTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SocketSetDontFragmentTag const &', 'arg0')])
    ## socket.h (module 'network'): ns3::SocketSetDontFragmentTag::SocketSetDontFragmentTag() [constructor]
    cls.add_constructor([])
    ## socket.h (module 'network'): void ns3::SocketSetDontFragmentTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketSetDontFragmentTag::Disable() [member function]
    cls.add_method('Disable', 
                   'void', 
                   [])
    ## socket.h (module 'network'): void ns3::SocketSetDontFragmentTag::Enable() [member function]
    cls.add_method('Enable', 
                   'void', 
                   [])
    ## socket.h (module 'network'): ns3::TypeId ns3::SocketSetDontFragmentTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): uint32_t ns3::SocketSetDontFragmentTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): static ns3::TypeId ns3::SocketSetDontFragmentTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## socket.h (module 'network'): bool ns3::SocketSetDontFragmentTag::IsEnabled() const [member function]
    cls.add_method('IsEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    ## socket.h (module 'network'): void ns3::SocketSetDontFragmentTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## socket.h (module 'network'): void ns3::SocketSetDontFragmentTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3SpectrumInterference_methods(root_module, cls):
    ## spectrum-interference.h (module 'spectrum'): ns3::SpectrumInterference::SpectrumInterference(ns3::SpectrumInterference const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumInterference const &', 'arg0')])
    ## spectrum-interference.h (module 'spectrum'): ns3::SpectrumInterference::SpectrumInterference() [constructor]
    cls.add_constructor([])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::AbortRx() [member function]
    cls.add_method('AbortRx', 
                   'void', 
                   [])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::AddSignal(ns3::Ptr<ns3::SpectrumValue const> spd, ns3::Time const duration) [member function]
    cls.add_method('AddSignal', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'spd'), param('ns3::Time const', 'duration')])
    ## spectrum-interference.h (module 'spectrum'): bool ns3::SpectrumInterference::EndRx() [member function]
    cls.add_method('EndRx', 
                   'bool', 
                   [])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::SetErrorModel(ns3::Ptr<ns3::SpectrumErrorModel> e) [member function]
    cls.add_method('SetErrorModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumErrorModel >', 'e')])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::SetNoisePowerSpectralDensity(ns3::Ptr<ns3::SpectrumValue const> noisePsd) [member function]
    cls.add_method('SetNoisePowerSpectralDensity', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'noisePsd')])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::StartRx(ns3::Ptr<const ns3::Packet> p, ns3::Ptr<ns3::SpectrumValue const> rxPsd) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'p'), param('ns3::Ptr< ns3::SpectrumValue const >', 'rxPsd')])
    ## spectrum-interference.h (module 'spectrum'): void ns3::SpectrumInterference::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3SpectrumModel_methods(root_module, cls):
    cls.add_binary_comparison_operator('==')
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(ns3::SpectrumModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumModel const &', 'arg0')])
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(std::vector<double, std::allocator<double> > centerFreqs) [constructor]
    cls.add_constructor([param('std::vector< double >', 'centerFreqs')])
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModel::SpectrumModel(ns3::Bands bands) [constructor]
    cls.add_constructor([param('ns3::Bands', 'bands')])
    ## spectrum-model.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const ns3::BandInfo*,std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> > > ns3::SpectrumModel::Begin() const [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::BandInfo const *, std::vector< ns3::BandInfo > >', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const ns3::BandInfo*,std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> > > ns3::SpectrumModel::End() const [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::BandInfo const *, std::vector< ns3::BandInfo > >', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): size_t ns3::SpectrumModel::GetNumBands() const [member function]
    cls.add_method('GetNumBands', 
                   'size_t', 
                   [], 
                   is_const=True)
    ## spectrum-model.h (module 'spectrum'): ns3::SpectrumModelUid_t ns3::SpectrumModel::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'ns3::SpectrumModelUid_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3SpectrumPhy_methods(root_module, cls):
    ## spectrum-phy.h (module 'spectrum'): ns3::SpectrumPhy::SpectrumPhy() [constructor]
    cls.add_constructor([])
    ## spectrum-phy.h (module 'spectrum'): static ns3::TypeId ns3::SpectrumPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetDevice(ns3::Ptr<ns3::NetDevice> d) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'd')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::NetDevice> ns3::SpectrumPhy::GetDevice() [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetMobility(ns3::Ptr<ns3::MobilityModel> m) [member function]
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'm')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::MobilityModel> ns3::SpectrumPhy::GetMobility() [member function]
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::MobilityModel >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::SetChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumModel const> ns3::SpectrumPhy::GetRxSpectrumModel() const [member function]
    cls.add_method('GetRxSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): ns3::Ptr<ns3::AntennaModel> ns3::SpectrumPhy::GetRxAntenna() [member function]
    cls.add_method('GetRxAntenna', 
                   'ns3::Ptr< ns3::AntennaModel >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-phy.h (module 'spectrum'): void ns3::SpectrumPhy::StartRx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3SpectrumSignalParameters_methods(root_module, cls):
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::SpectrumSignalParameters() [constructor]
    cls.add_constructor([])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::SpectrumSignalParameters(ns3::SpectrumSignalParameters const & p) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumSignalParameters const &', 'p')])
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumSignalParameters> ns3::SpectrumSignalParameters::Copy() [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::SpectrumSignalParameters >', 
                   [], 
                   is_virtual=True)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::duration [variable]
    cls.add_instance_attribute('duration', 'ns3::Time', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::psd [variable]
    cls.add_instance_attribute('psd', 'ns3::Ptr< ns3::SpectrumValue >', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::txAntenna [variable]
    cls.add_instance_attribute('txAntenna', 'ns3::Ptr< ns3::AntennaModel >', is_const=False)
    ## spectrum-signal-parameters.h (module 'spectrum'): ns3::SpectrumSignalParameters::txPhy [variable]
    cls.add_instance_attribute('txPhy', 'ns3::Ptr< ns3::SpectrumPhy >', is_const=False)
    return

def register_Ns3SpectrumValue_methods(root_module, cls):
    cls.add_binary_numeric_operator('*', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_unary_numeric_operator('-')
    cls.add_binary_numeric_operator('-', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('double', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::SpectrumValue'], root_module['ns3::SpectrumValue'], param('ns3::SpectrumValue const &', u'right'))
    cls.add_output_stream_operator()
    cls.add_inplace_numeric_operator('*=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('*=', param('double', u'right'))
    cls.add_inplace_numeric_operator('+=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('+=', param('double', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('double', u'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::SpectrumValue const &', u'right'))
    cls.add_inplace_numeric_operator('/=', param('double', u'right'))
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue(ns3::SpectrumValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumValue const &', 'arg0')])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue(ns3::Ptr<ns3::SpectrumModel const> sm) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::SpectrumModel const >', 'sm')])
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumValue::SpectrumValue() [constructor]
    cls.add_constructor([])
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const ns3::BandInfo*,std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> > > ns3::SpectrumValue::ConstBandsBegin() const [member function]
    cls.add_method('ConstBandsBegin', 
                   '__gnu_cxx::__normal_iterator< ns3::BandInfo const *, std::vector< ns3::BandInfo > >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const ns3::BandInfo*,std::vector<ns3::BandInfo, std::allocator<ns3::BandInfo> > > ns3::SpectrumValue::ConstBandsEnd() const [member function]
    cls.add_method('ConstBandsEnd', 
                   '__gnu_cxx::__normal_iterator< ns3::BandInfo const *, std::vector< ns3::BandInfo > >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const double*,std::vector<double, std::allocator<double> > > ns3::SpectrumValue::ConstValuesBegin() const [member function]
    cls.add_method('ConstValuesBegin', 
                   '__gnu_cxx::__normal_iterator< double const *, std::vector< double > >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<const double*,std::vector<double, std::allocator<double> > > ns3::SpectrumValue::ConstValuesEnd() const [member function]
    cls.add_method('ConstValuesEnd', 
                   '__gnu_cxx::__normal_iterator< double const *, std::vector< double > >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumValue> ns3::SpectrumValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::Ptr<ns3::SpectrumModel const> ns3::SpectrumValue::GetSpectrumModel() const [member function]
    cls.add_method('GetSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): ns3::SpectrumModelUid_t ns3::SpectrumValue::GetSpectrumModelUid() const [member function]
    cls.add_method('GetSpectrumModelUid', 
                   'ns3::SpectrumModelUid_t', 
                   [], 
                   is_const=True)
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<double*,std::vector<double, std::allocator<double> > > ns3::SpectrumValue::ValuesBegin() [member function]
    cls.add_method('ValuesBegin', 
                   '__gnu_cxx::__normal_iterator< double *, std::vector< double > >', 
                   [])
    ## spectrum-value.h (module 'spectrum'): __gnu_cxx::__normal_iterator<double*,std::vector<double, std::allocator<double> > > ns3::SpectrumValue::ValuesEnd() [member function]
    cls.add_method('ValuesEnd', 
                   '__gnu_cxx::__normal_iterator< double *, std::vector< double > >', 
                   [])
    return

def register_Ns3Time_methods(root_module, cls):
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('-=', param('ns3::Time const &', u'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    ## nstime.h (module 'core'): ns3::Time::Time() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::Time const & o) [copy constructor]
    cls.add_constructor([param('ns3::Time const &', 'o')])
    ## nstime.h (module 'core'): ns3::Time::Time(double v) [constructor]
    cls.add_constructor([param('double', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(int v) [constructor]
    cls.add_constructor([param('int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long int v) [constructor]
    cls.add_constructor([param('long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long int v) [constructor]
    cls.add_constructor([param('long long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(unsigned int v) [constructor]
    cls.add_constructor([param('unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long unsigned int v) [constructor]
    cls.add_constructor([param('long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long unsigned int v) [constructor]
    cls.add_constructor([param('long long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::int64x64_t const & v) [constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(std::string const & s) [constructor]
    cls.add_constructor([param('std::string const &', 's')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit ns3::Time::As(ns3::Time::Unit const unit) const [member function]
    cls.add_method('As', 
                   'ns3::TimeWithUnit', 
                   [param('ns3::Time::Unit const', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int ns3::Time::Compare(ns3::Time const & o) const [member function]
    cls.add_method('Compare', 
                   'int', 
                   [param('ns3::Time const &', 'o')], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value, ns3::Time::Unit unit) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromDouble(double value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromDouble', 
                   'ns3::Time', 
                   [param('double', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromInteger(uint64_t value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromInteger', 
                   'ns3::Time', 
                   [param('uint64_t', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDays() const [member function]
    cls.add_method('GetDays', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetFemtoSeconds() const [member function]
    cls.add_method('GetFemtoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetHours() const [member function]
    cls.add_method('GetHours', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetInteger() const [member function]
    cls.add_method('GetInteger', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMicroSeconds() const [member function]
    cls.add_method('GetMicroSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMilliSeconds() const [member function]
    cls.add_method('GetMilliSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetMinutes() const [member function]
    cls.add_method('GetMinutes', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetNanoSeconds() const [member function]
    cls.add_method('GetNanoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetPicoSeconds() const [member function]
    cls.add_method('GetPicoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time::Unit ns3::Time::GetResolution() [member function]
    cls.add_method('GetResolution', 
                   'ns3::Time::Unit', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetSeconds() const [member function]
    cls.add_method('GetSeconds', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetTimeStep() const [member function]
    cls.add_method('GetTimeStep', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetYears() const [member function]
    cls.add_method('GetYears', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsNegative() const [member function]
    cls.add_method('IsNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsPositive() const [member function]
    cls.add_method('IsPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyNegative() const [member function]
    cls.add_method('IsStrictlyNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyPositive() const [member function]
    cls.add_method('IsStrictlyPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsZero() const [member function]
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Max() [member function]
    cls.add_method('Max', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Min() [member function]
    cls.add_method('Min', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static void ns3::Time::SetResolution(ns3::Time::Unit resolution) [member function]
    cls.add_method('SetResolution', 
                   'void', 
                   [param('ns3::Time::Unit', 'resolution')], 
                   is_static=True)
    ## nstime.h (module 'core'): static bool ns3::Time::StaticInit() [member function]
    cls.add_method('StaticInit', 
                   'bool', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): ns3::int64x64_t ns3::Time::To(ns3::Time::Unit unit) const [member function]
    cls.add_method('To', 
                   'ns3::int64x64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::ToDouble(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToDouble', 
                   'double', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::ToInteger(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToInteger', 
                   'int64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    return

def register_Ns3TraceSourceAccessor_methods(root_module, cls):
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor(ns3::TraceSourceAccessor const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TraceSourceAccessor const &', 'arg0')])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor() [constructor]
    cls.add_constructor([])
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Connect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Connect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::ConnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('ConnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Disconnect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Disconnect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::DisconnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Trailer_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## trailer.h (module 'network'): ns3::Trailer::Trailer() [constructor]
    cls.add_constructor([])
    ## trailer.h (module 'network'): ns3::Trailer::Trailer(ns3::Trailer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Trailer const &', 'arg0')])
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::Deserialize(ns3::Buffer::Iterator end) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'end')], 
                   is_pure_virtual=True, is_virtual=True)
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): static ns3::TypeId ns3::Trailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TriangularRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::TriangularRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable::TriangularRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue(double mean, double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger(uint32_t mean, uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3UanMac_methods(root_module, cls):
    ## uan-mac.h (module 'uan'): ns3::UanMac::UanMac() [constructor]
    cls.add_constructor([])
    ## uan-mac.h (module 'uan'): ns3::UanMac::UanMac(ns3::UanMac const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanMac const &', 'arg0')])
    ## uan-mac.h (module 'uan'): int64_t ns3::UanMac::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): void ns3::UanMac::AttachPhy(ns3::Ptr<ns3::UanPhy> phy) [member function]
    cls.add_method('AttachPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): void ns3::UanMac::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): bool ns3::UanMac::Enqueue(ns3::Ptr<ns3::Packet> pkt, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Enqueue', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): ns3::Address ns3::UanMac::GetAddress() [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): ns3::Address ns3::UanMac::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): static ns3::TypeId ns3::UanMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-mac.h (module 'uan'): void ns3::UanMac::SetAddress(ns3::UanAddress addr) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::UanAddress', 'addr')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-mac.h (module 'uan'): void ns3::UanMac::SetForwardUpCb(ns3::Callback<void,ns3::Ptr<ns3::Packet>,const ns3::UanAddress&,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> cb) [member function]
    cls.add_method('SetForwardUpCb', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::UanAddress const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3UanPhy_methods(root_module, cls):
    ## uan-phy.h (module 'uan'): ns3::UanPhy::UanPhy() [constructor]
    cls.add_constructor([])
    ## uan-phy.h (module 'uan'): ns3::UanPhy::UanPhy(ns3::UanPhy const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhy const &', 'arg0')])
    ## uan-phy.h (module 'uan'): int64_t ns3::UanPhy::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::EnergyDepletionHandler() [member function]
    cls.add_method('EnergyDepletionHandler', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhy::GetCcaThresholdDb() [member function]
    cls.add_method('GetCcaThresholdDb', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): ns3::Ptr<ns3::UanChannel> ns3::UanPhy::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::UanChannel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): ns3::Ptr<ns3::UanNetDevice> ns3::UanPhy::GetDevice() [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::UanNetDevice >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): ns3::UanTxMode ns3::UanPhy::GetMode(uint32_t n) [member function]
    cls.add_method('GetMode', 
                   'ns3::UanTxMode', 
                   [param('uint32_t', 'n')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): uint32_t ns3::UanPhy::GetNModes() [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): ns3::Ptr<ns3::Packet> ns3::UanPhy::GetPacketRx() const [member function]
    cls.add_method('GetPacketRx', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhy::GetRxGainDb() [member function]
    cls.add_method('GetRxGainDb', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhy::GetRxThresholdDb() [member function]
    cls.add_method('GetRxThresholdDb', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): ns3::Ptr<ns3::UanTransducer> ns3::UanPhy::GetTransducer() [member function]
    cls.add_method('GetTransducer', 
                   'ns3::Ptr< ns3::UanTransducer >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhy::GetTxPowerDb() [member function]
    cls.add_method('GetTxPowerDb', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): static ns3::TypeId ns3::UanPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateBusy() [member function]
    cls.add_method('IsStateBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateCcaBusy() [member function]
    cls.add_method('IsStateCcaBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateIdle() [member function]
    cls.add_method('IsStateIdle', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateRx() [member function]
    cls.add_method('IsStateRx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateSleep() [member function]
    cls.add_method('IsStateSleep', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): bool ns3::UanPhy::IsStateTx() [member function]
    cls.add_method('IsStateTx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyIntChange() [member function]
    cls.add_method('NotifyIntChange', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyRxBegin(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyRxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyRxDrop(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyRxEnd(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyRxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyTransStartTx(ns3::Ptr<ns3::Packet> packet, double txPowerDb, ns3::UanTxMode txMode) [member function]
    cls.add_method('NotifyTransStartTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'txPowerDb'), param('ns3::UanTxMode', 'txMode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyTxBegin(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyTxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyTxDrop(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::NotifyTxEnd(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('NotifyTxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::RegisterListener(ns3::UanPhyListener * listener) [member function]
    cls.add_method('RegisterListener', 
                   'void', 
                   [param('ns3::UanPhyListener *', 'listener')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SendPacket(ns3::Ptr<ns3::Packet> pkt, uint32_t modeNum) [member function]
    cls.add_method('SendPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('uint32_t', 'modeNum')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetCcaThresholdDb(double thresh) [member function]
    cls.add_method('SetCcaThresholdDb', 
                   'void', 
                   [param('double', 'thresh')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetChannel(ns3::Ptr<ns3::UanChannel> channel) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanChannel >', 'channel')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetDevice(ns3::Ptr<ns3::UanNetDevice> device) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanNetDevice >', 'device')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetEnergyModelCallback(ns3::Callback<void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetEnergyModelCallback', 
                   'void', 
                   [param('ns3::Callback< void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetMac(ns3::Ptr<ns3::UanMac> mac) [member function]
    cls.add_method('SetMac', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanMac >', 'mac')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetReceiveErrorCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetReceiveOkCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, double, ns3::UanTxMode, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::UanTxMode, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetRxGainDb(double gain) [member function]
    cls.add_method('SetRxGainDb', 
                   'void', 
                   [param('double', 'gain')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetRxThresholdDb(double thresh) [member function]
    cls.add_method('SetRxThresholdDb', 
                   'void', 
                   [param('double', 'thresh')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetSleepMode(bool sleep) [member function]
    cls.add_method('SetSleepMode', 
                   'void', 
                   [param('bool', 'sleep')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetTransducer(ns3::Ptr<ns3::UanTransducer> trans) [member function]
    cls.add_method('SetTransducer', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanTransducer >', 'trans')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::SetTxPowerDb(double txpwr) [member function]
    cls.add_method('SetTxPowerDb', 
                   'void', 
                   [param('double', 'txpwr')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhy::StartRxPacket(ns3::Ptr<ns3::Packet> pkt, double rxPowerDb, ns3::UanTxMode txMode, ns3::UanPdp pdp) [member function]
    cls.add_method('StartRxPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('double', 'rxPowerDb'), param('ns3::UanTxMode', 'txMode'), param('ns3::UanPdp', 'pdp')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3UanPhyCalcSinr_methods(root_module, cls):
    ## uan-phy.h (module 'uan'): ns3::UanPhyCalcSinr::UanPhyCalcSinr() [constructor]
    cls.add_constructor([])
    ## uan-phy.h (module 'uan'): ns3::UanPhyCalcSinr::UanPhyCalcSinr(ns3::UanPhyCalcSinr const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyCalcSinr const &', 'arg0')])
    ## uan-phy.h (module 'uan'): double ns3::UanPhyCalcSinr::CalcSinrDb(ns3::Ptr<ns3::Packet> pkt, ns3::Time arrTime, double rxPowerDb, double ambNoiseDb, ns3::UanTxMode mode, ns3::UanPdp pdp, std::list<ns3::UanPacketArrival,std::allocator<ns3::UanPacketArrival> > const & arrivalList) const [member function]
    cls.add_method('CalcSinrDb', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('ns3::Time', 'arrTime'), param('double', 'rxPowerDb'), param('double', 'ambNoiseDb'), param('ns3::UanTxMode', 'mode'), param('ns3::UanPdp', 'pdp'), param('std::list< ns3::UanPacketArrival > const &', 'arrivalList')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyCalcSinr::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhyCalcSinr::DbToKp(double db) const [member function]
    cls.add_method('DbToKp', 
                   'double', 
                   [param('double', 'db')], 
                   is_const=True)
    ## uan-phy.h (module 'uan'): static ns3::TypeId ns3::UanPhyCalcSinr::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-phy.h (module 'uan'): double ns3::UanPhyCalcSinr::KpToDb(double kp) const [member function]
    cls.add_method('KpToDb', 
                   'double', 
                   [param('double', 'kp')], 
                   is_const=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyCalcSinr::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3UanPhyCalcSinrDefault_methods(root_module, cls):
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrDefault::UanPhyCalcSinrDefault(ns3::UanPhyCalcSinrDefault const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyCalcSinrDefault const &', 'arg0')])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrDefault::UanPhyCalcSinrDefault() [constructor]
    cls.add_constructor([])
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyCalcSinrDefault::CalcSinrDb(ns3::Ptr<ns3::Packet> pkt, ns3::Time arrTime, double rxPowerDb, double ambNoiseDb, ns3::UanTxMode mode, ns3::UanPdp pdp, std::list<ns3::UanPacketArrival,std::allocator<ns3::UanPacketArrival> > const & arrivalList) const [member function]
    cls.add_method('CalcSinrDb', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('ns3::Time', 'arrTime'), param('double', 'rxPowerDb'), param('double', 'ambNoiseDb'), param('ns3::UanTxMode', 'mode'), param('ns3::UanPdp', 'pdp'), param('std::list< ns3::UanPacketArrival > const &', 'arrivalList')], 
                   is_const=True, is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::TypeId ns3::UanPhyCalcSinrDefault::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3UanPhyCalcSinrFhFsk_methods(root_module, cls):
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrFhFsk::UanPhyCalcSinrFhFsk(ns3::UanPhyCalcSinrFhFsk const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyCalcSinrFhFsk const &', 'arg0')])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyCalcSinrFhFsk::UanPhyCalcSinrFhFsk() [constructor]
    cls.add_constructor([])
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyCalcSinrFhFsk::CalcSinrDb(ns3::Ptr<ns3::Packet> pkt, ns3::Time arrTime, double rxPowerDb, double ambNoiseDb, ns3::UanTxMode mode, ns3::UanPdp pdp, std::list<ns3::UanPacketArrival,std::allocator<ns3::UanPacketArrival> > const & arrivalList) const [member function]
    cls.add_method('CalcSinrDb', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('ns3::Time', 'arrTime'), param('double', 'rxPowerDb'), param('double', 'ambNoiseDb'), param('ns3::UanTxMode', 'mode'), param('ns3::UanPdp', 'pdp'), param('std::list< ns3::UanPacketArrival > const &', 'arrivalList')], 
                   is_const=True, is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::TypeId ns3::UanPhyCalcSinrFhFsk::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3UanPhyGen_methods(root_module, cls):
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyGen::UanPhyGen(ns3::UanPhyGen const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyGen const &', 'arg0')])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyGen::UanPhyGen() [constructor]
    cls.add_constructor([])
    ## uan-phy-gen.h (module 'uan'): int64_t ns3::UanPhyGen::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::EnergyDepletionHandler() [member function]
    cls.add_method('EnergyDepletionHandler', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyGen::GetCcaThresholdDb() [member function]
    cls.add_method('GetCcaThresholdDb', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): ns3::Ptr<ns3::UanChannel> ns3::UanPhyGen::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::UanChannel >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::UanModesList ns3::UanPhyGen::GetDefaultModes() [member function]
    cls.add_method('GetDefaultModes', 
                   'ns3::UanModesList', 
                   [], 
                   is_static=True)
    ## uan-phy-gen.h (module 'uan'): ns3::Ptr<ns3::UanNetDevice> ns3::UanPhyGen::GetDevice() [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::UanNetDevice >', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): ns3::UanTxMode ns3::UanPhyGen::GetMode(uint32_t n) [member function]
    cls.add_method('GetMode', 
                   'ns3::UanTxMode', 
                   [param('uint32_t', 'n')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): uint32_t ns3::UanPhyGen::GetNModes() [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): ns3::Ptr<ns3::Packet> ns3::UanPhyGen::GetPacketRx() const [member function]
    cls.add_method('GetPacketRx', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyGen::GetRxGainDb() [member function]
    cls.add_method('GetRxGainDb', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyGen::GetRxThresholdDb() [member function]
    cls.add_method('GetRxThresholdDb', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): ns3::Ptr<ns3::UanTransducer> ns3::UanPhyGen::GetTransducer() [member function]
    cls.add_method('GetTransducer', 
                   'ns3::Ptr< ns3::UanTransducer >', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyGen::GetTxPowerDb() [member function]
    cls.add_method('GetTxPowerDb', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::TypeId ns3::UanPhyGen::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateBusy() [member function]
    cls.add_method('IsStateBusy', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateCcaBusy() [member function]
    cls.add_method('IsStateCcaBusy', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateIdle() [member function]
    cls.add_method('IsStateIdle', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateRx() [member function]
    cls.add_method('IsStateRx', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateSleep() [member function]
    cls.add_method('IsStateSleep', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): bool ns3::UanPhyGen::IsStateTx() [member function]
    cls.add_method('IsStateTx', 
                   'bool', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::NotifyIntChange() [member function]
    cls.add_method('NotifyIntChange', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::NotifyTransStartTx(ns3::Ptr<ns3::Packet> packet, double txPowerDb, ns3::UanTxMode txMode) [member function]
    cls.add_method('NotifyTransStartTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'txPowerDb'), param('ns3::UanTxMode', 'txMode')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::RegisterListener(ns3::UanPhyListener * listener) [member function]
    cls.add_method('RegisterListener', 
                   'void', 
                   [param('ns3::UanPhyListener *', 'listener')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SendPacket(ns3::Ptr<ns3::Packet> pkt, uint32_t modeNum) [member function]
    cls.add_method('SendPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('uint32_t', 'modeNum')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetCcaThresholdDb(double thresh) [member function]
    cls.add_method('SetCcaThresholdDb', 
                   'void', 
                   [param('double', 'thresh')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetChannel(ns3::Ptr<ns3::UanChannel> channel) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanChannel >', 'channel')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetDevice(ns3::Ptr<ns3::UanNetDevice> device) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanNetDevice >', 'device')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetEnergyModelCallback(ns3::Callback<void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetEnergyModelCallback', 
                   'void', 
                   [param('ns3::Callback< void, int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetMac(ns3::Ptr<ns3::UanMac> mac) [member function]
    cls.add_method('SetMac', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanMac >', 'mac')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetReceiveErrorCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetReceiveOkCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, double, ns3::UanTxMode, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::UanTxMode, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetRxGainDb(double gain) [member function]
    cls.add_method('SetRxGainDb', 
                   'void', 
                   [param('double', 'gain')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetRxThresholdDb(double thresh) [member function]
    cls.add_method('SetRxThresholdDb', 
                   'void', 
                   [param('double', 'thresh')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetSleepMode(bool sleep) [member function]
    cls.add_method('SetSleepMode', 
                   'void', 
                   [param('bool', 'sleep')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetTransducer(ns3::Ptr<ns3::UanTransducer> trans) [member function]
    cls.add_method('SetTransducer', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanTransducer >', 'trans')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::SetTxPowerDb(double txpwr) [member function]
    cls.add_method('SetTxPowerDb', 
                   'void', 
                   [param('double', 'txpwr')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::StartRxPacket(ns3::Ptr<ns3::Packet> pkt, double rxPowerDb, ns3::UanTxMode txMode, ns3::UanPdp pdp) [member function]
    cls.add_method('StartRxPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('double', 'rxPowerDb'), param('ns3::UanTxMode', 'txMode'), param('ns3::UanPdp', 'pdp')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): void ns3::UanPhyGen::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3UanPhyPer_methods(root_module, cls):
    ## uan-phy.h (module 'uan'): ns3::UanPhyPer::UanPhyPer() [constructor]
    cls.add_constructor([])
    ## uan-phy.h (module 'uan'): ns3::UanPhyPer::UanPhyPer(ns3::UanPhyPer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyPer const &', 'arg0')])
    ## uan-phy.h (module 'uan'): double ns3::UanPhyPer::CalcPer(ns3::Ptr<ns3::Packet> pkt, double sinrDb, ns3::UanTxMode mode) [member function]
    cls.add_method('CalcPer', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('double', 'sinrDb'), param('ns3::UanTxMode', 'mode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyPer::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-phy.h (module 'uan'): static ns3::TypeId ns3::UanPhyPer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-phy.h (module 'uan'): void ns3::UanPhyPer::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3UanPhyPerGenDefault_methods(root_module, cls):
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerGenDefault::UanPhyPerGenDefault(ns3::UanPhyPerGenDefault const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyPerGenDefault const &', 'arg0')])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerGenDefault::UanPhyPerGenDefault() [constructor]
    cls.add_constructor([])
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyPerGenDefault::CalcPer(ns3::Ptr<ns3::Packet> pkt, double sinrDb, ns3::UanTxMode mode) [member function]
    cls.add_method('CalcPer', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('double', 'sinrDb'), param('ns3::UanTxMode', 'mode')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::TypeId ns3::UanPhyPerGenDefault::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3UanPhyPerUmodem_methods(root_module, cls):
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerUmodem::UanPhyPerUmodem(ns3::UanPhyPerUmodem const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPhyPerUmodem const &', 'arg0')])
    ## uan-phy-gen.h (module 'uan'): ns3::UanPhyPerUmodem::UanPhyPerUmodem() [constructor]
    cls.add_constructor([])
    ## uan-phy-gen.h (module 'uan'): double ns3::UanPhyPerUmodem::CalcPer(ns3::Ptr<ns3::Packet> pkt, double sinrDb, ns3::UanTxMode mode) [member function]
    cls.add_method('CalcPer', 
                   'double', 
                   [param('ns3::Ptr< ns3::Packet >', 'pkt'), param('double', 'sinrDb'), param('ns3::UanTxMode', 'mode')], 
                   is_virtual=True)
    ## uan-phy-gen.h (module 'uan'): static ns3::TypeId ns3::UanPhyPerUmodem::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3UanPropModel_methods(root_module, cls):
    ## uan-prop-model.h (module 'uan'): ns3::UanPropModel::UanPropModel() [constructor]
    cls.add_constructor([])
    ## uan-prop-model.h (module 'uan'): ns3::UanPropModel::UanPropModel(ns3::UanPropModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanPropModel const &', 'arg0')])
    ## uan-prop-model.h (module 'uan'): void ns3::UanPropModel::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-prop-model.h (module 'uan'): void ns3::UanPropModel::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## uan-prop-model.h (module 'uan'): ns3::Time ns3::UanPropModel::GetDelay(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b, ns3::UanTxMode mode) [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b'), param('ns3::UanTxMode', 'mode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-prop-model.h (module 'uan'): double ns3::UanPropModel::GetPathLossDb(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b, ns3::UanTxMode txMode) [member function]
    cls.add_method('GetPathLossDb', 
                   'double', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b'), param('ns3::UanTxMode', 'txMode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-prop-model.h (module 'uan'): ns3::UanPdp ns3::UanPropModel::GetPdp(ns3::Ptr<ns3::MobilityModel> a, ns3::Ptr<ns3::MobilityModel> b, ns3::UanTxMode mode) [member function]
    cls.add_method('GetPdp', 
                   'ns3::UanPdp', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'a'), param('ns3::Ptr< ns3::MobilityModel >', 'b'), param('ns3::UanTxMode', 'mode')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-prop-model.h (module 'uan'): static ns3::TypeId ns3::UanPropModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3UanTransducer_methods(root_module, cls):
    ## uan-transducer.h (module 'uan'): ns3::UanTransducer::UanTransducer() [constructor]
    cls.add_constructor([])
    ## uan-transducer.h (module 'uan'): ns3::UanTransducer::UanTransducer(ns3::UanTransducer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanTransducer const &', 'arg0')])
    ## uan-transducer.h (module 'uan'): void ns3::UanTransducer::AddPhy(ns3::Ptr<ns3::UanPhy> phy) [member function]
    cls.add_method('AddPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): void ns3::UanTransducer::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): std::list<ns3::UanPacketArrival,std::allocator<ns3::UanPacketArrival> > const & ns3::UanTransducer::GetArrivalList() const [member function]
    cls.add_method('GetArrivalList', 
                   'std::list< ns3::UanPacketArrival > const &', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): ns3::Ptr<ns3::UanChannel> ns3::UanTransducer::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::UanChannel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): std::list<ns3::Ptr<ns3::UanPhy>,std::allocator<ns3::Ptr<ns3::UanPhy> > > const & ns3::UanTransducer::GetPhyList() const [member function]
    cls.add_method('GetPhyList', 
                   'std::list< ns3::Ptr< ns3::UanPhy > > const &', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): ns3::UanTransducer::State ns3::UanTransducer::GetState() const [member function]
    cls.add_method('GetState', 
                   'ns3::UanTransducer::State', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): static ns3::TypeId ns3::UanTransducer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## uan-transducer.h (module 'uan'): bool ns3::UanTransducer::IsRx() const [member function]
    cls.add_method('IsRx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): bool ns3::UanTransducer::IsTx() const [member function]
    cls.add_method('IsTx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): void ns3::UanTransducer::Receive(ns3::Ptr<ns3::Packet> packet, double rxPowerDb, ns3::UanTxMode txMode, ns3::UanPdp pdp) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'rxPowerDb'), param('ns3::UanTxMode', 'txMode'), param('ns3::UanPdp', 'pdp')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): void ns3::UanTransducer::SetChannel(ns3::Ptr<ns3::UanChannel> chan) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanChannel >', 'chan')], 
                   is_pure_virtual=True, is_virtual=True)
    ## uan-transducer.h (module 'uan'): void ns3::UanTransducer::Transmit(ns3::Ptr<ns3::UanPhy> src, ns3::Ptr<ns3::Packet> packet, double txPowerDb, ns3::UanTxMode txMode) [member function]
    cls.add_method('Transmit', 
                   'void', 
                   [param('ns3::Ptr< ns3::UanPhy >', 'src'), param('ns3::Ptr< ns3::Packet >', 'packet'), param('double', 'txPowerDb'), param('ns3::UanTxMode', 'txMode')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3UniformRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::UniformRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable::UniformRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue(double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger(uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3VendorSpecificValue_methods(root_module, cls):
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificValue::VendorSpecificValue() [constructor]
    cls.add_constructor([])
    ## ff-mac-common.h (module 'lte'): ns3::VendorSpecificValue::VendorSpecificValue(ns3::VendorSpecificValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::VendorSpecificValue const &', 'arg0')])
    return

def register_Ns3WeibullRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::WeibullRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable::WeibullRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetScale() const [member function]
    cls.add_method('GetScale', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue(double scale, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'scale'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger(uint32_t scale, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'scale'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ZetaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZetaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable::ZetaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue(double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger(uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ZipfRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZipfRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable::ZipfRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue(uint32_t n, double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'n'), param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger(uint32_t n, uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'n'), param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3AttributeAccessor_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor(ns3::AttributeAccessor const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeAccessor const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Get(ns3::ObjectBase const * object, ns3::AttributeValue & attribute) const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'attribute')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasGetter() const [member function]
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasSetter() const [member function]
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object', transfer_ownership=False), param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeChecker_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker(ns3::AttributeChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeChecker const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Copy(ns3::AttributeValue const & source, ns3::AttributeValue & destination) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'source'), param('ns3::AttributeValue &', 'destination')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::CreateValidValue(ns3::AttributeValue const & value) const [member function]
    cls.add_method('CreateValidValue', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue(ns3::AttributeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3CallbackChecker_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker(ns3::CallbackChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackChecker const &', 'arg0')])
    return

def register_Ns3CallbackImplBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase(ns3::CallbackImplBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackImplBase const &', 'arg0')])
    ## callback.h (module 'core'): bool ns3::CallbackImplBase::IsEqual(ns3::Ptr<ns3::CallbackImplBase const> other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ptr< ns3::CallbackImplBase const >', 'other')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3CallbackValue_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackValue const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackBase const & base) [constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'base')])
    ## callback.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::CallbackValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## callback.h (module 'core'): std::string ns3::CallbackValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackValue::Set(ns3::CallbackBase base) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::CallbackBase', 'base')])
    return

def register_Ns3Channel_methods(root_module, cls):
    ## channel.h (module 'network'): ns3::Channel::Channel(ns3::Channel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Channel const &', 'arg0')])
    ## channel.h (module 'network'): ns3::Channel::Channel() [constructor]
    cls.add_constructor([])
    ## channel.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Channel::GetDevice(uint32_t i) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## channel.h (module 'network'): uint32_t ns3::Channel::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## channel.h (module 'network'): uint32_t ns3::Channel::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## channel.h (module 'network'): static ns3::TypeId ns3::Channel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3ConstantRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ConstantRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable::ConstantRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetConstant() const [member function]
    cls.add_method('GetConstant', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue(double constant) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'constant')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger(uint32_t constant) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'constant')])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3DataRateChecker_methods(root_module, cls):
    ## data-rate.h (module 'network'): ns3::DataRateChecker::DataRateChecker() [constructor]
    cls.add_constructor([])
    ## data-rate.h (module 'network'): ns3::DataRateChecker::DataRateChecker(ns3::DataRateChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DataRateChecker const &', 'arg0')])
    return

def register_Ns3DataRateValue_methods(root_module, cls):
    ## data-rate.h (module 'network'): ns3::DataRateValue::DataRateValue() [constructor]
    cls.add_constructor([])
    ## data-rate.h (module 'network'): ns3::DataRateValue::DataRateValue(ns3::DataRateValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DataRateValue const &', 'arg0')])
    ## data-rate.h (module 'network'): ns3::DataRateValue::DataRateValue(ns3::DataRate const & value) [constructor]
    cls.add_constructor([param('ns3::DataRate const &', 'value')])
    ## data-rate.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::DataRateValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## data-rate.h (module 'network'): bool ns3::DataRateValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## data-rate.h (module 'network'): ns3::DataRate ns3::DataRateValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::DataRate', 
                   [], 
                   is_const=True)
    ## data-rate.h (module 'network'): std::string ns3::DataRateValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## data-rate.h (module 'network'): void ns3::DataRateValue::Set(ns3::DataRate const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::DataRate const &', 'value')])
    return

def register_Ns3DeterministicRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::DeterministicRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable::DeterministicRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::DeterministicRandomVariable::SetValueArray(double * values, uint64_t length) [member function]
    cls.add_method('SetValueArray', 
                   'void', 
                   [param('double *', 'values'), param('uint64_t', 'length')])
    ## random-variable-stream.h (module 'core'): double ns3::DeterministicRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::DeterministicRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3DeviceEnergyModel_methods(root_module, cls):
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel::DeviceEnergyModel(ns3::DeviceEnergyModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DeviceEnergyModel const &', 'arg0')])
    ## device-energy-model.h (module 'energy'): ns3::DeviceEnergyModel::DeviceEnergyModel() [constructor]
    cls.add_constructor([])
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::ChangeState(int newState) [member function]
    cls.add_method('ChangeState', 
                   'void', 
                   [param('int', 'newState')], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::GetCurrentA() const [member function]
    cls.add_method('GetCurrentA', 
                   'double', 
                   [], 
                   is_const=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::GetTotalEnergyConsumption() const [member function]
    cls.add_method('GetTotalEnergyConsumption', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): static ns3::TypeId ns3::DeviceEnergyModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::HandleEnergyDepletion() [member function]
    cls.add_method('HandleEnergyDepletion', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::HandleEnergyRecharged() [member function]
    cls.add_method('HandleEnergyRecharged', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): void ns3::DeviceEnergyModel::SetEnergySource(ns3::Ptr<ns3::EnergySource> source) [member function]
    cls.add_method('SetEnergySource', 
                   'void', 
                   [param('ns3::Ptr< ns3::EnergySource >', 'source')], 
                   is_pure_virtual=True, is_virtual=True)
    ## device-energy-model.h (module 'energy'): double ns3::DeviceEnergyModel::DoGetCurrentA() const [member function]
    cls.add_method('DoGetCurrentA', 
                   'double', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EmpiricalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable::EmpiricalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::CDF(double v, double c) [member function]
    cls.add_method('CDF', 
                   'void', 
                   [param('double', 'v'), param('double', 'c')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::EmpiricalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::EmpiricalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::Interpolate(double arg0, double arg1, double arg2, double arg3, double arg4) [member function]
    cls.add_method('Interpolate', 
                   'double', 
                   [param('double', 'arg0'), param('double', 'arg1'), param('double', 'arg2'), param('double', 'arg3'), param('double', 'arg4')], 
                   visibility='private', is_virtual=True)
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::Validate() [member function]
    cls.add_method('Validate', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EmptyAttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue(ns3::EmptyAttributeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EmptyAttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EmptyAttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::EmptyAttributeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ErlangRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ErlangRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable::ErlangRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetK() const [member function]
    cls.add_method('GetK', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetLambda() const [member function]
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue(uint32_t k, double lambda) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'k'), param('double', 'lambda')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger(uint32_t k, uint32_t lambda) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'k'), param('uint32_t', 'lambda')])
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3EventImpl_methods(root_module, cls):
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl(ns3::EventImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EventImpl const &', 'arg0')])
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl() [constructor]
    cls.add_constructor([])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Invoke() [member function]
    cls.add_method('Invoke', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): bool ns3::EventImpl::IsCancelled() [member function]
    cls.add_method('IsCancelled', 
                   'bool', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Notify() [member function]
    cls.add_method('Notify', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3ExponentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ExponentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable::ExponentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue(double mean, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger(uint32_t mean, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3GammaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::GammaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable::GammaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetBeta() const [member function]
    cls.add_method('GetBeta', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue(double alpha, double beta) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha'), param('double', 'beta')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger(uint32_t alpha, uint32_t beta) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha'), param('uint32_t', 'beta')])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3Ipv4_methods(root_module, cls):
    ## ipv4.h (module 'internet'): ns3::Ipv4::Ipv4(ns3::Ipv4 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4 const &', 'arg0')])
    ## ipv4.h (module 'internet'): ns3::Ipv4::Ipv4() [constructor]
    cls.add_constructor([])
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::AddAddress(uint32_t interface, ns3::Ipv4InterfaceAddress address) [member function]
    cls.add_method('AddAddress', 
                   'bool', 
                   [param('uint32_t', 'interface'), param('ns3::Ipv4InterfaceAddress', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): uint32_t ns3::Ipv4::AddInterface(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddInterface', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ptr<ns3::Socket> ns3::Ipv4::CreateRawSocket() [member function]
    cls.add_method('CreateRawSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::DeleteRawSocket(ns3::Ptr<ns3::Socket> socket) [member function]
    cls.add_method('DeleteRawSocket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ipv4InterfaceAddress ns3::Ipv4::GetAddress(uint32_t interface, uint32_t addressIndex) const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Ipv4InterfaceAddress', 
                   [param('uint32_t', 'interface'), param('uint32_t', 'addressIndex')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): int32_t ns3::Ipv4::GetInterfaceForAddress(ns3::Ipv4Address address) const [member function]
    cls.add_method('GetInterfaceForAddress', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): int32_t ns3::Ipv4::GetInterfaceForDevice(ns3::Ptr<ns3::NetDevice const> device) const [member function]
    cls.add_method('GetInterfaceForDevice', 
                   'int32_t', 
                   [param('ns3::Ptr< ns3::NetDevice const >', 'device')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): int32_t ns3::Ipv4::GetInterfaceForPrefix(ns3::Ipv4Address address, ns3::Ipv4Mask mask) const [member function]
    cls.add_method('GetInterfaceForPrefix', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'address'), param('ns3::Ipv4Mask', 'mask')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): uint16_t ns3::Ipv4::GetMetric(uint32_t interface) const [member function]
    cls.add_method('GetMetric', 
                   'uint16_t', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): uint16_t ns3::Ipv4::GetMtu(uint32_t interface) const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): uint32_t ns3::Ipv4::GetNAddresses(uint32_t interface) const [member function]
    cls.add_method('GetNAddresses', 
                   'uint32_t', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): uint32_t ns3::Ipv4::GetNInterfaces() const [member function]
    cls.add_method('GetNInterfaces', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ptr<ns3::NetDevice> ns3::Ipv4::GetNetDevice(uint32_t interface) [member function]
    cls.add_method('GetNetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ptr<ns3::IpL4Protocol> ns3::Ipv4::GetProtocol(int protocolNumber) const [member function]
    cls.add_method('GetProtocol', 
                   'ns3::Ptr< ns3::IpL4Protocol >', 
                   [param('int', 'protocolNumber')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ptr<ns3::Ipv4RoutingProtocol> ns3::Ipv4::GetRoutingProtocol() const [member function]
    cls.add_method('GetRoutingProtocol', 
                   'ns3::Ptr< ns3::Ipv4RoutingProtocol >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): static ns3::TypeId ns3::Ipv4::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::Insert(ns3::Ptr<ns3::IpL4Protocol> protocol) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Ptr< ns3::IpL4Protocol >', 'protocol')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::IsDestinationAddress(ns3::Ipv4Address address, uint32_t iif) const [member function]
    cls.add_method('IsDestinationAddress', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'address'), param('uint32_t', 'iif')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::IsForwarding(uint32_t interface) const [member function]
    cls.add_method('IsForwarding', 
                   'bool', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::IsUp(uint32_t interface) const [member function]
    cls.add_method('IsUp', 
                   'bool', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::RemoveAddress(uint32_t interface, uint32_t addressIndex) [member function]
    cls.add_method('RemoveAddress', 
                   'bool', 
                   [param('uint32_t', 'interface'), param('uint32_t', 'addressIndex')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::RemoveAddress(uint32_t interface, ns3::Ipv4Address address) [member function]
    cls.add_method('RemoveAddress', 
                   'bool', 
                   [param('uint32_t', 'interface'), param('ns3::Ipv4Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4::SelectSourceAddress(ns3::Ptr<ns3::NetDevice const> device, ns3::Ipv4Address dst, ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e scope) [member function]
    cls.add_method('SelectSourceAddress', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ptr< ns3::NetDevice const >', 'device'), param('ns3::Ipv4Address', 'dst'), param('ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e', 'scope')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address source, ns3::Ipv4Address destination, uint8_t protocol, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'source'), param('ns3::Ipv4Address', 'destination'), param('uint8_t', 'protocol'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SendWithHeader(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Header ipHeader, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('SendWithHeader', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Header', 'ipHeader'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetDown(uint32_t interface) [member function]
    cls.add_method('SetDown', 
                   'void', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetForwarding(uint32_t interface, bool val) [member function]
    cls.add_method('SetForwarding', 
                   'void', 
                   [param('uint32_t', 'interface'), param('bool', 'val')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetMetric(uint32_t interface, uint16_t metric) [member function]
    cls.add_method('SetMetric', 
                   'void', 
                   [param('uint32_t', 'interface'), param('uint16_t', 'metric')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetRoutingProtocol(ns3::Ptr<ns3::Ipv4RoutingProtocol> routingProtocol) [member function]
    cls.add_method('SetRoutingProtocol', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4RoutingProtocol >', 'routingProtocol')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetUp(uint32_t interface) [member function]
    cls.add_method('SetUp', 
                   'void', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4.h (module 'internet'): ns3::Ipv4::IF_ANY [variable]
    cls.add_static_attribute('IF_ANY', 'uint32_t const', is_const=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::GetIpForward() const [member function]
    cls.add_method('GetIpForward', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## ipv4.h (module 'internet'): bool ns3::Ipv4::GetWeakEsModel() const [member function]
    cls.add_method('GetWeakEsModel', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetIpForward(bool forward) [member function]
    cls.add_method('SetIpForward', 
                   'void', 
                   [param('bool', 'forward')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## ipv4.h (module 'internet'): void ns3::Ipv4::SetWeakEsModel(bool model) [member function]
    cls.add_method('SetWeakEsModel', 
                   'void', 
                   [param('bool', 'model')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3Ipv4AddressChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker(ns3::Ipv4AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv4AddressValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4AddressValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4AddressValue::Set(ns3::Ipv4Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Address const &', 'value')])
    return

def register_Ns3Ipv4L3Protocol_methods(root_module, cls):
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4L3Protocol::Ipv4L3Protocol() [constructor]
    cls.add_constructor([])
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::AddAddress(uint32_t i, ns3::Ipv4InterfaceAddress address) [member function]
    cls.add_method('AddAddress', 
                   'bool', 
                   [param('uint32_t', 'i'), param('ns3::Ipv4InterfaceAddress', 'address')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): uint32_t ns3::Ipv4L3Protocol::AddInterface(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddInterface', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ptr<ns3::Socket> ns3::Ipv4L3Protocol::CreateRawSocket() [member function]
    cls.add_method('CreateRawSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::DeleteRawSocket(ns3::Ptr<ns3::Socket> socket) [member function]
    cls.add_method('DeleteRawSocket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4InterfaceAddress ns3::Ipv4L3Protocol::GetAddress(uint32_t interfaceIndex, uint32_t addressIndex) const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Ipv4InterfaceAddress', 
                   [param('uint32_t', 'interfaceIndex'), param('uint32_t', 'addressIndex')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ptr<ns3::Ipv4Interface> ns3::Ipv4L3Protocol::GetInterface(uint32_t i) const [member function]
    cls.add_method('GetInterface', 
                   'ns3::Ptr< ns3::Ipv4Interface >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## ipv4-l3-protocol.h (module 'internet'): int32_t ns3::Ipv4L3Protocol::GetInterfaceForAddress(ns3::Ipv4Address addr) const [member function]
    cls.add_method('GetInterfaceForAddress', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): int32_t ns3::Ipv4L3Protocol::GetInterfaceForDevice(ns3::Ptr<ns3::NetDevice const> device) const [member function]
    cls.add_method('GetInterfaceForDevice', 
                   'int32_t', 
                   [param('ns3::Ptr< ns3::NetDevice const >', 'device')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): int32_t ns3::Ipv4L3Protocol::GetInterfaceForPrefix(ns3::Ipv4Address addr, ns3::Ipv4Mask mask) const [member function]
    cls.add_method('GetInterfaceForPrefix', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'addr'), param('ns3::Ipv4Mask', 'mask')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): uint16_t ns3::Ipv4L3Protocol::GetMetric(uint32_t i) const [member function]
    cls.add_method('GetMetric', 
                   'uint16_t', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): uint16_t ns3::Ipv4L3Protocol::GetMtu(uint32_t i) const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): uint32_t ns3::Ipv4L3Protocol::GetNAddresses(uint32_t interface) const [member function]
    cls.add_method('GetNAddresses', 
                   'uint32_t', 
                   [param('uint32_t', 'interface')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): uint32_t ns3::Ipv4L3Protocol::GetNInterfaces() const [member function]
    cls.add_method('GetNInterfaces', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ptr<ns3::NetDevice> ns3::Ipv4L3Protocol::GetNetDevice(uint32_t i) [member function]
    cls.add_method('GetNetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ptr<ns3::IpL4Protocol> ns3::Ipv4L3Protocol::GetProtocol(int protocolNumber) const [member function]
    cls.add_method('GetProtocol', 
                   'ns3::Ptr< ns3::IpL4Protocol >', 
                   [param('int', 'protocolNumber')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ptr<ns3::Ipv4RoutingProtocol> ns3::Ipv4L3Protocol::GetRoutingProtocol() const [member function]
    cls.add_method('GetRoutingProtocol', 
                   'ns3::Ptr< ns3::Ipv4RoutingProtocol >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): static ns3::TypeId ns3::Ipv4L3Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::Insert(ns3::Ptr<ns3::IpL4Protocol> protocol) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Ptr< ns3::IpL4Protocol >', 'protocol')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::IsDestinationAddress(ns3::Ipv4Address address, uint32_t iif) const [member function]
    cls.add_method('IsDestinationAddress', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'address'), param('uint32_t', 'iif')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::IsForwarding(uint32_t i) const [member function]
    cls.add_method('IsForwarding', 
                   'bool', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::IsUnicast(ns3::Ipv4Address ad) const [member function]
    cls.add_method('IsUnicast', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'ad')], 
                   is_const=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::IsUp(uint32_t i) const [member function]
    cls.add_method('IsUp', 
                   'bool', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::Receive(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<const ns3::Packet> p, uint16_t protocol, ns3::Address const & from, ns3::Address const & to, ns3::NetDevice::PacketType packetType) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::Packet const >', 'p'), param('uint16_t', 'protocol'), param('ns3::Address const &', 'from'), param('ns3::Address const &', 'to'), param('ns3::NetDevice::PacketType', 'packetType')])
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::Remove(ns3::Ptr<ns3::IpL4Protocol> protocol) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Ptr< ns3::IpL4Protocol >', 'protocol')])
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::RemoveAddress(uint32_t interfaceIndex, uint32_t addressIndex) [member function]
    cls.add_method('RemoveAddress', 
                   'bool', 
                   [param('uint32_t', 'interfaceIndex'), param('uint32_t', 'addressIndex')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::RemoveAddress(uint32_t interface, ns3::Ipv4Address address) [member function]
    cls.add_method('RemoveAddress', 
                   'bool', 
                   [param('uint32_t', 'interface'), param('ns3::Ipv4Address', 'address')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4L3Protocol::SelectSourceAddress(ns3::Ptr<ns3::NetDevice const> device, ns3::Ipv4Address dst, ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e scope) [member function]
    cls.add_method('SelectSourceAddress', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ptr< ns3::NetDevice const >', 'device'), param('ns3::Ipv4Address', 'dst'), param('ns3::Ipv4InterfaceAddress::InterfaceAddressScope_e', 'scope')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address source, ns3::Ipv4Address destination, uint8_t protocol, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'source'), param('ns3::Ipv4Address', 'destination'), param('uint8_t', 'protocol'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SendWithHeader(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Header ipHeader, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('SendWithHeader', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Header', 'ipHeader'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetDefaultTtl(uint8_t ttl) [member function]
    cls.add_method('SetDefaultTtl', 
                   'void', 
                   [param('uint8_t', 'ttl')])
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetDown(uint32_t i) [member function]
    cls.add_method('SetDown', 
                   'void', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetForwarding(uint32_t i, bool val) [member function]
    cls.add_method('SetForwarding', 
                   'void', 
                   [param('uint32_t', 'i'), param('bool', 'val')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetMetric(uint32_t i, uint16_t metric) [member function]
    cls.add_method('SetMetric', 
                   'void', 
                   [param('uint32_t', 'i'), param('uint16_t', 'metric')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetRoutingProtocol(ns3::Ptr<ns3::Ipv4RoutingProtocol> routingProtocol) [member function]
    cls.add_method('SetRoutingProtocol', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4RoutingProtocol >', 'routingProtocol')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetUp(uint32_t i) [member function]
    cls.add_method('SetUp', 
                   'void', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): ns3::Ipv4L3Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint16_t const', is_const=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::GetIpForward() const [member function]
    cls.add_method('GetIpForward', 
                   'bool', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): bool ns3::Ipv4L3Protocol::GetWeakEsModel() const [member function]
    cls.add_method('GetWeakEsModel', 
                   'bool', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetIpForward(bool forward) [member function]
    cls.add_method('SetIpForward', 
                   'void', 
                   [param('bool', 'forward')], 
                   visibility='private', is_virtual=True)
    ## ipv4-l3-protocol.h (module 'internet'): void ns3::Ipv4L3Protocol::SetWeakEsModel(bool model) [member function]
    cls.add_method('SetWeakEsModel', 
                   'void', 
                   [param('bool', 'model')], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3Ipv4MaskChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker(ns3::Ipv4MaskChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4MaskChecker const &', 'arg0')])
    return

def register_Ns3Ipv4MaskValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4MaskValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4MaskValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4Mask const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4MaskValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4MaskValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask ns3::Ipv4MaskValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4MaskValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4MaskValue::Set(ns3::Ipv4Mask const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Mask const &', 'value')])
    return

def register_Ns3Ipv4MulticastRoute_methods(root_module, cls):
    ## ipv4-route.h (module 'internet'): ns3::Ipv4MulticastRoute::Ipv4MulticastRoute(ns3::Ipv4MulticastRoute const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4MulticastRoute const &', 'arg0')])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4MulticastRoute::Ipv4MulticastRoute() [constructor]
    cls.add_constructor([])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4MulticastRoute::GetGroup() const [member function]
    cls.add_method('GetGroup', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4MulticastRoute::GetOrigin() const [member function]
    cls.add_method('GetOrigin', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): std::map<unsigned int, unsigned int, std::less<unsigned int>, std::allocator<std::pair<unsigned int const, unsigned int> > > ns3::Ipv4MulticastRoute::GetOutputTtlMap() const [member function]
    cls.add_method('GetOutputTtlMap', 
                   'std::map< unsigned int, unsigned int >', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): uint32_t ns3::Ipv4MulticastRoute::GetParent() const [member function]
    cls.add_method('GetParent', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4MulticastRoute::SetGroup(ns3::Ipv4Address const group) [member function]
    cls.add_method('SetGroup', 
                   'void', 
                   [param('ns3::Ipv4Address const', 'group')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4MulticastRoute::SetOrigin(ns3::Ipv4Address const origin) [member function]
    cls.add_method('SetOrigin', 
                   'void', 
                   [param('ns3::Ipv4Address const', 'origin')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4MulticastRoute::SetOutputTtl(uint32_t oif, uint32_t ttl) [member function]
    cls.add_method('SetOutputTtl', 
                   'void', 
                   [param('uint32_t', 'oif'), param('uint32_t', 'ttl')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4MulticastRoute::SetParent(uint32_t iif) [member function]
    cls.add_method('SetParent', 
                   'void', 
                   [param('uint32_t', 'iif')])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4MulticastRoute::MAX_INTERFACES [variable]
    cls.add_static_attribute('MAX_INTERFACES', 'uint32_t const', is_const=True)
    ## ipv4-route.h (module 'internet'): ns3::Ipv4MulticastRoute::MAX_TTL [variable]
    cls.add_static_attribute('MAX_TTL', 'uint32_t const', is_const=True)
    return

def register_Ns3Ipv4Route_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Route::Ipv4Route(ns3::Ipv4Route const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Route const &', 'arg0')])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Route::Ipv4Route() [constructor]
    cls.add_constructor([])
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4Route::GetDestination() const [member function]
    cls.add_method('GetDestination', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4Route::GetGateway() const [member function]
    cls.add_method('GetGateway', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): ns3::Ptr<ns3::NetDevice> ns3::Ipv4Route::GetOutputDevice() const [member function]
    cls.add_method('GetOutputDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): ns3::Ipv4Address ns3::Ipv4Route::GetSource() const [member function]
    cls.add_method('GetSource', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4Route::SetDestination(ns3::Ipv4Address dest) [member function]
    cls.add_method('SetDestination', 
                   'void', 
                   [param('ns3::Ipv4Address', 'dest')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4Route::SetGateway(ns3::Ipv4Address gw) [member function]
    cls.add_method('SetGateway', 
                   'void', 
                   [param('ns3::Ipv4Address', 'gw')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4Route::SetOutputDevice(ns3::Ptr<ns3::NetDevice> outputDevice) [member function]
    cls.add_method('SetOutputDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'outputDevice')])
    ## ipv4-route.h (module 'internet'): void ns3::Ipv4Route::SetSource(ns3::Ipv4Address src) [member function]
    cls.add_method('SetSource', 
                   'void', 
                   [param('ns3::Ipv4Address', 'src')])
    return

def register_Ns3Ipv4RoutingProtocol_methods(root_module, cls):
    ## ipv4-routing-protocol.h (module 'internet'): ns3::Ipv4RoutingProtocol::Ipv4RoutingProtocol() [constructor]
    cls.add_constructor([])
    ## ipv4-routing-protocol.h (module 'internet'): ns3::Ipv4RoutingProtocol::Ipv4RoutingProtocol(ns3::Ipv4RoutingProtocol const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4RoutingProtocol const &', 'arg0')])
    ## ipv4-routing-protocol.h (module 'internet'): static ns3::TypeId ns3::Ipv4RoutingProtocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::NotifyAddAddress(uint32_t interface, ns3::Ipv4InterfaceAddress address) [member function]
    cls.add_method('NotifyAddAddress', 
                   'void', 
                   [param('uint32_t', 'interface'), param('ns3::Ipv4InterfaceAddress', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::NotifyInterfaceDown(uint32_t interface) [member function]
    cls.add_method('NotifyInterfaceDown', 
                   'void', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::NotifyInterfaceUp(uint32_t interface) [member function]
    cls.add_method('NotifyInterfaceUp', 
                   'void', 
                   [param('uint32_t', 'interface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::NotifyRemoveAddress(uint32_t interface, ns3::Ipv4InterfaceAddress address) [member function]
    cls.add_method('NotifyRemoveAddress', 
                   'void', 
                   [param('uint32_t', 'interface'), param('ns3::Ipv4InterfaceAddress', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::PrintRoutingTable(ns3::Ptr<ns3::OutputStreamWrapper> stream) const [member function]
    cls.add_method('PrintRoutingTable', 
                   'void', 
                   [param('ns3::Ptr< ns3::OutputStreamWrapper >', 'stream')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): bool ns3::Ipv4RoutingProtocol::RouteInput(ns3::Ptr<const ns3::Packet> p, ns3::Ipv4Header const & header, ns3::Ptr<ns3::NetDevice const> idev, ns3::Callback<void,ns3::Ptr<ns3::Ipv4Route>,ns3::Ptr<const ns3::Packet>,const ns3::Ipv4Header&,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> ucb, ns3::Callback<void,ns3::Ptr<ns3::Ipv4MulticastRoute>,ns3::Ptr<const ns3::Packet>,const ns3::Ipv4Header&,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> mcb, ns3::Callback<void,ns3::Ptr<const ns3::Packet>,const ns3::Ipv4Header&,unsigned int,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> lcb, ns3::Callback<void,ns3::Ptr<const ns3::Packet>,const ns3::Ipv4Header&,ns3::Socket::SocketErrno,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> ecb) [member function]
    cls.add_method('RouteInput', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet const >', 'p'), param('ns3::Ipv4Header const &', 'header'), param('ns3::Ptr< ns3::NetDevice const >', 'idev'), param('ns3::Callback< void, ns3::Ptr< ns3::Ipv4Route >, ns3::Ptr< ns3::Packet const >, ns3::Ipv4Header const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'ucb'), param('ns3::Callback< void, ns3::Ptr< ns3::Ipv4MulticastRoute >, ns3::Ptr< ns3::Packet const >, ns3::Ipv4Header const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'mcb'), param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::Ipv4Header const &, unsigned int, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'lcb'), param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, ns3::Ipv4Header const &, ns3::Socket::SocketErrno, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'ecb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): ns3::Ptr<ns3::Ipv4Route> ns3::Ipv4RoutingProtocol::RouteOutput(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Header const & header, ns3::Ptr<ns3::NetDevice> oif, ns3::Socket::SocketErrno & sockerr) [member function]
    cls.add_method('RouteOutput', 
                   'ns3::Ptr< ns3::Ipv4Route >', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Header const &', 'header'), param('ns3::Ptr< ns3::NetDevice >', 'oif'), param('ns3::Socket::SocketErrno &', 'sockerr')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-routing-protocol.h (module 'internet'): void ns3::Ipv4RoutingProtocol::SetIpv4(ns3::Ptr<ns3::Ipv4> ipv4) [member function]
    cls.add_method('SetIpv4', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4 >', 'ipv4')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3Ipv6AddressChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker(ns3::Ipv6AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv6AddressValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6AddressValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6AddressValue::Set(ns3::Ipv6Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Address const &', 'value')])
    return

def register_Ns3Ipv6PrefixChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker(ns3::Ipv6PrefixChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixChecker const &', 'arg0')])
    return

def register_Ns3Ipv6PrefixValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6PrefixValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6Prefix const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6PrefixValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6PrefixValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix ns3::Ipv6PrefixValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6PrefixValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6PrefixValue::Set(ns3::Ipv6Prefix const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Prefix const &', 'value')])
    return

def register_Ns3LogNormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::LogNormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable::LogNormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetMu() const [member function]
    cls.add_method('GetMu', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetSigma() const [member function]
    cls.add_method('GetSigma', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue(double mu, double sigma) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mu'), param('double', 'sigma')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger(uint32_t mu, uint32_t sigma) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mu'), param('uint32_t', 'sigma')])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3LteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::LteControlMessage::LteControlMessage(ns3::LteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::LteControlMessage::LteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::LteControlMessage::MessageType ns3::LteControlMessage::GetMessageType() [member function]
    cls.add_method('GetMessageType', 
                   'ns3::LteControlMessage::MessageType', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::LteControlMessage::SetMessageType(ns3::LteControlMessage::MessageType type) [member function]
    cls.add_method('SetMessageType', 
                   'void', 
                   [param('ns3::LteControlMessage::MessageType', 'type')])
    return

def register_Ns3LteHarqPhy_methods(root_module, cls):
    ## lte-harq-phy.h (module 'lte'): ns3::LteHarqPhy::LteHarqPhy(ns3::LteHarqPhy const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteHarqPhy const &', 'arg0')])
    ## lte-harq-phy.h (module 'lte'): ns3::LteHarqPhy::LteHarqPhy() [constructor]
    cls.add_constructor([])
    ## lte-harq-phy.h (module 'lte'): double ns3::LteHarqPhy::GetAccumulatedMiDl(uint8_t harqProcId, uint8_t layer) [member function]
    cls.add_method('GetAccumulatedMiDl', 
                   'double', 
                   [param('uint8_t', 'harqProcId'), param('uint8_t', 'layer')])
    ## lte-harq-phy.h (module 'lte'): double ns3::LteHarqPhy::GetAccumulatedMiUl(uint16_t rnti) [member function]
    cls.add_method('GetAccumulatedMiUl', 
                   'double', 
                   [param('uint16_t', 'rnti')])
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoList_t ns3::LteHarqPhy::GetHarqProcessInfoDl(uint8_t harqProcId, uint8_t layer) [member function]
    cls.add_method('GetHarqProcessInfoDl', 
                   'ns3::HarqProcessInfoList_t', 
                   [param('uint8_t', 'harqProcId'), param('uint8_t', 'layer')])
    ## lte-harq-phy.h (module 'lte'): ns3::HarqProcessInfoList_t ns3::LteHarqPhy::GetHarqProcessInfoUl(uint16_t rnti, uint8_t harqProcId) [member function]
    cls.add_method('GetHarqProcessInfoUl', 
                   'ns3::HarqProcessInfoList_t', 
                   [param('uint16_t', 'rnti'), param('uint8_t', 'harqProcId')])
    ## lte-harq-phy.h (module 'lte'): void ns3::LteHarqPhy::ResetDlHarqProcessStatus(uint8_t id) [member function]
    cls.add_method('ResetDlHarqProcessStatus', 
                   'void', 
                   [param('uint8_t', 'id')])
    ## lte-harq-phy.h (module 'lte'): void ns3::LteHarqPhy::ResetUlHarqProcessStatus(uint16_t rnti, uint8_t id) [member function]
    cls.add_method('ResetUlHarqProcessStatus', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('uint8_t', 'id')])
    ## lte-harq-phy.h (module 'lte'): void ns3::LteHarqPhy::SubframeIndication(uint32_t frameNo, uint32_t subframeNo) [member function]
    cls.add_method('SubframeIndication', 
                   'void', 
                   [param('uint32_t', 'frameNo'), param('uint32_t', 'subframeNo')])
    ## lte-harq-phy.h (module 'lte'): void ns3::LteHarqPhy::UpdateDlHarqProcessStatus(uint8_t id, uint8_t layer, double mi, uint16_t infoBytes, uint16_t codeBytes) [member function]
    cls.add_method('UpdateDlHarqProcessStatus', 
                   'void', 
                   [param('uint8_t', 'id'), param('uint8_t', 'layer'), param('double', 'mi'), param('uint16_t', 'infoBytes'), param('uint16_t', 'codeBytes')])
    ## lte-harq-phy.h (module 'lte'): void ns3::LteHarqPhy::UpdateUlHarqProcessStatus(uint16_t rnti, double mi, uint16_t infoBytes, uint16_t codeBytes) [member function]
    cls.add_method('UpdateUlHarqProcessStatus', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('double', 'mi'), param('uint16_t', 'infoBytes'), param('uint16_t', 'codeBytes')])
    return

def register_Ns3LteInterference_methods(root_module, cls):
    ## lte-interference.h (module 'lte'): ns3::LteInterference::LteInterference(ns3::LteInterference const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LteInterference const &', 'arg0')])
    ## lte-interference.h (module 'lte'): ns3::LteInterference::LteInterference() [constructor]
    cls.add_constructor([])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::AddInterferenceChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddInterferenceChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::AddRsPowerChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddRsPowerChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::AddSignal(ns3::Ptr<ns3::SpectrumValue const> spd, ns3::Time const duration) [member function]
    cls.add_method('AddSignal', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'spd'), param('ns3::Time const', 'duration')])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::AddSinrChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddSinrChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::EndRx() [member function]
    cls.add_method('EndRx', 
                   'void', 
                   [])
    ## lte-interference.h (module 'lte'): static ns3::TypeId ns3::LteInterference::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::SetNoisePowerSpectralDensity(ns3::Ptr<ns3::SpectrumValue const> noisePsd) [member function]
    cls.add_method('SetNoisePowerSpectralDensity', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'noisePsd')])
    ## lte-interference.h (module 'lte'): void ns3::LteInterference::StartRx(ns3::Ptr<ns3::SpectrumValue const> rxPsd) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'rxPsd')])
    return

def register_Ns3LtePhy_methods(root_module, cls):
    ## lte-phy.h (module 'lte'): ns3::LtePhy::LtePhy(ns3::LtePhy const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LtePhy const &', 'arg0')])
    ## lte-phy.h (module 'lte'): ns3::LtePhy::LtePhy() [constructor]
    cls.add_constructor([])
    ## lte-phy.h (module 'lte'): ns3::LtePhy::LtePhy(ns3::Ptr<ns3::LteSpectrumPhy> dlPhy, ns3::Ptr<ns3::LteSpectrumPhy> ulPhy) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::LteSpectrumPhy >', 'dlPhy'), param('ns3::Ptr< ns3::LteSpectrumPhy >', 'ulPhy')])
    ## lte-phy.h (module 'lte'): ns3::Ptr<ns3::SpectrumValue> ns3::LtePhy::CreateTxPowerSpectralDensity() [member function]
    cls.add_method('CreateTxPowerSpectralDensity', 
                   'ns3::Ptr< ns3::SpectrumValue >', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::DoSendMacPdu(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('DoSendMacPdu', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::DoSetCellId(uint16_t cellId) [member function]
    cls.add_method('DoSetCellId', 
                   'void', 
                   [param('uint16_t', 'cellId')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::GenerateCtrlCqiReport(ns3::SpectrumValue const & sinr) [member function]
    cls.add_method('GenerateCtrlCqiReport', 
                   'void', 
                   [param('ns3::SpectrumValue const &', 'sinr')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::GenerateDataCqiReport(ns3::SpectrumValue const & sinr) [member function]
    cls.add_method('GenerateDataCqiReport', 
                   'void', 
                   [param('ns3::SpectrumValue const &', 'sinr')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): std::list<ns3::Ptr<ns3::LteControlMessage>, std::allocator<ns3::Ptr<ns3::LteControlMessage> > > ns3::LtePhy::GetControlMessages() [member function]
    cls.add_method('GetControlMessages', 
                   'std::list< ns3::Ptr< ns3::LteControlMessage > >', 
                   [])
    ## lte-phy.h (module 'lte'): ns3::Ptr<ns3::LteNetDevice> ns3::LtePhy::GetDevice() [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::LteNetDevice >', 
                   [])
    ## lte-phy.h (module 'lte'): ns3::Ptr<ns3::LteSpectrumPhy> ns3::LtePhy::GetDownlinkSpectrumPhy() [member function]
    cls.add_method('GetDownlinkSpectrumPhy', 
                   'ns3::Ptr< ns3::LteSpectrumPhy >', 
                   [])
    ## lte-phy.h (module 'lte'): ns3::Ptr<ns3::PacketBurst> ns3::LtePhy::GetPacketBurst() [member function]
    cls.add_method('GetPacketBurst', 
                   'ns3::Ptr< ns3::PacketBurst >', 
                   [])
    ## lte-phy.h (module 'lte'): uint8_t ns3::LtePhy::GetRbgSize() const [member function]
    cls.add_method('GetRbgSize', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lte-phy.h (module 'lte'): uint16_t ns3::LtePhy::GetSrsPeriodicity(uint16_t srcCi) const [member function]
    cls.add_method('GetSrsPeriodicity', 
                   'uint16_t', 
                   [param('uint16_t', 'srcCi')], 
                   is_const=True)
    ## lte-phy.h (module 'lte'): uint16_t ns3::LtePhy::GetSrsSubframeOffset(uint16_t srcCi) const [member function]
    cls.add_method('GetSrsSubframeOffset', 
                   'uint16_t', 
                   [param('uint16_t', 'srcCi')], 
                   is_const=True)
    ## lte-phy.h (module 'lte'): double ns3::LtePhy::GetTti() const [member function]
    cls.add_method('GetTti', 
                   'double', 
                   [], 
                   is_const=True)
    ## lte-phy.h (module 'lte'): static ns3::TypeId ns3::LtePhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-phy.h (module 'lte'): ns3::Ptr<ns3::LteSpectrumPhy> ns3::LtePhy::GetUplinkSpectrumPhy() [member function]
    cls.add_method('GetUplinkSpectrumPhy', 
                   'ns3::Ptr< ns3::LteSpectrumPhy >', 
                   [])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::ReportInterference(ns3::SpectrumValue const & interf) [member function]
    cls.add_method('ReportInterference', 
                   'void', 
                   [param('ns3::SpectrumValue const &', 'interf')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::ReportRsReceivedPower(ns3::SpectrumValue const & power) [member function]
    cls.add_method('ReportRsReceivedPower', 
                   'void', 
                   [param('ns3::SpectrumValue const &', 'power')], 
                   is_pure_virtual=True, is_virtual=True)
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetControlMessages(ns3::Ptr<ns3::LteControlMessage> m) [member function]
    cls.add_method('SetControlMessages', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteControlMessage >', 'm')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetDevice(ns3::Ptr<ns3::LteNetDevice> d) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteNetDevice >', 'd')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetDownlinkChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetDownlinkChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetMacPdu(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('SetMacPdu', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetTti(double tti) [member function]
    cls.add_method('SetTti', 
                   'void', 
                   [param('double', 'tti')])
    ## lte-phy.h (module 'lte'): void ns3::LtePhy::SetUplinkChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetUplinkChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')])
    return

def register_Ns3LteSpectrumPhy_methods(root_module, cls):
    ## lte-spectrum-phy.h (module 'lte'): ns3::LteSpectrumPhy::LteSpectrumPhy() [constructor]
    cls.add_constructor([])
    ## lte-spectrum-phy.h (module 'lte'): static ns3::TypeId ns3::LteSpectrumPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetChannel(ns3::Ptr<ns3::SpectrumChannel> c) [member function]
    cls.add_method('SetChannel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumChannel >', 'c')], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetMobility(ns3::Ptr<ns3::MobilityModel> m) [member function]
    cls.add_method('SetMobility', 
                   'void', 
                   [param('ns3::Ptr< ns3::MobilityModel >', 'm')], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetDevice(ns3::Ptr<ns3::NetDevice> d) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'd')], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): ns3::Ptr<ns3::MobilityModel> ns3::LteSpectrumPhy::GetMobility() [member function]
    cls.add_method('GetMobility', 
                   'ns3::Ptr< ns3::MobilityModel >', 
                   [], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): ns3::Ptr<ns3::NetDevice> ns3::LteSpectrumPhy::GetDevice() [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): ns3::Ptr<ns3::SpectrumModel const> ns3::LteSpectrumPhy::GetRxSpectrumModel() const [member function]
    cls.add_method('GetRxSpectrumModel', 
                   'ns3::Ptr< ns3::SpectrumModel const >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): ns3::Ptr<ns3::AntennaModel> ns3::LteSpectrumPhy::GetRxAntenna() [member function]
    cls.add_method('GetRxAntenna', 
                   'ns3::Ptr< ns3::AntennaModel >', 
                   [], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::StartRx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_virtual=True)
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::StartRxData(ns3::Ptr<ns3::LteSpectrumSignalParametersDataFrame> params) [member function]
    cls.add_method('StartRxData', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteSpectrumSignalParametersDataFrame >', 'params')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::StartRxCtrl(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartRxCtrl', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetHarqPhyModule(ns3::Ptr<ns3::LteHarqPhy> harq) [member function]
    cls.add_method('SetHarqPhyModule', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteHarqPhy >', 'harq')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetTxPowerSpectralDensity(ns3::Ptr<ns3::SpectrumValue> txPsd) [member function]
    cls.add_method('SetTxPowerSpectralDensity', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue >', 'txPsd')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetNoisePowerSpectralDensity(ns3::Ptr<ns3::SpectrumValue const> noisePsd) [member function]
    cls.add_method('SetNoisePowerSpectralDensity', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumValue const >', 'noisePsd')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::Reset() [member function]
    cls.add_method('Reset', 
                   'void', 
                   [])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetAntenna(ns3::Ptr<ns3::AntennaModel> a) [member function]
    cls.add_method('SetAntenna', 
                   'void', 
                   [param('ns3::Ptr< ns3::AntennaModel >', 'a')])
    ## lte-spectrum-phy.h (module 'lte'): bool ns3::LteSpectrumPhy::StartTxDataFrame(ns3::Ptr<ns3::PacketBurst> pb, std::list<ns3::Ptr<ns3::LteControlMessage>, std::allocator<ns3::Ptr<ns3::LteControlMessage> > > ctrlMsgList, ns3::Time duration) [member function]
    cls.add_method('StartTxDataFrame', 
                   'bool', 
                   [param('ns3::Ptr< ns3::PacketBurst >', 'pb'), param('std::list< ns3::Ptr< ns3::LteControlMessage > >', 'ctrlMsgList'), param('ns3::Time', 'duration')])
    ## lte-spectrum-phy.h (module 'lte'): bool ns3::LteSpectrumPhy::StartTxDlCtrlFrame(std::list<ns3::Ptr<ns3::LteControlMessage>, std::allocator<ns3::Ptr<ns3::LteControlMessage> > > ctrlMsgList, bool pss) [member function]
    cls.add_method('StartTxDlCtrlFrame', 
                   'bool', 
                   [param('std::list< ns3::Ptr< ns3::LteControlMessage > >', 'ctrlMsgList'), param('bool', 'pss')])
    ## lte-spectrum-phy.h (module 'lte'): bool ns3::LteSpectrumPhy::StartTxUlSrsFrame() [member function]
    cls.add_method('StartTxUlSrsFrame', 
                   'bool', 
                   [])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyTxEndCallback(ns3::LtePhyTxEndCallback c) [member function]
    cls.add_method('SetLtePhyTxEndCallback', 
                   'void', 
                   [param('ns3::LtePhyTxEndCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyRxDataEndErrorCallback(ns3::LtePhyRxDataEndErrorCallback c) [member function]
    cls.add_method('SetLtePhyRxDataEndErrorCallback', 
                   'void', 
                   [param('ns3::LtePhyRxDataEndErrorCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyRxDataEndOkCallback(ns3::LtePhyRxDataEndOkCallback c) [member function]
    cls.add_method('SetLtePhyRxDataEndOkCallback', 
                   'void', 
                   [param('ns3::LtePhyRxDataEndOkCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyRxCtrlEndOkCallback(ns3::LtePhyRxCtrlEndOkCallback c) [member function]
    cls.add_method('SetLtePhyRxCtrlEndOkCallback', 
                   'void', 
                   [param('ns3::LtePhyRxCtrlEndOkCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyRxCtrlEndErrorCallback(ns3::LtePhyRxCtrlEndErrorCallback c) [member function]
    cls.add_method('SetLtePhyRxCtrlEndErrorCallback', 
                   'void', 
                   [param('ns3::LtePhyRxCtrlEndErrorCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyRxPssCallback(ns3::LtePhyRxPssCallback c) [member function]
    cls.add_method('SetLtePhyRxPssCallback', 
                   'void', 
                   [param('ns3::LtePhyRxPssCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyDlHarqFeedbackCallback(ns3::LtePhyDlHarqFeedbackCallback c) [member function]
    cls.add_method('SetLtePhyDlHarqFeedbackCallback', 
                   'void', 
                   [param('ns3::LtePhyDlHarqFeedbackCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetLtePhyUlHarqFeedbackCallback(ns3::LtePhyUlHarqFeedbackCallback c) [member function]
    cls.add_method('SetLtePhyUlHarqFeedbackCallback', 
                   'void', 
                   [param('ns3::LtePhyUlHarqFeedbackCallback', 'c')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetState(ns3::LteSpectrumPhy::State newState) [member function]
    cls.add_method('SetState', 
                   'void', 
                   [param('ns3::LteSpectrumPhy::State', 'newState')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetCellId(uint16_t cellId) [member function]
    cls.add_method('SetCellId', 
                   'void', 
                   [param('uint16_t', 'cellId')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddRsPowerChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddRsPowerChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddDataPowerChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddDataPowerChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddDataSinrChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddDataSinrChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddInterferenceCtrlChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddInterferenceCtrlChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddInterferenceDataChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddInterferenceDataChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddCtrlSinrChunkProcessor(ns3::Ptr<ns3::LteChunkProcessor> p) [member function]
    cls.add_method('AddCtrlSinrChunkProcessor', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteChunkProcessor >', 'p')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::AddExpectedTb(uint16_t rnti, uint8_t ndi, uint16_t size, uint8_t mcs, std::vector<int, std::allocator<int> > map, uint8_t layer, uint8_t harqId, uint8_t rv, bool downlink) [member function]
    cls.add_method('AddExpectedTb', 
                   'void', 
                   [param('uint16_t', 'rnti'), param('uint8_t', 'ndi'), param('uint16_t', 'size'), param('uint8_t', 'mcs'), param('std::vector< int >', 'map'), param('uint8_t', 'layer'), param('uint8_t', 'harqId'), param('uint8_t', 'rv'), param('bool', 'downlink')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::UpdateSinrPerceived(ns3::SpectrumValue const & sinr) [member function]
    cls.add_method('UpdateSinrPerceived', 
                   'void', 
                   [param('ns3::SpectrumValue const &', 'sinr')])
    ## lte-spectrum-phy.h (module 'lte'): void ns3::LteSpectrumPhy::SetTransmissionMode(uint8_t txMode) [member function]
    cls.add_method('SetTransmissionMode', 
                   'void', 
                   [param('uint8_t', 'txMode')])
    ## lte-spectrum-phy.h (module 'lte'): ns3::Ptr<ns3::SpectrumChannel> ns3::LteSpectrumPhy::GetChannel() [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::SpectrumChannel >', 
                   [])
    ## lte-spectrum-phy.h (module 'lte'): int64_t ns3::LteSpectrumPhy::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    return

def register_Ns3Mac48AddressChecker_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker(ns3::Mac48AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48AddressChecker const &', 'arg0')])
    return

def register_Ns3Mac48AddressValue_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48AddressValue const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48Address const & value) [constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'value')])
    ## mac48-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Mac48AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## mac48-address.h (module 'network'): ns3::Mac48Address ns3::Mac48AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): std::string ns3::Mac48AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48AddressValue::Set(ns3::Mac48Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Mac48Address const &', 'value')])
    return

def register_Ns3MibLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::MibLteControlMessage::MibLteControlMessage(ns3::MibLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MibLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::MibLteControlMessage::MibLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::LteRrcSap::MasterInformationBlock ns3::MibLteControlMessage::GetMib() const [member function]
    cls.add_method('GetMib', 
                   'ns3::LteRrcSap::MasterInformationBlock', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): void ns3::MibLteControlMessage::SetMib(ns3::LteRrcSap::MasterInformationBlock mib) [member function]
    cls.add_method('SetMib', 
                   'void', 
                   [param('ns3::LteRrcSap::MasterInformationBlock', 'mib')])
    return

def register_Ns3MobilityModel_methods(root_module, cls):
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel::MobilityModel(ns3::MobilityModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MobilityModel const &', 'arg0')])
    ## mobility-model.h (module 'mobility'): ns3::MobilityModel::MobilityModel() [constructor]
    cls.add_constructor([])
    ## mobility-model.h (module 'mobility'): int64_t ns3::MobilityModel::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## mobility-model.h (module 'mobility'): double ns3::MobilityModel::GetDistanceFrom(ns3::Ptr<const ns3::MobilityModel> position) const [member function]
    cls.add_method('GetDistanceFrom', 
                   'double', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'position')], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::GetPosition() const [member function]
    cls.add_method('GetPosition', 
                   'ns3::Vector', 
                   [], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): double ns3::MobilityModel::GetRelativeSpeed(ns3::Ptr<const ns3::MobilityModel> other) const [member function]
    cls.add_method('GetRelativeSpeed', 
                   'double', 
                   [param('ns3::Ptr< ns3::MobilityModel const >', 'other')], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): static ns3::TypeId ns3::MobilityModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::GetVelocity() const [member function]
    cls.add_method('GetVelocity', 
                   'ns3::Vector', 
                   [], 
                   is_const=True)
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::SetPosition(ns3::Vector const & position) [member function]
    cls.add_method('SetPosition', 
                   'void', 
                   [param('ns3::Vector const &', 'position')])
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::NotifyCourseChange() const [member function]
    cls.add_method('NotifyCourseChange', 
                   'void', 
                   [], 
                   is_const=True, visibility='protected')
    ## mobility-model.h (module 'mobility'): int64_t ns3::MobilityModel::DoAssignStreams(int64_t start) [member function]
    cls.add_method('DoAssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'start')], 
                   visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::DoGetPosition() const [member function]
    cls.add_method('DoGetPosition', 
                   'ns3::Vector', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): ns3::Vector ns3::MobilityModel::DoGetVelocity() const [member function]
    cls.add_method('DoGetVelocity', 
                   'ns3::Vector', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## mobility-model.h (module 'mobility'): void ns3::MobilityModel::DoSetPosition(ns3::Vector const & position) [member function]
    cls.add_method('DoSetPosition', 
                   'void', 
                   [param('ns3::Vector const &', 'position')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3NetDevice_methods(root_module, cls):
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice() [constructor]
    cls.add_constructor([])
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice(ns3::NetDevice const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::NetDevice const &', 'arg0')])
    ## net-device.h (module 'network'): void ns3::NetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Channel> ns3::NetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint32_t ns3::NetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint16_t ns3::NetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv4Address multicastGroup) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): static ns3::TypeId ns3::NetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetPromiscReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3NixVector_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector() [constructor]
    cls.add_constructor([])
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector(ns3::NixVector const & o) [copy constructor]
    cls.add_constructor([param('ns3::NixVector const &', 'o')])
    ## nix-vector.h (module 'network'): void ns3::NixVector::AddNeighborIndex(uint32_t newBits, uint32_t numberOfBits) [member function]
    cls.add_method('AddNeighborIndex', 
                   'void', 
                   [param('uint32_t', 'newBits'), param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::BitCount(uint32_t numberOfNeighbors) const [member function]
    cls.add_method('BitCount', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfNeighbors')], 
                   is_const=True)
    ## nix-vector.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::NixVector::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Deserialize(uint32_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint32_t const *', 'buffer'), param('uint32_t', 'size')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::ExtractNeighborIndex(uint32_t numberOfBits) [member function]
    cls.add_method('ExtractNeighborIndex', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetRemainingBits() [member function]
    cls.add_method('GetRemainingBits', 
                   'uint32_t', 
                   [])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Serialize(uint32_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint32_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3Node_methods(root_module, cls):
    ## node.h (module 'network'): ns3::Node::Node(ns3::Node const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Node const &', 'arg0')])
    ## node.h (module 'network'): ns3::Node::Node() [constructor]
    cls.add_constructor([])
    ## node.h (module 'network'): ns3::Node::Node(uint32_t systemId) [constructor]
    cls.add_constructor([param('uint32_t', 'systemId')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddApplication(ns3::Ptr<ns3::Application> application) [member function]
    cls.add_method('AddApplication', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Application >', 'application')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddDevice(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddDevice', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    ## node.h (module 'network'): static bool ns3::Node::ChecksumEnabled() [member function]
    cls.add_method('ChecksumEnabled', 
                   'bool', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::Application> ns3::Node::GetApplication(uint32_t index) const [member function]
    cls.add_method('GetApplication', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Node::GetDevice(uint32_t index) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNApplications() const [member function]
    cls.add_method('GetNApplications', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): static ns3::TypeId ns3::Node::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): void ns3::Node::RegisterDeviceAdditionListener(ns3::Callback<void,ns3::Ptr<ns3::NetDevice>,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> listener) [member function]
    cls.add_method('RegisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::RegisterProtocolHandler(ns3::Callback<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> handler, uint16_t protocolType, ns3::Ptr<ns3::NetDevice> device, bool promiscuous=false) [member function]
    cls.add_method('RegisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler'), param('uint16_t', 'protocolType'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'promiscuous', default_value='false')])
    ## node.h (module 'network'): void ns3::Node::UnregisterDeviceAdditionListener(ns3::Callback<void,ns3::Ptr<ns3::NetDevice>,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> listener) [member function]
    cls.add_method('UnregisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::UnregisterProtocolHandler(ns3::Callback<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> handler) [member function]
    cls.add_method('UnregisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler')])
    ## node.h (module 'network'): void ns3::Node::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## node.h (module 'network'): void ns3::Node::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3NormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::INFINITE_VALUE [variable]
    cls.add_static_attribute('INFINITE_VALUE', 'double const', is_const=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::NormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::NormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetVariance() const [member function]
    cls.add_method('GetVariance', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue(double mean, double variance, double bound=ns3::NormalRandomVariable::INFINITE_VALUE) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'variance'), param('double', 'bound', default_value='ns3::NormalRandomVariable::INFINITE_VALUE')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger(uint32_t mean, uint32_t variance, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'variance'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ObjectFactoryChecker_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker(ns3::ObjectFactoryChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactoryChecker const &', 'arg0')])
    return

def register_Ns3ObjectFactoryValue_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactoryValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactoryValue const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactory const & value) [constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'value')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::ObjectFactoryValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): bool ns3::ObjectFactoryValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## object-factory.h (module 'core'): ns3::ObjectFactory ns3::ObjectFactoryValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::ObjectFactory', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): std::string ns3::ObjectFactoryValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactoryValue::Set(ns3::ObjectFactory const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::ObjectFactory const &', 'value')])
    return

def register_Ns3OutputStreamWrapper_methods(root_module, cls):
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(ns3::OutputStreamWrapper const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::OutputStreamWrapper const &', 'arg0')])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(std::string filename, std::_Ios_Openmode filemode) [constructor]
    cls.add_constructor([param('std::string', 'filename'), param('std::_Ios_Openmode', 'filemode')])
    ## output-stream-wrapper.h (module 'network'): ns3::OutputStreamWrapper::OutputStreamWrapper(std::ostream * os) [constructor]
    cls.add_constructor([param('std::ostream *', 'os')])
    ## output-stream-wrapper.h (module 'network'): std::ostream * ns3::OutputStreamWrapper::GetStream() [member function]
    cls.add_method('GetStream', 
                   'std::ostream *', 
                   [])
    return

def register_Ns3Packet_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## packet.h (module 'network'): ns3::Packet::Packet() [constructor]
    cls.add_constructor([])
    ## packet.h (module 'network'): ns3::Packet::Packet(ns3::Packet const & o) [copy constructor]
    cls.add_constructor([param('ns3::Packet const &', 'o')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint32_t size) [constructor]
    cls.add_constructor([param('uint32_t', 'size')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size, bool magic) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size'), param('bool', 'magic')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddAtEnd(ns3::Ptr<const ns3::Packet> packet) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## packet.h (module 'network'): void ns3::Packet::AddByteTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddByteTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddHeader(ns3::Header const & header) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header')])
    ## packet.h (module 'network'): void ns3::Packet::AddPacketTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddPacketTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddPaddingAtEnd(uint32_t size) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddTrailer(ns3::Trailer const & trailer) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer')])
    ## packet.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::Packet::BeginItem() const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnablePrinting() [member function]
    cls.add_method('EnablePrinting', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): bool ns3::Packet::FindFirstMatchingByteTag(ns3::Tag & tag) const [member function]
    cls.add_method('FindFirstMatchingByteTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator ns3::Packet::GetByteTagIterator() const [member function]
    cls.add_method('GetByteTagIterator', 
                   'ns3::ByteTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::Packet::GetNixVector() const [member function]
    cls.add_method('GetNixVector', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator ns3::Packet::GetPacketTagIterator() const [member function]
    cls.add_method('GetPacketTagIterator', 
                   'ns3::PacketTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint64_t ns3::Packet::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekHeader(ns3::Header & header) const [member function]
    cls.add_method('PeekHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')], 
                   is_const=True)
    ## packet.h (module 'network'): bool ns3::Packet::PeekPacketTag(ns3::Tag & tag) const [member function]
    cls.add_method('PeekPacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('PeekTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): void ns3::Packet::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintByteTags(std::ostream & os) const [member function]
    cls.add_method('PrintByteTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintPacketTags(std::ostream & os) const [member function]
    cls.add_method('PrintPacketTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllByteTags() [member function]
    cls.add_method('RemoveAllByteTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllPacketTags() [member function]
    cls.add_method('RemoveAllPacketTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtEnd(uint32_t size) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtStart(uint32_t size) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveHeader(ns3::Header & header) [member function]
    cls.add_method('RemoveHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')])
    ## packet.h (module 'network'): bool ns3::Packet::RemovePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('RemovePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('RemoveTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): bool ns3::Packet::ReplacePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('ReplacePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::SetNixVector(ns3::Ptr<ns3::NixVector> nixVector) [member function]
    cls.add_method('SetNixVector', 
                   'void', 
                   [param('ns3::Ptr< ns3::NixVector >', 'nixVector')])
    ## packet.h (module 'network'): std::string ns3::Packet::ToString() const [member function]
    cls.add_method('ToString', 
                   'std::string', 
                   [], 
                   is_const=True)
    return

def register_Ns3ParetoRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ParetoRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable::ParetoRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue(double mean, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger(uint32_t mean, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3RachPreambleLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::RachPreambleLteControlMessage::RachPreambleLteControlMessage(ns3::RachPreambleLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RachPreambleLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::RachPreambleLteControlMessage::RachPreambleLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): uint32_t ns3::RachPreambleLteControlMessage::GetRapId() const [member function]
    cls.add_method('GetRapId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): void ns3::RachPreambleLteControlMessage::SetRapId(uint32_t rapid) [member function]
    cls.add_method('SetRapId', 
                   'void', 
                   [param('uint32_t', 'rapid')])
    return

def register_Ns3RarLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::RarLteControlMessage(ns3::RarLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RarLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::RarLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): void ns3::RarLteControlMessage::AddRar(ns3::RarLteControlMessage::Rar rar) [member function]
    cls.add_method('AddRar', 
                   'void', 
                   [param('ns3::RarLteControlMessage::Rar', 'rar')])
    ## lte-control-messages.h (module 'lte'): uint16_t ns3::RarLteControlMessage::GetRaRnti() const [member function]
    cls.add_method('GetRaRnti', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): std::_List_const_iterator<ns3::RarLteControlMessage::Rar> ns3::RarLteControlMessage::RarListBegin() const [member function]
    cls.add_method('RarListBegin', 
                   'std::_List_const_iterator< ns3::RarLteControlMessage::Rar >', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): std::_List_const_iterator<ns3::RarLteControlMessage::Rar> ns3::RarLteControlMessage::RarListEnd() const [member function]
    cls.add_method('RarListEnd', 
                   'std::_List_const_iterator< ns3::RarLteControlMessage::Rar >', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): void ns3::RarLteControlMessage::SetRaRnti(uint16_t raRnti) [member function]
    cls.add_method('SetRaRnti', 
                   'void', 
                   [param('uint16_t', 'raRnti')])
    return

def register_Ns3RarLteControlMessageRar_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::Rar::Rar() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::Rar::Rar(ns3::RarLteControlMessage::Rar const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RarLteControlMessage::Rar const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::Rar::rapId [variable]
    cls.add_instance_attribute('rapId', 'uint8_t', is_const=False)
    ## lte-control-messages.h (module 'lte'): ns3::RarLteControlMessage::Rar::rarPayload [variable]
    cls.add_instance_attribute('rarPayload', 'ns3::BuildRarListElement_s', is_const=False)
    return

def register_Ns3RectangleChecker_methods(root_module, cls):
    ## rectangle.h (module 'mobility'): ns3::RectangleChecker::RectangleChecker() [constructor]
    cls.add_constructor([])
    ## rectangle.h (module 'mobility'): ns3::RectangleChecker::RectangleChecker(ns3::RectangleChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RectangleChecker const &', 'arg0')])
    return

def register_Ns3RectangleValue_methods(root_module, cls):
    ## rectangle.h (module 'mobility'): ns3::RectangleValue::RectangleValue() [constructor]
    cls.add_constructor([])
    ## rectangle.h (module 'mobility'): ns3::RectangleValue::RectangleValue(ns3::RectangleValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RectangleValue const &', 'arg0')])
    ## rectangle.h (module 'mobility'): ns3::RectangleValue::RectangleValue(ns3::Rectangle const & value) [constructor]
    cls.add_constructor([param('ns3::Rectangle const &', 'value')])
    ## rectangle.h (module 'mobility'): ns3::Ptr<ns3::AttributeValue> ns3::RectangleValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## rectangle.h (module 'mobility'): bool ns3::RectangleValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## rectangle.h (module 'mobility'): ns3::Rectangle ns3::RectangleValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Rectangle', 
                   [], 
                   is_const=True)
    ## rectangle.h (module 'mobility'): std::string ns3::RectangleValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## rectangle.h (module 'mobility'): void ns3::RectangleValue::Set(ns3::Rectangle const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Rectangle const &', 'value')])
    return

def register_Ns3Sib1LteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::Sib1LteControlMessage::Sib1LteControlMessage(ns3::Sib1LteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Sib1LteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::Sib1LteControlMessage::Sib1LteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::LteRrcSap::SystemInformationBlockType1 ns3::Sib1LteControlMessage::GetSib1() const [member function]
    cls.add_method('GetSib1', 
                   'ns3::LteRrcSap::SystemInformationBlockType1', 
                   [], 
                   is_const=True)
    ## lte-control-messages.h (module 'lte'): void ns3::Sib1LteControlMessage::SetSib1(ns3::LteRrcSap::SystemInformationBlockType1 sib1) [member function]
    cls.add_method('SetSib1', 
                   'void', 
                   [param('ns3::LteRrcSap::SystemInformationBlockType1', 'sib1')])
    return

def register_Ns3SpectrumChannel_methods(root_module, cls):
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel::SpectrumChannel() [constructor]
    cls.add_constructor([])
    ## spectrum-channel.h (module 'spectrum'): ns3::SpectrumChannel::SpectrumChannel(ns3::SpectrumChannel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumChannel const &', 'arg0')])
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddPropagationLossModel(ns3::Ptr<ns3::PropagationLossModel> loss) [member function]
    cls.add_method('AddPropagationLossModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationLossModel >', 'loss')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddRx(ns3::Ptr<ns3::SpectrumPhy> phy) [member function]
    cls.add_method('AddRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::AddSpectrumPropagationLossModel(ns3::Ptr<ns3::SpectrumPropagationLossModel> loss) [member function]
    cls.add_method('AddSpectrumPropagationLossModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumPropagationLossModel >', 'loss')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): static ns3::TypeId ns3::SpectrumChannel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::SetPropagationDelayModel(ns3::Ptr<ns3::PropagationDelayModel> delay) [member function]
    cls.add_method('SetPropagationDelayModel', 
                   'void', 
                   [param('ns3::Ptr< ns3::PropagationDelayModel >', 'delay')], 
                   is_pure_virtual=True, is_virtual=True)
    ## spectrum-channel.h (module 'spectrum'): void ns3::SpectrumChannel::StartTx(ns3::Ptr<ns3::SpectrumSignalParameters> params) [member function]
    cls.add_method('StartTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::SpectrumSignalParameters >', 'params')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3TimeValue_methods(root_module, cls):
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::TimeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TimeValue const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::Time const & value) [constructor]
    cls.add_constructor([param('ns3::Time const &', 'value')])
    ## nstime.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TimeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): bool ns3::TimeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## nstime.h (module 'core'): ns3::Time ns3::TimeValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): std::string ns3::TimeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): void ns3::TimeValue::Set(ns3::Time const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Time const &', 'value')])
    return

def register_Ns3TypeIdChecker_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker(ns3::TypeIdChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeIdChecker const &', 'arg0')])
    return

def register_Ns3TypeIdValue_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeIdValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeIdValue const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeId const & value) [constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'value')])
    ## type-id.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TypeIdValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): bool ns3::TypeIdValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeIdValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeIdValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): void ns3::TypeIdValue::Set(ns3::TypeId const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::TypeId const &', 'value')])
    return

def register_Ns3UanModesListChecker_methods(root_module, cls):
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListChecker::UanModesListChecker() [constructor]
    cls.add_constructor([])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListChecker::UanModesListChecker(ns3::UanModesListChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanModesListChecker const &', 'arg0')])
    return

def register_Ns3UanModesListValue_methods(root_module, cls):
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListValue::UanModesListValue() [constructor]
    cls.add_constructor([])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListValue::UanModesListValue(ns3::UanModesListValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UanModesListValue const &', 'arg0')])
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesListValue::UanModesListValue(ns3::UanModesList const & value) [constructor]
    cls.add_constructor([param('ns3::UanModesList const &', 'value')])
    ## uan-tx-mode.h (module 'uan'): ns3::Ptr<ns3::AttributeValue> ns3::UanModesListValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uan-tx-mode.h (module 'uan'): bool ns3::UanModesListValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## uan-tx-mode.h (module 'uan'): ns3::UanModesList ns3::UanModesListValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::UanModesList', 
                   [], 
                   is_const=True)
    ## uan-tx-mode.h (module 'uan'): std::string ns3::UanModesListValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## uan-tx-mode.h (module 'uan'): void ns3::UanModesListValue::Set(ns3::UanModesList const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::UanModesList const &', 'value')])
    return

def register_Ns3UintegerValue_methods(root_module, cls):
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue() [constructor]
    cls.add_constructor([])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(ns3::UintegerValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UintegerValue const &', 'arg0')])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(uint64_t const & value) [constructor]
    cls.add_constructor([param('uint64_t const &', 'value')])
    ## uinteger.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::UintegerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): bool ns3::UintegerValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## uinteger.h (module 'core'): uint64_t ns3::UintegerValue::Get() const [member function]
    cls.add_method('Get', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## uinteger.h (module 'core'): std::string ns3::UintegerValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): void ns3::UintegerValue::Set(uint64_t const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint64_t const &', 'value')])
    return

def register_Ns3UlDciLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::UlDciLteControlMessage::UlDciLteControlMessage(ns3::UlDciLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UlDciLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::UlDciLteControlMessage::UlDciLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::UlDciListElement_s ns3::UlDciLteControlMessage::GetDci() [member function]
    cls.add_method('GetDci', 
                   'ns3::UlDciListElement_s', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::UlDciLteControlMessage::SetDci(ns3::UlDciListElement_s dci) [member function]
    cls.add_method('SetDci', 
                   'void', 
                   [param('ns3::UlDciListElement_s', 'dci')])
    return

def register_Ns3Vector2DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker(ns3::Vector2DChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2DChecker const &', 'arg0')])
    return

def register_Ns3Vector2DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2DValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'value')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector2DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector2DValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector2D ns3::Vector2DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector2D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector2DValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector2DValue::Set(ns3::Vector2D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector2D const &', 'value')])
    return

def register_Ns3Vector3DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker(ns3::Vector3DChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3DChecker const &', 'arg0')])
    return

def register_Ns3Vector3DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3DValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'value')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector3DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector3DValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector3D ns3::Vector3DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector3D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector3DValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector3DValue::Set(ns3::Vector3D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector3D const &', 'value')])
    return

def register_Ns3AddressChecker_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker(ns3::AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AddressChecker const &', 'arg0')])
    return

def register_Ns3AddressValue_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressValue::AddressValue() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AddressValue const &', 'arg0')])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::Address const & value) [constructor]
    cls.add_constructor([param('ns3::Address const &', 'value')])
    ## address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): bool ns3::AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## address.h (module 'network'): ns3::Address ns3::AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): std::string ns3::AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): void ns3::AddressValue::Set(ns3::Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Address const &', 'value')])
    return

def register_Ns3BsrLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::BsrLteControlMessage::BsrLteControlMessage(ns3::BsrLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BsrLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::BsrLteControlMessage::BsrLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::MacCeListElement_s ns3::BsrLteControlMessage::GetBsr() [member function]
    cls.add_method('GetBsr', 
                   'ns3::MacCeListElement_s', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::BsrLteControlMessage::SetBsr(ns3::MacCeListElement_s bsr) [member function]
    cls.add_method('SetBsr', 
                   'void', 
                   [param('ns3::MacCeListElement_s', 'bsr')])
    return

def register_Ns3DlCqiLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::DlCqiLteControlMessage::DlCqiLteControlMessage(ns3::DlCqiLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DlCqiLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::DlCqiLteControlMessage::DlCqiLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::CqiListElement_s ns3::DlCqiLteControlMessage::GetDlCqi() [member function]
    cls.add_method('GetDlCqi', 
                   'ns3::CqiListElement_s', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::DlCqiLteControlMessage::SetDlCqi(ns3::CqiListElement_s dlcqi) [member function]
    cls.add_method('SetDlCqi', 
                   'void', 
                   [param('ns3::CqiListElement_s', 'dlcqi')])
    return

def register_Ns3DlDciLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::DlDciLteControlMessage::DlDciLteControlMessage(ns3::DlDciLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DlDciLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::DlDciLteControlMessage::DlDciLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::DlDciListElement_s ns3::DlDciLteControlMessage::GetDci() [member function]
    cls.add_method('GetDci', 
                   'ns3::DlDciListElement_s', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::DlDciLteControlMessage::SetDci(ns3::DlDciListElement_s dci) [member function]
    cls.add_method('SetDci', 
                   'void', 
                   [param('ns3::DlDciListElement_s', 'dci')])
    return

def register_Ns3DlHarqFeedbackLteControlMessage_methods(root_module, cls):
    ## lte-control-messages.h (module 'lte'): ns3::DlHarqFeedbackLteControlMessage::DlHarqFeedbackLteControlMessage(ns3::DlHarqFeedbackLteControlMessage const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DlHarqFeedbackLteControlMessage const &', 'arg0')])
    ## lte-control-messages.h (module 'lte'): ns3::DlHarqFeedbackLteControlMessage::DlHarqFeedbackLteControlMessage() [constructor]
    cls.add_constructor([])
    ## lte-control-messages.h (module 'lte'): ns3::DlInfoListElement_s ns3::DlHarqFeedbackLteControlMessage::GetDlHarqFeedback() [member function]
    cls.add_method('GetDlHarqFeedback', 
                   'ns3::DlInfoListElement_s', 
                   [])
    ## lte-control-messages.h (module 'lte'): void ns3::DlHarqFeedbackLteControlMessage::SetDlHarqFeedback(ns3::DlInfoListElement_s m) [member function]
    cls.add_method('SetDlHarqFeedback', 
                   'void', 
                   [param('ns3::DlInfoListElement_s', 'm')])
    return

def register_Ns3LteNetDevice_methods(root_module, cls):
    ## lte-net-device.h (module 'lte'): static ns3::TypeId ns3::LteNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-net-device.h (module 'lte'): ns3::LteNetDevice::LteNetDevice() [constructor]
    cls.add_constructor([])
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): uint32_t ns3::LteNetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Ptr<ns3::Channel> ns3::LteNetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): uint16_t ns3::LteNetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Address ns3::LteNetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Address ns3::LteNetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Ptr<ns3::Node> ns3::LteNetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::SetReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Address ns3::LteNetDevice::GetMulticast(ns3::Ipv4Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): ns3::Address ns3::LteNetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::SetPromiscReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lte-net-device.h (module 'lte'): bool ns3::LteNetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-net-device.h (module 'lte'): void ns3::LteNetDevice::Receive(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    return

def register_Ns3LteUeNetDevice_methods(root_module, cls):
    ## lte-ue-net-device.h (module 'lte'): static ns3::TypeId ns3::LteUeNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::LteUeNetDevice::LteUeNetDevice() [constructor]
    cls.add_constructor([])
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): bool ns3::LteUeNetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetMacAddress(ns3::Address address) [member function]
    cls.add_method('SetMacAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetGatewayMacAddress(ns3::Address address) [member function]
    cls.add_method('SetGatewayMacAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Address ns3::LteUeNetDevice::GetMacAddress() const [member function]
    cls.add_method('GetMacAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Address ns3::LteUeNetDevice::GetGatewayMacAddress() const [member function]
    cls.add_method('GetGatewayMacAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetPromiscReceiveCallback(ns3::Callback<bool, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::Receive(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')], 
                   is_virtual=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Ptr<ns3::LteUeMac> ns3::LteUeNetDevice::GetMac() const [member function]
    cls.add_method('GetMac', 
                   'ns3::Ptr< ns3::LteUeMac >', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Ptr<ns3::LteUeRrc> ns3::LteUeNetDevice::GetRrc() const [member function]
    cls.add_method('GetRrc', 
                   'ns3::Ptr< ns3::LteUeRrc >', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Ptr<ns3::LteUePhy> ns3::LteUeNetDevice::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::LteUePhy >', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): ns3::Ptr<ns3::EpcUeNas> ns3::LteUeNetDevice::GetNas() const [member function]
    cls.add_method('GetNas', 
                   'ns3::Ptr< ns3::EpcUeNas >', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): uint64_t ns3::LteUeNetDevice::GetImsi() const [member function]
    cls.add_method('GetImsi', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): uint16_t ns3::LteUeNetDevice::GetDlEarfcn() const [member function]
    cls.add_method('GetDlEarfcn', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetDlEarfcn(uint16_t earfcn) [member function]
    cls.add_method('SetDlEarfcn', 
                   'void', 
                   [param('uint16_t', 'earfcn')])
    ## lte-ue-net-device.h (module 'lte'): uint32_t ns3::LteUeNetDevice::GetCsgId() const [member function]
    cls.add_method('GetCsgId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetCsgId(uint32_t csgId) [member function]
    cls.add_method('SetCsgId', 
                   'void', 
                   [param('uint32_t', 'csgId')])
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::SetTargetEnb(ns3::Ptr<ns3::LteEnbNetDevice> enb) [member function]
    cls.add_method('SetTargetEnb', 
                   'void', 
                   [param('ns3::Ptr< ns3::LteEnbNetDevice >', 'enb')])
    ## lte-ue-net-device.h (module 'lte'): ns3::Ptr<ns3::LteEnbNetDevice> ns3::LteUeNetDevice::GetTargetEnb() [member function]
    cls.add_method('GetTargetEnb', 
                   'ns3::Ptr< ns3::LteEnbNetDevice >', 
                   [])
    ## lte-ue-net-device.h (module 'lte'): void ns3::LteUeNetDevice::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3LteEnbNetDevice_methods(root_module, cls):
    ## lte-enb-net-device.h (module 'lte'): static ns3::TypeId ns3::LteEnbNetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## lte-enb-net-device.h (module 'lte'): ns3::LteEnbNetDevice::LteEnbNetDevice() [constructor]
    cls.add_constructor([])
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## lte-enb-net-device.h (module 'lte'): bool ns3::LteEnbNetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_virtual=True)
    ## lte-enb-net-device.h (module 'lte'): ns3::Ptr<ns3::LteEnbMac> ns3::LteEnbNetDevice::GetMac() const [member function]
    cls.add_method('GetMac', 
                   'ns3::Ptr< ns3::LteEnbMac >', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): ns3::Ptr<ns3::LteEnbPhy> ns3::LteEnbNetDevice::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::LteEnbPhy >', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): ns3::Ptr<ns3::LteEnbRrc> ns3::LteEnbNetDevice::GetRrc() const [member function]
    cls.add_method('GetRrc', 
                   'ns3::Ptr< ns3::LteEnbRrc >', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): uint16_t ns3::LteEnbNetDevice::GetCellId() const [member function]
    cls.add_method('GetCellId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): uint8_t ns3::LteEnbNetDevice::GetUlBandwidth() const [member function]
    cls.add_method('GetUlBandwidth', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetUlBandwidth(uint8_t bw) [member function]
    cls.add_method('SetUlBandwidth', 
                   'void', 
                   [param('uint8_t', 'bw')])
    ## lte-enb-net-device.h (module 'lte'): uint8_t ns3::LteEnbNetDevice::GetDlBandwidth() const [member function]
    cls.add_method('GetDlBandwidth', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetDlBandwidth(uint8_t bw) [member function]
    cls.add_method('SetDlBandwidth', 
                   'void', 
                   [param('uint8_t', 'bw')])
    ## lte-enb-net-device.h (module 'lte'): uint16_t ns3::LteEnbNetDevice::GetDlEarfcn() const [member function]
    cls.add_method('GetDlEarfcn', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetDlEarfcn(uint16_t earfcn) [member function]
    cls.add_method('SetDlEarfcn', 
                   'void', 
                   [param('uint16_t', 'earfcn')])
    ## lte-enb-net-device.h (module 'lte'): uint16_t ns3::LteEnbNetDevice::GetUlEarfcn() const [member function]
    cls.add_method('GetUlEarfcn', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetUlEarfcn(uint16_t earfcn) [member function]
    cls.add_method('SetUlEarfcn', 
                   'void', 
                   [param('uint16_t', 'earfcn')])
    ## lte-enb-net-device.h (module 'lte'): uint32_t ns3::LteEnbNetDevice::GetCsgId() const [member function]
    cls.add_method('GetCsgId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetCsgId(uint32_t csgId) [member function]
    cls.add_method('SetCsgId', 
                   'void', 
                   [param('uint32_t', 'csgId')])
    ## lte-enb-net-device.h (module 'lte'): bool ns3::LteEnbNetDevice::GetCsgIndication() const [member function]
    cls.add_method('GetCsgIndication', 
                   'bool', 
                   [], 
                   is_const=True)
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::SetCsgIndication(bool csgIndication) [member function]
    cls.add_method('SetCsgIndication', 
                   'void', 
                   [param('bool', 'csgIndication')])
    ## lte-enb-net-device.h (module 'lte'): void ns3::LteEnbNetDevice::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ConfigMatchContainer_methods(root_module, cls):
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer(ns3::Config::MatchContainer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Config::MatchContainer const &', 'arg0')])
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer() [constructor]
    cls.add_constructor([])
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer(std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > const & objects, std::vector<std::string, std::allocator<std::string> > const & contexts, std::string path) [constructor]
    cls.add_constructor([param('std::vector< ns3::Ptr< ns3::Object > > const &', 'objects'), param('std::vector< std::string > const &', 'contexts'), param('std::string', 'path')])
    ## config.h (module 'core'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Object>*,std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > > ns3::Config::MatchContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Object > const, std::vector< ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Connect(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('Connect', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::ConnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('ConnectWithoutContext', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Disconnect(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('Disconnect', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::DisconnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Object>*,std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > > ns3::Config::MatchContainer::End() const [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Object > const, std::vector< ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): ns3::Ptr<ns3::Object> ns3::Config::MatchContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Object >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## config.h (module 'core'): std::string ns3::Config::MatchContainer::GetMatchedPath(uint32_t i) const [member function]
    cls.add_method('GetMatchedPath', 
                   'std::string', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## config.h (module 'core'): uint32_t ns3::Config::MatchContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): std::string ns3::Config::MatchContainer::GetPath() const [member function]
    cls.add_method('GetPath', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Set(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    return

def register_Ns3HashImplementation_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation(ns3::Hash::Implementation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Implementation const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation() [constructor]
    cls.add_constructor([])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Implementation::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_pure_virtual=True, is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Implementation::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Implementation::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3HashFunctionFnv1a_methods(root_module, cls):
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a(ns3::Hash::Function::Fnv1a const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Fnv1a const &', 'arg0')])
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a() [constructor]
    cls.add_constructor([])
    ## hash-fnv.h (module 'core'): uint32_t ns3::Hash::Function::Fnv1a::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): uint64_t ns3::Hash::Function::Fnv1a::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): void ns3::Hash::Function::Fnv1a::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash32_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Function::Hash32 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash32 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Hash32Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash32Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash32::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash32::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash64_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Function::Hash64 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash64 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Hash64Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash64Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash64::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Function::Hash64::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash64::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionMurmur3_methods(root_module, cls):
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3(ns3::Hash::Function::Murmur3 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Murmur3 const &', 'arg0')])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3() [constructor]
    cls.add_constructor([])
    ## hash-murmur3.h (module 'core'): uint32_t ns3::Hash::Function::Murmur3::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): uint64_t ns3::Hash::Function::Murmur3::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): void ns3::Hash::Function::Murmur3::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    register_functions_ns3_Config(module.get_submodule('Config'), root_module)
    register_functions_ns3_FatalImpl(module.get_submodule('FatalImpl'), root_module)
    register_functions_ns3_Hash(module.get_submodule('Hash'), root_module)
    register_functions_ns3_internal(module.get_submodule('internal'), root_module)
    return

def register_functions_ns3_Config(module, root_module):
    return

def register_functions_ns3_FatalImpl(module, root_module):
    return

def register_functions_ns3_Hash(module, root_module):
    register_functions_ns3_Hash_Function(module.get_submodule('Function'), root_module)
    return

def register_functions_ns3_Hash_Function(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()

