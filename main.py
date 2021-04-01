from tkinter import *
import requests

def exit():
    global root
    root.quit()
def searcher(cityname):
    pass


root = Tk()
root.geometry('200x250')
root.resizable(0,0)


search = Entry(root)
city=search.get()
search.pack()

search_btn= Button(text='Search')
search_btn.pack()
x=1

if len(city)!=0:
    #------------------URL CREATION-----------------
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "6b2efb27b43cb20d6c0b88c1c762b080"
    URL = BASE_URL + "q=" + search + "&appid=" + API_KEY
    print(URL)
    response=requests.get(URL)
    data=response.json()
    main=data['main']
    temp=main['temp']


#---------------BackEnd Variables---------------------
weather_print = Label(text=f'Weather:')
#weather_pic=bitmap('') #image

#temperature = Label(text=f'Temperature:{temp}')


#temperature.pack()


exit = Button(text='Exit',command=exit)
exit.pack()

root.mainloop()
