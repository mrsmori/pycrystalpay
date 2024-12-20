# pyCrystalPay

## Install

From Pypi\
```pip install pycrystalpay```

## Async 
### Инициализация
```python
from pycrystalpay import AsyncCrystalPay, types


client = AsyncCrystalPay(
    auth_login="mylogin",
    auth_secret="mysecret",
    wait_cooldown=True # auto wait 5 rps
)
```
### Методы /invoice/
Создание платежа\
[/invoice/create](https://docs.crystalpay.io/metody-api/invoice-platezhi/sozdanie-invoisa)
```python
payment: types.InvoiceCreate = await client.invoice_create("100","purchase","1")

payment.url # Ссылка для оплаты
payment.id
```

Получение информации о платеже по id\
[/invoice/info](https://docs.crystalpay.io/metody-api/invoice-platezhi/poluchenie-informacii-ob-invoise)
```python

response: types.InvoiceInfo = await client.invoice_info("id_платежа")

if response.is_payed:
    ...
```


### Методы /me/

[/me/info](https://docs.crystalpay.io/metody-api/me-kassa/poluchenie-informacii-o-kasse)
```python
response: types.MeInfo = await client.me_info()
```

### Методы /balance/
[/balance/list](https://docs.crystalpay.io/metody-api/balance-balansy/poluchenie-spiska-balansov)
```python
response: types.BalanceList = await client.balance_list(hide_empty=True)
```

[/balance/get](https://docs.crystalpay.io/metody-api/balance-balansy/poluchenie-spiska-balansov)
```python
response: types.BalanceGet = await client.balance_list(method="BITCOIN")
```

### Методы /method/
[/method/list](https://docs.crystalpay.io/metody-api/method-metody/poluchenie-spiska-metodov)
```python
response: types.MethodList = await client.method_list(compact=True)
```

[/method/get](https://docs.crystalpay.io/metody-api/method-metody/poluchenie-spiska-metodov)
```python
response: types.MethodInfo = await client.method_get(method="BITCOIN")
```

[/method/edit](https://docs.crystalpay.io/metody-api/method-metody/izmenenie-nastroek-metoda)
```python
response: bool = await client.method_edit(method="BITCOIN", enabled=True, extra_commission_percent=0)
```