### Before starting application make sure to use the environmnet pyWebSearch
#   :> source pyWebSearch/bin/activate
#

from urllib.request import urlopen,Request
import re,sys
import base64

try:
    query_item = str(sys.argv[1]).lower()
except IndexError:
    print("Please ensure your input is as follows:")
    print("python3 main.py <product>")
    print("-----------------------------")
    print("Searching for 'Beans'")
    query_item = "beans"

## Dunnes Stores Request
#url = "https://www.dunnesstoresgrocery.com/sm/delivery/rsid/258/results?q="+query_item

## Tesco Request
url = "https://www.tesco.ie/groceries/en-IE/search?query="+query_item
req = Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'utf-8, deflate',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'close'
    }
)
currency = "€"

print(url)

#print(urlopen(req).read().decode('utf-8'))
html_content = urlopen(req).read().decode('utf-8')

print("Content Recieved")

split_html_content = re.split('text">|</',html_content)

items_on_sale = []

## Tesco
### Split string and get desired content line by line
for string in split_html_content:
    if query_item in string.lower() or currency in string:
        if "__" not in string and ">" not in string and "-" not in string:
            if "quot;" not in string:
                items_on_sale.append(string.replace("&amp;","&"))

#for item in items_on_sale:
#    print(item)


#### Tabularize array
row = 0
item_row = ["Product","Discount","Price","Price/vol"]
item_array = []
item_array.append(item_row)
for item in items_on_sale:
    if query_item in item.lower():
        item_row = ["","","",""]
        item_row[0] = item
    if "€" in item:
        if "Clubcard Price" in item or "Save" in item:
            item_row[1] = item
        elif "/" in item:
            item_row[3] = item
        else:
            item_row[2] = item
    else:
        item_array.append(item_row)

for row in item_array:
    print("|{:<60} | {:<40} | {:<8} | {:<8}".format(row[0],row[1],row[2],row[3] ))
