import time
import requests

urltrigger_1 = 'https://api.particle.io/v1/devices/310047000447343232363230/detect-spots'
urlget_1 = 'https://api.particle.io/v1/devices/310047000447343232363230/spot1?access_token=f8093528e7b81caceeaecd0569423df524dffbab'

urltrigger_2 = 'https://api.particle.io/v1/devices/33003b000d47343233323032/detect-spots'
urlget_2 = 'https://api.particle.io/v1/devices/33003b000d47343233323032/spot1?access_token=f8093528e7b81caceeaecd0569423df524dffbab'

query = {'access_token':'f8093528e7b81caceeaecd0569423df524dffbab'}


res = requests.post(urltrigger_1, data=query)
photon =  requests.get(urlget_1)
res = requests.post(urltrigger_2, data=query)
photon =  requests.get(urlget_2)
