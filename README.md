# ApexFetch 🖥️



ApexFetch is a tool similar to **Neofetch**, developed by **Linuxawy**.  
It was programmed specifically for a certain person named encrypted **A...** 🕵️‍♂️  

---

## Requirements

1. **Python 3** installed on your system.
2. **pip** package manager.
3. Linux or any system supporting **bash**.

---

# installing:
```bash
git clone https://github.com/malekhussein/apexfetch.git
cd apexfetch/
```

```bash
python3 -m venv --copies venv
# if Bash
source venv/bin/activate

source venv/bin/activate.fish
pip install --upgrade pip
pip install psutil colorama
```
```bash
mkdir -p ~/bin
cp apexfetch.py ~/bin/apexfetch
chmod +x ~/bin/apexfetch
```
```bash
set -U fish_user_paths $HOME/bin $fish_user_paths
```
```bash
apexfetch
```


# Notes
This is an experimental version, it may contain bugs.

The official C++ version will be faster and more stable.

You can customize or modify the script as needed.
