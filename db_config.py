from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'db_emp'
app.config['MYSQL_DATABASE_HOST'] = '10.2.1.27'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
