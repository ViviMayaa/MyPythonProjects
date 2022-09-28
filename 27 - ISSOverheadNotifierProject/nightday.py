import requests
import datetime
MY_LAT = -23.5506507
MY_LONG = -46.6333824

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0

}


def day_night_verify():
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    # or requests.get('https://api.sunrise-sunset.org/json?lat=-23.5506507&lng=-46.6333824')
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    now = int(list(str(datetime.datetime.now()).split(' ')[1].split(':'))[0])

    if sunrise <= now < sunset:
        # daytime
        return False
    else:
        return True
