#Program to block particular websites during specified hours to increase productivity.
#Directs the specified URLs to local machine IP address during specified hours so that actual website does not get opened.

import time
from datetime import datetime as dt

hosts_temp=r"hosts"          # Path of the hosts file in windows
redirect="127.0.0.1"        # IP address of the localhost
website_list=["primevideo.com","www.primevideo.com"]    # List of sites to be blocked during working hours

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):  # Check if the current time falls within working hours
        print("Working hours")
        with open (hosts_temp,'r+') as file: 
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")   # Write the websites to be blocked and the localhost IP if that website is not present in the file.
    else:                                                         # Action to be performed after working hours: Check if the sites in the website_list variable are present in the hosts file. If yes, remove them
        with open (hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list): 
                    file.write(line)
            file.truncate()
            print("Fun hours")
    time.sleep(5)
