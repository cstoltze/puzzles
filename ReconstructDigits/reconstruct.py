from collections import defaultdict
from typing import Dict, List, Tuple
from dataclasses import dataclass

CHOICES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


@dataclass
class UniqueChoice:
    digit: int
    name: str
    unique_char: str


def reconstruct(_input: str) -> str:
    remaining_chars = character_frequency(_input)
    remaining_choices = CHOICES
    digit_frequency = {}
    while remaining_choices:
        u, remaining_choices = unique_choices(remaining_choices)
        for choice in u:
            occurrences = calc_occurrences(remaining_chars, choice)
            digit_frequency[choice.digit] = occurrences
            remaining_chars = remove_chars(remaining_chars, choice, occurrences)

    # validate that no characters remain
    assert all(v == 0 for v in remaining_chars.values())
    return "".join(str(i) * digit_frequency[i] for i in range(10))


def calc_occurrences(input_chars: Dict[str, int], choice: UniqueChoice) -> int:
    """Returns the number of occurrences of the choice in the given input_chars"""
    return input_chars[choice.unique_char] // sum(
        1 for x in choice.name if x == choice.unique_char
    )


def remove_chars(
    remaining: Dict[str, int], choice: UniqueChoice, occurrences: int
) -> Dict[str, int]:
    for char in choice.name:
        remaining[char] -= occurrences
    return remaining


def character_frequency(_input: str) -> Dict[str, int]:
    character_frequency = defaultdict(int)
    for c in _input:
        character_frequency[c] += 1
    return character_frequency


def unique_choices(
    choices: Dict[int, str]
) -> Tuple[List[UniqueChoice], Dict[int, str]]:
    """Returns unique_choices and remaining choices from input choices

    Unique choices are those with at least one character that is not found in
    any of the other choices. Any choices without a unique character are
    returned in the second return value.
    
    """
    unique_choices = []
    for k, v in choices.items():
        chars_in_other_choices = set()
        for k2, v2 in choices.items():
            if k2 != k:
                chars_in_other_choices.update(v2)
        unique_chars = set(v) - chars_in_other_choices
        if unique_chars:
            unique_choices.append(
                UniqueChoice(digit=k, name=v, unique_char=list(unique_chars)[0])
            )

    return (
        unique_choices,
        {
            k: v
            for k, v in choices.items()
            if k not in (r.digit for r in unique_choices)
        },
    )
