import requests

def init_four(long=42.51,lat=1.53):
    import os
    from dotenv import load_dotenv

    #Tokens

    load_dotenv()
    Access_Token = os.getenv("FOUR_API")
    Access_Secret = os.getenv("FOUR_SECRET_API")

    # guarderías = "4f4532974b9074f6e4fb0104"

    v = "20200204"
    category = "4f4532974b9074f6e4fb0104"

    baseUrl = "https://api.foursquare.com"
    endpoint = f"/v2/venues/search?ll={long},{lat}"
    header1 = f"&client_id={Access_Token}"
    header2 = f"&client_secret={Access_Secret}"
    header3 = f"&v={v}"
    header4 = f"&categoryId={category}"

    url = baseUrl + endpoint +header1 + header2 + header3 +header4
    print(url)

    #Solicitar la petición correspondiente por HTTP:
    peticion = requests.get(url)
    print(peticion.status_code)
    result = peticion.json()

    return result
