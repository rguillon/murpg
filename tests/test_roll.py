import pytest

from murpg.roll import Roll


def test_build_roll():
    roll = Roll([(1, 0.0), (1, 1.0)])
    assert roll.get_events() == [(1, 0.0), (1, 1.0)]


@pytest.mark.parametrize(
    ("events", "esperance"), [([(1, 0.0), (1, 1.0)], 0.5), ([(1, 1.0), (1, 1.0)], 1.0), ([(1, 1.0), (1, 1.0)], 1.0)]
)
def test_roll_get_esperance(events: list[tuple[int, float]], esperance: float):
    roll = Roll(events)
    assert roll.get_esperance() == esperance
