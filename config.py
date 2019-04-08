import os

db_user = os.getenv("DB_USER", "insights")
db_password = os.getenv("DB_PASS", "insights")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "test_db")

db_uri = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
db_pool_timeout = int(os.getenv("DB_POOL_TIMEOUT", "5"))
db_pool_size = int(os.getenv("DB_POOL_SIZE", "5"))
