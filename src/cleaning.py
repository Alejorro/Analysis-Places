import pandas as pd
from src.coordenadas import *


def cleaning(collection):

    query = list(collection.find({},{"name":1,"offices":1,"category_code":1}))
   
    df = pd.DataFrame(query)

    df = df.explode('offices')

    dfOfficeData = df[["offices"]].apply(lambda r: r.offices, result_type="expand", axis=1)

    cleanData = pd.concat([df,dfOfficeData], axis=1)

    cleanData = cleanData.drop(columns=["_id","offices"])

    cleanData["location"] = cleanData[["latitude","longitude"]].apply(lambda x:asGeoJSON(x.latitude,x.longitude), axis=1)

    cleanData = cleanData.drop(columns=["latitude","longitude"])

    return cleanData

