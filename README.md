# at-helper-py
Helper programm for managing modem


ppd command
pppd /dev/ttyUSB2 115200 noauth debug defaultroute noipdefault novj novjccomp noccp ipcp-accept-local ipcp-accept-remote local lock dump nodetach nocrtscts ipparam PPPE logfile /tmp/pppd.log ip-up-script /lib/netifd/ppp-up ip-down-script /lib/netifd/ppp-down
