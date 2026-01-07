import subprocess
import sys
import os

def exp():
    
    command = ["bash", "-c", "id > /tmp/pwned"]
    subprocess.run(command,check=True)
if __name__ == "__main__":
    exp()
