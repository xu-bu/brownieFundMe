from scripts.helpfulScript import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deployFundMe
from brownie import network,accounts,exceptions
import pytest

def test_fundAndWithdraw():
    account=get_account()
    fundMe=deployFundMe()
    entranceFee=fundMe.getEntranceFee()+100
    txn=fundMe.fund({"from":account,"value":entranceFee})
    # when invoking function of contract to make transaction, we need to wait
    txn.wait(1)
    assert fundMe.addressToAmountFunded(account.address)==entranceFee
    txn=fundMe.withdraw({"from":account})
    txn.wait(1)
    assert fundMe.addressToAmountFunded(account.address)==0

def test_onlyOwner():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    
    fundMe=deployFundMe()
    badActor=accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from":badActor, "gas_limit": 6721975})
