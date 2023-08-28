from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import json
import time



# class Item(BaseModel):
#     hari: str | None = None
#     peristiwa: str | None = None
#     negara:str | None = None
#     keterangan: str | None = None
#     aktual: str | None = None
#     prakiraan: str | None = None
#     sebelumnya: str | None = None
#     dampak: str | None = None











options = Options()
options.add_experimental_option("debuggerAddress","localhost:9222")
service = ChromeService(executable_path='/home/yasashibp/Documents/ngoding/project/forexPph/env/chromedriver-linux64/chromedriver') 


driver = webdriver.Chrome(service=service,options=options)


elements = driver.find_elements(By.CSS_SELECTOR,'.economic-calendar__table-date') #hari
table = driver.find_elements(By.CSS_SELECTOR,'.economic_calendar__body.js_economic_calendar_body table.table-t03:nth-child(12) tbody.table-t03__tbody') #table pembungkus
tablePemb = driver.find_elements(By.CSS_SELECTOR,'economic_calendar__body.js_economic_calendar_body table')

indexStart = [2,4,6,8,10,12] #untuk def tablecont
indexTdnya = [1,4,5,6,7,8] #data tdnya #td3 yang diambil span.text


# urutan tablenya
def udin(j,k):
    tableTr = driver.find_elements(By.CSS_SELECTOR,f".table-t03__tbody td:nth-child({k})") #dampak
    return tableTr

def tableCont(k,j):
    table = driver.find_elements(By.CSS_SELECTOR,f".economic_calendar__body.js_economic_calendar_body table.table-t03:nth-child({k}) tbody.table-t03__tbody tr td:nth-child({j})")
    return table

def tableContTd(k):
    table = driver.find_elements(By.CSS_SELECTOR,f".economic_calendar__body.js_economic_calendar_body table.table-t03:nth-child({k}) tbody.table-t03__tbody tr td:nth-child(4) > span")
    return table


def reset():
    jsonD = 'data.json'
    with open(jsonD,'w') as files:
        files.write('[]')

def readJson():
    jsonD = 'data.json'
    with open(jsonD,'r') as file:
        dataForex=json.load(file)
    return dataForex




def runProg():

    for x in range(len(elements)): #hari
        hari = elements[x].text
        contTab = tableCont(indexStart[x],8)
        # data yang akan ada di json
        peristiwa = tableCont(indexStart[x],1)
        negara = tableCont(indexStart[x],3)
        keteranganTd = tableContTd(indexStart[x])
        aktual = tableCont(indexStart[x],5)
        prakiraan = tableCont(indexStart[x],6)
        sebelumnya = tableCont(indexStart[x],7)



        
        for z in range(len(contTab)):
            jsonD = 'data.json'
            dataForex = readJson()

            if contTab[z].text == 'Tinggi':

                newDataForex = {"hari":hari, "peristiwa":peristiwa[z].text, "negara":negara[z].text, "keterangan":keteranganTd[z].text,"aktual":aktual[z].text, "prakiraan":prakiraan[z].text, "sebelumnya":sebelumnya[z].text, "dampak":contTab[z].text}
                dataForex.append(newDataForex)
                with open(jsonD,'w') as files:
                    json.dump(dataForex,files,indent=4)
    return False



def gaSetiap10Detik():
    while True:
        print("Refreshing...")
        reset()
        time.sleep(5)
        runProg()
        time.sleep(10)



runProg()




# gaSetiap10Detik()
# @app.post("/udin")
# async def create_item(item: Item):
#     dataForex = []
#     with open(jsonD,'w') as files:
#         json.dump(dataForex,files,indent=4)
#     print("ada yang masuk nih")
#     return item
        
        # Tempatkan kode Anda yang ingin di-refresh di sini
        


# gaSetiap10Detik()






