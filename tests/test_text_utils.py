import pytest
from src.text_utils import reverse_string, is_palindrome, count_vowels, to_title_case

@pytest.mark.parametrize("inp,expected", [
    ("abc", "cba"),
    ("", ""),
    ("💻🔥", "🔥💻"),
    ("mañana", "anañam"),
])
def test_reverse_string(inp, expected):
    assert reverse_string(inp) == expected

@pytest.mark.parametrize("s,expected", [
    ("racecar", True),
    ("RaceCar", True),
    ("A man, a plan, a canal: Panama!", True),
    ("hello", False),
    ("", True),
])
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

@pytest.mark.parametrize("s,include_y,expected", [
    ("hello", False, 2),
    ("HELLO", False, 2),
    ("rhythm", False, 0),
    ("rhythm", True, 1),
    ("naïve", False, 3),
])
def test_count_vowels(s, include_y, expected):
    assert count_vowels(s, include_y) == expected

def test_to_title_case_basic():
    assert to_title_case("hello world") == "Hello World"

def test_to_title_case_mixed_and_acronyms():
    assert to_title_case("hello API gateway") == "Hello API Gateway"
    assert to_title_case("SIMPLE api TEST") == "Simple api TEST"

@pytest.mark.xfail(reason="Demonstration of expected failure for CI visibility")
def test_expected_failure_demo():
    assert reverse_string("abc") == "abc"
