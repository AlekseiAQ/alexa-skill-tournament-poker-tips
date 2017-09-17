from poker.constants import HANDS, POSITIONS, ALL_POSITIONS


def is_correct_card(card):
    return isinstance(card, str) and card in HANDS.keys()


def is_correct_stack_size(stack_size):
    return isinstance(stack_size, int)


def is_correct_position(position):
    return isinstance(position, str) and position in ALL_POSITIONS


def is_correct_input(first_card, second_card, stack_size, position):
    return is_correct_card(first_card) and is_correct_card(second_card) and \
        is_correct_stack_size(stack_size) and is_correct_position(position)


def convert_cards_to_hand(first_card, second_card):
    if first_card == second_card:
        hand = HANDS.get(first_card) + HANDS.get(second_card)
    else:
        # rewrite when alexa will handle 'suited' variable
        hand = HANDS.get(first_card) + HANDS.get(second_card) + 'o'
    return hand


def adjust_stack_size(stack_size):
    if stack_size >= 14:
        stack_size = 14
    elif stack_size >= 12:
        stack_size = 12
    elif stack_size >= 10:
        stack_size = 10
    elif stack_size >= 8:
        stack_size = 8
    elif stack_size >= 6:
        stack_size = 6
    else:
        stack_size = 5
    return stack_size
