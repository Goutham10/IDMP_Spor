import requests


auth_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIng1dCI6ImJJZDNaTjdNemU0OXZqTjZ3U0ZUZS00LUxxSSIsImtpZCI6Im9yYWtleSJ9.eyJvcmFjbGUub2F1dGgudGtfY29udGV4dCI6InVzZXJfYXNzZXJ0aW9uIiwiZXhwIjoxNjUzNDgxMzE3LCJzdWIiOiJzcG9yZ3Vlc3QiLCJpc3MiOiJlbWEuZXVyb3BhLmV1IiwicHJuIjoic3Bvcmd1ZXN0IiwianRpIjoiZTU2Y2EyZDUtZWQ4Yi00ZmFjLTljODItMzc3MWYwMjJlYjAxIiwib3JhY2xlLm9hdXRoLnN2Y19wX24iOiJPQXV0aFNlcnZpY2VQcm9maWxlIiwiaWF0IjoxNjUzNDUyNTE3LCJvcmFjbGUub2F1dGguaWRfZF9pZCI6IjEyMzQ1Njc4LTEyMzQtMTIzNC0xMjM0LTEyMzQ1Njc4OTAxMiIsInVzZXIudGVuYW50Lm5hbWUiOiJEZWZhdWx0RG9tYWluIiwib3JhY2xlLm9hdXRoLnBybi5pZF90eXBlIjoiTERBUF9VSUQifQ.MA6Ck9odVapgo6dvhXNh0fLoPmaMk1mopWeP8-3fwqstvRKJ-JsgZN2DizGGMVq7GpLQXBPaHR60CYzyXTLmoExq4uWLbrFKGkVPFUExeWjaYXk2nk2zInufRp4PXzztBHtEni0EGhoMJbGONxBE_g6HxLFd5SX3ysfb2vGdjY0'
header = {
    'accept' : "application/json",
    'Authorization': 'Bearer ' + auth_token
}


url = 'https://spor.ema.europa.eu/v1/lists?pagesize=500'
response = requests.get(url,  headers=header)
print(response)
data = response.json()

list_data = data["list-of-lists"]["list-summary"]
# print(list_data)
list_ids = []

for i in range(len(list_data)):
    list_id = list_data[i]["list-id"]["id"]
    list_ids.append(list_id)

for list_id in range(len(list_ids)):
    list_name = list_data[list_id]["list-name"]
    # print(list_name)
    
    # next_page = data["list-of-lists"]["next-page"]
    # print(next_page)
    page = 1
    if list_name == "Age Range" and page == 1:
        url = f'https://spor.ema.europa.eu/v1/lists/{list_ids[list_id]}/term-summaries?lang=en&page={page}&pagesize=1000&parent=all&sortby=term-name'
        print(url)
        page += 1
        response = requests.get(url,  headers=header)
        data = response.json()
        print(data.keys())
        next_page = data["controlled-terms-list-summary"]["next-page"]
        # while next_page != "":
        #     page+=1
        #     url = f'https://spor.ema.europa.eu/v1/lists/{list_ids[list_id]}/term-summaries?lang=en&page={page}&pagesize=1000&parent=all&sortby=term-name'
        #     print(url)
        print(next_page)
        itemlist = data['controlled-terms-list-summary']['controlled-term-summaries']["controlled-term-summary"]
        # print(itemlist)
        spor_list = []
        for i in range(len(itemlist)):
            dict_val = {}

            id = itemlist[i]["term-id"]["id"] 
            term_name = itemlist[i]["term-names"]["term-name"]["name"]["text"]

            if "short-names" not in  itemlist[i].keys():
                short_name = ""
            else:
                short_name=itemlist[i]["short-names"]["short-name"]["name"]["text"]
            
            source_id = ""

            status = itemlist[i]["status"]["code"]

            dict_val["id"] = id
            dict_val["term-name"] = term_name
            dict_val["short-name"] = short_name
            dict_val["source_id"] = source_id
            dict_val["status"] = status

            spor_list.append(dict_val)
        print(spor_list)
        #     page += 1
