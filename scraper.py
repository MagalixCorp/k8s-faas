from bs4 import BeautifulSoup
import requests
import json

def main(event, context):
    url = event['data']['url']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    items =  [x.find("p",{"class":"description"}).text for x in soup.find_all("div",{"class":["col-sm-4", "col-lg-4", "col-md-4"]})]
    return json.dumps(items)

# print(main({"data":{"url":"https://webscraper.io/test-sites/e-commerce/allinone"}},""))