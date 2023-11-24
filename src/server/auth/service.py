import hashlib


async def get_password_hash(password: str) -> str:
    hast_obj = hashlib.sha256()
    password_encode = password.encode("utf-8")
    hast_obj.update(password_encode)
    hash_data = hast_obj.hexdigest()

    return hash_data

