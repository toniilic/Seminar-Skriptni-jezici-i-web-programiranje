#!/usr/local/bin/python3

import requests
from funcs import print_dict_vals
from funcs import bcolors
from bs4 import BeautifulSoup
import sys

try:
    keyword = sys.argv[1]
except IndexError:
    message = bcolors.FAIL + "Ključna riječ je potrebna! Primjer: ./beautiful_soup php" + bcolors.ENDC
    #print(message)
    sys.exit(message)

URL = "https://www.moj-posao.net/Pretraga-Poslova/?searchWord=php&keyword=" + keyword + "&job_title=&job_title_id=&area=&category="
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="searchlist")

job_elements = results.find_all("div", class_="job")

'''
for job_element in job_elements:
    print(job_element, end="\n"*2)
'''

for job_element in job_elements:
    title_element = job_element.find("p", class_="job-title")
    company_element = job_element.find("p", class_="job-company")
    location_element = job_element.find("p", class_="job-location")
    links = job_element.find_all("a")
    job_to_be_stored = {
        'title': title_element.text.strip(),
        'company_name': company_element.text.strip(),
        'location': location_element.text.strip()
    }

    link_url = links[-1]["href"]

    print_dict_vals(job_to_be_stored)

    print(f"Pošalji prijavu ovdje: {link_url}\n")

if __name__ == '__main__':
    pass





