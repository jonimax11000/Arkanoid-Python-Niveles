import pytest
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BG, COLOR_NEON_CYAN, COLOR_NEON_PINK
from src.main import init_game

def test_config_constants():
    assert isinstance(SCREEN_WIDTH, int)
    assert SCREEN_WIDTH == 800
    assert isinstance(SCREEN_HEIGHT, int)
    assert SCREEN_HEIGHT == 600
    assert isinstance(FPS, int)
    assert FPS == 60
    
    assert isinstance(COLOR_BG, tuple)
    assert len(COLOR_BG) == 3
    assert all(isinstance(c, int) for c in COLOR_BG)
    assert COLOR_BG == (10, 10, 25)
    
    assert isinstance(COLOR_NEON_CYAN, tuple)
    assert len(COLOR_NEON_CYAN) == 3
    assert all(isinstance(c, int) for c in COLOR_NEON_CYAN)
    assert COLOR_NEON_CYAN == (0, 255, 240)
    
    assert isinstance(COLOR_NEON_PINK, tuple)
    assert len(COLOR_NEON_PINK) == 3
    assert all(isinstance(c, int) for c in COLOR_NEON_PINK)
    assert COLOR_NEON_PINK == (255, 0, 128)


def test_init_game():
    result = init_game()
    assert result['status'] == 'initialized'
    assert 'screen_size' in result
    assert result['screen_size'] == (800, 600)