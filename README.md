# create .env:
example:

```
export WEB3_INFURA_PROJECT_ID=(get it from infura API keys)

export PRIVATE_KEY=(get it from metamask's account)

export ETHERSCAN_TOKEN=(variable name must be this, get it from ethescan-API keys, used for verification and deploying)
```

# deploy:

## test locally:

run `brownie compile` to compile

run `brownie.exe run .\scripts\deploy.py` to deploy on default network (see networks-default in brownie-config.yaml)



## test on testnet:

1. add network

run

`brownie.exe networks add development mainnet-fork-dev cmd=ganache-cli host='$ALCHEMY_API_KEY' accounts=10 mnemonic=brownie port=8545` 

to add fork-mainnet, accounts=10 means brownie will create 10 fake accounts on our fork-mainnet for us

or run 

`brownie.exe networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=5777`

to add ganache-local network, if you deploy contracts on ganache-local network, you are able to see the transactions on ganache

2. run

`brownie.exe run .\scripts\deploy.py --network mainnet-fork-dev`

 to deploy on specific network

# test:

run `brownie test` to execute all functions of all test files in tests folder (if a file starts with "test_", then it will be ragarded as a test file)

to specify one particular test function on specific network, run `brownie.exe test -k test_onlyOwner --network sepolia`