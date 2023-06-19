from brownie import Vote, accounts

def main():
    vote = Vote.deploy({'from': accounts[0]})
    print("Vote contract deployed at:", vote.address)