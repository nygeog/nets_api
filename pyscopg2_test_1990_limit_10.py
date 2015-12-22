import psycopg2
import _secret_info
import csv 

dbname   = _secret_info.s_dbname
user     = _secret_info.s_user
host     = _secret_info.s_host
password = _secret_info.s_password

try:
    conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""SELECT * from nets_23_cty_ne WHERE beh_end < 1991 LIMIT 10""")

rows = cur.fetchall()

cur.execute("""SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'nets_23_cty_ne'""")

db_cols = cur.fetchall()

col_list = []

for i in db_cols:
	print i[3]
	col_list.append(i[3])

with open('data/test_1990_limit_10.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerow(col_list)
    a.writerows(rows)

print "\nShow me the database:\n"
for row in rows:
    print "   ", row


