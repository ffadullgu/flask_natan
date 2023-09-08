from app import app
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Mysql Settings
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or 'L51sJWZ2fftDHwo48o9j'
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or 'containers-us-west-144.railway.app' # localhost
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'flaskcrud'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT')
# MySQL Connection
mysql = MySQL(app)
