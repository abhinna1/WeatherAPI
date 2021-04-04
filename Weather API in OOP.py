from tkinter import *
from tkinter import ttk
import requests


class API:

    def __init__(self, master):
        # Entry Box and Search Button
        self.AskCity = ttk.Entry(text='Weather API')
        self.AskCity.grid(row=0, column=0)
        self.SearchBtn = ttk.Button(text='Search Weather', command=self.btn_Click)
        self.SearchBtn.grid(row=1, column=0)

    def btn_Click(self):  # Function That Runs when search weather button is clicked
        self.key = '6b2efb27b43cb20d6c0b88c1c762b080'  # API Key
        self.location = self.AskCity.get()  # Location
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={self.key}'  # Weather URL
        self.response = requests.get(self.url)
        self.json = self.response.json()  # converts API data to JSON format
        self.main = self.json['main']  # enters the main section in the JSON file

        # Temperature
        self.temp_inKelvin = (self.main['temp'])  # stores temperature data from JSON file
        self.temp_inCelcius = (round(self.temp_inKelvin - 273.15))  # converts the kevlin data from API to Celcius
        self.temp_Label = ttk.Label(text=f'Temperaature: {self.temp_inCelcius}').grid(row=4,
                                                                                      column=0)  # Temprerature output label

        # humidity
        self.humidity = Label(text=f"humidity: {self.main['humidity']}").grid(row=6,
                                                                              column=0)  # Stores and outputs Humidity data from API

        # weather
        self.weather = self.json['weather']  # stores weather section
        self.weatherArray = self.weather[0]  # Weather data is stored in array so we access the first index of the array
        self.weather_Main = self.weatherArray['main']  # the main key contains the weather of location in the array
        self.weatherOut = Label(text=f"Weather: {self.weather_Main}").grid(row=2, column=0)  # Outputs the array


# main function
def main():
    root = Tk()  # creates window
    API(root)  # calling the API class inside the root I GUESS
    root.mainloop()  # GUI is a loop so mainloop function creates a loop for the GUI


if __name__ == "__main__":  # Not sure what this does
    main()