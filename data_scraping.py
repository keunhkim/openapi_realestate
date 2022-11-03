from pwd import credentials
from bs4 import BeautifulSoup

import pandas as pd
import requests

url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

# Temporary input variables
YYMMDD = pd.period_range(start='2021-01', end='2021-12', freq ="M") # Pandas date range
area_code = ['11110']

# storage list variable
composite_dict = list()

for date in YYMMDD:
    parameters = {
        "serviceKey" : credentials["decode"], # Use decode credentials
        "LAWD_CD" : '11440',
        "DEAL_YMD" : str(date).replace("-","")
    }
    
    res = requests.get(url, params = parameters)
    soup = BeautifulSoup(res.text, "xml")

    items = soup.findAll('item')

    for i in range(len(items)):
        temp = items[i].find_all()
        temp_dict = dict()
        for j in range(len(temp)):
            temp_dict[temp[j].name] = (temp[j].text.strip())
        
        composite_dict.append(temp_dict)  

df = pd.DataFrame.from_dict(composite_dict)
df.head()
