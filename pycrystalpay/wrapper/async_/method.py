from pycrystalpay.types import MethodList

from .base import BaseApiWrapper


class Method(BaseApiWrapper):
    """Providing `method` methods

    Doc - https://docs.crystalpay.io/metody-api/method-metody
    """

    async def method_list(self, compact: bool=False) -> MethodList:
        """Getting information about merchant

        Doc - https://docs.crystalpay.io/metody-api/me-kassa/poluchenie-informacii-o-kasse
        
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
