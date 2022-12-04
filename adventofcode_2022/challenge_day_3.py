from __future__ import annotations

from dataclasses import dataclass
import sys

from functools import reduce
from typing import List

from adventofcode_2022 import chunks, read_text_file, bin_2_str


CHARACTERS = [chr(ord("a") + c) for c in range(ord("z") - ord("a") + 1)] + [
    chr(ord("A") + c) for c in range(ord("Z") - ord("A") + 1)
]


def _create_hash(rushback: str) -> int:
    hash = 0

    for c in rushback:
        mask = 1 << CHARACTERS.index(c)
        # mask_str = bin_2_str(mask)

        hash = hash | mask

    # hash_str = bin_2_str(hash)

    return hash


def _get_first_bit_position(number: int) -> int:
    number_bin_str = bin(number)[2:]

    return number_bin_str[::-1].index("1")


def _calulate_id(rushback: str) -> str:
    half_length = len(rushback) // 2

    compartment_a = rushback[0:half_length]
    compartment_b = rushback[half_length:]

    compartment_a_hash = _create_hash(compartment_a)
    compartment_b_hash = _create_hash(compartment_b)

    # compartment_a_hash_str = bin_2_str(compartment_a_hash)
    # compartment_b_hash_str = bin_2_str(compartment_b_hash)

    shared_hash = compartment_a_hash & compartment_b_hash
    # shared_hash_str = bin_2_str(shared_hash)

    bit = _get_first_bit_position(shared_hash)
    id = CHARACTERS[bit]

    return id


@dataclass
class ElfRushback:
    rushback: str = None

    def __init__(self, rushback: str):
        if not rushback or len(rushback) % 2 != 0:
            raise ValueError("rushback length is not even")

        self.rushback = rushback
        self.id = _calulate_id(rushback)
        self.hash = _create_hash(rushback)


def _read_elf_rushbacks() -> List[ElfRushback]:
    data = read_text_file(3, "input.txt")

    rushbacks = []

    for line in data.splitlines():
        if line:
            try:
                rushbacks.append(ElfRushback(line))
            except Exception:
                print("Error reading rushback")

    return rushbacks


def _get_priority(c: str) -> int:
    return CHARACTERS.index(c) + 1


def _calculate_group_id(elf_rushback_list: List[ElfRushback]) -> str:
    shared_hash = 0

    for elf_rushback in elf_rushback_list:
        if shared_hash:
            shared_hash = shared_hash & elf_rushback.hash
        else:
            shared_hash = elf_rushback.hash

    shared_hash_str = bin_2_str(shared_hash)

    return CHARACTERS[_get_first_bit_position(shared_hash)]


def main() -> int:
    elf_rushback_list = _read_elf_rushbacks()

    repeated = [r.id for r in elf_rushback_list]

    repeated_priorities = [_get_priority(c) for c in repeated]

    total_repeated_priorities = reduce(
        lambda a, b: a + b,
        repeated_priorities,
        0,
    )

    print(f"The total rushbacks priorities is {total_repeated_priorities}")

    chunk_size = 3

    elf_rushback_chunks = chunks(elf_rushback_list, chunk_size)

    groups = [_calculate_group_id(chunk) for chunk in elf_rushback_chunks]

    group_priorities = [_get_priority(c) for c in groups]

    total_group_priorities = reduce(
        lambda a, b: a + b,
        group_priorities,
        0,
    )

    print(f"The total groups priorities is {total_group_priorities}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
