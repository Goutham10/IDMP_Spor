for table_name, value in main_dict.items():
#     print(table_name)
    if table_name == "idsp_xevmpd_domain":
#         print(table_name)
        rowcount = 0
        for each_row in value:
#             print(each_row)
#             cursor.execute(f"insert into idsp_xevmpd_domain (identifier, term_name,short_name, source_id, status) values(%s,%s,%s,%s,%s)", (each_row["id"], each_row["term-name"],each_row["short-name"],each_row["source_id"],each_row["status"]))
            cursor.execute(f"""insert into idsp_xevmpd_domain (identifier, term_name,short_name, source_id, status)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}', 
                            '{each_row["status"]}' 
                            where not exists
                            (select identifier from idsp_xevmpd_domain where identifier = '{each_row["id"]}' )""")
            conn.commit()
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_legal_status_supply":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            cursor.execute(f"""insert into idsp_xevmpd_legal_status_supply (identifier, term_name,short_name, source_id, status)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}', 
                            '{each_row["status"]}' 
                            where not exists
                            (select identifier from idsp_xevmpd_legal_status_supply where identifier = '{each_row["id"]}' limit 1)""")
            conn.commit()
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_full_indication_text":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_xevmpd_full_indication_text (identifier, term_name,short_name, source_id, status)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}', 
                            '{each_row["status"]}' 
                            where not exists
                            (select identifier from idsp_xevmpd_full_indication_text where identifier = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_product_type_information":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_xevmpd_product_type_information (identifier, name, owner, version)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}'
                            where not exists
                            (select identifier from idsp_xevmpd_product_type_information where identifier = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_pharmaceutical_dose_forms":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_xevmpd_pharmaceutical_dose_forms (`key`, value, type)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}'
                            where not exists
                            (select `key` from idsp_xevmpd_pharmaceutical_dose_forms where `key` = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_legal_basis":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_legal_basis (`key`, value)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}'
                            where not exists
                            (select `key` from idsp_legal_basis where `key` = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)  
    elif table_name == "idsp_xevmpd_product_cross_reference_type":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            cursor.execute(f"""insert into idsp_xevmpd_product_cross_reference_type (identifier, term_name,short_name, source_id, status)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}', 
                            '{each_row["status"]}' 
                            where not exists
                            (select identifier from idsp_xevmpd_product_cross_reference_type where identifier = '{each_row["id"]}' limit 1)""")
            conn.commit()
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_marketing_status":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            cursor.execute(f"""insert into idsp_xevmpd_marketing_status (identifier, term_name,short_name, source_id, status)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}', 
                            '{each_row["short-name"]}', 
                            '{each_row["source_id"]}', 
                            '{each_row["status"]}' 
                            where not exists
                            (select identifier from idsp_xevmpd_marketing_status where identifier = '{each_row["id"]}' limit 1)""")
            conn.commit()
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name)
    elif table_name == "idsp_xevmpd_units_of_presentation":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_xevmpd_units_of_presentation (`key`, value)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}'
                            where not exists
                            (select `key` from idsp_xevmpd_units_of_presentation where `key` = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name) 
    elif table_name == "idsp_xevmpd_routes_of_administration":
#         print(table_name)
        rowcount = 0
        for each_row in value:
            try:
                cursor.execute(f"""insert into idsp_xevmpd_routes_of_administration (`key`, value)
                            select 
                            '{each_row["id"]}', 
                            '{each_row["term-name"]}'
                            where not exists
                            (select `key` from idsp_xevmpd_routes_of_administration where `key` = '{each_row["id"]}' limit 1)""")
                conn.commit()
            except Exception as e:
                print(e)
            if cursor.rowcount != 0:
                rowcount += 1
        if rowcount == 0 :
            print("already inserted")
        else:
            print(rowcount," rows inserted in", table_name) 
            
            
            
            
