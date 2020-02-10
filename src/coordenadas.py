import requests
import math

from src.distanceCalc import *

def geocode(address):

    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }


def withGeoQuery(location,maxDistance=10000,minDistance=0,field="location"):
    return {
       field: {
         "$near": {
           "$geometry": location if type(location)==dict else geocode(location),
           "$maxDistance": maxDistance,
           "$minDistance": minDistance
         }
       }
    }


def asGeoJSON(lng,lat):

    try:
        lat = float(lat)
        lng = float(lng)
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        return None


def fixCoords(lng,lat):

    lngTest = int(lng)

    latTest = int(lat)

    if (lngTest == -122 or lngTest == -73) and (latTest == 37 or latTest == 40):

        return 1


def compareCoords(lng,lat):

    lngTest = int(lng)

    latTest = int(lat)

    if lngTest == -122 and latTest == 37:

        result1 = distCalc(37.775196,-122.419204, lat, lng)

        result2 = distCalc(37.535876,-122.257331, lat, lng)

        return min(result1,result2)

    if lngTest == -73 and latTest == 40:

        result = distCalc(40.7398335,-73.9931582, lat, lng)

        return result

        



