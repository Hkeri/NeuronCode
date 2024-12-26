import requests
crypto = "bitcoin"
url = f'https://api.coingecko.com/api/v3/simple/price?ids={str(crypto)}&vs_currencies=usd'
response = requests.get(url)
data = response.json()
print(str(data[crypto]['usd']))