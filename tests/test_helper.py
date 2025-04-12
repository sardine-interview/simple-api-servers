import requests
import time
import subprocess
import atexit

class EchoServerTest:
    def __init__(self, server_type):
        self.server_type = server_type
        self.base_url = f"http://localhost"
        self.process = None
        
    def start_server(self, commands):
        print(f"Starting {self.server_type} server with commands: {commands}...")

        self.process = subprocess.Popen(commands)

        # Wait for server to start
        time.sleep(2)
        
        # Register cleanup
        atexit.register(self.stop_server)
        
    def stop_server(self):
        if self.process:
            print(f"Stopping {self.server_type} server...")
            self.process.terminate()
            self.process.wait()
            
    def test_echo(self, port):
        """Test the echo endpoint"""
        test_data = "Hello, World!"
        try:
            response = requests.post(f"{self.base_url}:{port}/echo", data=test_data)
            assert response.status_code == 200
            assert response.content == test_data.encode() if isinstance(test_data, str) else test_data
            return True
        except Exception as e:
            print(f"Error testing {self.server_type} server: {str(e)}")
            return False 