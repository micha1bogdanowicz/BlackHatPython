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
    print "-l --listen      -nasłuchuje na [host]:[port] polaczen przychodzacych"
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