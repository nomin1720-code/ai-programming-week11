import pytest

from bug3_logic import find_max


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([1, 2, 3], 3),
        ([-8, -3, -5], -3),
        ([42], 42),
        ([4, 9, 9, 2], 9),
        ([7, 1, 5], 7),
    ],
)
def test_find_max(scores, expected):
    assert find_max(scores) == expected