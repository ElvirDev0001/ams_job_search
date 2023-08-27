# ams_job_search
Search AMS job site and save to excel 

Remote Job Scraper README
About
This Python script is designed to scrape remote job titles and descriptions from the AMS website and stores them in an Excel file.

Dependencies
asyncio
pandas
pyppeteer
numpy
How to Run
Install dependencies: pip install asyncio pandas pyppeteer numpy
Run the script: python script_name.py
Configuration
Page Count
To adjust the number of pages scraped, find this line:

python
Copy code
for i in range(1, 10):
Change 10 to the last page you want to scrape + 1 (e.g., for 24 pages, use range(1, 25)).

Web Page URL
To change the webpage URL, locate this line:

python
Copy code
url = f"https://jobs.ams.at/public/emps/jobs?page={i}&query=remote%20100&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&EMPLOYMENT_RELATIONSHIP=AA&sortField=_SCORE"
Replace the URL but keep the {i} as it iterates through pages.

Note: This script is specifically tailored for AMS. Changing the URL to another site likely won't work without modifications.
