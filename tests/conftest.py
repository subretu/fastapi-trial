import pytest
import psycopg2

# DB接続用関数
def get_connection():

    user = os.getenv("POSTGRES_USER", None)
    pwd = os.getenv("POSTGRES_PASS", None)
    server = os.getenv("POSTGRES_HOST", None)
    port = os.getenv("POSTGRES_HOST", None)
    db = os.getenv("POSTGRES_PORT", None)

    con = psycopg2.connect(
        "host="
        + server
        + " port="
        + port
        + " dbname="
        + db
        + " user="
        + user
        + " password="
        + pwd
    )

    return con

@pytest.fixture
def cursor():
    with get_connection() as conn:
        with conn.cursor() as cur:
            print("\n" + "START TEST")
            yield cur
            print("\n" + "END TEST")
        conn.rollback()  # テスト完了後にロールバックする