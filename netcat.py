import sys
import socket
import getopt
import threading
import subprocess

#kilka zmiennnych globalnych
listen=False
command=False
upload=False
execute=""
target=""
upload_destination = ""
port=0

def usage():
    print "NetCat na podstawie BlackHatPython"
    print
    print "Sposob uzycia: netcat.py -t target_host -p port"
    print "-l --listen      -nasluchuje na [host]:[port] polaczen przychodzacych"
    print "-e --execute=file_to_run -wykonuje dany plik, gdy odbierze polaczenie"
    print "-c --command     -inicjuje wiersz polecen"
    print "-u --upload=destination -gdy odbierze polaczenie,wysyla plik i zapisuje go w destination"
    print
    print
    print "Przyklady:"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -c"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -u=C:\\target.exe"
    print "netcap.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'sdjasbdkasd' | ./netcat.py -t 192.168.2.12 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in("-h","--help"):
            usage()
        elif o in("-l","--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port=int(a)
        else:
            assert False, "Nie obslugiwana opcja"

    if not listen and len(target) and port > 0:
        #blokada
        #uzyj ctrl+d
        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()


def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
        while True:
            #zwrot danych
            recv_len=1
            response=""

            while recv_len:
                data=client.recv(4096)
                recv_len=len(data)
                response+=data

                if recv_len<4096:
                    break
            print response,

            #wiecej danych
            buffer = raw_input("")
            buffer+="\n"
            #wyslanie danych
            client.send(buffer)
    except:
        print "[*] Wyjatek! Zamykanie."
        client.close()

if __name__=="__main__":
    main()