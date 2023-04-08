# create .env:
example:

```
export WEB3_INFURA_PROJECT_ID=(get it from infura API keys)

export PRIVATE_KEY=(get it from metamask's account)

export ETHERSCAN_TOKEN=(variable name must be this, get it from ethescan-API keys, used for verification and deploying)
```

# deploy:

run `brownie compile` to compile


`brownie.exe run .\scripts\deploy.py` to deploy on default network (see networks-default in brownie-config.yaml)

after deploying, you are able to see the transactions on ganache

if you want to deploy on mainnet, you have to add network at first (for eaxample: run 

`brownie.exe networks add development mainnet-fork-dev cmd=ganache-cli host='$ALCHEMY_API_KEY' accounts=10 mnemonic=brownie port=8545` 

to add fork-mainnet, accounts=10 means brownie will create 10 fake accounts on our fork-mainnet for us), then run

`brownie.exe run .\scripts\deploy.py --network mainnet-fork-dev`

 to deploy on specific network

# test:

run `brownie test` to execute all functions of all test files in tests folder (if a file starts with "test_", then it will be ragarded as a test file)

to specify one particular test function on specific network, run `brownie.exe test -k test_onlyOwner --network sepolia`