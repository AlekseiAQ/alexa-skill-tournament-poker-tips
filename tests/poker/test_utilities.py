import pytest

from poker.utilities import (adjust_stack_size, hand_in_pushrange,
                             is_correct_input, merge_range, merge_ranges)

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
def test_returns_correct_result_for_is_correct_input(args, expected):
    assert is_correct_input(*args) == expected

MERGE_RANGE_EXAMPLES = (
    ('arg', 'expected'),
    [
        ("AA", "AA"),
        ("QQ+", "AA,KK,QQ"),
        ("KK+", "AA,KK"),
        ("22+", "AA,KK,QQ,JJ,TT,99,88,77,66,55,44,33,22"),
        ("QJs+", "AKs,KQs,QJs"),
        ("QJo+", "AKo,KQo,QJo"),
        ("QTs+", "QJs,QTs"),
        ("QTo+", "QJo,QTo"),
        ("K9s+", "KQs,KJs,KTs,K9s"),
        ("K9o+", "KQo,KJo,KTo,K9o"),
    ]
)

@pytest.mark.parametrize(*MERGE_RANGE_EXAMPLES)
def test_returns_correct_result_for_merge_range(arg, expected):
    assert merge_range(arg) == expected

MERGE_RANGES_EXAMPLES = (
    ('arg', 'expected'),
    [
        ("QQ+,QJs+", "AA,KK,QQ,AKs,KQs,QJs"),
        ("QQ+,QJo+", "AA,KK,QQ,AKo,KQo,QJo"),
        ("QQ+,K9s+,K9o+", "AA,KK,QQ,KQs,KJs,KTs,K9s,KQo,KJo,KTo,K9o"),
        ("QQ+,K9s+,QTo+", "AA,KK,QQ,KQs,KJs,KTs,K9s,QJo,QTo"),
    ]
)

@pytest.mark.parametrize(*MERGE_RANGES_EXAMPLES)
def test_returns_correct_result_for_merge_ranges(arg, expected):
    assert merge_ranges(arg) == expected

HAND_IN_PUSHRANGE_EXAMPLES = (
    ('args', 'expected'),
    [
        (("AKs", 14, "utg"), True),
        (("AKs", 14, "mp"), True),
        (("AKs", 14, "co"), True),
        (("AKs", 14, "bu"), True),
        (("AKs", 14, "sb"), True),
        (("32o", 14, "utg"), False),
        (("32o", 14, "mp"), False),
        (("32o", 14, "co"), False),
        (("32o", 14, "bu"), False),
        (("32o", 14, "sb"), False),
        (("AQo", 5, "utg"), True),
        (("AQo", 5, "mp"), True),
        (("AQo", 5, "co"), True),
        (("AQo", 5, "bu"), True),
        (("AQo", 5, "sb"), True),
        (("52s", 5, "utg"), False),
        (("52s", 5, "mp"), False),
        (("52s", 5, "co"), False),
        (("52s", 5, "bu"), False),
        (("52s", 5, "sb"), False),
        (("AKs", 12, "utg"), True),
        (("AKs", 12, "mp"), True),
        (("AKs", 12, "co"), True),
        (("AKs", 12, "bu"), True),
        (("AKs", 12, "sb"), True),
        (("32o", 12, "utg"), False),
        (("32o", 12, "mp"), False),
        (("32o", 12, "co"), False),
        (("32o", 12, "bu"), False),
        (("32o", 12, "sb"), False),
        (("AQo", 8, "utg"), True),
        (("AQo", 8, "mp"), True),
        (("AQo", 8, "co"), True),
        (("AQo", 8, "bu"), True),
        (("AQo", 8, "sb"), True),
        (("52s", 8, "utg"), False),
        (("52s", 8, "mp"), False),
        (("52s", 8, "co"), False),
        (("52s", 8, "bu"), False),
        (("52s", 8, "sb"), False),
    ]
)

@pytest.mark.parametrize(*HAND_IN_PUSHRANGE_EXAMPLES)
def test_returns_correct_result_hand_in_pushrange(args, expected):
    assert hand_in_pushrange(*args) == expected
