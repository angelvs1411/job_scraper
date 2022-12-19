from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

s=Service('/path/to/chromedriver') # Change this (e.g., '/usr/local/bin/chromedriver') 
driver = webdriver.Chrome(service=s)

while True:
    keywords = str(input('What job title or key terms would you like to search for? '))
    loc = str(input('What location would you like to filter on? (For WFH jobs enter "Remote") '))
    levels = ["ENTRY", "MID", "SENIOR"]

    while True:
        level = str(input(('What experience level would you like to filer by? (Enter one of three options: Entry, Mid, Senior '))).upper()
        if level not in levels:
            print("Your entry for experience did not equal one of the three valid options, please try again.")
            continue
        else:
            break

    titles = []
    companies = []
    locations = []
    salaries = []
    dates = []
    apply_links = []
    job_attributes = []

    driver.get(f'https://www.indeed.com/jobs?q={keywords}&l={loc}&sc=0kf%3Aexplvl({level}_LEVEL)%3B')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    job_card_titles = soup.find_all('h2', class_='jobTitle css-1h4a4n5 eu4oa1w0')
    job_card_companies = soup.find_all('div', class_='heading6 company_location tapItem-gutter companyInfo')
    job_card_locations = soup.find_all('div', class_='companyLocation')
    job_card_salaries = soup.find_all('div', class_='attribute_snippet')
    job_card_dates = soup.find_all('span', class_='date')


    if len(job_card_titles) > 0:      #Find a way to consolidate these for loops
        for job_card_title in job_card_titles:
            title = job_card_title.find('span')
            titles.append(title.text)
            title_link = job_card_title.find('a', href=True)
            title_link = title_link['href']
            driver.get(f'https://indeed.com{title_link}')
            html2 = driver.page_source
            soup2 = BeautifulSoup(html2, 'html.parser')
            full_link = soup2.find('div', class_='icl-u-lg-hide')
            apply_link = full_link.find('a', href=True)                              
            apply_links.append(apply_link)
            
        for job_card_company in job_card_companies:
            company = job_card_company.find('span')
            companies.append(company.text)
    
        for job_card_location in job_card_locations:
            locations.append(job_card_location.text)
        
        for job_card_salary in job_card_salaries:
            salaries.append(job_card_salary.text)
        
        for job_card_date in job_card_dates:
            dates.append(job_card_date.text)
    
        job_attributes.append(titles)
        job_attributes.append(companies)
        job_attributes.append(locations)
        job_attributes.append(salaries)
        job_attributes.append(dates)
        job_attributes.append(apply_links)
    
        df = pd.DataFrame(job_attributes).transpose()
        df.columns = ['Title', 'Company', 'Location', 'Salary', 'Date Posted/Last Activity', 'Apply Links']
    
        df.to_csv('/path/to/download/jobs.csv', index=False)   # Change this (e.g., '/home/admin/Downloads/jobs.csv')
        driver.quit()
        break
    
    else:
        print('No search results were found, try searching something else.')
        continue

