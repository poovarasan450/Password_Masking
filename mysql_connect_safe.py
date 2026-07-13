import mysql.connector

from password_utills import get_decrypted_password

def connect_to_mysql():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="test"
    )
    
    print("connected  to  Mysql succesfully")
    conn.close()
    
if __name__=="__main__":
    connect_to_mysql()