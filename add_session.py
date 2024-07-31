from connect_mysql import connect_database


def add_session(session_id, member_id, session_date, session_time, activity):

    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()


            query = "insert into workoutsessions (session_id, member_id, session_date, session_time, activity) values (%s, %s, %s, %s, %s)"

            cursor.execute(query, (session_id, member_id, session_date, session_time, activity))
            conn.commit()
            print("New session added successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

add_session(4, 4, "2022-04-20", "45 minutes", "300 calories")