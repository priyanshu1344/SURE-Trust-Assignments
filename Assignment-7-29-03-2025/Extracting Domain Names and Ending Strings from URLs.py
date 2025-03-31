from urllib.parse import urlparse
import pandas as pd

url_list = [
    "https://blog.hubspot.com/marketing/parts-url",
    "https://www.almabetter.com/enrollments",
    "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html",
    "https://www.programiz.com/python-programming/list"
]

domains = []
endings = []

for url in url_list:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc  
    ending = parsed_url.path.split(".")[-1]  
    
    domains.append(domain)
    endings.append(ending)

data = {
    'URL': url_list,
    'Domain': domains,
    'Ending': endings
}

df = pd.DataFrame(data)
print(df)
