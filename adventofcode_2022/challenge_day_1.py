from __future__ import annotations

import heapq
import sys
from functools import reduce

from attr import dataclass

from adventofcode_2022 import read_text_file


@dataclass
class Elf:
    total_calories: int = 0
    id: int = 1

    def add_calories(self, calories: int):
        self.total_calories += calories

    def next_elf(self) -> Elf:
        return Elf(id=self.id + 1)

    def __lt__(self, other: Elf) -> bool:
        return self.total_calories > other.total_calories


class ElfHeap(Elf):
    def __init__(self):
        self.data = []

    def push(self, elf_inventory: Elf):
        heapq.heappush(self.data, elf_inventory)

    def pop(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


def _read_elf_inventory() -> ElfHeap:
    data = read_text_file(1, "input.txt")

    heap = ElfHeap()
    current_elf = Elf()
    to_add = False

    for line in data.splitlines():
        if line:
            try:
                current_elf.add_calories(int(line))

                to_add = True
            except Exception:
                print("Error adding calories")
        elif current_elf.total_calories > 0:
            heap.push(current_elf)
            to_add = False

            current_elf = current_elf.next_elf()

    if to_add:
        heap.push(current_elf)

    return heap


def main() -> int:
    elf_inventory = _read_elf_inventory()

    fatest_elf = elf_inventory.pop()

    print(f"The elf with most calories is {fatest_elf}")

    num_fatest_elfs = 3

    total_calories = reduce(
        lambda a, b: a + b,
        [
            elf_inventory.pop().total_calories
            for i in range(min(len(elf_inventory), num_fatest_elfs))
        ],
        0,
    )

    print(
        f"The total calories of the {num_fatest_elfs} fatest_elfs is {total_calories}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
