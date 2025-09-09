#!/usr/bin/env python3
import platform
import os
import subprocess
import psutil
import time
from datetime import timedelta
from colorama import init, Fore, Style

# تهيئة الألوان
init(autoreset=True)

ASCII_LOGO = f"""
{Fore.RED}    /\\    
{Fore.RED}   /  \\   {Fore.CYAN}A{Fore.YELLOW}x
{Fore.RED}  / /\\ \\   
{Fore.RED} / ____ \\  
{Fore.RED}/_/    \\_\\ 
"""

def get_system_info():
    # OS info
    distro = platform.system() + " " + platform.release()
    
    # Kernel info
    kernel = platform.version()
    
    # Uptime
    uptime_seconds = psutil.boot_time()
    uptime = timedelta(seconds=int(time.time() - uptime_seconds))
    
    # CPU info
    cpu = platform.processor() or "Unknown CPU"
    
    # Memory info
    total_memory = round(psutil.virtual_memory().total / (1024 ** 2))  # MB
    
    # GPU info (Linux)
    try:
        gpu = subprocess.check_output(
            "lspci | grep -i 'vga\\|3d\\|2d'", shell=True
        ).decode().strip()
    except subprocess.CalledProcessError:
        gpu = "Unknown GPU"
    
    # Network info
    network = []
    for iface, addrs in psutil.net_io_counters(pernic=True).items():
        network.append((iface, addrs.bytes_recv, addrs.bytes_sent))
    
    # Package manager detection
    if os.path.exists("/usr/bin/pacman"):
        pkg_manager = "pacman"
    elif os.path.exists("/usr/bin/apt"):
        pkg_manager = "apt"
    elif os.path.exists("/usr/bin/dnf"):
        pkg_manager = "dnf"
    elif os.path.exists("/usr/bin/zypper"):
        pkg_manager = "zypper"
    else:
        pkg_manager = "unknown"
    
    return {
        "distro": distro,
        "kernel": kernel,
        "uptime": str(uptime),
        "cpu": cpu,
        "total_memory": total_memory,
        "gpu": gpu,
        "network": network,
        "package_manager": pkg_manager
    }

def display_info(info):
    print(ASCII_LOGO)
    print(f"{Fore.GREEN}=== System Info ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}Distro:{Style.RESET_ALL} {info['distro']}")
    print(f"{Fore.CYAN}Kernel:{Style.RESET_ALL} {info['kernel']}")
    print(f"{Fore.CYAN}Uptime:{Style.RESET_ALL} {info['uptime']}")
    print(f"{Fore.CYAN}CPU:{Style.RESET_ALL} {info['cpu']}")
    print(f"{Fore.CYAN}Total Memory:{Style.RESET_ALL} {info['total_memory']} MB")
    print(f"{Fore.CYAN}GPU:{Style.RESET_ALL} {info['gpu']}")
    print(f"{Fore.CYAN}Package Manager:{Style.RESET_ALL} {info['package_manager']}")
    print(f"{Fore.CYAN}Network Interfaces:{Style.RESET_ALL}")
    for iface, rx, tx in info['network']:
        print(f"  {iface}: RX {rx} bytes, TX {tx} bytes")

if __name__ == "__main__":
    info = get_system_info()
    display_info(info)
