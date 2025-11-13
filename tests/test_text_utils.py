import pytest
from src.text_utils import reverse_string, is_palindrome, count_vowels, to_title_case, remove_last_letter

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

@pytest.mark.parametrize("s,expected", [
    ("hello API gateway", "Hello API Gateway"),
    ("simple api TEST", "Simple Api TEST"),
])

def test_to_title_case_mixed_and_acronyms(s, expected):
    assert to_title_case(s) == expected

@pytest.mark.paramterize("s,expected", [
    ("hello", "hell"),
    ("world", "worl"),
])

def test_remove_last_letter(s, expected):
    assert remove_last_letter(s) == expected

@pytest.mark.xfail(reason="Demonstration of expected failure for CI visibility")
def test_expected_failure_demo():
    assert reverse_string("abc") == "abc"
