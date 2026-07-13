import pymysql

# from password_utills import get_decrypted_password

def connect_to_mysql():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="lionking",
        database="test"
    )
    # print(get_decrypted_password)
    print("connected  to  Mysql succesfully")
    conn.close()
    
if __name__=="__main__":
    connect_to_mysql()