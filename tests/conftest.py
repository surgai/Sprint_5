import pytest
import time
import secrets
import string

@pytest.fixture
def generate_data(request):
    alphabet = string.ascii_letters + string.digits
    request.cls.password = ''.join(secrets.choice(alphabet) for i in range(6))
    request.cls.login = f"Nuykin_9_{request.cls.password}@ya.ru"
#    request.cls.password = "qwerrrrty21"