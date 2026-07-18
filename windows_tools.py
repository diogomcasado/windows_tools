# pip install pywin32
# pip install pypiwin32

import ctypes
import os
import shutil
import sys
import time
from win32com.client import GetObject
import windows_tools.product_key as product_key
import windows_tools.bitness as bitness
import windows_tools.server as server
import windows_tools.bitlocker as bitlocker
import windows_tools.windows_firewall as windows_firewall


os.system("cls")


# Product key per Windows edition (works for both Windows 10 and 11).
WINDOWS_PRODUCT_KEYS = {
    'Home': 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
    'Home N': '3KHY7-WNT83-DGQKR-F7HPR-844BM',
    'Pro': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
    'Professional': 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
    'Professional N': 'MH37W-N47XK-V7XM9-C7227-GCQG9',
    'Education': 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
    'Education N': '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
    'Enterprise': 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
    'Enterprise N': 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
}


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def get_windows_caption():
    wim = GetObject('winmgmts:')
    return [o.Caption for o in wim.ExecQuery(
        "Select * from Win32_OperatingSystem")][0]


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

    windows_detected = get_windows_caption()

    edition = (windows_detected
               .replace('Microsoft Windows 10 ', '')
               .replace('Microsoft Windows 11 ', ''))
    serial_key = WINDOWS_PRODUCT_KEYS.get(edition)

    if serial_key is None:
        print("\nError: invalid version\n")
        return


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


def run_system_file_checker():
    os.system("cls")
    print("Running System File Checker...")
    os.system("sfc /scannow")


def run_CHKDSK():
    os.system("cls")
    print("Running CHKDSK...")
    os.system("chkdsk /f /r")


def run_disk_cleanup():
    os.system("cls")
    print("Running Disk Cleanup...")
    os.system("cleanmgr")


def clear_temp_folders():
    os.system("cls")
    print("Clearing temporary files...")

    temp_dirs = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        r'C:\Windows\Temp',
    ]

    seen = set()
    deleted = 0
    for temp_dir in temp_dirs:
        if not temp_dir:
            continue
        temp_dir = os.path.normpath(temp_dir)
        if temp_dir in seen or not os.path.isdir(temp_dir):
            continue
        seen.add(temp_dir)

        print("Cleaning: " + temp_dir)
        for entry in os.listdir(temp_dir):
            path = os.path.join(temp_dir, entry)
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)
                    deleted += 1
                elif os.path.isdir(path):
                    shutil.rmtree(path, ignore_errors=True)
                    deleted += 1
            except (PermissionError, OSError):
                # File or folder in use — skip it.
                pass

    print("\nDone. Removed {} items (files in use were skipped).".format(deleted))


def flush_dns_reset_network():
    os.system("cls")
    print("Flushing DNS and resetting network...")
    os.system("ipconfig /flushdns")
    os.system("netsh winsock reset")
    os.system("netsh int ip reset")
    print("\nDone. Please restart your computer for the reset to take full effect.")



if is_admin():
    while True:
        bit64 = ""

        print('https://github.com/diogomcasado\n')

        print("---- Windows Info ----")
        print("")
        print(os.environ['COMPUTERNAME'])
        print(os.environ['USERNAME'])
        print(os.environ['PROCESSOR_ARCHITECTURE'], os.environ['NUMBER_OF_PROCESSORS'], "cores")

        try:
            if bitness.is_64bit():
                bit64 = "64-bit"
            else:
                bit64 = "32-bit"
        except Exception:
            bit64 = "??-bit"

        print(get_windows_caption(), bit64)

        try:
            print("Current Windows Serial Key: ",
                  product_key.get_windows_product_key_from_reg())
        except Exception:
            print("Current Windows Serial Key: Not detected")

        try:
            print("Server: ", server.get_windows_version())
        except Exception:
            pass

        try:
            if windows_firewall.is_firewall_active():
                print("Firewall: Active")
            else:
                print("Firewall: Inactive")
        except Exception:
            print("Firewall: Not detected")

        print()

        print("\n---- Windows Tools ----")
        print("\n1- Disable Windows update")
        print("2- Activate Windows update")
        print("3- Activate Windows license (KMS)")
        print("4- Remove Windows license")
        print("5- Disable Windows telemetry and diagnostics")
        print("6- Enable Windows telemetry and diagnostics")
        print("7- Repair missing or corrupted system files (SFC.exe)")
        print("8- Disk error checking (CHKDSK)")
        print("9- Disk cleanup (CLEANMGR)")
        print("10- Clear temporary files")
        print("11- Flush DNS and reset network")
        print("0- Exit\n")
        option = input("Select an option: ")

        if option == "0":
            break
        elif option == "1":
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
        elif option == "7":
            run_system_file_checker()
        elif option == "8":
            run_CHKDSK()
        elif option == "9":
            run_disk_cleanup()
        elif option == "10":
            clear_temp_folders()
        elif option == "11":
            flush_dns_reset_network()
        else:
            print("Invalid option")

        print("\nPress Enter Key to continue.")
        input()
        os.system("cls")


else:
    # Re-run the program with admin rights
    print("Trying to run as an admin")
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
