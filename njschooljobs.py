import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get("https://www.njschooljobs.com/search/Music%20teacher/-")
soup = BeautifulSoup(res.text, 'html.parser')
job_id = soup.select("#lnkJobId")
company_name = soup.select(".company")
job_description = soup.select(".abstract")


JN = []
CN = []
JD = []
Apply = []
# looping for title and job link
for item in job_id:
    title = item.getText()
    link = f"=HYPERLINK(\"https://njschooljobs.com{item.get('href', None)}\", \"Apply\")"
    JN.append(title)
    Apply.append(link)

# looping for Company Name
for item in company_name:
    name = item.getText()
    CN.append(name)

# looping for the Job description
for item in job_description:
    description = item.getText()
    JD.append(description)

result = pd.DataFrame({'Title': JN, "Company name": CN, "Description": JD, "Apply": Apply})

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(result.to_excel('music-teacher-jobs.xlsx'))




