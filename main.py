from address import Address
from blockchain import Blockchain

trillion, quadrillion, quintillion, sextillion = 10**12, 10**15, 10**18, 10**21
priority_fee = 10**10

blockchain = Blockchain()
vitalik_eth = Address()
pukach_wallet = Address()
my_wallet = Address()

vitalik_eth.eth_balance = sextillion

vitalik_eth.transfer_eth(my_wallet.address, sextillion // 10, trillion,quintillion * 10,priority_fee,'hello!')
vitalik_eth.transfer_eth(pukach_wallet.address, sextillion  // 10 ,trillion,quintillion * 10,priority_fee,'hello!')

uniswap1 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', 1,1,1,['swap', 'add_liquidity'],'Dex')
uniswap2 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', 1,2,4,['swap', 'add_liquidity'],'Dex')
uniswap3 = my_wallet.deploy_contract('create uniswap', 'uniswap', '1.0', trillion, quintillion * 10, priority_fee,['swap', 'add_liquidity'],'Dex')

my_wallet.call_contract(uniswap2,'swap', quintillion, trillion, quintillion * 10, priority_fee)
my_wallet.call_contract(uniswap3,'mint', quintillion, trillion, quintillion * 10, priority_fee)
my_wallet.call_contract(uniswap3,'swap', quintillion, trillion, quintillion * 10, priority_fee)

doge_coin = pukach_wallet.deploy_contract('create token', 'doge', '1.0', trillion,quintillion * 10,priority_fee,['mint', 'transfer'],'erc20',100,'DOGE')
pukach_wallet.call_contract(doge_coin,'mint',quintillion,trillion,quintillion * 10, priority_fee,int(101))
pukach_wallet.call_contract(doge_coin,'mint',quintillion,trillion,quintillion * 10,priority_fee,int(100))
pukach_wallet.call_contract(doge_coin,'transfer',quintillion,trillion,quintillion * 10,priority_fee,int(100),my_wallet.address)

bored_apes = my_wallet.deploy_contract('create not fungible token', 'Bored Ape Yacht Club', '1.0', trillion,quintillion * 10,priority_fee,['mint', 'transfer'],'erc721',10,'BAYC')
my_wallet.call_contract(bored_apes,'mint',quintillion,trillion,quintillion * 10,priority_fee,5)
my_wallet.call_contract(bored_apes,'mint',quintillion,trillion,quintillion * 10,priority_fee,3)
my_wallet.call_contract(bored_apes,'transfer',quintillion,trillion,quintillion * 10,priority_fee,3,pukach_wallet.address,[0,7,3])

blockchain.show_addresses()

