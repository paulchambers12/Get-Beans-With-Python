### Before starting application make sure to use the environmnet pyWebSearch
#   :> source pyWebSearch/bin/activate
#

from urllib.request import urlopen,Request
import urllib.request
import re,sys
#import numpy#,pandas

#comment
def get_number_of_pages(split_html_content):

    page_no = 0
    query_item1 = "Go to results page"
    for string in split_html_content:
        #print("in the for loop.")
        if query_item1 in string:
            broken_string = re.split('page=|"', string)
            #print("words = ", broken_string)
            for part in broken_string:
                if part.isdigit():
                    #print("part is : ", part)
                    port = int(part)
                    if port > page_no:
                        page_no = port
    #print("page_no is : ", page_no)
    return page_no

def get_htlm_stuff(pages):
    found_html_content = []
    print("pages of {0}".format(pages))
    print(type(pages))
    page = 1
    try:
        query_item = str(sys.argv[1]).lower()
    except IndexError:
        print("Please ensure your input is as follows:")
        print("python3 main.py <product>")
        print("-----------------------------")
        print("Searching for 'Beans'")
        query_item = "beans"
    #query_item = str(sys.argv[1]).lower()
    #query_item = "beans"
    if pages == 0:
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
        #print(url)
        found_html_content = urllib.request.urlopen(req).read().decode('utf-8')
    else:
        #while page <= pages:
        print("page {0} of {1}".format(page, pages))
        url = "https://www.tesco.ie/groceries/en-IE/search?query="+query_item+"&page="+str(pages)
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
        #print(url)
        found_html_content = urllib.request.urlopen(req).read().decode('utf-8')
        #page += 1
    return found_html_content


if __name__ == "__main__":
    query_item = "beans"
    currency = "€"
    page = 0
    html_content = get_htlm_stuff(0)


    split_html_content = re.split('text">|</', html_content)

    special_chars = [">","<",";"]

    items_on_sale = []

    page_number = get_number_of_pages(split_html_content)

    print("page_number = ", page_number)
    while page <= page_number:
        #html_content.append(get_htlm_stuff(page_number))
        print("page {0} of {1}".format(page, page_number))
        page_of_info = get_htlm_stuff(page_number)
        split_html_content = re.split('text">|</', page_of_info)

        ### Split string and get
        for string in split_html_content:
            if query_item in string.lower() or currency in string:
                if "__" not in string and ">" not in string and "-" not in string:
                    if "quot;" not in string:
                        items_on_sale.append(string.replace("&amp;","&"))
        page += 1

    for item in items_on_sale:
        print(item)


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

    for row in item_array:
        print("|{:<70} | {:<40} | {:<8} | {:<8}".format(row[0],row[1],row[2],row[3] ))

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
