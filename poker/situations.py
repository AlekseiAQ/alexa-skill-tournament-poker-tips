from poker.constants import POSITIONS, PUSH_RANGES
from poker.expand_ranges import expand_ranges
from poker.utilities import adjust_stack_size


def get_push_range(stack_size, position):
    for position_name, position_values in POSITIONS.items():
        if position in position_values:
            push_range = PUSH_RANGES[position_name]

    push_range = expand_ranges(push_range.get(stack_size))

    return push_range


def push_this_hand(hand, stack_size, position):
    stack_size = adjust_stack_size(stack_size)
    push_range = get_push_range(stack_size, position)
    return hand in push_range
