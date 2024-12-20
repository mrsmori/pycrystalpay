from pycrystalpay.types import MeInfo

from .base import BaseApiWrapper


class Me(BaseApiWrapper):
    """Providing `me` methods

    Doc - https://docs.crystalpay.io/metody-api/me-kassa
    """

    async def me_info(self) -> MeInfo:
        """Getting information about merchant

        Doc - https://docs.crystalpay.io/metody-api/me-kassa/poluchenie-informacii-o-kasse
        
        Returns:
            MeInfo: api parsed response
        """
        data = await self._send_request(
            "POST",
            "me/info/"
        )
        return MeInfo.model_validate(data)
