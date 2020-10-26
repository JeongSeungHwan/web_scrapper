from indeed import *

URL = "https://kr.indeed.com/jobs?q=python&limit="
LIMIT = 50

pn_list = call_page(URL,LIMIT)

print(pn_list)
