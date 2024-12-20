# pyCrystalPay

## Install

From Pypi\
```pip install pycrystalpay```

## Async 
### Create instance
```python
from pycrystalpay import AsyncCrystalPay, types


client = AsyncCrystalPay(
    auth_login="mylogin",
    auth_secret="mysecret",
    wait_cooldown=True # auto wait 5 rps
)
```
### Methods /me/

[/me/info](https://docs.crystalpay.io/metody-api/me-kassa/poluchenie-informacii-o-kasse)
```python
response: types.MeInfo = await client.me_info()
```

### Methods /balance/
[/balance/list](https://docs.crystalpay.io/metody-api/balance-balansy/poluchenie-spiska-balansov)
```python
response: types.BalanceList = await client.balance_list(hide_empty=True)
```
[/balance/get](https://docs.crystalpay.io/metody-api/balance-balansy/poluchenie-spiska-balansov)
```python
response: types.BalanceGet = await client.balance_list(method="BITCOIN")
```

### Methods /method/
[/method/list](https://docs.crystalpay.io/metody-api/method-metody/poluchenie-spiska-metodov)
```python
response: types.MethodList = await client.method_list(compact=True)
```