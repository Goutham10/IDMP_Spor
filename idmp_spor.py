import requests

class Idmp_spor:

    @staticmethod
    def login_api():
        pass

    @staticmethod
    def fetch_data():
        main_id_lists = ["100000000001", "200000000009", "200000000008"] # replace this with the required list ids array from the db

        auth_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsIng1dCI6ImJJZDNaTjdNemU0OXZqTjZ3U0ZUZS00LUxxSSIsImtpZCI6Im9yYWtleSJ9.eyJvcmFjbGUub2F1dGgudGtfY29udGV4dCI6InVzZXJfYXNzZXJ0aW9uIiwiZXhwIjoxNjUzNTYzNTg2LCJzdWIiOiJzcG9yZ3Vlc3QiLCJpc3MiOiJlbWEuZXVyb3BhLmV1IiwicHJuIjoic3Bvcmd1ZXN0IiwianRpIjoiYTMxYThkZjctN2EyYy00MmJhLWFiNmEtNzA4NGU5YTkxNzFjIiwib3JhY2xlLm9hdXRoLnN2Y19wX24iOiJPQXV0aFNlcnZpY2VQcm9maWxlIiwiaWF0IjoxNjUzNTM0Nzg2LCJvcmFjbGUub2F1dGguaWRfZF9pZCI6IjEyMzQ1Njc4LTEyMzQtMTIzNC0xMjM0LTEyMzQ1Njc4OTAxMiIsInVzZXIudGVuYW50Lm5hbWUiOiJEZWZhdWx0RG9tYWluIiwib3JhY2xlLm9hdXRoLnBybi5pZF90eXBlIjoiTERBUF9VSUQifQ.RJB_sL5UaB6F2H2inOtbjsGvPSryv5GKeNKZl5jcqd9iznIROb5_7l2HtM_I7VvdgJ-LD3bsZdnla9dapPo8dEbsOkW2Bbt3Q68Fq5Qt582ozNecnXzYsd7TDvMOwUHB9qE788N_1e_r7WWPLBl03MkGrWzYfjjMetEBM3fhVtA'
        header = {
            'accept' : "application/json",
            'Authorization': 'Bearer ' + auth_token
        }

        main_dict = {}

        for main_id in main_id_lists:
            url = f'https://spor.ema.europa.eu/v1/lists/{main_id}/term-summaries?lang=en&page=1&pagesize=20&parent=all&sortby=term-name'
            response = requests.get(url,  headers=header)
        #     print(response)
            data = response.json()
            main_list = []
            sub_list = []
            while url != "":
                spor_list = []
                try:
                    response = requests.get(url,  headers=header)
                    
                    data = response.json()

                    itemlist = data['controlled-terms-list-summary']['controlled-term-summaries']["controlled-term-summary"]
                
                    for i in range(len(itemlist)):

                        dict_val = {}

                        list_name = data['controlled-terms-list-summary']['list-summary']['list-name']

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
                except Exception as e:
                    print()
                sub_list.append(spor_list)
                main_list.extend(sub_list)

                nextpage = data["controlled-terms-list-summary"]["next-page"]
                url = nextpage
                main_dict[list_name] = main_list

        # print(main_dict)

        for list_item, value in main_dict.items():
            print(list_item, ":", value)
            print()
            

idmp_spor = Idmp_spor()
idmp_spor.fetch_data()
