import sys
from web3 import Web3, HTTPProvider
from web3.eth import Eth

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
eth = Eth(w3)
accounts = w3.eth.accounts


# 定义一个十六进制字符串格式化输出函数
def bytesToHexString(bs):
    return "".join(["%02x" % b for b in bs])


def saveDataOnBlock(data):
    # 检查是否连接成功
    if w3.eth.get_block(0) is None:
        print("Blockchain connect failed!")
    else:
        print("Blockchain connect successfully!")

    # 读取账户余额
    balance = w3.eth.get_balance(accounts[0], 'latest')
    # 输出交易前的余额
    print(f"balance before tx => {balance}")

    data_into_block = Web3.to_hex(text=data)

    # 设置交易，从节点第1个账户向第二个账户转500Wei
    payload = {'from': accounts[0], 'to': accounts[1], 'value': 500, 'data': data_into_block}

    # 向以太坊提出交易，以太坊节点将返回交易的哈希值
    tx_hash = w3.eth.send_transaction(payload)
    print(f'tx hash => {Web3.to_hex(tx_hash)}')

    w3.geth.miner.start(2)  # 启动2个CPU挖矿进程进行挖矿，因为是在本地测试上链，所以速度很快
    w3.geth.miner.stop()

    # 读取交易后的余额
    balance = w3.eth.get_balance(accounts[0], 'latest')
    # 输出交易后的余额
    print(f"balance after tx => {balance}")

    trans_result = w3.eth.get_transaction(tx_hash)

    # 获取交易返回的详细信息
    print("Block Hash:", bytesToHexString(trans_result['blockHash']))
    print("Block Number:", trans_result['blockNumber'])
    print("Transaction Index:", trans_result['transactionIndex'])
    print("Input Data:", w3.to_text(trans_result['input']))  # 显示刚上链的原始数据信息

    count = 0

    block_num = w3.eth.get_block('latest').number

    for i in range(block_num):
        try:
            blockn = w3.eth.get_block(i)
            print("Block", str(i), "hash:", bytesToHexString(blockn.hash))
            count += 1
        except:
            print("No more blocks in current blockchain.")
            break

    print(f'\n{count} blocks in current blockchain.')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong parameters! Usage Example:python saveDataOnBlock.py -d 'Sample Data'")
        exit(0)

    data = sys.argv[2]

    saveDataOnBlock(data)
