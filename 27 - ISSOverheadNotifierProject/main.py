import requests
from nightday import day_night_verify
from issoverhead import iss_is_overhead

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

is_it_night = day_night_verify()

if is_it_night and iss_is_overhead:
    print('Look up!')
else:
    print('Is not here yet.')
