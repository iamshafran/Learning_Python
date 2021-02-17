import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers={"User-Agent":"Defined"})
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#buyNewSection > div > div > span > span')
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?crid=HXA7MTPDLMIT&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1612878496&sprefix=automate+the+%2Caps%2C148&sr=8-1')
print('The price is ' + price)