__author__ = 'chris'

import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://192.168.178.33:9999")
# proxy.openUri('spotify:track:3cQGb2POE359G9WH81bF60')
proxy.getVolume()
