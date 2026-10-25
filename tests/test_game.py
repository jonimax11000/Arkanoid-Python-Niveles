import pytest
from src.game import Game
from src.entities.player import Player

def test_game_initialization():
    game = Game()
    assert game.get_score() == 0
    assert game.running is True

def test_game_score_update():
    game = Game()
    game.update_score(10)
    assert game.get_score() == 10
    game.update_score(20)
    assert game.get_score() == 30

def test_game_negative_score_raises_error():
    game = Game()
    with pytest.raises(ValueError, match="Score cannot be negative"):
        game.update_score(-5)

def test_player_entity_event():
    player = Player()
    assert player.score == 0
    player.handle_event({"type": "increase_score", "value": 15})
    assert player.score == 15
    player.handle_event({"type": "increase_score"})
    assert player.score == 25
