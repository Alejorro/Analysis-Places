import pandas as pd
from src.coordenadas import *


def cleaning(collection):

    filter = {"$and": [{"deadpooled_year": {"$eq": None}},
                       {"founded_year": {"$ne": None}}]}

    projection = {"name": 1, "offices": 1, "category_code": 1,
                  "founded_year": 1, "total_money_raised": 1}

    df = pd.DataFrame(list(collection.find(
        filter=filter, projection=projection)))

    df = df.explode('offices')

    dfOfficeData = df[["offices"]].apply(
        lambda r: r.offices, result_type="expand", axis=1)

    cleanData = pd.concat([df, dfOfficeData], axis=1)

    cleanData = cleanData.drop(columns=["_id", "offices"])

    cleanData["location"] = cleanData[["latitude", "longitude"]].apply(
        lambda x: asGeoJSON(x.latitude, x.longitude), axis=1)

    cleanData = cleanData.drop(columns=["latitude", "longitude"])

    return cleanData


def cleaning_money(string):

    division = list(string)

    lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    result = []

    for element in division:

        if element in lista:

            result.append(element)

        if element == ".":

            result.append(element)

    union = "".join(result)

    return float(union)


def cleaning_tech(x):

    tech = ["analytics", "biotech", "cleantech", "ecommerce", "hardware",
            "mobile", "nanotech", "network_hosting", "semiconductor", "software"]

    if x in tech:

        return x

    else:

        return None

def cleaning_design(x):

    design = ["design", "web", "advertising", "fashion", "games_video"]

    if x in design:

        return x

    else:

        return None


