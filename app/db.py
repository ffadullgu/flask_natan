from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_URL'] = os.getenv('MYSQL_URL') or 'mysql://root:L51sJWZ2fftDHwo48o9j@containers-us-west-144.railway.app:5876/railway'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'L51sJWZ2fftDHwo48o9j'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'containers-us-west-144.railway.app' # localhost
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'railway'
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT') or '5876'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# MySQL Connection
mysql = MySQL(app)
