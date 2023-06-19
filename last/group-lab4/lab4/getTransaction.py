import sys
from web3 import Web3, HTTPProvider
from web3.eth import Eth

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))  # 初始化区块链节点连接
eth = Eth(w3)
accounts = w3.eth.accounts


def saveDataOnBlock(blockNumber):
    # 检查是否连接成功
    if w3.eth.get_block(0) is None:
        print("Blockchain connect failed!")
    else:
        print("Blockchain connect successfully!")

    block = w3.eth.get_block(blockNumber)
    trans = w3.eth.get_transaction(block["transactions"][0])
    print(w3.to_text(trans.input))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong parameters! Usage Example:python saveDataOnBlock.py -n 2")
        exit(0)

    n = eval(sys.argv[2])

    saveDataOnBlock(n)
