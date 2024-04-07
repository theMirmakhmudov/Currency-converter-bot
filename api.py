import requests

url = "https://fast-currency-convertor.p.rapidapi.com/api/Fetch-Currency/"

querystring = {"amount": "100", "fromCurrency": "USD", "toCurrency": "UZS"}

headers = {
    "X-RapidAPI-Key": "47e6e83752msh94207fba448cf4cp16da37jsn1790f629b32d",
    "X-RapidAPI-Host": "fast-currency-convertor.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
result = response.json().get("value")
print(result)
