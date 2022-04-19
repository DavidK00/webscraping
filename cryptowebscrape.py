from twilio.rest import Client
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.tradingview.com/markets/cryptocurrencies/prices-all/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req =  Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

crypto_table =  soup.findAll('tbody') #tbody = table

crypto_table = crypto_table[0]

rows = crypto_table.findAll('tr')

for row in rows[:5]:
    cols = row.findAll('td')
    name = cols[0].find('a', attrs = {'class':'tv-screener__symbol' })
    name = name.text.strip()
    symbol = cols[0].find('a', attrs = {'class':'tv-screener__symbol' })
    symbol = str(symbol)
    symbol = symbol.rsplit('/')[2].upper()
    if name != 'USD Coin':
        symbol = symbol.strip('USD')
    else: 
        symbol 
    price = float(cols[3].text)
    change_text = cols[7].text
    change_float = float(cols[7].text.strip('%'))

    s_price = round(price/(1+(change_float/100)),2)

    print(f'Coin Name: {name}')
    print(f'Symbol: {symbol}')
    print(f'Current Price: {price}')
    print(f'% Change: {change_text}')
    print(f'% Change Price: {s_price}')
    input()

    account_sid = 'ACa7891b338605415778fe56b47100b4f2'
    auth_token = '623b7276ce8f5881f34ec5cfc15fefe1'
    client = Client(account_sid, auth_token)
    if name == 'Bitcoin' and float(price) < 40000:
        message = client.messages.create(
                                    body='Bitcoin price is under $40,000. Time to buy!',
                                    from_='+17657905351',
                                    to='+14695342551'
                                )
    if name == 'Ethereum' and float(price) < 3000:
        message = client.messages.create(
                                    body='Etherium price is under $3,000. Time to buy!',
                                    from_='+17657905351',
                                    to='+14695342551'
                                )

