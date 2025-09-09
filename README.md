# ApexFetch 🖥️



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
```

### On Arch Linux
```bash
sudo pacman -Syu python python-pip --noconfirm
```

# Installation & Usage
```bash
cd apexfetch_py
```

# Create virtual environment
```bash
python3 -m venv venv --copies
source venv/bin/activate
```
# Upgrade pip and install psutil
```bash
pip install --upgrade pip
pip install psutil
```
# Copy apexfetch script to ~/bin
```bash
cp apexfetch.py ~/bin/apexfetch
```
# Add ~/bin to PATH
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
# Run ApexFetch
```bash
apexfetch
```

# Notes
This is an experimental version, it may contain bugs.

The official C version will be faster and more stable.

You can customize or modify the script as needed.
