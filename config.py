import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# On Vercel only /tmp is writable, and it's wiped between invocations.
IS_SERVERLESS = bool(os.environ.get("VERCEL"))
_default_sqlite_dir = "/tmp" if IS_SERVERLESS else os.path.join(BASE_DIR, "instance")
os.makedirs(_default_sqlite_dir, exist_ok=True)

_db_url = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(_default_sqlite_dir, 'crm.db')}"
# SQLAlchemy 2.x doesn't accept the old "postgres://" scheme some providers hand out
if _db_url.startswith("postgres://"):
    _db_url = _db_url.replace("postgres://", "postgresql://", 1)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me")
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = Falseimport os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'crm.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
