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
import networkx as nx
#Sistema
import os
import requests
import pickle
#from classe import Classe

'''
Itens copiado do l3-qos-> Alexandre
'''
path_home = os.getenv("HOME") #Captura o caminho da pasta HOME

##### Porta do servidor
SERVER_PORT = 23000

##### Vazao maxima da rede (bps)
TX_MAX = 1000000000

#Ip de comunicacao com Controlador
IP_SERVER_QoS = '10.0.0.99'

#MAC do Controlador
MAC_SERVER_QoS = 'ff:ff:ff:00:00:00'

#Id do Switch onde esta os Servidores
ID_SWITCH = 3

#Porta que vai gerar o Packet_In
PORTA_Packet_In = 1234

#Mapeamento id em dpid
table_id = []

#Teste da Topologia
TABLE_MAC_SWITCH = []
#link_list = []

#Tabelas
TABELA_IP_SWITCH = [] #Mapea a saida do IP para cada switch
TABELA_MAC_SWITCH = [] #Mapea a saida de MAC para cada switch

#Arquivos
filename = path_home+'/ryu/Bruno/classes.conf'	#Arquivo de lista de objetos Classe
contador = 0



class MeuApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
    def __init__(self, *args, **kwargs):
        super(MeuApp, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.topology_api_app = self
        #self.net=nx.DiGraph()
        self.nodes = {}
        self.links = {}
        self.no_of_nodes = 0
        self.no_of_links = 0
        #self.contador = 0

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


        #Preenche as tabelas de IP e MAC
        #self.preencheTabelaIP(pkt)
        #self.preencheTabelaMAC(pkt)


        #Pacote ethernet
        if eth.ethertype == ether_types.ETH_TYPE_LLDP:
            # ignore lldp packet
            #self.logger.info("Pacote LLDP")
            return
        if not pkt_ethernet:
            #self.logger.info("Pacote Nao Sei!!")
            return
        if pkt_icmp:
            global contador
            print(contador)
            contador = contador + 1
            if contador == 20:
                print("Acabou o tempo!!")
                id_switch = datapath.id
                os.system('ovs-ofctl add-flow s' + str(id_switch) + ' priority=60000,dl_type=0x0800,nw_proto=1,nw_src=10.0.0.1,nw_dst=10.0.0.8,actions=drop')
                contador = 0
            #print(pkt_icmp)
            #print("Ping!!")
            #print(pkt_ipv4)


        #Se for pacote ARP
        if pkt_arp:
            pass


        #Se for IPv4
        if pkt_ipv4:
            pass

#app_manager.require_app('ryu.app.ofctl_rest')
app_manager.require_app('ryu.app.simple_switch_13_mod')
#app_manager.require_app('ryu.app.simple_switch_13')
#app_manager.require_app('ryu.app.rest_conf_switch')
#app_manager.require_app('ryu.app.rest_topology')
#app_manager.require_app('ryu.app.rest_qos_mod')
