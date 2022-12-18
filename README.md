# job_scraper

The purpose of this python script is to assist with the job application process that can be very stressfull and time consuming. When executed, the script will prompt the user for input about what job, location and experience level they are searching for. It will then use that input to search for jobs on indeed and export the search results to a csv file with the attributes such as "Title", "Company" and "Salary".

This script utilizes chrome as the webdriver but feel free to edit to use other broswers.

INSTALLATION

If you don’t already have Python installed on your machine, run the following commands in your terminal.

Mac:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
brew install python
brew install git

Linux:

suduo apt-get update
sudo apt install python3
sudo apt install python3-pip
sudo apt-get install git-all

Windows:

Install chocolatey at this link https://chocolatey.org/install and then run the command below.

choco install python python -m pip install -U pip

Download the latest git for windows version at https://gitforwindows.org/.

EXECUTION

Run the following commands in your terminal.

git clone https://github.com/angelvs1411/job_scraper

open job_scraper.py and edit the chromedriver path and the path to download the csv file.

navigate to the scripts directory and run the command below.

python3 job_scraper.py












