import requests
import json
from datetime import datetime


api_url ="https://openexchangerates.org/api/latest.json?app_id=50f11acd9a29453f8888f7c2cb59e2de"

from_currency = input("from currency: ")
to_currency   = input("To currency: ")
amount        = int(input("Amount: "))  
    
result = requests.get(api_url)
result = json.loads(result.text)

dt = datetime.fromtimestamp(1678701606)

print("1",from_currency,result["rates"][to_currency],to_currency,dt)
print("Agg=",amount * result["rates"][to_currency],to_currency)
 
