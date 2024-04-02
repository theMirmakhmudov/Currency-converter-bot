import requests

url = "https://fast-currency-convertor.p.rapidapi.com/api/Fetch-Currency/"

querystring = {"amount": "100", "fromCurrency": "USD", "toCurrency": "UZS"}

headers = {
    "X-RapidAPI-Key": "d30a4c727fmshc47e10cf5e8e3eap1cfcdfjsndf29e40f8f0b",
    "X-RapidAPI-Host": "fast-currency-convertor.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
result = response.json()
print(result.get("value"))
