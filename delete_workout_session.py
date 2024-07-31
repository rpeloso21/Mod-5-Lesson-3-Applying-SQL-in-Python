from connect_mysql import connect_database

def delete_workout_session(session_id):
    conn = connect_database()

    if conn is not None:
        try:
            cursor = conn.cursor()    

            session_to_delete = (session_id,)    

            query = "delete from workoutsessions where session_id = %s"

            cursor.execute(query, session_to_delete)
            conn.commit()
            print("Session removed successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_workout_session(3)