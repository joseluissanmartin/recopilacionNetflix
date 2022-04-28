import json
import requests
import pandas as pd
from deep_translator import GoogleTranslator

API_KEY = "ab84d51392mshd0e6303e642d8d8p13d80bjsn6fb149d9a572"
AUDIO = "spanish"
ACTOR = "Keanu Reeves"
URL_API = f"https://unogs-unogs-v1.p.rapidapi.com/search/titles?rapidapi-key={API_KEY}&audio={AUDIO}&person={ACTOR}"

results = dict()
columns = ('title', 'year', 'synopsis')


def getResults():
    data = dict()
    try:
        response = requests.get(URL_API)
        data = response.json()
        if 'error' in data:
            raise Exception(f"{data['error']['message']}")
    except Exception as error:
        #print(f"ERROR {error} in API {URL_API}")
        print(f"ERROR in API {URL_API}")
    return data


def loadExercise():
    with open('pywombat.json', 'r') as f:
        data = json.load(f)
        return data['results']


data = getResults()

for idx, item in enumerate(data.get('results', []), 1):
    title = item['title']
    year = item['year']
    synopsis = item['synopsis']

    results[idx] = {'title': GoogleTranslator(source='auto', target='spanish').translate(title),
                    'year': year,
                    'synopsis': GoogleTranslator(source='auto', target='spanish').translate(synopsis)}

df = pd.DataFrame(data=results, index=columns).T
df.to_csv(f'peliculas/{ACTOR}.csv', index=False)
df


# Traducir

to_translate = 'I want to translate this text'
translated = GoogleTranslator(source='auto', target='sp').translate(synopsis)
# outpout -> Ich möchte diesen Text übersetzen

print(translated)