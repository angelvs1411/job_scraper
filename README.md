# job_scraper

The purpose of this python script is to assist with the job application process that can be very stressfull and time consuming. When executed, the script will prompt the user for input about what job, location and experience level they are searching for. It will then use that input to search for jobs on indeed and export the search results to a csv file with the attributes "Title", "Company", "Salary", "Date Posted" and "Apply Link". (I'm aware the current code exports the entire html element for the "apply link" field. Currently in the process of adding logic to export just the link.)

This script utilizes chrome as the webdriver but feel free to edit to use other broswers.

INSTALLATION

You will need to install chromedriver, you can find the latest version at this link: https://chromedriver.chromium.org/getting-started

If you don’t already have Python3 or Git on your machine, you'll need to install them as well.

You can check if you have python/git installed and the versions with the following commands:

python -v

git --version

Other wise enter the commands below in your terminal depending on your OS:

Mac:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

export PATH="/usr/local/opt/python/libexec/bin:$PATH"

brew install python

brew install git

Linux:

sudo apt-get update

sudo apt install python3

sudo apt install python3-pip

sudo apt-get install git-all

Windows:

Install chocolatey at this link https://chocolatey.org/install and then run the command below.

choco install python python -m pip install -U pip

Download the latest git for windows version at https://gitforwindows.org/.

EXECUTION

Run the following command in your terminal:

git clone https://github.com/angelvs1411/job_scraper

Open job_scraper.py and edit the chromedriver path and the path to download the csv file.

Run the commands below:

pip3 install -r requirements.txt

python3 job_scraper.py

FINISH - CSV file should be located in the path you specified.

Hope this helps someone find a job, feel free to lmk any suggestions or edits. Trying to condense this anyway I can. - AVS











