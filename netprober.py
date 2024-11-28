#import necessary modules

import requests
import time
import os
import datetime



print("""



╔════════════════════════════════════════════════════════════╗
║_____   __    _____________             ______              ║
║___  | / /______  /___  __ \_______________  /______________║
║__   |/ /_  _ \  __/_  /_/ /_  ___/  __ \_  __ \  _ \_  ___/║
║_  /|  / /  __/ /_ _  ____/_  /   / /_/ /  /_/ /  __/  /    ║
║/_/ |_/  \___/\__/ /_/     /_/    \____//_.___/\___//_/     ║
╚════════════════════════════════════════════════════════════╝
                                              By: NomesPaladin

""")

#user inputs 
w_path = input("Enter Wordlist full path:")
domain = input("Enter domain:")
#get username of system and create a full path to user's desktop
user_path = os.getlogin()
desktop_path = f"/home/{user_path}/Desktop"


#function to process the words in the wordlist file given by user
def read_wordlist(w_path):
    subdomains_list = []
    try:
        with open(w_path,"r") as file:
            for subdomain in file:
                subdomain = subdomain.strip()
                subdomains_list.append(subdomain)
    except FileNotFoundError:
        print(f"FILE|{w_path}| DOES NOT EXIST ")
        pass
    return subdomains_list

content = read_wordlist(w_path)


now = datetime.datetime.now()#gets actual datetime

time.sleep(2)
print("Program will proceed and will create a 'txt' file at your Desktop with the results.")
time.sleep(0.5)
print(f"Program Started [{(now.strftime("%d/%m/%Y %H:%M:%S"))}]")#prints the readable format of actual datetime
time.sleep(0.5)

#main funtion to process the values on the worlists and save them on a file at the desktop if they exist
def subdomain_finder(content, domain,desktop_path):
    os.chdir(desktop_path)
   
    
    for cont in content:
            #time.sleep(0.001)
            url = f"http://{cont}.{domain}"
            try:
                response = requests.get(url, timeout=0.1)  # Set a timeout for requests
                response.raise_for_status()  # Raise an exception for error HTTP statuses
                print(f"SUBDOMAIN FOUND >>> {url}  ---------- Status : {response.status_code} ")

                with open(f'results_{domain}','a') as file:
                    file.write(f"SUBDOMAIN FOUND >>> {url}\n")
            except requests.exceptions.RequestException as e:
                #print(f"ERROR FETCHING >>> {url}")
                pass
                # You might want to log the error or take other actions here
                continue
                    

subdomain_finder(content,domain,desktop_path)


