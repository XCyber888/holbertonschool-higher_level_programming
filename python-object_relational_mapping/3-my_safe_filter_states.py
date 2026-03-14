#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument,
safe from MySQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )
    cursor = db.cursor()
    # SQL injection-dan qorunmaq üçün '%s' placeholder istifadə edirik
    # Və arqumenti execute funksiyasının ikinci parametri kimi ötürürük
    query = "SELECT * FROM states WHERE name LIKE BINARY %s \
ORDER BY states.id ASC"
    cursor.execute(query, (state_searched,))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
