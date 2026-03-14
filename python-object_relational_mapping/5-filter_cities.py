#!/usr/bin/python3
"""
Lists all cities of a state given as argument from hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # SQL query-ni tək sətirdə və ən sadə formada saxlayırıq
    query = "SELECT cities.name FROM cities \
JOIN states ON cities.state_id = states.id \
WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (sys.argv[4],))
    
    rows = cur.fetchall()
    # Şəhər adlarını list comprehension ilə çıxarırıq
    cities = [row[0] for row in rows]
    # Çap formatı: 'City1, City2, City3'
    print(", ".join(cities))
    
    cur.close()
    db.close()
