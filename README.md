# netprober
# Subdomain Discovery Tool

This Python script is a simple subdomain discovery for a given domain. It retrieves subdomains that have a valid status code.
Saves the result of discovery directly in user's Desktop as "results_domain.txt"

## Features

- Subdomain discovery using requests module

## Prerequisites

- Python 3.x
- Required Python packages:
  - `os`
  - `requests`
  - `datetime` 
  - `time`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nomespaladin/netprober.git
    cd netprober
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script and enter a domain when prompted:
```sh
python netprober.py
```
Example of "wordlist" path ":
```
Windows : C:/<user_name>/Downloads/<name_of_file>.txt/.lst

Linux : /home/<user_name>/Downloads/<name_of_file>.txt/.lst

```

## Utils

One `subdomain.txt` wordlist  included inside:
```
netprober/wordlists/subdomains.txt
```

## Example Overview
```
╔════════════════════════════════════════════════════════════╗
║_____   __    _____________             ______              ║
║___  | / /______  /___  __ \_______________  /______________║
║__   |/ /_  _ \  __/_  /_/ /_  ___/  __ \_  __ \  _ \_  ___/║
║_  /|  / /  __/ /_ _  ____/_  /   / /_/ /  /_/ /  __/  /    ║
║/_/ |_/  \___/\__/ /_/     /_/    \____//_.___/\___//_/     ║
╚════════════════════════════════════════════════════════════╝
                                              By: NomesPaladin


Enter Wordlist full path:/home/admin/GitHub/netprober/wordlists/subdomains.txt
Enter domain:google.com
Program will proceed and will create a 'txt' file at your Desktop with the results.
Program Started [02/12/2024 17:06:54]
SUBDOMAIN FOUND >>> http://mail.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://m.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://mobile.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://calendar.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://apps.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://files.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://tv.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://jobs.example.com  ---------- Status : 200 
SUBDOMAIN FOUND >>> http://meet.example.com  ---------- Status : 200 
```
