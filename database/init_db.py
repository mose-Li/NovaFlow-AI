from sqlalchemy import create_engine, text
from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_filename TEXT NOT NULL,
            stored_filename TEXT NOT NULL,

            file_type TEXT NOT NULL,
            mime_type TEXT,

            file_size INTEGER NOT NULL,

            checksum TEXT UNIQUE,

            upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            status TEXT DEFAULT 'READY'
        )
    """))
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS document_contents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            page_count INTEGER DEFAULT 1,
            word_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(document_id)
                REFERENCES documents(id)
                ON DELETE CASCADE
        )
    """))
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS document_chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            content TEXT NOT NULL,
            token_count INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(document_id)
                     REFERENCES documents(id)
         )
         """))
    conn.execute(text("""
             CREATE TABLE IF NOT EXISTS embeddings (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,

                       chunk_id INTEGER NOT NULL,

                        model_name TEXT NOT NULL,

                        embedding TEXT NOT NULL,

                        dimension INTEGER NOT NULL,

                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                       FOREIGN KEY(chunk_id)
                                 REFERENCES document_chunks(id)
                                 ON DELETE CASCADE
              )
       """))

    conn.commit()
print("Database initialized successfully!")