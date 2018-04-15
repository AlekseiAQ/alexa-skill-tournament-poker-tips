from .utilities import convert_cards_to_hand, hand_in_pushrange


def make_tournament_decision(first_card, second_card, stack_size, position):
    hand = convert_cards_to_hand(first_card, second_card)
    return hand_in_pushrange(hand, stack_size, position)
