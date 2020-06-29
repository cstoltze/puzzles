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


def reconstruct(input: str) -> str:
    input_chars = character_frequency(input)
    digit_frequency = {}
    remaining_choices = CHOICES
    while remaining_choices:
        u, remaining_choices = unique_choices(remaining_choices)
        for choice in u:
            # split into two funcs
            input_chars, occurrences = calc_occurrences(input_chars, choice)
            digit_frequency[choice.digit] = occurrences

    # validate that no characters remain
    assert all(v == 0 for v in input_chars.values())
    return "".join(str(i) * digit_frequency[i] for i in range(10))


def calc_occurrences(
    input_chars: Dict[str, int], choice: UniqueChoice
) -> Tuple[Dict[str, int], int]:
    occurrences = input_chars[choice.unique_char] // sum(
        1 for x in choice.name if x == choice.unique_char
    )
    for char in choice.name:
        input_chars[char] -= occurrences
    return input_chars, occurrences


def character_frequency(input: str) -> Dict[str, int]:
    character_frequency = defaultdict(int)
    for c in input:
        character_frequency[c] += 1
    return character_frequency


def unique_choices(
    choices: Dict[int, str]
) -> Tuple[List[UniqueChoice], Dict[int, str]]:
    """Returns unique choices with the character that makes them unique

    Also returns nonunique remaining choices
    
    """
    to_return = []
    for k, v in choices.items():
        chars_in_other_choices = set()
        for k2, v2 in choices.items():
            if k2 != k:
                chars_in_other_choices.update(v2)
        unique_chars = set(v) - chars_in_other_choices
        if unique_chars:
            to_return.append(
                UniqueChoice(digit=k, name=v, unique_char=list(unique_chars)[0])
            )

    return (
        to_return,
        {k: v for k, v in choices.items() if k not in [r.digit for r in to_return]},
    )
