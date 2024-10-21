#itransferable.py

from abc import ABC, abstractmethod

class ITransferable(ABC):
    @abstractmethod
    def transfer(self, from_address, value, gas_limit, max_fee, priority_fee, *args):
        pass