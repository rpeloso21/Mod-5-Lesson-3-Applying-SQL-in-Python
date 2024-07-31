from connect_mysql import connect_database


def get_members_in_age_range(start_age, end_age):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "select * from members where age > %s and age < %s"

            cursor.execute(query, (start_age, end_age))

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

get_members_in_age_range(25, 30)