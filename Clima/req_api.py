import requests
import pprint

cidade = input('Digite a cidade: ')
estado = input('Digite a sigla do estado ou província: ')

link_geo = "https://api.opencagedata.com/geocode/v1/json?q="+cidade+'-'+estado+"&key=623dd04f40bd4296b85c2743f91a7bae"

chama_api = requests.get(link_geo)
info_geo = chama_api.json()

resultados = info_geo['results'][0]['geometry']

pais = info_geo['results'][0]['components']['country']
latitude = str(resultados['lat'])
longitude = str(resultados['lng'])

link_weather = 'https://api.openweathermap.org/data/2.5/weather?lat='+latitude+'&units=metric&lon='+longitude+'&lang=pt_br&appid=6083e5dfb89afcb9b509a94cd8c978c3'

requisita = requests.get(link_weather)
info = requisita.json()

cidade = info['name']
temp_atual = str(info['main']['temp'])
temp_maxima = str(info['main']['temp_max'])
temp_minima = str(info['main']['temp_min'])
cond_climatica = str(info['weather'][0]['description'])
vel_vento = str(info['wind']['speed'])
umid_ar = str(info['main']['humidity'])

print(' ')
print("Está fazendo {} graus em {}, {}".format(temp_atual,cidade,pais))
print('Hoje, a mínima é de {} já a máxima é de {}'.format(temp_minima,temp_maxima))
print('O Vento está há {}Km/h e a umidade do ar é de {}%'.format(vel_vento,umid_ar))
print('A condição climática atual é: {}'.format(cond_climatica))
print(' ')
