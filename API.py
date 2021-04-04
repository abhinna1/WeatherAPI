from tkinter import *
import requests




root = Tk()
root.geometry('300x250')
root.title('Weather Machine')
#root.resizable(0,0)
bg=Frame(bg='#FFFFFF')
bg.pack(expand=True,fill='both')



def btn_Click():

    ctname=city.get()
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
        weather=data['weather']

        location = Label(bg, text=f'Location: {ctname}', bg='#FFFFFF')
        tempOut = Label(bg, text=f'temperature: {temp_celceus}°C', anchor='se', bg='#FFFFFF')
        weatherout = Label(bg, text=(f"Weather : {weather[0]['description']}"), bg='#FFFFFF')

        location.pack()
        weatherout.pack()
        tempOut.pack()
    else:
        msg=Label(text='Enter Location',font=('Areal',22))
        msg.pack(bg)



    #Dialoge box to enter city name
city=Entry(bg)
city.pack()
search_btn=Button(bg,text='Check Weather',command=btn_Click)
search_btn.pack()



root.mainloop()