import pymysql.cursors
### TEST_PYMYSQL_BEST_01
### GET SQL
################################
# CODE HERE NA KRUSH!
def main():
    # just 'hello world!'
    print('hello world!')
    # setting up sever infomations
    # setSQL(host, port, username, password)
    # example: setSQL(h='localhost', po=8889, u='root', pa='root') << default
    connect = setSQL('localhost', 8889, 'root', 'root') #create object(refer to SEVER dai na)
    getSQL(connect, "SELECT * FROM new_schema.coordinate") #getSQL(indicate sever here, queries here, all = 1 or 0)
    #uncomment below to INSERT

    #insertSQL(connect)

    #Example: insertSQL(connect, "INSERT INTO new_schema.coordinate (`x_coordinate`, `y_coordinate`) VALUES (7, 77)")
################################
def getSQL(connect, q="SELECT * FROM new_schema.coordinate", all = 0):
    try: # TRY if error CONTINUE
        with connect.cursor() as cursor:
            sql = q
            cursor.execute(sql)
            if all == 0:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            print(result)
    finally:
        connect.close()

def insertSQL(connect, q="INSERT INTO new_schema.coordinate (`x_coordinate`, `y_coordinate`) VALUES (7, 77)"):
    try: # TRY if error CONTINUE
        with connect.cursor() as cursor:
            sql = q
            cursor.execute(sql)
        connect.commit()
    finally:
        connect.close()

def setSQL(h='localhost', po=8889, u='root', pa='root'):
    return pymysql.connect(host= h,
                            port= po,
                            user= u,
                            password= pa,
                            cursorclass=pymysql.cursors.DictCursor)
################################
if __name__ == '__main__': # check if current .py is running na
    main()
################################
