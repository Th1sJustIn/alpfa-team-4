from database import create_connection

conn = create_connection()

if conn:
    cursor = conn.cursor()
    cursor.execute("show tables") ## sql function
    tables = cursor.fetchall()
    
    for table in tables:
        print(table[0])  
    conn.close()  # Close the connection when done
else:
    print("Failed to connect to the database") 
