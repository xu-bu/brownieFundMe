from brownie import FundMe
from scripts.helpfulScript import get_account

def fund():
    # get the latest deployed contract
    fundMe=FundMe[-1]
    account=get_account()
    entranceFee=fundMe.getEntranceFee()
    print(f'current entrance fee is: {entranceFee}')
    print("funding....")
    fundMe.fund({"from":account,"value":entranceFee})

def withdraw():
    fundMe=FundMe[-1]
    account=get_account()
    print("withdrawing....")
    fundMe.withdraw({"from":account})


def main():
    fund()
    withdraw()