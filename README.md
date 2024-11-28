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


