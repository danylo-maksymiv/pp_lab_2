#erc20.py
from blockchain import Blockchain
from token_ import Token
from transaction import Transaction

class Erc20(Token):
    def __init__(self, creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol):
        super().__init__(creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol)

    def mint(self, from_address, value, gas_limit, max_fee, priority_fee, *args, **kwargs):
        amount = args[0]

        if self._remaining_supply >= amount:
            transaction = Transaction(from_address, self.contract_address, 0, gas_limit, max_fee, priority_fee, 25000, f'mint {amount}')

            if transaction.status == 'Confirmed':
                print(f'Successfully minted {amount} tokens with ! Transaction hash: {transaction.hash}.')
                self._remaining_supply -= amount

                blockchain = Blockchain()
                from_address_instance = blockchain.get_address_by_address(from_address)
                from_address_instance.set_token_balance(self.contract_address, amount)

                from_address_instance.eth_balance -= (value + transaction.transaction_fee)
            else:
                print(f'Can\'t mint token, user may have not enough ether on balance. Transaction hash: {transaction.hash}.')

        else:
            print('Invalid amount of tokens.')

    def transfer(self, from_address, value, gas_limit, max_fee, priority_fee, *args):
        amount = args[0]
        to_address = args[1]

        blockchain = Blockchain()
        from_address_instance = blockchain.get_address_by_address(from_address)
        to_address_instance = blockchain.get_address_by_address(to_address)

        if to_address is not None:

            balance = from_address_instance.token_balance.get(self.contract_address, [0, None])[0]
            if balance >= amount:
                transaction = Transaction(from_address, self.contract_address,0, gas_limit, max_fee, priority_fee, 21000, f'{self.contract_address} transfer {amount} to {to_address_instance.address}')

                if transaction.status == 'Confirmed':
                    print(f'Successfully transferred {amount} tokens to {to_address_instance.address}! Transaction hash: {transaction.hash}.')
                    from_address_instance.set_token_balance(self.contract_address, -amount)
                    to_address_instance.set_token_balance(self.contract_address, amount)

                    from_address_instance.eth_balance -= (value + transaction.transaction_fee)

                else:
                    print(f'Can\'t transfer {amount} tokens to {to_address_instance.address}, user may have not enough ether on balance. Transaction hash: {transaction.hash}.')

            else:
                print(f'Can\'t transfer {amount} tokens to {to_address_instance.address}, user have not enough tokens on balance.')

        else:
            print('Receiver doesn\'t exist.')