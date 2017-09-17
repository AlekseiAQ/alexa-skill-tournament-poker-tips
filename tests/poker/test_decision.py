import pytest

from poker.decision import make_tournament_decision

EXAMPLES = (
    ('args', 'expected'),
    [
        (("ace", "king", 14, "utg"), True),
        (("ace", "ace", 5, "bu"), True),
        (("three", "two", 14, "utg"), False),
        (("two", "two", 14, "mp"), False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert make_tournament_decision(*args) == expected
