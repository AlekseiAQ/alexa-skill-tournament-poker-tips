from poker.constants import CARDS


def expand_range(range_):
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


def expand_ranges(push_range):
    push_range = push_range.split(",")
    new_push_range = []
    for range_ in push_range:
        new_push_range.append(expand_range(range_))
    return ",".join(new_push_range)
