import random
from collections import defaultdict


class Roll:
    def __init__(self, events: list[tuple[float, int]]):
        self.events: list[tuple[float, int]] = events

    def get_stats(self) -> list[tuple[float, int]]:
        return self.events

    def normalize(self) -> "Roll":
        total = self.get_size()
        normal = [(event / total, prob) for event, prob in self.events]
        return Roll(normal)

    def get_esperance(self) -> float:
        return sum(event * prob for prob, event in self.events) / self.get_size() if self.get_size() > 0 else 0.0

    def get_size(self) -> float:
        return sum(prob for prob, _ in self.events)

    def __add__(self, other: "Roll") -> "Roll":
        combined_events = defaultdict(int)
        for prob1, event1 in self.events:
            for prob2, event2 in other.get_stats():
                combined_events[event1 + event2] += prob1 * prob2

        return Roll([(prob, event) for event, prob in combined_events.items()])

    # Choose a value based on the weighted probabilities in self.events
    def roll(self) -> float:
        weights, values = zip(*self.events)
        return random.choices(values, weights=weights, k=1)[0]  # noqa: S311
