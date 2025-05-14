import random
import string
def make_email(domain='test.com'):
    local = ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=8
        )
    )
    return f"{local}@{domain}"


def make_password(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
