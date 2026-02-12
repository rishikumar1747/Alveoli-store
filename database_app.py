import sqlite3

def connect_db(db_name="users.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()

def insert_user(conn, name, email, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()

def fetch_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\n--- User Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")

def update_user_age(conn, user_id, new_age):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()

def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def main():
    conn = connect_db()
    create_table(conn)

    # Insert sample users
    insert_user(conn, "Alice", "alice@example.com", 25)
    insert_user(conn, "Bob", "bob@example.com", 30)
    insert_user(conn, "Charlie", "charlie@example.com", 28)

    # Fetch and display users
    fetch_users(conn)

    # Update Bob's age
    update_user_age(conn, 2, 35)
    print("\nAfter updating Bob's age:")
    fetch_users(conn)

    # Delete Charlie
    delete_user(conn, 3)
    print("\nAfter deleting Charlie:")
    fetch_users(conn)

    conn.close()

if __name__ == "__main__":
    main()