__author__ = 'chris'

from SimpleXMLRPCServer import SimpleXMLRPCServer
from Spotify import Spotify


HOST, PORT = "localhost", 9999

server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)
server.register_instance(Spotify())
server.serve_forever()
