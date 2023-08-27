import asyncio
import pandas as pd
from pyppeteer import launch
import numpy as np

async def get_jobs():
    browser = await launch(headless=True)
    page = await browser.newPage()

    job_titles = []
    job_descriptions = []

    for i in range(1, 25):  # Loop through 2 pages for example
        url = f"https://jobs.ams.at/public/emps/jobs?page={i}&query=remote%20100&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&EMPLOYMENT_RELATIONSHIP=AA&sortField=_SCORE"
        await page.goto(url)
        await asyncio.sleep(5)  # Wait for 5 seconds

        titles = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('h2[role="presentation"] a')).map(a => a.childNodes[0].nodeValue.trim());
        }''')

        descriptions = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('div[id^="ams-search-joboffer-summary"]')).map(div => div.innerText.trim());
        }''')

        for title in titles:
            job_titles.append(title)
            # If a description exists for this title, use it; otherwise, use NaN
            job_descriptions.append(descriptions.pop(0) if descriptions else np.nan)

    await browser.close()

    df = pd.DataFrame({'Job Titles': job_titles, 'Job Descriptions': job_descriptions})
    df.to_excel('job_titles_descriptions.xlsx', index=False)

# Run the function
asyncio.get_event_loop().run_until_complete(get_jobs())
