import requests
import urllib 

sparql_endpoint = "http://query.wikidata.org/sparql?query="
accept = "&format=json"
query="""SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q146.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} 
limit 10"""

response = requests.get(sparql_endpoint+query+accept)

print(response.text)
