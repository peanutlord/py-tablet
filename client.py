__author__ = 'chris'

import xmlrpclib

# Test File

proxy = xmlrpclib.ServerProxy("http://localhost:9999")
# proxy.openUri('spotify:track:3cQGb2POE359G9WH81bF60')
proxy.getVolume()
