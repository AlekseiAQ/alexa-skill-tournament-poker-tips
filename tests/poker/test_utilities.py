import pytest

from poker.utilities import adjust_stack_size, is_correct_input


ADJUST_STACK_SIZE_EXAMPLES = (
    ('arg', 'expected'),
    [
        (15, 14),
        (14, 14),
        (13, 12),
        (12, 12),
        (11, 10),
        (10, 10),
        (9, 8),
        (8, 8),
        (7, 6),
        (6, 6),
        (5, 5),
        (4, 5),
        (3, 5),
        (2, 5),
        (1, 5),
    ]
)


@pytest.mark.parametrize(*ADJUST_STACK_SIZE_EXAMPLES)
def test_returns_correct_result_adjust_stack_size(arg, expected):
    assert adjust_stack_size(arg) == expected


IS_CORRECT_INPUT_EXAMPLES = (
    ('args', 'expected'),
    [
        (("ace", "king", 14, "utg"), True),
        (("smoke", "zoo", 14, "utg"), False),
        ((1, 2, "s", 3), False),
    ]
)


@pytest.mark.parametrize(*IS_CORRECT_INPUT_EXAMPLES)
def test_returns_correct_result_for_expand_ranges(args, expected):
    assert is_correct_input(*args) == expected
