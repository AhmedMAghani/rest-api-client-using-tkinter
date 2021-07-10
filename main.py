from tkinter import *
import requests
import json


def call_api(label,city_name):
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"name": city_name.get()}
    headers = {
        'x-rapidapi-key': "97a630f821msh60b236c67fdc5cep198335jsn51ba52ead6ef",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_dict = json.loads(response.text)
    if len(response_dict) <= 0:
        label.configure(text="No Such Country\nPlease Re-Enter the Country Name")
    else:
        label.configure(text=json.dumps(response_dict, indent=4, sort_keys=True), anchor='w', justify=LEFT)


if __name__ == '__main__':
    covid_info_main_window = Tk()
    covid_info_main_window.title("covid-19 Info app")
    covid_info_main_window.geometry("300x300")
    country_name_label = Label(covid_info_main_window, text="Enter City Name ")
    country_name_label.grid(row=0, column=0)
    country_input_text = Entry(covid_info_main_window, width=30)
    country_input_text.grid(row=0, column=1)
    api_output = Label(covid_info_main_window)
    call_api_button = Button(covid_info_main_window, text="Display country covid-19 information", width=40, command= lambda: call_api(api_output,country_input_text))
    call_api_button.grid(row=1, column=0, columnspan=2)
    api_output.grid(row=2, column=0, columnspan=2)
    covid_info_main_window.mainloop()
