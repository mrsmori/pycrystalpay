import warnings
from typing import Union
from pycrystalpay.types import INVOICE_TYPES, PAYMENT_METHODS, InvoiceInfo

from .base import BaseApiWrapper


class Invoice(BaseApiWrapper):
    """Методы `invoice` 
    Doc - https://docs.crystalpay.io/metody-api/invoice-platezhi
    """

    async def invoice_create(
            self,
            amount: int,
            type_: INVOICE_TYPES,
            lifetime: int,
            amount_currency: str=None, # type: ignore
            required_method: Union[PAYMENT_METHODS]=None, # type: ignore
            payer_details: str=None, # type: ignore
            description: str=None, # type: ignore
            extra: str=None, # type: ignore
            redirect_url: str=None, # type: ignore
            callback_url: str = None # type: ignore


        ) -> 'InvoiceWorker':
        """Создание платежа

        Args:
            amount (int): Сумма к оплате
            type (INVOICE_TYPES): Тип инвойса
            lifetime (int): Время жизни инвойса в минутах
            amount_currency (str, optional): Валюта суммы. Defaults to None.
            required_method (Union[PAYMENT_METHODS], optional): Заранее заданный метод, плательщик не сможет выбрать другой. Defaults to None.
            payer_details (str, optional): E-mail плательщика. Defaults to None.
            description (str, optional): Описание или назначение. Defaults to None.
            extra (str, optional): Любые данные, например ID платежа в вашей системе. Defaults to None.
            redirect_url (str, optional): Ссылка для перенаправления после оплаты. Defaults to None.
            callback_url (str, optional): Ссылка для отправки http callback уведомления об оплате. Defaults to None.
        """
        data = await self._send_request(
            "POST",
            "invoice/create/",
            {
                "amount": amount,
                "type": type_,
                "lifetime": lifetime,
                "amount_currency": amount_currency,
                "required_method": required_method,
                "payer_details": payer_details,
                "description": description,
                "extra": extra,
                "redirect_url": redirect_url,
                "callback_url": callback_url

            }
        )
        return InvoiceWorker(
            wrapper=self,
            id_=data.get("id", None),
            url=data.get("url",  None),
            type_=data.get("type",  None),
            rub_amount=data.get("rub_amount", None)
        )
    
    async def invoice_info(self, id_: str) -> InvoiceInfo:
        """Получить информацию о платеже

        Args:
            id_ (str): id платежа
        """
        data = await self._send_request(
            "POST",
            "invoice/info/",
            {
                "id": id_
            }
        )
        return InvoiceInfo.model_validate(data)
    
class InvoiceWorker:
    """Класс для работы с платежом
    """

    def __init__(self, wrapper: Invoice, id_: str, url: str, type_: INVOICE_TYPES, rub_amount: int):
        self.__wrapper = wrapper
        self.__id = id_
        self.__url = url
        self.__type = type_
        self.__rub_amount = rub_amount
        self.__invoice_data: InvoiceInfo = None #type: ignore

    @property
    def id(self) -> str:
        """ID платежа
        """
        return self.__id
    
    @property
    def url(self) -> str:
        """Ссылка для оплаты
        """
        return self.__url
    
    @property
    def type(self) -> INVOICE_TYPES:
        """Тип платежа
        """
        return self.__type
    
    @property
    def rub_amount(self) -> int:
        """Сумма платежа в рублях
        """
        return self.__rub_amount
    
    @property
    def info(self) -> InvoiceInfo:
        """Получение кешированной ифнормации о платеже

        Кешируется ответ от .update_info()
        """
        if self.__invoice_data is None:
            warnings.warn("нет информации о платеже. Используйте .update_info перед её запросом.",UserWarning)
        return self.__invoice_data
    
    @property
    def is_payed(self) -> bool:
        data = self.info
        if data is None:
            return False
        return data.state == "payed"
    
    async def refresh(self) -> InvoiceInfo:
        """Обновление информации о платеже
        """
        self.__invoice_data = await self.__wrapper.invoice_info(self.id)
        return self.info