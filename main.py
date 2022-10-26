### Before starting application make sure to use the environmnet pyWebSearch
#   :> source pyWebSearch/bin/activate
#

from urllib.request import urlopen
import re,sys
#import numpy#,pandas

#comment
def get_number_of_pages(split_html_content):
    print(split_html_content)
    pages = []
    query_item1 = "Go to results page"
    for string in split_html_content:
        if query_item1 in string:
            pages.append(string.replace("&amp;", "&"))

if __name__ == "__main__":
    #query_item = str(sys.argv[1]).lower()
    query_item = "beans"
    url = "https://www.tesco.ie/groceries/en-IE/search?query="+query_item

    currency = "€"

    print(url)

    html_content = urlopen(url).read().decode('utf-8')
    #print("html_content = ", html_content)
    #html_content = urlopen('https://www.tesco.ie/groceries/zone/contact-us/').read().decode('utf-8')

    #split_html_content = html_content.split('>')[-1].split('<')[0]
    split_html_content = re.split('text">|</',html_content)
    #print(split_html_content)
    special_chars = [">","<",";"]

    items_on_sale = []

    page_number = get_number_of_pages(split_html_content)
'''
### Split string and get
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
for item in items_on_sale:
    if query_item in item.lower():
        item_array.append(item_row)
        item_row = ["","","",""]
        #row += 1
#        print(row)
        item_row[0] = item
    if "€" in item:
        if "Clubcard Price" in item or "Save" in item:
            item_row[1] = item
        elif "/" in item:
            item_row[3] = item
        else:
            item_row[2] = item
'''
#for row in item_array:
#    print("|{:<70} | {:<40} | {:<8} | {:<8}".format(row[0],row[1],row[2],row[3] ))

#print("{:<20} {:<8} {:<8} {:<8}".format("Product","Discount","Price","Price/kg"))
#for k,v in item_array.items():
#    p,d,c,k = v
#    print("{:<20} {:<8} {:<8} {:<8}".format(p,d,c,k ))
#    print(v)

#for string in items_on_sale:
#    if currency in string:
#        print(string)

# matches =re.findall(regex,split_html_content,re.IGNORECASE);

#if len(matches) == 0:
#    print('This website has no beans to sell')
#else:
#    print(matches)
#    print(html_content)
