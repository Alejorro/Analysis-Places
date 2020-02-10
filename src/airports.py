
import requests
import pandas as pd


def airportsDF():

    r = requests.get("https://services2.arcgis.com/jUpNdisbWqRpMo35/arcgis/rest/services/Airports28062017/FeatureServer/0/query?where=1%3D1&outFields=longitude_deg,latitude_deg,name&returnGeometry=false&outSR=4326&f=json").json()


    airportName = []

    airport_longitude_deg= []

    airport_latitude_deg = []


    for element in r["features"]:

        airportName.append(element["attributes"]["name"])

        airport_longitude_deg.append(element["attributes"]["longitude_deg"])

        airport_latitude_deg.append(element["attributes"]["latitude_deg"])


    airportZipped = list(zip(airportName,airport_longitude_deg,airport_latitude_deg))

    df = pd.DataFrame(airportZipped).rename(columns={0: 'nombre', 1: 'long', 2:'lat'})
    
    return df
