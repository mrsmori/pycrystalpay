import os
import pytest

from dotenv import load_dotenv

from pycrystalpay import AsyncCrystalPay


load_dotenv()

def test_creation_client():
    client = AsyncCrystalPay("", "")

class TestClient:
    client: AsyncCrystalPay

    @classmethod
    def setup_class(cls):
        cls.client = AsyncCrystalPay(
            os.getenv("MERCHANT_NAME"),
            os.getenv("MERCHANT_TOKEN"),
        )

    @pytest.mark.asyncio(loop_scope="session")
    async def test_me_info(self):
        await self.client.me_info()


    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize("hide_empty", [
        True,
        False
    ])
    async def test_balance_list(self, hide_empty: bool):
        await self.client.balance_list(hide_empty)

    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize("method", [
        "BITCOIN",
        "ETHEREUM"
    ])
    async def test_balance_get(self, method: str):
        await self.client.balance_get(method)