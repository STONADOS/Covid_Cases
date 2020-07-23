import requests
from bs4 import BeautifulSoup

while True:
    countryname = input("Country name: ")
    country = countryname.lower()
    
    if country == "quit":
        exit()

    url = ("https://www.worldometers.info/coronavirus/country/"+country)
    req = requests.get(url)
    obj = BeautifulSoup(req.text, "html.parser")
    data = obj.find_all("div", class_ = "maincounter-number")

    try:

        print("Total case: ",data[0].text.strip())
        print("Total deaths: ",data[1].text.strip())
        print("Total recoveries: ",data[2].text.strip())

    except:

        print("Somthing got wrong you stupid as well as eidot!!")
