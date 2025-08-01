import requests
from bs4 import BeautifulSoup

def scrape_jobs_indeed(keyword="Python Developer", location="Remote"):
    query = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    resp = requests.get(query)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    jobs = []
    for card in soup.select('.result'):
        title = card.h2.text.strip()
        company = card.find('span', {'class': 'companyName'}).text.strip()
        summary = card.find('div', {'class': 'job-snippet'}).text.strip()
        jobs.append({'title': title, 'company': company, 'summary': summary})
    return jobs
