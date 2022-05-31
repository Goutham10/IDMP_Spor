# import mysql.connector.pooling

# db_config = {
#             'user' : 'root',
#             'database' : 'persons_db',
#             'host' : 'localhost',
#             'password' : 'Goutham@1005',
#             'port' : 3306
#         }

# connection_pool = mysql.connector.pooling.MySQLConnectionPool(
#     pool_name = "new_pool",
#     pool_size = 10,
#     # auth_plugin='mysql_native_password',
#     **db_config)


# print(connection_pool)


import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", 
                               port="3306", 
                               user="root", 
                               password="Goutham@1005", 
                               auth_plugin="mysql_native_password", 
                               database="idmp_spor")
mycursor = mydb.cursor()


mycursor.execute(f'insert into idsp_xevmpd_pharmaceutical_dose_forms(`key`,value,type) values(%s,%s,%s)', ("a","dsf","ssd"))
mydb.commit()
print("inserted")