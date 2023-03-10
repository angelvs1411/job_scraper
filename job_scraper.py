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

    driver.get(f'https://www.indeed.com/jobs?q={keywords}&l={loc}&sc=0kf%3Aexplvl({level}_LEVEL)%3B')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    job_card_titles = soup.find_all('h2', class_='jobTitle css-1h4a4n5 eu4oa1w0')
    job_card_companies = soup.find_all('div', class_='heading6 company_location tapItem-gutter companyInfo')
    job_card_locations = soup.find_all('div', class_='companyLocation')
    job_card_salaries = soup.find_all('div', class_='attribute_snippet')
    job_card_dates = soup.find_all('span', class_='date')


    if len(job_card_titles) > 0:      
        
        titles = [job_card_title.find('span').text for job_card_title in job_card_titles]       
        companies = [job_card_company.find('span').text for job_card_company in job_card_companies]
        locations = [job_card_location.text for job_card_location in job_card_locations]
        salaries = [job_card_salary.text for job_card_salary in job_card_salaries]
        dates = [job_card_date.text for job_card_date in job_card_dates]
        
        job_attributes = [titles, companies, locations, salaries, dates]
        
        df = pd.DataFrame(job_attributes).transpose()
        df.columns = ['Title', 'Company', 'Location', 'Salary', 'Date Posted/Last Activity']
    
        df.to_csv('/path/to/download/jobs.csv', index=False)   # Change this (e.g., '/home/admin/Downloads/jobs.csv')
        driver.quit()
        break
    
    else:
        print('No search results were found, try searching something else.')
        continue

