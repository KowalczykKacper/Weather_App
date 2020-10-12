import requests
from bs4 import BeautifulSoup
import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox

root = tkinter.Tk()
root.title('Weather App')
root.iconbitmap('weather.ico')
root.geometry('360x250+500+350')

#Images
clear_img = ImageTk.PhotoImage(Image.open("images/clear_night.svg"))
cloudy_img = ImageTk.PhotoImage(Image.open("images/cloudy.svg"))
partly_cloudy_img = ImageTk.PhotoImage(Image.open("images/partly_cloudy.svg"))
heavy_thunder_img = ImageTk.PhotoImage(Image.open("images/heavy_thunder.svg"))
light_thunder_img = ImageTk.PhotoImage(Image.open("images/light_thunder.svg"))
rain_img = ImageTk.PhotoImage(Image.open("images/rain.svg"))
rain_sun_img = ImageTk.PhotoImage(Image.open("images/rain_sun.svg"))
snow_img = ImageTk.PhotoImage(Image.open("images/snow.svg"))
sunny_img = ImageTk.PhotoImage(Image.open("images/sunny.svg"))
windy_img = ImageTk.PhotoImage(Image.open("images/wind.svg"))

countries_url = 'https://www.latlong.net/countries.html'
cities_url = ''
weather_url = ''

countries_r = requests.get(countries_url)
countries_page = BeautifulSoup(countries_r.content, 'html.parser')
countries_page_links = countries_page.ul

countries_name_list = []
countries_href_num = []
cities_name_list = []


number_of_countries = len(countries_page_links.findAll("a"))
for i in range(number_of_countries):
    countries_name_list.append(countries_page_links.findAll("a")[i]["title"])
    help = countries_page_links.findAll("a")[i]["href"].rsplit('.')[0].rsplit('-')
    countries_href_num.append(help[len(help) - 1])

countries_name_list.sort()
country_lbl = tkinter.Label(root)
city_lbl = tkinter.Label(root)

