import os
import pytest

from dotenv import load_dotenv

from pycrystalpay import AsyncCrystalPay


load_dotenv()

def test_creation_client():
    AsyncCrystalPay("", "")

class TestClient:
    client: AsyncCrystalPay

    @classmethod
    def setup_class(cls):
        cls.client = AsyncCrystalPay(
            os.getenv("MERCHANT_NAME"),
            os.getenv("MERCHANT_TOKEN"),
            os.getenv("MERCHANT_SALT")
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

    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize("compact", [
        False,
        True
    ])
    async def test_method_list(self, compact: bool):
        await self.client.method_list(compact)

    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize("method", [
        "BITCOIN",
        "ETHEREUM"
    ])
    async def test_method_get(self, method: str):
        await self.client.method_get(method)

    @pytest.mark.asyncio(loop_scope="session")
    @pytest.mark.parametrize("method, enabled, extra_commission_percent", [
        ("BITCOIN", False, 10),
        ("BITCOIN", True, 10),
        ("BITCOIN", True, 0),
        ("BITCOIN", None, 10),
        ("BITCOIN", None, 0),
        ("BITCOIN", False, None),
        ("BITCOIN", True, None)
    ])
    async def test_method_edit(self, method: str, enabled: bool, extra_commission_percent: int):
        response = await self.client.method_edit(method, enabled, extra_commission_percent)
        assert response is True, "edit cause error"

    @pytest.mark.asyncio(loop_scope="session")
    async def test_method_edit_empty_params(self):
        with pytest.raises(ValueError):
            await self.client.method_edit("BITCOIN")

    @pytest.mark.asyncio(loop_scope="session")
    async def test_create_invoice(self):
        response = await self.client.invoice_create(
            "100",
            "purchase",
            "1"
        )
        assert response.id != ""
        assert response.url != ""
        assert response.rub_amount != 0
        updated_info_requst = await self.client.invoice_info(response.id)

        assert updated_info_requst.is_payed is False

    @pytest.mark.skip
    @pytest.mark.asyncio(loop_scope="session")
    async def test_create_payoff(self):
        response = await self.client.payoff_create(
            "SBPP2P",
            "somewallet",
            1,
            "amount"
        )

    @pytest.mark.asyncio(loop_scope="session")
    async def test_ticker_list(self):
        await self.client.ticker_list()

    @pytest.mark.asyncio(loop_scope="session")
    async def test_ticker_get(self):
        await self.client.ticker_get(["ETH", "BTC"], "BNB")

