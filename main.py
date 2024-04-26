from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_adresses


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

w3.middleware_onion.inject(geth_poa_middleware, layer=0)


contract = w3.eth.contract(address=contract_adresses, abi=abi)

accounts = w3.eth.accounts
print (contract.address)
print (f"Баланс смарт контракта {w3.eth.get_balance(contract.address)}")
# Вывод баланса каждого аккаунта
for account in accounts:
    balance = w3.eth.get_balance(account)
    print(f"Аккаунт: {account}, Баланс: {balance} wei")