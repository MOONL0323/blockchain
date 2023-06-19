from brownie import Vote, accounts

def test_vote():
    vote = Vote.deploy({'from': accounts[0]})
    assert not vote.votes(accounts[1])
    vote.vote({'from': accounts[1]})
    assert vote.votes(accounts[1])
    with brownie.reverts("You have already voted."):
        vote.vote({'from': accounts[1]})