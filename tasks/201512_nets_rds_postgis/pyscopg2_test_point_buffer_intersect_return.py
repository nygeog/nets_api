import psycopg2
import _secret_info
import csv 
from datetime import datetime

dbname   = _secret_info.s_dbname
user     = _secret_info.s_user
host     = _secret_info.s_host
password = _secret_info.s_password

def getNetsFromLatLng(inLngLat,bufDist):
	fileDate = datetime.now().strftime('%Y%m%d_%H%M%S')
	fd = fileDate

	#ADD ERROR HANDLING FOR TOO LARGE OF BUFFERS

	try:
	    conn = psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
	except:
	    print "I am unable to connect to the database"

	cur = conn.cursor()

	sql1 = """CREATE TABLE latlngtablebuffer_"""+fd+""" AS SELECT ST_Buffer(ST_GeomFromText('POINT("""+inLngLat+""")'), """+bufDist+""")"""
	sql2 = """CREATE TABLE latlngtablebufferintersect_"""+fd+""" AS (SELECT ST_Intersection(a.geom, b.st_buffer), a.*, b.* FROM nets_23_cty_ne as a, latlngtablebuffer_"""+fd+""" as b WHERE ST_Intersects(a.geom, b.st_buffer))"""
	sql3 = """SELECT * from latlngtablebufferintersect_"""+fd+""""""
	sql4 = """DROP TABLE latlngtablebuffer_"""+fd#+""", latlngtablebufferintersect_"""+fd
	
	print 'creating buffer'
	cur.execute(sql1)
	print 'executing intersect'
	cur.execute(sql2)
	print 'selecting data'
	cur.execute(sql3)

	rows = cur.fetchall()

	cur.execute("""SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'latlngtablebufferintersect_"""+fd+"""'""")

	db_cols = cur.fetchall()

	col_list = []

	for i in db_cols:
		print i[3]
		col_list.append(i[3])

	with open('test_point_buffer_intersect_return_'+fd+'.csv', 'w') as fp:
	    a = csv.writer(fp, delimiter=',')
	    a.writerow(col_list)
	    a.writerows(rows)

	print 'deleting table'
	cur.execute(sql4)

getNetsFromLatLng('-74.0059 40.7127','0.01') #unprojected, in degrees, need to turn to meters. 
