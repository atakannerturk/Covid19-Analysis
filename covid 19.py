import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *

def getStats(country):
    api_url = 'https://api.smartable.ai/coronavirus/stats/'+country
    api_params = {
        'Cache-Control': 'no-cache',
        'Subscription-Key': '***********************',
    }
    r = requests.get(url=api_url, params=api_params) 
    return r.text
def data():    
    ulkekodu = box.get()
    data = getStats(ulkekodu)
    jsonData = json.loads(data)
        
    if 'location' in jsonData.keys():
        country = jsonData['location']['countryOrRegion']
        history = pd.DataFrame(jsonData['stats']['history'])
        history['date']=pd.to_datetime(history['date'])
        history.plot(figsize=(10,15), x='date', title=country, subplots=True, grid=True)
        plt.show()         
    else:
        print("HATA")
        if 'message' in jsonData.keys():
            print(jsonData['message'])
def data2():
    
    ulkekodu = box.get()
    data = getStats(ulkekodu)
    jsonData = json.loads(data)  
    history = pd.DataFrame(jsonData['stats']['history'])
    history['ddeaths']=history['deaths'].pct_change()*100
    partialhistory = history[40:70]
    partialhistory.plot(x='date',y='ddeaths',figsize=(10,5))
    plt.show()

    
window = Tk()
window.title("Ülke Bazlı Covid 19 Verileri")
window.geometry("500x250")
description = Label(window, text="Verisine bakmak istediğiniz ülkenin kodunu giriniz (ES,GB,BR,AZ,DE,TR ,vb.): ").pack()
box = Entry(window)
box.pack()
buton = Button(window)
buton.config(text = "Vaka Sayısı,Ölüm Sayısı,İyileşen Sayısı Grafikleri",command = data)
buton.pack()
buton = Button(window)
buton.config(text = " Toplam Ölüm Sayısının Yüzdesel Grafiği",command = data2)
buton.pack()
exitButton = Button(window,text = "Çıkış",command = window.destroy).pack()
window.mainloop()

  
        
