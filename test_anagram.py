import string
import unicodedata
from collections import Counter

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Remove accents by decomposing Unicode characters and removing combining marks
def clean(s):
    normalized = unicodedata.normalize('NFKD', s)
    without_accents = ''.join(c for c in normalized if not unicodedata.combining(c))
    return ''.join(c for c in without_accents.lower() if c.isalnum())

def is_anagram(str1, str2):
    return Counter(clean(str1)) == Counter(clean(str2))

test_cases = [
    ("Listen", "Silent", True),
    ("Hello", "World", False),
    ("A gentleman", "Elegant man", True),
    ("Clint Eastwood", "Old West Action", True),
    ("Dormitory", "Dirty room", True),
    ("The eyes", "They see", True),
    ("Astronomer", "Moon starer", True),
    ("Conversation", "Voices rant on", True),
    ("12345", "54321", True),
    ("12345", "123456", False),
    ("", "", True),
    ("a", "A", True),
    ("éclair", "câlier", True), 
    ("School master", "The classroom", True),
    ("Eleven plus two", "Twelve plus one", True),
    ("Listen!", "Silent.", True),  # punctuation ignored
    ("Debit card", "Bad credit", True),
    ("The Morse Code", "Here come dots", True),
    ("Slot machines", "Cash lost in me", True),
    ("Conversation", "Voices rant onn", False),  # extra 'n' on one side
    ("Funeral", "Real fun", True),
    ("Funeral", "Real funn", False),
]

for str1, str2, expected in test_cases:
    result = is_anagram(str1, str2)
    status = "PASS" if result == expected else "FAIL"
    color = GREEN if status == "PASS" else RED
    print(f'is_anagram("{str1:20}", "{str2:20}") = {str(result):5} (Expect: {expected}) -> {color}{status}{RESET}')

    if status == "FAIL":
        cleaned_str1 = clean(str1)
        cleaned_str2 = clean(str2)
        print(f"  Cleaned strings:\n    {str1:20} -> {cleaned_str1}")
        print(f"    {str2:20} -> {cleaned_str2}")
        print(f"  Counts:\n    {str1:20} -> {Counter(cleaned_str1)}")
        print(f"    {str2:20} -> {Counter(cleaned_str2)}")
