from typing import Literal, Optional

from pydantic import BaseModel


TICKERS_LIST = Literal['BTC', 'ETH', 'USD', 'USDT', 'LTC', 'BCH', 'XMR', 'TUSD', 'USDC', 'EUR', 'EUROC', 'DOGE', 'TRX', 'DASH', 'BNB', 'TON', 'POL', 'TRY', 'UAH', 'KZT', 'RUB']

class TickerInfo(BaseModel):
    price: float

class TickerGet(BaseModel):
    base_currency: str
    currencies: Optional[dict[str, TickerInfo]] = None
