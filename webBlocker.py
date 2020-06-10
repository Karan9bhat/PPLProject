import time

from datetime import datetime as dt

redirect = "127.0.0.1"
hostPath = r"/etc/hosts"
websites = ["www.youtube.com", "www.bing.com", "www.primevideo.com"]

while True :
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 18) :
        #print("Working hours...")
        #break
        with open(hostPath, 'r+') as file :
            content = file.read()
            for site in websites :
                if site in content :
                    pass
                else :
                    file.write(redirect + " " + site + "\n")
    else :
        with open(hostPath, 'r+') as file :
            content = file.readlines()
            file.seek(0)
            for line in content :
                if not any (site in line for site in websites) :
                    file.write(line)
                file.truncate()
    #print("Access Allowed")
time.sleep(5)
