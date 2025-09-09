#!/usr/bin/env python3
import platform
import psutil
import os
import subprocess
import time
from colorama import Fore, Style, init

init(autoreset=True)

def get_system_info():
    uname = platform.uname()
    info = {
        "distro": "",
        "kernel": uname.release,
        "uptime": "",
        "cpu": uname.processor,
        "memory": f"{round(psutil.virtual_memory().total / (1024*1024))} MB",
        "gpu": "",
        "package_manager": "",
        "network": ""
    }

    # Distro
    try:
        info["distro"] = subprocess.check_output(["uname", "-sr"]).decode().strip()
    except:
        info["distro"] = "Unknown"

    # Uptime
    uptime_seconds = psutil.boot_time()
    uptime_hours = int((time.time() - uptime_seconds) // 3600)
    uptime_minutes = int(((time.time() - uptime_seconds) % 3600) // 60)
    info["uptime"] = f"{uptime_hours}:{uptime_minutes:02d}"

    # GPU
    try:
        gpu_info = subprocess.check_output("lspci | grep VGA", shell=True).decode().strip()
        info["gpu"] = gpu_info
    except:
        info["gpu"] = "Unknown GPU"

    # Package manager
    for pm in ["pacman", "apt", "dnf", "zypper"]:
        if subprocess.call(f"command -v {pm}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            info["package_manager"] = pm
            break

    # Network
    net_io = psutil.net_io_counters(pernic=True)
    interfaces = []
    for iface, stats in net_io.items():
        interfaces.append(f"{iface}: RX {stats.bytes_recv} bytes, TX {stats.bytes_sent} bytes")
    info["network"] = "\n  ".join(interfaces)

    return info


def print_logo():
    logo = f"""
{Fore.CYAN}    /\\    
   /  \\   Ax
  / /\\ \\   
 / ____ \\  
/_/    \\_\\ {Style.RESET_ALL}
"""
    print(logo)


def main():
    info = get_system_info()
    print_logo()

    print("=== System Info ===")
    print(f"{Fore.CYAN}Distro:{Style.RESET_ALL} {info['distro']}")
    print(f"{Fore.CYAN}Kernel:{Style.RESET_ALL} {info['kernel']}")
    print(f"{Fore.CYAN}Uptime:{Style.RESET_ALL} {info['uptime']}")
    print(f"{Fore.CYAN}CPU:{Style.RESET_ALL} {info['cpu']}")
    print(f"{Fore.CYAN}Total Memory:{Style.RESET_ALL} {info['memory']}")
    print(f"{Fore.CYAN}GPU:{Style.RESET_ALL} {info['gpu']}")
    print(f"{Fore.CYAN}Package Manager:{Style.RESET_ALL} {info['package_manager']}")
    print(f"{Fore.CYAN}Network Interfaces:{Style.RESET_ALL}\n  {info['network']}")


if __name__ == "__main__":
    main()
