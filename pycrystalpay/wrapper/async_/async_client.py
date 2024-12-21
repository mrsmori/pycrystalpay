from .me import Me
from .balance import Balance
from .method import Method
from .invoice import Invoice
from .payoff import Payoff
from .ticker import Ticker


class AsyncCrystalPay(Me, Balance, Method, Invoice, Payoff, Ticker):
    """Асинхронный клиент
    """
