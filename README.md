# job_scraper

The purpose of this python script is to assist with the job application process that can be annoying and time consuming. When executed, the script will prompt the user for input about what job, location and experience level they are searching for. It will then use that input to search for jobs on indeed and export the search results to a csv file with the attributes "Title", "Company", "Salary", and "Date Posted". Currently in the process of adding logic to get the apply link.

This script utilizes chrome as the webdriver but feel free to edit to use other broswers.

# Install

You will need to install chromedriver, you can find the latest version at this link: https://chromedriver.chromium.org/getting-started

If you don't already have python3 and pip installed go ahead and install them.

# Run

Run the following command in your terminal:

git clone https://github.com/angelvs1411/job_scraper

Open job_scraper.py and edit the chromedriver path(line 8) and the path to download the csv file(line 79).

Run the commands below:

pip3 install -r requirements.txt

python3 job_scraper.py

If you dont have git installed you can manually install the dependency requirements with pip and run.













