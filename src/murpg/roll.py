class Roll:
    def __init__(self, events: list[tuple[int, float]]):
        self.events: list[tuple[int, float]] = events

    def getevents(self) -> list[tuple[int, float]]:
        return self.events

    def get_esperance(self) -> float:
        sum_events = sum(prob for prob, _ in self.events)
        return sum(event * prob for prob, event in self.events) / sum_events if sum_events > 0 else 0.0

    def add(self, other: "Roll"):
        # Implement the rolling logic here
        for event, rolls in other.events.items():
            if event in self.events:
                self.events[event].extend(rolls)
            else:
                self.events[event] = rolls
