import hashlib
import sqlite3
from pathlib import Path


# =========================================================
# DATABASE FILE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATABASE_NAME = BASE_DIR / "laptop.db"


# =========================================================
# PASSWORD HASHING
# =========================================================

def hash_password(password):
    """
    Convert a password into a protected hash.
    """

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


# =========================================================
# INITIALIZE DATABASE
# =========================================================

def initialize_database():
    """
    Create the users table and default admin account.
    """

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # # Default admin account
    # admin_password = hash_password("admin")

    # cursor.execute(
    #     """
    #     INSERT OR IGNORE INTO users (
    #         username,
    #         password_hash
    #     )
    #     VALUES (?, ?)
    #     """,
    #     (
    #         "admin",
    #         admin_password
    #     )
    # )

    # =====================================================
    # MULTIPLE DEFAULT USERS
    # =====================================================

    users = [
        ("admin", "admin"),
        ("john", "john123"),
        ("rahul", "rahul123"),
        ("student", "student123"),
        ("manager", "manager123"),
    ]

    # =====================================================
    # INSERT USERS
    # =====================================================

    for username, password in users:

        password_hash = hash_password(password)

        cursor.execute(
            """
            INSERT OR IGNORE INTO users (
                username,
                password_hash
            )
            VALUES (?, ?)
            """,
            (
                username,
                password_hash
            )
        )

    connection.commit()
    connection.close()


# =========================================================
# AUTHENTICATE USER
# =========================================================

def authenticate_user(username, password):
    """
    Check username and password.

    Returns:
        (id, username) if valid
        None if invalid
    """

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = connection.cursor()

    password_hash = hash_password(password)

    cursor.execute(
        """
        SELECT id, username
        FROM users
        WHERE username = ?
        AND password_hash = ?
        """,
        (
            username,
            password_hash
        )
    )

    user = cursor.fetchone()

    connection.close()

    return user
