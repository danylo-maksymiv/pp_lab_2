#transction.py

from hex_generator import HexGenerator
from random import randint
import requests
import time
from blockchain import Blockchain


class Transaction:
    def __init__(self, from_address , to_address, value, gas_limit, max_fee, priority_fee, gas_used, input_data):
        self.__from_address = from_address
        self.__to_address = to_address
        self.__value = value
        self.__gas_limit = gas_limit
        self.__max_fee = max_fee
        self.__priority_fee = priority_fee
        self.__gas_used = gas_used
        self.__input_data = input_data
        self.__hash = HexGenerator().generate_hash()

        self.__base_fee = randint(1,200_000_000_000)
        validator_wanted_priority_fee = randint(1,10_000_000_000)

        self.__gas_price = self.__base_fee + self.__priority_fee
        self.__eth_burnt = self.__base_fee
        self.__transaction_fee = self.__gas_used * self.__gas_price

        blockchain = Blockchain()
        from_address_instance = blockchain.get_address_by_address(from_address)
        to_address_instance = blockchain.get_address_by_address(to_address)


        if value + self.__transaction_fee <= from_address_instance.eth_balance:
            if priority_fee < max_fee:
                if gas_used <= gas_limit:
                    if self.__base_fee <= self.__max_fee and validator_wanted_priority_fee <= self.__priority_fee :
                        self.__status = 'Confirmed'
                    else:
                        self.__status = 'Rejected'
                else:
                    self.__status = 'Rejected'
            else:
                self.__status = 'Rejected'
        else:
            self.__status = 'Rejected'
        self.__eth_price = randint(1, 10000)
        # response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
        # self.__eth_price = response.json()["ethereum"]["usd"]


        self.__timestamp = time.time()


        if self.__status == 'Confirmed':
            address = blockchain.get_address_by_address(self.__from_address)
            address.nonce = address.nonce + 1
            self.__nonce = address.nonce
        else:
            self.__nonce = None


        if self.__status == 'Confirmed':
            if to_address_instance is not None:
                to_address_instance.eth_balance += value
            from_address_instance.eth_balance -= (value + self.__transaction_fee)

        blockchain.add_transaction(self)

    @property
    def from_address(self):
        return self.__from_address

    @property
    def to_address(self):
        return self.__to_address

    @property
    def value(self):
        return self.__value

    @property
    def gas_limit(self):
        return self.__gas_limit

    @property
    def gas_used(self):
        return self.__gas_used

    @property
    def max_fee(self):
        return self.__max_fee

    @property
    def priority_fee(self):
        return self.__priority_fee

    @property
    def input_data(self):
        return self.__input_data

    @property
    def hash(self):
        return self.__hash

    @property
    def base_fee(self):
        return self.__base_fee

    @property
    def status(self):
        return self.__status

    @property
    def eth_price(self):
        return self.__eth_price

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def nonce(self):
        return self.__nonce

    @property
    def gas_price(self):
        return self.__gas_price

    @property
    def eth_burnt(self):
        return self.__eth_burnt

    @property
    def transaction_fee(self):
        return self.__transaction_fee