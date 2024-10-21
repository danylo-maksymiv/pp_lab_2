#address.py

from erc721 import Erc721
from erc20 import Erc20
from hex_generator import HexGenerator
from contract import Contract
from blockchain import Blockchain
from transaction import Transaction


class Address:
    def __init__(self):
        self.__address = HexGenerator().generate_address()
        self.__eth_balance = 0
        self.__nonce = -1
        self.__token_balance = dict()

        chain = Blockchain()
        chain.add_address(self)

    @property
    def address(self):
        return self.__address

    @property
    def eth_balance(self):
        return self.__eth_balance

    @eth_balance.setter
    def eth_balance(self, value):
        self.__eth_balance = value

    @property
    def token_balance(self):
        return self.__token_balance

    def set_token_balance(self, contract_address, amount, *args):
        if args:
            ids = args[0]
        chain = Blockchain()

        if isinstance(chain.get_contract_by_address(contract_address), Erc721):
            if contract_address not in self.__token_balance.keys():
                self.__token_balance[contract_address] = [0, []]
            self.__token_balance[contract_address][1] = ids
            self.__token_balance[contract_address][0] += amount
        elif isinstance(chain.get_contract_by_address(contract_address), Erc20):
            if contract_address not in self.__token_balance.keys():
                self.__token_balance[contract_address] = [0, None]
            self.__token_balance[contract_address][0] += amount

    @property
    def nonce(self):
        return self.__nonce

    @nonce.setter
    def nonce(self, nonce):
        self.__nonce = nonce

    def deploy_contract(self, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, type_, *args):
        if type_ == 'erc20':
            supply, symbol = args[0], args[1]
            contract = Erc20(self.__address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol)
        elif type_ == 'erc721':
            supply, symbol = args[0], args[1]
            contract = Erc721(self.__address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol)
        else:
            contract = Contract(self.__address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names)

        if contract.contract_address is None:
            return None
        else:
            return contract

    def call_contract(self, contract, function_name, value, gas_limit, max_fee, priority_fee, *args, **kwargs):
        if contract is not None:
            contract(function_name, self.__address, value, gas_limit, max_fee, priority_fee, *args, **kwargs)
        else:
            print('Such contract doesn\'t exist.')

    def transfer_eth(self, to_address, value, gas_limit, max_fee, priority_fee, input_data):
        chain = Blockchain()
        to_address_instance = chain.get_address_by_address(to_address)
        if to_address_instance is not None:
            transaction = Transaction(self.__address, to_address, value, gas_limit, max_fee, priority_fee, 21000, input_data)
            if transaction.status == 'Confirmed':
                print(f'Successfully transferred {value} $ETH to {to_address_instance.address}! Transaction hash: {transaction.hash}.')
                self.__eth_balance -= (value + transaction.gas_fee)
                to_address_instance.eth_balance += value
            else:
                print(f'Transaction was rejected, try to add more gas! Transaction hash: {transaction.hash}')
        else:
            print('Such address doesn\'t exist.')