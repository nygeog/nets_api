# NETS API for 25 year national dataset

## Getting data via simple SQL query
![](img/pyscopg2_test_1990_limit_10.gif)

## Buffering and intersecting data via PostGIS SQL
![](img/pyscopg2_test_buffer_intersect_return.gif)

## Protecting your _secret_info (database username and password) with .gitignore

###.gitignore<a name="gitignore"></a>
gitignore is a file you store in your repo, name the file **.gitignore**. Yes, with the **.** starting the file extension, with no file name.

	# Secret Python files #
	###################
	*_secret_info.py
	*.pyc
	

	
###\_secret_info.py 
<a name="secret_info"></a>
Here's what your **\_secret_info.py** file should look like, if you choose to use it. 

	s_dbname   = 'nets'
	s_user     = <username>
	s_host     = <db host address>
	s_password = <password>
	
	
##To Do:
* port to R
* reference and create nets_api.py with functions in that file
* include reference modules