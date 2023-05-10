import subprocess

def start_terminal(command):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

def main():
    start_terminal("python3 tcpService.py")
    start_terminal("python3 blueService.py")

if __name__ == '__main__':
    main()
