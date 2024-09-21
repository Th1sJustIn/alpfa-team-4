from dotenv import load_dotenv
import os 
import pymysql

# Load environment variables
if not load_dotenv():
    print('No env file found')
    exit()

# Database credentials
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')

# Function to create a database connection
def create_connection():
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        ) 

        if connection:
            print('Connection successful')
            return connection
    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
