import sqlite3

# The name of the database
DB_NAME = "sqlite_db.db"


# # Create new database
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn.autocommit)
#     print(sqlite3.sqlite_version)


# # Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

# The list of tuple courses
courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C# course", 151, 10)
]

# Inset all values for the list to the database
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """INSERT INTO courses VALUES (?, ?, ?, ?)"""
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty >= 50"
    sql_cursor = sqlite_conn.execute(sql_request)
    for record in sql_cursor:
        print(record)
    # records = sql_cursor.fetchall()
    # print(records)
