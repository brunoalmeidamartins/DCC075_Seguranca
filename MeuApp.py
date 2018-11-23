from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
#Pacotes
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import arp
from ryu.lib.packet import ipv4
from ryu.lib.packet import icmp
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
#Extras
from ryu.lib.dpid import dpid_to_str
from ryu.ofproto.ofproto_v1_2 import OFPG_ANY
from ryu.lib.mac import haddr_to_bin
#Topologia
from ryu.topology import event, switches
from ryu.topology.api import get_switch, get_link
#Sistema
import os


path_home = os.getenv("HOME") #Captura o caminho da pasta HOME

#Id do Switch onde esta o Firewall
ID_SWITCH = 1

#Porta que vai gerar o Packet_In
PORTA_Packet_In = 1234

#Contador PING
contador = 0



class MeuApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    def __init__(self, *args, **kwargs):
        super(MeuApp, self).__init__(*args, **kwargs)
    '''
    Instala regras na inicializacao
    '''
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def _switch_features_handler(self, ev):



        """Handle switch features reply to remove flow entries in table 0 and 1."""
        msg = ev.msg
        datapath = msg.datapath
        try:
            id_switch = datapath.id
            os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=40000,dl_type=0x0800,nw_proto=17,tp_dst='+str(PORTA_Packet_In)+',actions=output:controller')
            os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=40000,dl_type=0x0800,nw_proto=1,actions=output:controller')
            if id_switch == ID_SWITCH:
                #Regra: Somente cliente 2 acessa h8 e h9
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.2,nw_dst=10.0.0.8,tp_dst=23000,actions=output:6')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.2,nw_dst=10.0.0.9,tp_dst=23000,actions=output:6')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.8,tp_dst=23000,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.9,tp_dst=23000,actions=drop')
                #Regra: Somente cliente 3 acessa h6 e h7
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.3,nw_dst=10.0.0.6,tp_dst=23000,actions=output:5')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.3,nw_dst=10.0.0.7,tp_dst=23000,actions=output:5')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.6,tp_dst=23000,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.7,tp_dst=23000,actions=drop')
                #Regra: Somente cliente 1 acessa h4 e h5
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.1,nw_dst=10.0.0.4,tp_dst=23000,actions=output:4')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_src=10.0.0.1,nw_dst=10.0.0.5,tp_dst=23000,actions=output:4')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.4,tp_dst=23000,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=6,nw_dst=10.0.0.5,tp_dst=23000,actions=drop')

                #Bloquear o ping do cliente 3
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.4,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.5,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.6,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.7,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.8,actions=drop')
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=50005,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.3,nw_dst=10.0.0.9,actions=drop')

                #Elemento Desconhecido h10
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=60005,dl_type=0x0800,nw_src=10.0.0.10,actions=output:controller')

            else:
                os.system('python '+path_home+'/DCC075_Seguranca/Rotas_IoT.py s'+str(id_switch)) #Define as rotas dos elementos IoT "Rede Interna"

        except Exception as e:
            print(e)

    '''
    Area do Packet_In
    '''
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]

        #Tipos de pacotes
        pkt_ethernet = pkt.get_protocol(ethernet.ethernet)
        pkt_arp = pkt.get_protocol(arp.arp)
        pkt_icmp = pkt.get_protocol(icmp.icmp)
        pkt_ipv4 = pkt.get_protocol(ipv4.ipv4)
        pkt_udp = pkt.get_protocol(udp.udp)

        #Pacote ethernet
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            # ignore lldp packet
            #self.logger.info("Pacote LLDP")
            return
        if not pkt_ethernet:
            #self.logger.info("Pacote Nao Sei!!")
            return
        if pkt_icmp:
            if datapath.id == ID_SWITCH:
                if pkt_ipv4.src == '10.0.0.1':
                    global contador
                    print('Ping numero: '+str(contador+1))
                    contador = contador + 1
                    if contador == 10:
                        print("Numero de Ping Esgotado!!")
                        id_switch = datapath.id
                        os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=60000,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.1,nw_dst='+pkt_ipv4.dst+',idle_timeout=30,actions=drop')
                        contador = 0
        #Se for pacote ARP
        if pkt_arp:
            pass


        #Se for IPv4
        if pkt_ipv4:
            if pkt_ipv4.src == '10.0.0.10':
                print('ALERTA!!!\nElemento descohecido na rede!! IP: '+str(pkt_ipv4.src))

#APIs necessaria para funcionamento
app_manager.require_app('ryu.app.simple_switch_13_TrabalhoEdelberto')
