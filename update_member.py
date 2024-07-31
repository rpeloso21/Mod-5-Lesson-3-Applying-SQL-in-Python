from connect_mysql import connect_database


def update_member(member_id, age):
    conn = connect_database()

    if conn is not None:
        try:
            
            cursor = conn.cursor()

            query = "update members set age = %s where id = %s"

            cursor.execute(query, (age, member_id))
            conn.commit()
            print("Member details updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

update_member(2, "35")