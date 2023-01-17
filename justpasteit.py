import random
from random import randint
import requests
import time

links = 0
while links < 1000:
    randomnumber = (randint(0,99999))
    link = "https://justpaste.it/"
    valid = link + str(randomnumber)
    
    print ("The number is: ", randomnumber)
    
    response = requests.get(valid, headers = {'User-agent': 'your bot 0.1'})
    
    print("Site: ", response.url)
    print("status: ", response.status_code)

    links = links + 1
    print("=========" + str(links) + "=========")

    if response.status_code == 200:
        file = open('200.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(4)
        pass
    if response.status_code == 404:
        file = open('400.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(4)
        pass

    if response.status_code == 451:
        file = open('451blocked.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(4)
        pass

    if response.status_code == 429:
        file = open('retry.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(120)
        print("Try again later!")
        pass      

    pass