# ApexFetch 🖥️

/\    
/ \ Ax
/ /\ \
/ ____ \
/_/ _\







ApexFetch is a tool similar to **Neofetch**, developed by **Linuxawy**.  
It was programmed specifically for a certain person named encrypted **A...** 🕵️‍♂️  

> ⚠️ This project is **experimental**. The current version is written in **Python**, and an official **C version** will be released later.

---

## Requirements

1. **Python 3** installed on your system.
2. **pip** package manager.
3. Linux or any system supporting **bash**.

---

## Installing Python and pip

### On **Ubuntu / Debian**
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y

### On Arch Linux

sudo pacman -Syu python python-pip --noconfirm


# Installation & Usage

# Create virtual environment
python3 -m venv venv --copies
source venv/bin/activate

# Upgrade pip and install psutil
pip install --upgrade pip
pip install psutil

# Copy apexfetch script to ~/bin
cp apexfetch.py ~/bin/apexfetch

# Add ~/bin to PATH
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Run ApexFetch
apexfetch


# Notes
This is an experimental version, it may contain bugs.

The official C version will be faster and more stable.

You can customize or modify the script as needed.
