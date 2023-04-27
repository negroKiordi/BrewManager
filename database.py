import mysql.connector as mysql


def connect(db_name):
    try:
        return mysql.connect(
            host='localhost',
            user='root',
            password='Ale#1980Sole#1981',
            database=db_name)
    except Error as e:
        print(e)
        

if __name__ == '__main__':
    db = connect("Brewry")
    cursor = db.cursor()
    
    cursor.execute("show tables")
    project_records = cursor.fetchall()
    print('\n  Tables: ')
    for r in project_records:
        print('   -',r[0])

    print('\n')
    
    db.close()