# pip install pywin32
# pip install pypiwin32

import ctypes
import os
import sys
import time
from win32com.client import GetObject


os.system("cls")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def disable_win_update():
    os.system("cls")
    print("Disabling Windows Update...")
    os.system("net stop wuauserv")
    os.system("sc config wuauserv start= disabled")


def enable_win_update():
    os.system("cls")
    print("Activating Windows Update...")
    os.system("sc config wuauserv start= auto")
    os.system("net start wuauserv")
    
def activate_win():
    os.system("cls")
    print("--- Windows Activator ---")
    
    wim = GetObject('winmgmts:')
    windows_detected = ([o.Caption for o in wim.ExecQuery("Select * from Win32_OperatingSystem")][0])

    if windows_detected == 'Microsoft Windows 10 Home':
        serial_key = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
    elif windows_detected == 'Microsoft Windows 10 Home N':
        serial_key = '3KHY7-WNT83-DGQKR-F7HPR-844BM'
    elif windows_detected == 'Microsoft Windows 10 Pro':
        serial_key = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    elif windows_detected == 'Microsoft Windows 10 Professional':
        serial_key = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    elif windows_detected == 'Microsoft Windows 10 Professional N':
        serial_key = 'MH37W-N47XK-V7XM9-C7227-GCQG9'
    elif windows_detected == 'Microsoft Windows 10 Education':
        serial_key = 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'
    elif windows_detected == 'Microsoft Windows 10 Education N':
        serial_key = '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ'
    elif windows_detected == 'Microsoft Windows 10 Enterprise':
        serial_key = 'NPPR9-FWDCX-D2C8J-H872K-2YT43'
    elif windows_detected == 'Microsoft Windows 10 Enterprise N':
        serial_key = 'WGGHN-J84D6-QYCPR-T7PJ7-X766F'
    else:
        serial_key = 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
    
    print("--- Windows Activator ---")
    print(windows_detected)

    print("\nActivating Windows...\n")

    time.sleep(1)
    print('Serial key: ' + serial_key)
    os.system("slmgr //b /ipk " + serial_key)
    os.system("slmgr //b /skms kms8.msguides.com")
    os.system("slmgr /ato")

    print("\nWindows Activated!")
    print("\nPlease restart you computer")
    
    
def deactivate_win():
    os.system("slmgr.vbs /upk")
    print("\nWindows deactivated!")
    print("\nPlease restart you computer")
    
    
def disable_telemetry():
    os.system("cls")
    print("Disabling Windows Telemetry and Diagnostics...")
    #os.system("net stop DiagTrack ")
    #os.system("net stop dmwappushservice")
    os.system("sc config dmwappushservice start= disabled")
    os.system("sc config DiagTrack start= disabled")
    

def enable_telemetry():
    os.system("cls")
    print("Enabling Windows Telemetry and Diagnostics...")
    #os.system("net start DiagTrack ")
    #os.system("net start dmwappushservice")
    os.system("sc config dmwappushservice start= auto")
    os.system("sc config DiagTrack start= auto")


if is_admin():

    # ask for file name
    while True:
        option = ""
        try:
            print('https://github.com/diogomcasado\n')
            print("--- Windows Tools ---")
            print("\n1- Disable Windows update")
            print("2- Activate Windows update")
            print("3- Activate Windows license (KMS)")
            print("4- Remove Windows license")
            print("5- Disable Windows telemetry and diagnostics")
            print("6- Enable Windows telemetry and diagnostics\n")
            option = input("Select an option: ")

        finally:
            if option == "1":
                disable_win_update()
            elif option == "2":
                enable_win_update()
            elif option == "3":
                activate_win()
            elif option == "4":
                deactivate_win()
            elif option == "5":
                disable_telemetry()
            elif option == "6":
                enable_telemetry()
            else:
                print("Invalid option")
            break

    print("Press Enter Key to close.")
    input()


else:
    # Re-run the program with admin rights
    print("Trying to run as an admin")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
