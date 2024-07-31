from connect_mysql import connect_database


def add_member(id, name, age):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()


            query = "insert into Members (id, name, age) values (%s, %s, %s)"

            cursor.execute(query, (id, name, age))
            conn.commit()
            print("New member added successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

add_member(5, "Bruce Banner", "27")