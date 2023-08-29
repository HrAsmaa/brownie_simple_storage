from brownie import accounts, config, myFirstContract, network

def deploy_simple_storage():
    account = get_account()
    print(account)
    simple_storage = myFirstContract.deploy({"from":account})
    print(simple_storage)
    stored_value = simple_storage.getMyFavoritNumber()
    print(stored_value)
    transaction = simple_storage.setMyFavoritNumber(20,{"from":account})
    transaction.wait(1)
    stored_value = simple_storage.getMyFavoritNumber()
    print(stored_value)
    #account = accounts.load("asmaa")
    #print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

    

def main():
    deploy_simple_storage()