import requests 

URL = "https://httpbin.org/ip"
HEADERS = {}
TIMEOUT = 5

#send GET request and get response data
def get_text(url):
    print("requesting url:", url)

    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)

    #print response code
    print("Response status:", response.status_code)
    response.raise_for_status

    #inspect data
    response_json = response.json()
    print("FULL Response:", response_json)

    return response_json

#run 
response_json = get_text(URL)
print("Results: ", response_json)

#extract data
def get_text_field(url):
    text = response_json.get("origin", "")

    print("Extracted data", text)
    return text

#run 
text = get_text_field(URL)
print("Results_2: ", text)

#find ips 
import re 

def get_ips(text):
    ips = re.findall(r"\d+\.\d+\.\d+\.\d+", text)
    print("IPs found:" , ips)

    return ips

#run
ips = get_ips(text)
print("Results_3: ", ips)

#Fetch from both urls

URL_2 = " "

def get_all_ips():
    ips =[]

    for url in [URL, URL_2]:
        text = get_text_field(url)
        ips.extend(get_ips(text))


    print("All IPs: ", ips)
    return ips

#RUN
all_ips = get_all_ips()
print("Results_4:", all_ips)


#Count and sort

from collections import Counter

#return the count
def get_count(item):
    return item[1]

#Count and sort 
def count_ips(ips):
    counts = Counter(ips)

    results =sorted(
        counts.items(),
        key=get_count,
        reverse=True
    )

    return results

#Run
all_ips = get_all_ips()
results = count_ips(all_ips)

print("Final results: ", results)
