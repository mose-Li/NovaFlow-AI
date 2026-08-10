from sqlalchemy import create_engine, text
from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:

    rows = conn.execute(
        text("PRAGMA table_info(document_contents)")
    )

    for row in rows:
        print(row)