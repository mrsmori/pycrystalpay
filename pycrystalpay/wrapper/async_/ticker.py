from typing import List, Optional, Union

from pycrystalpay.types import TICKERS_LIST, TickerGet
from .base import BaseApiWrapper


class Ticker(BaseApiWrapper):
    """Методы `tickers` 

    Doc - https://docs.crystalpay.io/metody-api/ticker-kursy-valyut
    """

    async def ticker_list(self) -> List[str]:
        """Получить список валют

        Doc - https://docs.crystalpay.io/metody-api/ticker-kursy-valyut/poluchenie-spiska-valyut
        """
        data = await self._send_request(
            "POST",
            "ticker/list/"
        )

        return data.get("tickers") #type: ignore
    
    async def ticker_get(self, tickers: List[Union[TICKERS_LIST, str]], base_currency: Optional[Union[TICKERS_LIST, str]]=None) -> TickerGet:
        """Получить отношения валют к другой валюте

        Doc - https://docs.crystalpay.io/metody-api/ticker-kursy-valyut/poluchenie-kursa-valyut
        """
        data = await self._send_request(
            "POST",
            "ticker/get/",
            {
                "tickers": tickers,
                "base_currency": base_currency
            }
        )

        return TickerGet.model_validate(data)

