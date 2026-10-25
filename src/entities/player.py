from typing import Dict, Any

class Player:
    def __init__(self):
        self.score = 0

    def handle_event(self, event: Dict[str, Any]) -> None:
        if event.get("type") == "increase_score":
            self.score += event.get("value", 10)