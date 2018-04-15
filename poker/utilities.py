from .constants import ALL_POSITIONS, CARDS, HANDS, POSITIONS, PUSH_RANGES


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

def merge_range(range_):
    if len(range_) == 2:
        return range_
    elif len(range_) == 3:
        if "+" in range_:
            first_card, second_card, _ = range_
        else:
            first_card, second_card, suited = range_
    elif len(range_) == 4:
        first_card, second_card, suited, _ = range_
    else:
        raise ValueError("Incorrech range")

    if first_card == second_card and "+" in range_:
        index = CARDS.index(first_card)
        hands = ",".join(card + card for card in reversed(CARDS[index:]))
    else:
        min_index = min(CARDS.index(first_card), CARDS.index(second_card))
        max_index = max(CARDS.index(first_card), CARDS.index(second_card))
        if max_index - min_index < 2:
            hands = ",".join(reversed([i + j + suited
                                       for i, j in zip(CARDS[max_index:],
                                                       CARDS[min_index:])]))
        else:
            hands = ",".join(CARDS[max_index] + card + suited
                             for card in reversed(CARDS[min_index:max_index]))
    return hands


def merge_ranges(push_range):
    push_range = push_range.split(",")
    new_push_range = []
    for range_ in push_range:
        new_push_range.append(merge_range(range_))
    return ",".join(new_push_range)

def get_push_range(stack_size, position):
    for position_name, position_values in POSITIONS.items():
        if position in position_values:
            push_range = PUSH_RANGES[position_name]

    push_range = merge_ranges(push_range.get(stack_size))

    return push_range


def hand_in_pushrange(hand, stack_size, position):
    stack_size = adjust_stack_size(stack_size)
    push_range = get_push_range(stack_size, position)
    return hand in push_range
