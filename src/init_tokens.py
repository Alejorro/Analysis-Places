import requests

def init_four(long,lat):
    import os
    from dotenv import load_dotenv

    #Tokens

    load_dotenv()
    Access_Token = os.getenv("FOUR_API")
    Access_Secret = os.getenv("FOUR_SECRET_API")

    # guarderías = "4f4532974b9074f6e4fb0104"

    # vegano = "4bf58dd8d48988d1d3941735"

    # local_nocturno = "4d4b7105d754a06376d81259"

    v = "20200204"
    category = "4f4532974b9074f6e4fb0104"
    # limit=0

    baseUrl = "https://api.foursquare.com"
    endpoint = f"/v2/venues/search?ll={long},{lat}"
    header1 = f"&client_id={Access_Token}"
    header2 = f"&client_secret={Access_Secret}"
    header3 = f"&v={v}"
    header4 = f"&categoryId={category}"
    # header5 = f"&limit={limit}"

    url = baseUrl + endpoint +header1 + header2 + header3 +header4
    print(url)

    #Solicitar la petición correspondiente por HTTP:
    peticion = requests.get(url)
    print(peticion.status_code)
    result = peticion.json()

    return result




def iteration(x):

    result = []

    for element in range(len(x['response']['venues'])):

        name = x["response"]["venues"][element]["name"]

        distance_guard = x["response"]["venues"][element]["location"]["distance"]

        distance_lat = x["response"]["venues"][element]["location"]["lat"]

        distance_long = x["response"]["venues"][element]["location"]["lng"]

        distance_guard = distance_guard/1000

        result.append((name,distance_long,distance_lat,distance_guard))

    return result



