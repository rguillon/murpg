import pytest

from murpg.roll import Roll


@pytest.mark.parametrize(
    ("stats", "size"),
    [
        ([(1, 0), (1, 1)], 2),
        ([(1, 2), (2, 5)], 3),
        ([(2, 2), (3, 5)], 5),
        ([(1, 0), (6, 1), (4, 2)], 11),
    ],
)
def test_get_size(stats: list[tuple[float, int]], size: float):
    roll = Roll(stats)
    assert roll.get_size() == size


@pytest.mark.parametrize(
    ("stats", "esperance"),
    [
        ([(1, 0), (1, 1)], 0.5),
        ([(1, 1), (1, 1)], 1.0),
        ([(1, 2), (2, 5)], 4.0),
        ([(1, 0), (1, 1), (1, 2)], 1.0),
    ],
)
def test_roll_get_esperance(stats: list[tuple[float, int]], esperance: float):
    roll = Roll(stats)
    assert roll.get_esperance() == esperance


@pytest.mark.parametrize(
    ("stat1", "stat2", "result"),
    [
        ([(1, 0), (1, 1)], [(1, 0), (1, 1)], [(1, 0.0), (2, 1), (1, 2)]),
        ([(1, 0.0), (2, 1), (1, 2)], [(1, 0), (1, 1)], [(1, 0.0), (3, 1), (3, 2), (1, 3)]),
    ],
)
def test_add(stat1: list[tuple[float, int]], stat2: list[tuple[float, int]], result: list[tuple[float, int]]):
    assert (Roll(stat1) + Roll(stat2)).get_stats() == result


@pytest.mark.parametrize(
    ("stats", "normalized"),
    [
        ([(1, 0), (1, 1)], [(0.5, 0), (0.5, 1)]),
        (
            [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
            [(1 / 6, 1), (1 / 6, 2), (1 / 6, 3), (1 / 6, 4), (1 / 6, 5), (1 / 6, 6)],
        ),
    ],
)
def test_normalize(stats: list[tuple[float, int]], normalized: list[tuple[float, int]]):
    roll = Roll(stats)
    assert roll.normalize().get_stats() == normalized
    assert roll.normalize().get_size() == 1.0


def test_roll_returns_value_from_events(monkeypatch):
    # Patch random.choices to always return the first value
    monkeypatch.setattr("random.choices", lambda values, weights, k: [values[0]])
    stats = [(1, 10), (2, 20), (3, 30)]
    roll = Roll(stats)
    result = roll.roll()
    assert result == 10


def test_roll_distribution(monkeypatch):
    # Simulate random.choices to return values based on weights
    stats = [(1, 10), (3, 20)]
    roll = Roll(stats)
    # We'll run roll many times and check the distribution
    results = []
    for _ in range(1000):
        results.append(roll.roll())
    # Since weights are 1:3, expect roughly 1/4 to be 10, 3/4 to be 20
    count_10 = results.count(10)
    count_20 = results.count(20)
    ratio = count_20 / (count_10 + count_20)
    assert 0.70 < ratio < 0.80  # Allow some randomness


def test_roll_with_single_event():
    stats = [(5, 42)]
    roll = Roll(stats)
    for _ in range(10):
        assert roll.roll() == 42


def test_roll_with_zero_weights():
    stats = [(0, 1), (0, 2), (5, 3)]
    roll = Roll(stats)
    for _ in range(10):
        assert roll.roll() == 3
