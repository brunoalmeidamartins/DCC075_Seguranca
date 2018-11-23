import os
import sys

if sys.argv[1] == 's2':
    #h4
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.4,nw_dst=10.0.0.6,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.4,nw_dst=10.0.0.7,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.4,nw_dst=10.0.0.8,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.4,nw_dst=10.0.0.9,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.4,nw_dst=10.0.0.10,actions=drop')
    #h5
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.6,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.7,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.8,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.9,actions=drop')
    os.system('ovs-ofctl add-flow s2 priority=60005,dl_type=0x0800,nw_src=10.0.0.5,nw_dst=10.0.0.10,actions=drop')
elif sys.argv[1] == 's3':
    #h6
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.6,nw_dst=10.0.0.4,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.6,nw_dst=10.0.0.5,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.6,nw_dst=10.0.0.8,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.6,nw_dst=10.0.0.9,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.6,nw_dst=10.0.0.10,actions=drop')
    #h7
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.7,nw_dst=10.0.0.4,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.7,nw_dst=10.0.0.5,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.7,nw_dst=10.0.0.8,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.7,nw_dst=10.0.0.9,actions=drop')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.7,nw_dst=10.0.0.10,actions=drop')
    #h10
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.4,actions=output:5')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.5,actions=output:5')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.6,actions=output:5')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.7,actions=output:5')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.8,actions=output:5')
    os.system('ovs-ofctl add-flow s3 priority=60005,dl_type=0x0800,nw_src=10.0.0.10,nw_dst=10.0.0.9,actions=output:5')
else:
    #h8
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.8,nw_dst=10.0.0.4,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.8,nw_dst=10.0.0.5,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.8,nw_dst=10.0.0.6,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.8,nw_dst=10.0.0.7,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.8,nw_dst=10.0.0.10,actions=drop')
    #h9
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.9,nw_dst=10.0.0.4,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.9,nw_dst=10.0.0.5,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.9,nw_dst=10.0.0.6,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.9,nw_dst=10.0.0.7,actions=drop')
    os.system('ovs-ofctl add-flow s4 priority=60005,dl_type=0x0800,nw_src=10.0.0.9,nw_dst=10.0.0.10,actions=drop')
