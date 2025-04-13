import requests
import time
import subprocess
import atexit

class EchoServerTest:
    def __init__(self, server_type):
        self.server_type = server_type
        self.process = None
        
    def start_server(self, dir, commands):
        print(f"Starting {self.server_type} server with commands: {commands}...")

        self.process = subprocess.Popen(commands, cwd=dir)

        # Wait for server to start
        time.sleep(2)
        
        # Register cleanup
        atexit.register(self.stop_server)
        
    def stop_server(self):
        if self.process:
            print(f"Stopping {self.server_type} server...")
            self.process.terminate()
            self.process.wait()
            
    def test_api(self, url):
        """Test the echo endpoint and return error message if any"""
        test_input = '{"name": "John"}'
        test_output = '{"message":"Hello John!"}'
        try:
            response = requests.post(url, data=test_input)
            if response.status_code != 200:
              return f"Error unexpected status code: {response.status_code} {response.text}"
            
            # Strip trailing whitespace and newlines from both expected and actual content
            actual_content = response.content.decode().strip()
            expected_content = test_output.strip()
            
            print(f"output from {self.server_type} server: {actual_content}")
            
            if actual_content != expected_content:
              return f"Error unexpected content: '{actual_content}' != '{expected_content}'"
            return ""
        except Exception as e:
            return f"Error testing {self.server_type} server: {str(e)}"
