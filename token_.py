#token_.py

from abc import abstractmethod

from itransferable import ITransferable
from contract import Contract


class Token(Contract, ITransferable):
    def __init__(self, creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names, supply, symbol):
        super().__init__(creator_address, source_code, name, version, gas_limit, max_fee, priority_fee, function_names)
        self.__supply = supply
        self.__symbol = symbol
        self._remaining_supply = supply

    @property
    def supply(self):
        return self.__supply

    @property
    def symbol(self):
        return self.__symbol

    @abstractmethod
    def mint(self, from_address, value, gas_limit, max_fee, priority_fee, *args, **kwargs):
        pass