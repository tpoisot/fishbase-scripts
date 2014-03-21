import requests as re

FB_API_ROOT = 'http://www.deepspaceweb.com:80/fishbase/api/'

SPECIES_ID = [10, 11, 23]

for SP in SPECIES_ID:
    request_url = FB_API_ROOT + 'species/id/' + str(SP)
    r = re.get(request_url)
    if r.status_code == 200 :
        if len(r.json()) == 1 :
            record = r.json()[0] # This will become unecessary later
            print "#" + str(SP) + "\t" + record['Genus'] + ' ' + record['Species']
