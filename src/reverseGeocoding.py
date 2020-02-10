

import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt
import plotly_express as px

import tqdm
from tqdm._tqdm_notebook import tqdm_notebook

def reverseGeocoding(lat, long):

    locator = Nominatim(user_agent="myGeocoder")
    coordinates = f"{lat}, {long}"
    location = locator.reverse(coordinates)
    
    location =  location.raw

    return location["address"]["city"]
    

