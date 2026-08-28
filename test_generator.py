"""
Automated tests for generator.py.

Run in VS Code's terminal with:  pytest
Or click "Run Test" above any test_ function if you have the Python
extension's test explorer enabled (Testing icon in the left sidebar,
then "Configure Tests" -> pytest).

These aren't "backtests" in the trading sense - there's no historical data
here. What we're checking is: does the generator reliably do what it
claims, across different word lists and grid sizes, every single time?
"""

import pytest
from generator import generate, verify, DIRECTIONS_EASY, DIRECTIONS_MEDIUM, DIRECTIONS_HARD

SAMPLE_WORDS = ["LINA", "WILLIAM", "ALEXANDER", "KAILAI", "KIKO",
                "BALLET", "HOCKEY", "CAMERA", "TRIPOD", "PIROUETTE"]


def test_all_words_get_placed():
    result = generate(SAMPLE_WORDS, size=25, seed=1)
    assert result["failed"] == []
    assert len(result["placements"]) == len(SAMPLE_WORDS)


def test_every_placed_word_is_actually_readable():
    # this is the important one: it catches bugs where a word was
    # "placed" but overlapping letters got clobbered afterwards
    result = generate(SAMPLE_WORDS, size=25, seed=1)
    assert verify(result) == []


def test_grid_is_the_requested_size():
    result = generate(SAMPLE_WORDS, size=20, seed=1)
    assert len(result["grid"]) == 20
    assert all(len(row) == 20 for row in result["grid"])


def test_same_seed_gives_same_puzzle():
    a = generate(SAMPLE_WORDS, size=25, seed=99)
    b = generate(SAMPLE_WORDS, size=25, seed=99)
    assert a["grid"] == b["grid"]


def test_different_seed_gives_different_puzzle():
    a = generate(SAMPLE_WORDS, size=25, seed=1)
    b = generate(SAMPLE_WORDS, size=25, seed=2)
    assert a["grid"] != b["grid"]


def test_too_small_grid_reports_failures_instead_of_crashing():
    # a 3x3 grid can't fit "ALEXANDER" (9 letters) - the generator should
    # report it as failed, not raise an exception or silently corrupt data
    result = generate(["ALEXANDER"], size=3, seed=1)
    assert "ALEXANDER" in result["failed"]
    assert verify(result) == []  # nothing bogus got placed either


@pytest.mark.parametrize("directions", [DIRECTIONS_EASY, DIRECTIONS_MEDIUM, DIRECTIONS_HARD])
def test_works_for_every_difficulty_level(directions):
    result = generate(SAMPLE_WORDS, size=25, directions=directions, seed=1)
    assert result["failed"] == []
    assert verify(result) == []


def test_every_cell_gets_filled_in_no_blanks():
    result = generate(SAMPLE_WORDS, size=15, seed=1)
    for row in result["grid"]:
        for cell in row:
            assert cell != "" and cell.isalpha()
