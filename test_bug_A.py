from bug3_logic import find_max


def test_find_max_returns_largest_score():
    assert find_max([10, 20, 15]) == 20


def test_find_max_handles_single_score():
    assert find_max([7]) == 7


def test_find_max_returns_last_score_when_largest():
    assert find_max([3, 9]) == 9


def test_find_max_handles_negative_scores():
    assert find_max([-8, -2, -5]) == -2