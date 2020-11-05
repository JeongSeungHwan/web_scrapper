from bs4 import BeautifulSoup
import requests
import time

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def call_page(keyword):
    responsed_page = requests.get(f"https://kr.indeed.com/jobs?q={keyword}&limit={LIMIT}")
    soup = BeautifulSoup(responsed_page.text, "html.parser")
    try : 
        pagination = soup.find("div",{"class" : "pagination"})
        page_numbers = pagination.find_all("a")

        pn_list = []
        for pn in page_numbers[:-1] :
            pn_list.append(int(pn.text))
        max_page = pn_list[-1]
        return max_page
    except:
        return 0

def job_detail(num,job_card):
    title = job_card.find("h2",{"class":"title"}).find("a")["title"]
    company = job_card.find("span",{"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None :
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()

    return {"No":num, "title":title, "company":company}


def extract_data(max_page):
    jobs = []
    num = 0
    for page in range(max_page) :
        print(f"Scrapping{page}")
        responsed_page = requests.get(URL + f"&start={0*LIMIT}")
        soup = BeautifulSoup(responsed_page.text, "html.parser")
        job_cards = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        
        for job_card in job_cards :
            num += 1
            jobs.append(job_detail(num, job_card))
    return jobs

def search_job(keyword):
    return extract_data(call_page(keyword))

print("indeed module is loaded")
