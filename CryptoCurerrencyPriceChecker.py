# Importing the requests library to fetch web content
import requests
# Importing the BeautifulSoup module from bs4 for web scraping
import bs4

# Setting the URL of the Wikipedia page for Riga Technical University as the target for scraping
url = "https://coinmarketcap.com/"
url_zkf = "https://coinmarketcap.com/currencies/zkfair/"
# Using requests.get() to send a GET request to the specified URL and fetch its content
saturs = requests.get(url)
saturs2 = requests.get(url_zkf)

# Checking if the request was successful (HTTP status code 200 means OK/successful)
if saturs.status_code == 200:
    #get price of cryptocurencies
    lapas_saturs = bs4.BeautifulSoup(saturs.content, 'html.parser')
    btc_price = lapas_saturs.find_all(href="/currencies/bitcoin/#markets")
    eth_price = lapas_saturs.find_all(href="/currencies/ethereum/#markets")
    bnb_price = lapas_saturs.find_all(href="/currencies/bnb/#markets")
    usdt_price = lapas_saturs.find_all(href="/currencies/tether/#markets")
    sol_price = lapas_saturs.find_all(href="/currencies/solana/#markets")
    matic_price = lapas_saturs.find_all(href="/currencies/polygon/#markets")
    atom_price = lapas_saturs.find_all(href="/currencies/cosmos/#markets")
    apt_price = lapas_saturs.find_all(href="/currencies/aptos/#markets")
    arb_price = lapas_saturs.find_all(href="/currencies/arbitrum/#markets")
    sui_price = lapas_saturs.find_all(href="/currencies/sui/#markets")
    
if saturs2.status_code == 200:
    lapas_saturs2 = bs4.BeautifulSoup(saturs2.content, 'html.parser')
    zkf_price = lapas_saturs2.find_all(class_="sc-f70bb44c-0 jxpCgO base-text")
    
    
    
print(zkf_price[0].string)
