import bcrypt


def generate_password_hash(password: str) -> str:
    """
    Generate a hashed password using bcrypt.
    """
    # return password_context.hash(password)
    return bcrypt.hashpw(
        password=password.encode(encoding="utf-8"), salt=bcrypt.gensalt()
    ).decode(encoding="utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    Returns True if the passwords match, False otherwise.
    """
    # return password_context.verify(secret=plain_password, hash=hashed_password)
    return bcrypt.checkpw(
        password=plain_password.encode(encoding="utf-8"),
        hashed_password=hashed_password.encode(encoding="utf-8"),
    )

