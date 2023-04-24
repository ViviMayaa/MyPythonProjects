import requests


def iss_is_overhead():
    MY_LAT = -23.5506507
    MY_LONG = -46.6333824

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    # parameters = {
    #     "lat": MY_LAT,
    #     "lng": MY_LONG,
    #     "formatted": 0,
    # }
    #
    # response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    # response.raise_for_status()
    # data = response.json()
    # sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    #
    # time_now = datetime.now()

    if iss_latitude - 50 < MY_LAT < iss_latitude + 50 and iss_longitude < MY_LONG < iss_longitude:
        return True
    else:
        return False
