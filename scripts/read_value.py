from brownie import accounts, config, myFirstContract, network


def read_value():
    simple_storage = myFirstContract[-1]
    value = simple_storage.getMyFavoritNumber()
    print(value)


def main():
    read_value()