from address import Address
from blockchain import Blockchain

blockchain = Blockchain()

vitalik_eth = Address()
pukach_wallet = Address()
my_wallet = Address()

vitalik_eth.eth_balance = int(1e23)

vitalik_eth.transfer_eth(my_wallet.address, int(1e21),int(1e11),int(1e19),int(1e18),'hello!')
vitalik_eth.transfer_eth(pukach_wallet.address, int(1e21),int(1e11),int(1e19),int(1e18),'hello!')

uniswap1 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', 1,1,1,['swap', 'add_liquidity'],'Dex')
uniswap2 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', 1,2,4,['swap', 'add_liquidity'],'Dex')
uniswap3 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', int(1e11),int(1e19),int(1e18),['swap', 'add_liquidity'],'Dex')

my_wallet.call_contract(uniswap2,'swap', int(1e18), int(1e11), int(1e19), int(1e18))
my_wallet.call_contract(uniswap3,'mint', int(1e18), int(1e11), int(1e19), int(1e18))
my_wallet.call_contract(uniswap3,'swap', int(1e18), int(1e11), int(1e19), int(1e18))

doge_coin = pukach_wallet.deploy_contract('create token', 'doge', '1.0', int(1e11),int(1e19),int(1e18),['mint', 'transfer'],'erc20',100,'DOGE')
pukach_wallet.call_contract(doge_coin,'mint',int(1e18),int(1e11),int(1e19), int(1e18),int(101))
pukach_wallet.call_contract(doge_coin,'mint',int(1e18),int(1e11),int(1e19),int(1e18),int(100))
pukach_wallet.call_contract(doge_coin,'transfer',int(1e18),int(1e11),int(1e19),int(1e18),int(100),my_wallet.address)

bored_apes = my_wallet.deploy_contract('create not fungible token', 'Bored Ape Yacht Club', '1.0', int(1e11),int(1e19),int(1e18),['mint', 'transfer'],'erc721',10,'BAYC')
my_wallet.call_contract(bored_apes,'mint',int(1e18),int(1e11),int(1e19),int(1e18),5)
my_wallet.call_contract(bored_apes,'mint',int(1e18),int(1e11),int(1e19),int(1e18),3)
my_wallet.call_contract(bored_apes,'transfer',int(1e18),int(1e11),int(1e19),int(1e18),3,pukach_wallet.address,[0,7,3])

blockchain.show_addresses()