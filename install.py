import subprocess
import sys
import os

def exp():
    
    command = ["calc"]
    subprocess.run(command,check=True)
if __name__ == "__main__":
    exp()
