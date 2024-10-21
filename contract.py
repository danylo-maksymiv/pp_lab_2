#contract.py
from hex_generator import HexGenerator
from transaction import Transaction
from random import randint
from blockchain import Blockchain

class Contract:
    def __init__(self, creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names):
        self.__creator_address = creator_address
        self.__source_code = source_code
        self.__name = name
        self.__version = version
        self.__function_names = function_names
        self.__abi = source_code

        self.__byte_code = HexGenerator.generate_bytes(len(self.__source_code))

        self.__contract_address = HexGenerator.generate_address()

        transaction = Transaction(creator_address, self.contract_address,0, gas_limit, max_fee, priority_fee, 21000, 'create_contract ' + name)

        if transaction.status == 'Confirmed':
            print(f'Contract creation was successful! Created at txn: {transaction.hash} by {self.__creator_address}')
            chain = Blockchain()
            chain.add_contract(self)
            address = chain.get_address_by_address(self.__creator_address)
            address.eth_balance = address.eth_balance - transaction.transaction_fee
        else:
            print(f'Can\'t deploy contract, user may have not enough ether on balance. Transaction hash: {transaction.hash}')
            self.__contract_address = None

    @property
    def creator_address(self):
        return self.__creator_address

    @property
    def contract_address(self):
        return self.__contract_address

    @property
    def source_code(self):
        return self.__source_code

    @property
    def byte_code(self):
        return self.__byte_code

    @property
    def abi(self):
        return self.__abi

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    def __call__(self, function_name, from_address, value, gas_limit, max_fee, priority_fee, *args, **kwargs):
        if function_name in self.__function_names:
            if hasattr(self, function_name):
                method = getattr(self, function_name)
                method(from_address, value, gas_limit, max_fee, priority_fee, *args, **kwargs)
            else:
                gas_used = randint(21000, 100_000)
                transaction = Transaction(from_address, self.contract_address, value, gas_limit, max_fee, priority_fee, gas_used, str(function_name) + '\n' + str(args) + '\n' + str(kwargs))

                if transaction.status == "Confirmed":
                    print(f'Successfully confirmed transaction! Transaction hash: {transaction.hash}')
                    # chain = Blockchain()
                    # address = chain.get_address_by_address(from_address)
                    # address.eth_balance = address.eth_balance - transaction.transaction_fee - transaction.value
                else:
                    print(f'Transaction was rejected, try to add more gas! Transaction hash: {transaction.hash}')
        else:
            print(f"No such function: {function_name}")