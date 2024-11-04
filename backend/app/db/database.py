import mongoengine


def connect_db():
    print("Database connection skipped (no database configured).")

def close_db():
    print("Database disconnection skipped (no database configured).")
# async def connect_db():
#     # Make sure this function does something and does not return None
#     mongoengine.connect(db="your_database_name", host="localhost", port=27017)

# async def close_db():
#     # This should close the MongoDB connection
#     mongoengine.disconnect()
