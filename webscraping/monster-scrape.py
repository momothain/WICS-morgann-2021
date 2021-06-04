import requests
import pprint

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page= requests.get(URL)
printable_page = page.content

pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(printable_page)
