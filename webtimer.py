from termcolor import *
from time import strftime
import requests, colorama

cprint("Confused? Dropoff ID is upload file input on your Domain; Not the button", "red")

Domain = input("Dropoff Domain: "); released=0
Package = input("Package (file path): ")
Time = input("Time to release: ")
try:
    cprint("You can interrupt the process by pressing Ctrl + C; or ^C", "blue")
    cprint("Server is now running; waiting until: "+str(Time), "green")

    while released == 0:
        if(strftime("%H:%M")>=Time):
            released = 1
            cprint("RELEASING PACKAGE ("+Package+") TO DOMAIN: "+Domain, "green")
            File = open(Package)
            releaseinfo = requests.post(Domain, Package = File)
            cprint(releaseinfo, "red")
            
except:
    cprint("Stopped service or invalid inputs","red")