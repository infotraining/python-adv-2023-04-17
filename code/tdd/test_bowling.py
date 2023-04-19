import pytest

class BowlingGame:
    pins_in_frame = 10

    def __init__(self) -> None:
        self._index = 0
        self._rolls = [0] * 21

    @classmethod
    def _is_strike(cls, rolls: int) -> bool:
        return rolls == cls.pins_in_frame

    def _strike_bonus(self, index: int) -> int:
        return self._rolls[index + 1] + self._rolls[index + 2]

    @property
    def score(self) -> int:
        total = sum(self._rolls)            
        for index, roll in enumerate(self._rolls):
            if self._is_strike(roll):
                total += self._strike_bonus(index + 1)            
        return total

    def roll(self, pins: int):        
        self._rolls[self._index] = pins
        if self._is_strike(pins):
            self._index += 2
        else:
            self._index += 1

@pytest.fixture
def game() -> BowlingGame:
    return BowlingGame()

def test_when_game_starts_then_score_is_zero(game):
    assert game.score == 0

@pytest.mark.parametrize("pins,score", [
    (1, 20),
    (2, 40),
    (0, 0),
    (9, 180)
])
def test_when_no_marks_in_game_score_is_sum_of_pins(game, pins, score):    
    for _ in range(20):
        game.roll(pins)
    
    assert game.score == score

def test_when_strike_next_two_rolls_score_is_doubled(game):
    game.roll(10)
    for i in range(18):
        game.roll(1)

    assert game.score == 10 + (2 * 1) + (2 * 1) + 16

def test_when_spare_next_roll_score_is_doubled(game):
    game.roll(5)
    game.roll(5) # spare
    for i in range(18):
        game.roll(1)

    assert game.score == eval("5 + 5 + (2 * 1) + 17")
