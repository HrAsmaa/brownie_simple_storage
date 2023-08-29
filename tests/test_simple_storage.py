from brownie import myFirstContract, accounts

def test_deploy():
    account = accounts[0]
    simple_storage = myFirstContract.deploy({"from": account})
    starting_value = simple_storage.getMyFavoritNumber()
    expected = 0
    assert starting_value == expected


def test_Set_My_Favorite_Number():
    account = accounts[0]
    simple_storage = myFirstContract.deploy({"from": account})
    simple_storage.setMyFavoritNumber(20,{"from":account})
    value = simple_storage.getMyFavoritNumber()
    expected = 20
    assert value == expected