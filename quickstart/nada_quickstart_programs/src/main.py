from nada_dsl import *

def nada_main():
    party = Party(name="Participant")

    item_value = SecretInteger(Input(name="Item_Value", party=party))

    bid_value = SecretInteger(Input(name="Bid_Value", party=party))

    auction_result = bid_value >= item_value

    return [
        Output(auction_result, "Auction_Result", party)
    ]
