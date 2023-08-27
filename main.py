import asyncio
import pandas as pd
from pyppeteer import launch


async def get_jobs():
    browser = await launch(headless=True)
    page = await browser.newPage()

    job_titles = []

    for i in range(1, 25):  # Loop through 2 pages for example
        url = f"https://jobs.ams.at/public/emps/jobs?page={i}&query=remote%20100&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&EMPLOYMENT_RELATIONSHIP=AA&sortField=_SCORE"
        await page.goto(url)

        # Wait for a known element to ensure the page has loaded
        await page.waitForSelector('h2[role="presentation"]', timeout=5000)

        titles = await page.evaluate('''() => {
            return Array.from(document.querySelectorAll('h2[role="presentation"] a')).map(a => {
                return a.childNodes[0].nodeValue.trim();
            });
        }''')

        if titles:
            job_titles.extend(titles)
        else:
            print(f"No titles found on page {i}")

    await browser.close()

    if job_titles:
        # Save to Excel
        df = pd.DataFrame({'Job Titles': job_titles})
        df.to_excel('job_titles.xlsx', index=False)
    else:
        print("No job titles found.")


# Run the asynchronous function
asyncio.get_event_loop().run_until_complete(get_jobs())
