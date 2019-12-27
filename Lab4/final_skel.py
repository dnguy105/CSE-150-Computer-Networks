#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class final_topo(Topo):
  def build(self):

    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
    # h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='1.1.1.1/24', defaultRoute="h1-eth0")
    # h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='2.2.2.2/24', defaultRoute="h2-eth0")

    # Create a switch. No changes here from Lab 1.
    # s1 = self.addSwitch('s1')

    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    #
    # IMPORTANT NOTES: 
    # - On a single device, you can only use each port once! So, on s1, only 1 device can be
    #   plugged in to port 1, only one device can be plugged in to port 2, etc.
    # - On the "host" side of connections, you must make sure to always match the port you 
    #   set as the default route when you created the device above. Usually, this means you 
    #   should plug in to port 0 (since you set the default route to h#-eth0).
    #
    # self.addLink(s1,h1, port1=8, port2=0)
    # self.addLink(s1,h2, port1=9, port2=0)

	switch1 = self.addSwitch('s1')    ## Adds a Switch
	switch2 = self.addSwitch('s2')    ## Adds a Switch
	switch3 = self.addSwitch('s3')    ## Adds a Switch
	switch4 = self.addSwitch('s4')    ## Adds a Switch
	switch5 = self.addSwitch('s5')    ## Adds a Switch

    host1 =self.addHost('h1', mac='00:00:00:00:00:01',ip='10.1.1.10/24', defaultRoute="h1-eth0")       ## Adds a Host
    host2 =self.addHost('h2',mac='00:00:00:00:00:02',ip='10.2.2.20/24', defaultRoute="h2-eth0")       ## Adds a Host
    host3 =self.addHost('h3',mac='00:00:00:00:00:03',ip='10.3.3.30/24', defaultRoute="h3-eth0")       ## Adds a Host
    host4 =self.addHost('h4',mac='00:00:00:00:00:04',ip='123.45.67.89/24', defaultRoute="h4-eth0")       ## Adds a Host
	host5 =self.addHost('h5',mac='00:00:00:00:00:05',ip='10.5.5.50/24', defaultRoute="h5-eth0")       ## Adds a Host

    self.addLink(host1, switch1, port1=0, port2=1)      ## Add a link
    self.addLink(host2, switch2, port1=0, port2=1)      ## Add a link
    self.addLink(host3, switch3, port1=0, port2=1)      ## Add a link
    self.addLink(host4, switch4, port1=0, port2=1)      ## Add a link
	self.addLink(host5, switch5, port1=0, port2=1)      ## Add a link


	self.addLink(switch1, switch4, port1=2, port2=2)      ## Add a link
	self.addLink(switch2, switch4, port1=2, port2=3)      ## Add a link
	self.addLink(switch3, switch4, port1=2, port2=4)      ## Add a link
	self.addLink(switch5, switch4, port1=2, port2=5)      ## Add a link





    print "Delete me!"

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, controller=RemoteController)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
