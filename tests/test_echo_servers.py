import unittest
from test_helper import EchoServerTest

# in progress
class TestEchoServers(unittest.TestCase):  
    def test_go_server(self):
        server = EchoServerTest("go")
        server.start_server("./go", ["go", "run", "main.go"])
        self.assertEqual("", server.test_api("http://localhost:8080/api"), "go server should return no error")
        server.stop_server()
        
    def test_python_server(self):
        server = EchoServerTest("python")
        server.start_server("./python", ["fastapi", "dev", "api.py"])
        self.assertEqual("", server.test_api("http://localhost:8000/api"), "python server should return no error")
        server.stop_server()
    
    # this one is currently failing on test but if you run locally server works
    def test_node_server(self):
        server = EchoServerTest("node")
        server.start_server("./node-js", ["npm", "run", "start"])
        self.assertEqual("", server.test_api("http://localhost:3000/api"), "node server should return no error")
        server.stop_server()

if __name__ == '__main__':
    unittest.main() 