from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import json
import time
import requests
import math

dari = 1926
ke = 1940



options = Options()
options.add_experimental_option("debuggerAddress","localhost:9222")
service = ChromeService(executable_path='/home/yasashibp/Documents/ngoding/project/forexPph/env/chromedriver-linux64/chromedriver') 


driver = webdriver.Chrome(service=service,options=options)


element = driver.find_element(By.CSS_SELECTOR,'div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last') #hari



jsonLocate = '/home/yasashibp/Documents/ngoding/project/forexPph/env/data.json'


url = f"https://alertzy.app/send?accountKey=pzkwtjiipuyx981&title=Notif+Saham&message={element.text}"

# Define the headers (optional)
headers = {"Content-Type": "application/json"}

# Define the request payload (if sending JSON data)
data = {
    "accountKey":'pzkwtjiipuyx981',
    "title": "Notif Saham",
    "message": f"Ini Harganya {element.text}",
    "group":"testing"
}

def StrtoInt():
    jumlahAngka = element.text
    try:
        return int(jumlahAngka)
    except:
        return float(jumlahAngka)
    

def sendNotif():
    time.sleep(0.2)
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code)
        print("Response:", response.text)
    time.sleep(0.2)


def runProg():
    jumlahAngka = math.floor(StrtoInt())
    print(jumlahAngka >= dari and jumlahAngka <= ke)
    with open(jsonLocate,'r') as file:
        dataHarga=json.load(file)['harga']
    if dataHarga != jumlahAngka:
        if jumlahAngka >= dari and jumlahAngka <= ke :
            dataHarga = {"harga":jumlahAngka}
            sendNotif()
            with open(jsonLocate,'w') as files:
                json.dump(dataHarga,files,indent=4)
            print(f"angkanya beda {dataHarga}")
        else:
            print('angkanya masih sama saja')
    else:
        print(f"angkanya sama {dataHarga}")

runProg()

    

    




    
