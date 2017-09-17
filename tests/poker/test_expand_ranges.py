import pytest

from poker.expand_ranges import expand_range, expand_ranges

EXPAND_RANGE_EXAMPLES = (
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


@pytest.mark.parametrize(*EXPAND_RANGE_EXAMPLES)
def test_returns_correct_result_for_expand_range(arg, expected):
    assert expand_range(arg) == expected


EXPAND_RANGES_EXAMPLES = (
    ('arg', 'expected'),
    [
        ("QQ+,QJs+", "AA,KK,QQ,AKs,KQs,QJs"),
        ("QQ+,QJo+", "AA,KK,QQ,AKo,KQo,QJo"),
        ("QQ+,K9s+,K9o+", "AA,KK,QQ,KQs,KJs,KTs,K9s,KQo,KJo,KTo,K9o"),
        ("QQ+,K9s+,QTo+", "AA,KK,QQ,KQs,KJs,KTs,K9s,QJo,QTo"),
    ]
)


@pytest.mark.parametrize(*EXPAND_RANGES_EXAMPLES)
def test_returns_correct_result_for_expand_ranges(arg, expected):
    assert expand_ranges(arg) == expected
