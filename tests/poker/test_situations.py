import pytest

from poker.situations import push_this_hand


PUSH_THIS_HAND_EXAMPLES = (
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


@pytest.mark.parametrize(*PUSH_THIS_HAND_EXAMPLES)
def test_returns_correct_result_push_this_hand(args, expected):
    assert push_this_hand(*args) == expected
