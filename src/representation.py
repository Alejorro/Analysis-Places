import pandas as pd
from src.coordenadas import *


def geojsonize(df):

    df["location"] = df[["long","lat"]].apply(lambda x:asGeoJSON(x.long,x.lat), axis=1)

    return df

