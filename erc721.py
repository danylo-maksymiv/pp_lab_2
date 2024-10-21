#erc721.py
from blockchain import Blockchain
from token_ import Token

class Erc721(Token):
    def __init__(self, creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol):
        super().__init__(creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol)
        self.__id_generator = self._id_generator()

    def _id_generator(self):
        for id_ in range(self.supply):
            yield id_

    def mint(self, from_address, value, gas_limit, max_fee, priority_fee, *args):
        amount = args[0]

        minted_ids = []
        if self._remaining_supply >= amount:
            for _ in range(amount):
                token_id = next(self.__id_generator)
                minted_ids.append(token_id)

            from transaction import Transaction
            transaction = Transaction(from_address, self.contract_address, 0, gas_limit, max_fee, priority_fee, 30000, f'mint {amount}\n {minted_ids}')

            if transaction.status == 'Confirmed':
                print(f'Successfully minted {len(minted_ids)} tokens with IDs: {minted_ids}! Transaction hash: {transaction.hash}.')
                self._remaining_supply -= len(minted_ids)
                blockchain = Blockchain()
                from_address_instance = blockchain.get_address_by_address(from_address)
                from_address_instance.set_token_balance(self.contract_address, len(minted_ids), minted_ids)


            else:
                print(f'Can\'t mint token, user may have not enough ether on balance. Transaction hash: {transaction.hash}.')
        else:
            print('Invalid amount of tokens.')

    def transfer(self, from_address, value, gas_limit, max_fee, priority_fee, *args):
        amount = args[0]
        to_address = args[1]
        ids = args[2]


        from blockchain import Blockchain
        blockchain = Blockchain()
        from_address_instance = blockchain.get_address_by_address(from_address)
        to_address_instance = blockchain.get_address_by_address(to_address)

        has_tokens = True
        for id_ in ids:
            if id_ not in from_address_instance.token_balance[self.contract_address][1]:
                has_tokens = False
                break

        if amount == len(ids):
            if has_tokens:
                from transaction import Transaction
                transaction = Transaction(from_address, self.contract_address, 0, gas_limit, max_fee, priority_fee, 21000 * len(ids),f'{self.contract_address} transfer {ids} to {to_address_instance.address}')

                if transaction.status == 'Confirmed':
                    print(f'Successfully transferred {ids} tokens to {to_address_instance.address}! Transaction hash: {transaction.hash}.')
                    tokens_from = []
                    tokens_to = []
                    for id_ in ids:
                        tokens_to.append(id_)
                    for id_ in ids:
                        tokens_from.remove(id_)

                    from_address_instance.set_token_balance(self.contract_address, -amount, tokens_from)
                    to_address_instance.set_token_balance(self.contract_address, amount, tokens_to)

                else:
                    print(f'Can\'t transfer {amount} tokens to {to_address_instance.address}, user may have not enough ether on balance. Transaction hash: {transaction.hash}.')

            else:
                print(f'Can\'t transfer {amount} tokens to {to_address_instance.address}, user have not enough tokens on balance.')
        else:
            print('Amount of tokens does not match with count of ids.')