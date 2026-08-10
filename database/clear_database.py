from sqlalchemy import create_engine, text

from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

with engine.begin() as conn:

    conn.execute(text("DELETE FROM embeddings"))
    conn.execute(text("DELETE FROM document_chunks"))
    conn.execute(text("DELETE FROM document_contents"))
    conn.execute(text("DELETE FROM documents"))

print("Database cleared successfully!")