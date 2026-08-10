from sqlalchemy import create_engine, text

from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:

    result = conn.execute(
        text("PRAGMA table_info(document_chunks)")
    )

    for row in result:
        print(row)