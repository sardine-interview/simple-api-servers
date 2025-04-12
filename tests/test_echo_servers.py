import unittest
from test_helper import EchoServerTest

# in progress
class TestEchoServers(unittest.TestCase):  
    def test_go_server(self):
        server = EchoServerTest("go")
        server.start_server(["go", "run", "../go/main.go"])
        self.assertTrue(server.test_echo(8080))
        server.stop_server()
        
    def test_python_server(self):
        server = EchoServerTest("python")
        server.start_server(["fastapi", "dev", "../python/echo.py"])
        self.assertTrue(server.test_echo(8081))
        server.stop_server()
        
    def test_node_server(self):
        server = EchoServerTest("node")
        server.start_server(["node", "../node-js/echo.js"])
        self.assertTrue(server.test_echo(8000))
        server.stop_server()

if __name__ == '__main__':
    unittest.main() 