import uuid
import os
from dotenv import load_dotenv
from langchain_postgres import PostgresChatMessageHistory
import psycopg

load_dotenv()

def get_chat_history(session_name : str):

    DB_URI = os.getenv("POSTGRES_DB_URL")
    sync_connection = psycopg.connect(DB_URI)

    table_name = "chat_history"
    session_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, session_name))

    PostgresChatMessageHistory.create_tables(sync_connection, table_name)

    chat_history = PostgresChatMessageHistory(
    table_name, session_id, sync_connection=sync_connection
    )
    
    return chat_history


