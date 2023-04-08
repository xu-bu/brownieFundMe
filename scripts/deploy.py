# brownie will go through all files in /contracts folder to import all contracts like FundMe and MockV3Aggregator
from brownie import accounts, FundMe, network, config, MockV3Aggregator
from scripts.helpfulScript import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deployFundMe():
    account = get_account()
    # network.show_active() is the network where we deploy contract
    # if don't use --network to specify, it will deploy locally and network.show_active() will be "development"
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # using the variable in brownie-config.yaml
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        # to save time, we need to test locally, so we need to mock price feed
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address
    # publish_source=True means publish and verify our contract after deploying, in this process we need the API key of ETHSCAN
    # the first parameter here is the parameter of constructor of FundMe in FundMe.sol
    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"contract deployed to {fundMe.address}")
    return fundMe


def main():
    deployFundMe()