def submit_country():
    cities_name_list = []

    def show_weather():
        weather_window = tkinter.Toplevel()
        weather_window.title('Weather Report')
        weather_window.iconbitmap('weather.ico')
        weather_window.geometry('530x655+1000+200')
        isDay = True
        if current_time != "Problems while getting the actual Time":
            time_help = current_time.rsplit(' ')
            time_hour = time_help[0].rsplit(':')[0]
            time_min = time_help[0].rsplit(':')[1]
            time_ampm = time_help[1]
            if time_ampm == 'pm':
                time_hour = int(time_hour) + 12

            if int(time_hour) >= 6 and int(time_hour) <= 19:
                isDay = True
            if int(time_hour) >= 20 or int(time_hour) <= 5:
                isDay = False

        background = '#ffffff'
        if (isDay==False and (current_conditions == 'Clear' or current_conditions == 'Mostly Clear' or current_conditions == 'Fair' or current_conditions == 'Partly Cloudy' or current_conditions == 'AM Clouds/PM Sun')):
            background = '#406487'
            tkinter.Label(weather_window, bg=background, image=clear_img).grid(row=0, column=0, columnspan=3)
        if (isDay==True and (current_conditions == 'Clear' or current_conditions == 'Mostly Clear' or current_conditions == 'Fair')):
            background = '#22a9ff'
            tkinter.Label(weather_window, bg=background, image=sunny_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Sunny' or current_conditions == 'Mostly Sunny'):
            background = '#22a9ff'
            tkinter.Label(weather_window, bg=background, image=sunny_img).grid(row=0, column=0, columnspan=3)
        if (isDay == True and (current_conditions == 'Partly Cloudy' or current_conditions == 'AM Clouds/PM Sun')):
            background = '#00c8ff'
            tkinter.Label(weather_window, bg=background, image=partly_cloudy_img).grid(row=0, column=0, columnspan=3)
        if (isDay == False and (current_conditions == 'Cloudy' or current_conditions == 'Mostly Cloudy')):
            background = '#406487'
            tkinter.Label(weather_window, bg=background, image=cloudy_img).grid(row=0, column=0, columnspan=3)
        if (isDay == True and (current_conditions == 'Cloudy' or current_conditions == 'Mostly Cloudy')):
            background = '#00c8ff'
            tkinter.Label(weather_window, bg=background, image=cloudy_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'AM Showers' or current_conditions == 'AM Rain' or current_conditions == 'Showers' or current_conditions == 'PM Rain' or current_conditions == 'PM Showers' or current_conditions == 'Rain'):
            background = '#006dc3'
            tkinter.Label(weather_window, bg=background, image=rain_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Light Rain'):
            background = '#00dcff'
            tkinter.Label(weather_window, bg=background, image=rain_sun_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Scattered Thunderstorms' or current_conditions == 'Isolated Thunderstorms' or current_conditions == 'AM Thunderstorms' or current_conditions == 'PM Thunderstorms'):
            background = '#405a87'
            tkinter.Label(weather_window, bg=background, image=light_thunder_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Thunderstorms' or current_conditions == 'Haze'):
            background = '#003c5a'
            tkinter.Label(weather_window, bg=background, image=heavy_thunder_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Snowing' or current_conditions == 'Snowy' or current_conditions == 'Snow'):
            background = '#ffffff'
            tkinter.Label(weather_window, bg=background, image=snow_img).grid(row=0, column=0, columnspan=3)
        if (current_conditions == 'Winds' or current_conditions == 'Windy' or current_conditions == 'Fog'):
            background = '#dcdbdf'
            tkinter.Label(weather_window, bg=background, image=windy_img).grid(row=0, column=0, columnspan=3)

        weather_window.configure(bg=background)
        tkinter.Label(weather_window, bg=background, text=current_temp, font=("Helvetica",32)).grid(row=1, column=0, rowspan=2)
        tkinter.Label(weather_window, bg=background, text=current_conditions, font=("Helvetica",16)).grid(row=1, column=1)
        tkinter.Label(weather_window, bg=background, text='Air Quality', font=("Helvetica", 16)).grid(row=1, column=2)
        tkinter.Label(weather_window, bg=background, text=air_quality, font=("Helvetica", 16)).grid(row=2, column=2)
        tkinter.Label(weather_window, bg=background, text=rain_chance, font=("Helvetica",16)).grid(row=2, column=1, padx=20)
        tkinter.Label(weather_window, bg=background, text=current_time, font=("Helvetica", 16)).grid(row=3, column=0, columnspan=3,  padx=20)

        exit_txt = 'Exit Weather Report for : ' + str(chosen_city) + ', ' + str(chosen_country)
        if len(exit_txt) > 55:
            Quit_weather_btn = tkinter.Button(weather_window, bg=background, width=50,font=("Helvetica", 12), text=exit_txt, command=weather_window.destroy)
        else:
            Quit_weather_btn = tkinter.Button(weather_window, bg=background, width=40, font=("Helvetica", 16), text=exit_txt, command=weather_window.destroy)
        Quit_weather_btn.grid(row=4, column=0, columnspan=3)

    def submit_city():
        global current_temp
        global current_conditions
        global rain_chance
        global air_quality
        global current_time
        global chosen_city
        y = city_entry.get()
        wrong_city = True
        global city_lbl
        for j in range(number_of_cities):
            if y == cities_name_list[j]:
                wrong_city = False
                chosen_city = y
                city_lbl.destroy()
                city_lbl = tkinter.Label(root, text='You chose : ' + str(chosen_city))
                city_lbl.grid(row=3, column=0, columnspan=3)
                latitude = cities_page.table.findAll("td")[3*j+1].text
                longtitude = cities_page.table.findAll("td")[3*j+2].text
                weather_url = 'https://weather.com/weather/today/l/' + str(latitude) + ',' + str(longtitude) + '?par=google&temp=c'
                weather_r = requests.get(weather_url)
                weather_page = BeautifulSoup(weather_r.content, 'html.parser')
                weather_btn = tkinter.Button(root, text='Weather Report', command=show_weather)
                weather_btn.grid(row=4, column=0, columnspan=3, padx=10, ipady=20,ipadx=60)
                quit_btn = tkinter.Button(root, text='Quit Weather App', command=root.destroy)
                quit_btn.grid(row=5, column=0, columnspan=3, padx=10, pady=5, ipady=20, ipadx=60)
                current_temp = weather_page.body.findAll("span", {'data-testid': 'TemperatureValue'})[0].text
                current_conditions = weather_page.body.findAll("div", {'data-testid': 'wxPhrase'})[0].text
                air_quality = weather_page.body.findAll("span", {'data-testid': 'AirQualityCategory'})[0].text
                if air_quality  == 'Unhealthy for Sensitive Groups':
                    air_quality = 'Unhealthy'
                try:
                    current_time = weather_page.body.findAll("div", {'class': '_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--timestamp--1SWy5'})[0].text.rsplit('of ')[1].rsplit('m ')[0] + str('m')
                except:
                    current_time = "Problems while getting the actual Time"
                try:
                    rain_chance = weather_page.body.findAll("div", {'data-testid': 'precipPhrase'})[0].text
                except:
                    rain_chance = "0% chance of rain"
        if wrong_city:
            add = ''
            if (city_entry.get().islower()):
                add = 'Keep in mind, that cities starts with upper letter.'
            city_entry.delete(0, 'end')
            city_entry.insert(0, 'Enter City')
            messagebox.showerror('Error', "You entered wrong city." + '\n' + add)

    global cities_url
    x = country_entry.get()

    def show_cities():
        cities_window = tkinter.Toplevel()
        cities_window.title('Cities List')
        cities_window.iconbitmap('weather.ico')
        col_qt = (int((len(cities_name_list))/30)+1)
        longest_city = []
        for i in range(col_qt):
            longest_city.append(0)

        for i in range(col_qt-1):
            for j in range(30):
                current_length = len(cities_name_list[j + 30*i])
                if current_length > longest_city[i]:
                    longest_city[i] = current_length

        for i in range(len(cities_name_list) - (col_qt - 1)*30):
            current_length = len(cities_name_list[(col_qt-1)*30 + i])
            if current_length > longest_city[col_qt-1]:
                longest_city[col_qt-1] = current_length

        x_window = 0
        for i in range(col_qt):
            x_window += int(6.5*longest_city[i])
        if col_qt == 1:
            cities_window.geometry(str(x_window) + 'x' + str(21*len(cities_name_list) + 50) + '+1000+150')
            for i in range(len(cities_name_list)):
                tkinter.Label(cities_window, text=cities_name_list[i]).grid(row=i, column=0)
            cities_exit_btn = tkinter.Button(cities_window, font=("Helvetica", 11), pady=10, padx=10, text='Quit cities list', command=cities_window.destroy).grid(row=34, column=0, columnspan=col_qt)
        else:
            cities_window.geometry(str(x_window) + 'x700+1000+150')
            for i in range(len(cities_name_list)):
                tkinter.Label(cities_window, text=cities_name_list[i]).grid(row=i % 30, column=int(i / 30))
            cities_exit_btn = tkinter.Button(cities_window, font=("Helvetica", 16), pady=10, padx=10,text='Quit cities list', command=cities_window.destroy).grid(ipadx= col_qt*22, row=34, column=0, columnspan=col_qt)

    wrong_country = True
    global country_lbl
    for i in range(number_of_countries):
        if x == countries_name_list[i]:
            wrong_country = False
            chosen_country = x
            country_lbl.destroy()
            country_lbl = tkinter.Label(root, text='You chose : ' + str(chosen_country))
            country_lbl.grid(row=1,column=0,columnspan=3)
            cities_url = 'https://www.latlong.net/category/cities-' + str(countries_href_num[i]) + '-15.html'
            cities_r = requests.get(cities_url)
            cities_page = BeautifulSoup(cities_r.content, 'html.parser')
            try:
                number_of_cities = int(len(cities_page.table.findAll("td")) / 3)
                for i in range(number_of_cities):
                    cities_name_list.append(cities_page.table.findAll("td")[3*i].text.rsplit(',')[0])
                city_entry = tkinter.Entry(root, width=30)
                city_entry.grid(row=2, column=0, padx=5, pady=5)
                city_entry.insert(0, 'Enter City')
                city_btn = tkinter.Button(root, text='Submit', command=submit_city)
                city_btn.grid(row=2, column=1)
                cities_name_list.sort()
                show_countries_btn = tkinter.Button(root, text='Show Cities List', command=show_cities)
                show_countries_btn.grid(row=2, column=2, ipadx=10)
            except:
                country_entry.delete(0, 'end')
                country_entry.insert(0, 'Enter Country')
                messagebox.showerror('Error', 'It seems that this country is not available.')
                country_lbl.destroy()
                country_lbl = tkinter.Label(root, text='Choose again')
                country_lbl.grid(row=1, column=0, columnspan=3)

    if wrong_country:
        add = ''
        if(country_entry.get().islower()):
            add = 'Keep in mind, that countries starts with upper letter.'
        country_entry.delete(0, 'end')
        country_entry.insert(0, 'Enter Country')
        messagebox.showerror('Error', "You entered wrong country." + '\n' + add)

def show_countries():
    countries_window = tkinter.Toplevel()
    countries_window.title('Countries List')
    countries_window.iconbitmap('weather.ico')
    countries_window.geometry('1250x800+400+150')
    for i in range(len(countries_name_list)):
        tkinter.Label(countries_window, text=countries_name_list[i]).grid(row=i % 34, column=int(i/34))
    countries_exit_btn = tkinter.Button(countries_window,width=40, font=("Helvetica",16), pady=10 ,text='Quit countries list', command=countries_window.destroy).grid(row=34, pady=20,column=0, columnspan=7)

country_entry = tkinter.Entry(root,width=30)
country_entry.grid(row=0, column=0, padx=5, pady=5)
country_entry.insert(0,'Enter Country')
country_btn = tkinter.Button(root, text='Submit', command=submit_country)
country_btn.grid(row=0, column=1)
show_countries_btn = tkinter.Button(root, text='Show Countries List', command = show_countries)
show_countries_btn.grid(row=0, column=2)

root.mainloop()
