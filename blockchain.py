#blockchain.py

from datetime import datetime as dt

class Blockchain:
    _blockchain = None

    def __new__(cls, *args, **kwargs):
        if cls._blockchain is None:
            cls._blockchain = super(Blockchain, cls).__new__(cls)
            cls._blockchain.__initialize()
        return cls._blockchain

    def __initialize(self):
        self.__transactions = dict()
        self.__addresses = dict()
        self.__contracts = dict()

    def add_address(self, address):
        self.__addresses.update({address.address: address})

    def add_transaction(self, txn):
        self.__transactions.update({txn.hash: txn})

    def add_contract(self, contract):
        self.__contracts.update({contract.contract_address: contract})

    def get_transaction_by_hash(self, hash_):
        return self.__transactions.get(hash_)

    def get_address_by_address(self, address):
        return self.__addresses.get(address)

    def get_contract_by_address(self, contract_address):
        return self.__contracts.get(contract_address)

    def show_transactions(self):
        for txn in self.__transactions.values():
            print(f''' 
                Transaction : {txn.hash}\n\n
                From : {txn.from_address}\n
                To : {txn.to_address}\n
                Value : {txn.value  / int(1e18)}\n
                Eth price : {txn.eth_price}\n
                Status : {txn.status}\n
                Transaction fee : {txn.transaction_fee}\n
                Gas fee : {txn.gas_price}\n
                Gas limit : {txn.gas_limit}\n
                Gas used : {txn.gas_used}\n
                Max fee : {txn.max_fee}\n
                Priority fee : {txn.priority_fee}\n
                Base fee : {txn.base_fee}\n
                ETH burnt : {txn.eth_burnt}\n
                Timestamp: {dt.fromtimestamp(txn.timestamp)}\n
                Input data : {txn.input_data}
                ''')

    def show_addresses(self):
        for adr in self.__addresses.values():
            print(f'''
                Address : {adr.address}\n\n
                ETH balance : {adr.eth_balance / int(1e18)}\n
                ''')
            for ca,balance in adr.token_balance.items():
                print(f'''{self.get_contract_by_address(ca).symbol} : ${balance} ''')

    def show_contracts(self):
        for ca in self.__contracts.values():
            print(f'''
            Contract : {ca.contract_address}\n\n
            Creator address: {ca.creator_address}\n
            Name : {ca.name}\n
            Version : {ca.version}\n
            Source code : {ca.source_code}\n
            Byte code : {ca.byte_code}\n
            ABI : {ca.abi}\n
            ''')

            from token_ import Token
            if isinstance(ca, Token):
                print(f'''
                Supply: {ca.supply}\n
                Symbol : ${ca.symbol.upper()}\n
                ''')

    def show_blockchain(self):
        self.show_transactions()
        self.show_addresses()
        self.show_contracts()


