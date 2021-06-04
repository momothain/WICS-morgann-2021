import requests
import pprint
from bs4 import BeautifulSoup

## use requests to send a get request and get the html content
URL = 'https://www.monster.com/jobs/search?q=Software+Developer&where=Pennsylvania'
page_GET_request_response = requests.get(URL)
pcontent = page_GET_request_response.content

pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(pcontent)

## use BeautifulSoup to parse html/dom
# can search html elements by id, classname
soup = BeautifulSoup(pcontent, 'html.parser')
#print(soup.prettify())
# id
app = soup.find(id='app')
print(app.prettify()) #prints better
#results = soup.find(id='results-page container')
#print(results.prettify()) #prints better
# class name

# job_elems = results.find_all('section', class_='card-content')
