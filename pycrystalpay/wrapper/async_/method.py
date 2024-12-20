from typing import Union
from pycrystalpay.types import MethodList, PAYMENT_METHODS, MethodGet

from .base import BaseApiWrapper


class Method(BaseApiWrapper):
    """Providing `method` methods

    Doc - https://docs.crystalpay.io/metody-api/method-metody
    """

    async def method_list(self, compact: bool=False) -> MethodList:
        """Getting methods list

        Doc - https://docs.crystalpay.io/metody-api/method-metody/poluchenie-spiska-metodov
        
        Returns:
            MeInfo: api parsed response
        """
        data = await self._send_request(
            "POST",
            "method/list/",
            {
                "compact": compact
            }
        )
        return MethodList.model_validate(data)
    
    async def method_get(self, method: Union[PAYMENT_METHODS, str]) -> MethodGet:
        """Getting information about method

        Doc - https://docs.crystalpay.io/metody-api/method-metody/poluchenie-metoda
        
        Returns:
            MeInfo: api parsed response
        """
        data = await self._send_request(
            "POST",
            "method/get/",
            {
                "method": method
            }
        )
        return MethodGet.model_validate(data)

