import http.client
import mimetypes
import json
import sys
import datetime
try:
    #url de la api
    conn = http.client.HTTPSConnection("api.covid19api.com")
    payload = ''
    #no hace falta headers pero lo metemos vacio
    headers = {}
    #la conexion en si
    conn.request("GET", "https://api.covid19api.com/live/country/argentina/status/confirmed/date/2020-03-21T13:13:30Z", payload, headers)
    #obtenemos response
    res = conn.getresponse()
    #leemos response
    data = res.read()
    #parseamos a json obj
    resp = json.loads(data.decode("utf-8"))
    #la api devuelve un array de objetos, asi que si queremos obtener la ultima novedad, vamos al index n-1 
    latest = len(resp)-1
    #el return es un print.
    #variable fecha de hoy
    today = datetime.datetime.now()
    print(resp[latest]['Country']+':',resp[latest]['Confirmed'],'confirmed,',resp[latest]['Active'],'active,',resp[latest]['Deaths'],'deaths,',resp[latest]['Recovered'],'recovered. (Last API Update:'+resp[latest]['Date'][0:10]+') (Queried:',today,')')
except:
    #si no te anda el wifi o no se logra conectar a la api, para que no rompa el conky.
    #si bien corro el conky cada 3 seg, este exec de script en particular corre cada 15 min en el conky config filenb
    print('Data unavailable, retrying...')