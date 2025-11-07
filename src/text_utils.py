import re
import unicodedata

def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    normalized = unicodedata.normalize("NFKD", s)
    cleaned = re.sub(r"[^A-Za-z0-9]", "", normalized).lower()
    return cleaned == cleaned[::-1]

def count_vowels(s: str, include_y: bool=False) -> int:
    vowels = set("aeiouAEIOU")
    if include_y:
        vowels.update(set("yY"))
    return sum(1 for ch in s if ch in vowels)

def to_title_case(s: str) -> str:
    words = s.split()
    out = []
    for w in words:
        if len(w) > 1 and w.isupper():
            out.append(w)
        else:
            out.append(w[:1].upper() + w[1:].lower() if w else w)
    return " ".join(out)
