from poker.situations import push_this_hand
from poker.utilities import convert_cards_to_hand


def make_tournament_decision(first_card, second_card, stack_size, position):
    hand = convert_cards_to_hand(first_card, second_card)
    return push_this_hand(hand, stack_size, position)
