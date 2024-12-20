from pydantic import BaseModel


class MeInfo(BaseModel):
    """Response of me/info method

    Doc - https://docs.crystalpay.io/metody-api/me-kassa/poluchenie-informacii-o-kasse
    """
    id: int
    name: str
    status_level: int
    created_at: str
