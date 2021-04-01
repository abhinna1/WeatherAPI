from tkinter import *
import requests

root = Tk()
root.geometry('300x250')
root.title('Weather Machine')
root.resizable(0,0)
bg=Frame()
bg.pack(expand=True,fill='both')


def btn_Click():
    ctname=city.get()
    print(ctname)
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "6b2efb27b43cb20d6c0b88c1c762b080"
    if len(ctname)!=0:
        URL = (BASE_URL +"q="+ctname+"&appid="+API_KEY)
        print(URL)
        response = requests.get(URL)
        data = response.json()
        main = data['main']
        temp = main['temp']
        temp_celceus=round(temp - 273.15)
        report=data['weather']
        location= Label(bg,text=ctname)
        tempOut = Label(bg,text=f'temperature:{temp_celceus}C',anchor='se')
        weatherout=Label(bg,text=(f"Weather : {report[0]['description']}"))
        weatherout.pack()
        location.pack()

        tempOut.pack()



    #Dialoge box to enter city name
city=Entry(bg)
city.pack()
search_btn=Button(bg,text='Search',command=btn_Click)
search_btn.pack()



root.mainloop()