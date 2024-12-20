from .me import Me
from .balance import Balance
from .method import Method
from .invoice import Invoice


class AsyncCrystalPay(Me, Balance, Method, Invoice):
    """Асинхронный клиент
    """
