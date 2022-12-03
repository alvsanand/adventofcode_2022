import sys

from functools import reduce

from adventofcode_2022 import read_elf_inventory


def main() -> int:
    elf_inventory = read_elf_inventory()

    num_fatest_elfs = 3

    total_calories = reduce(
        lambda a, b: a + b,
        [
            elf_inventory.pop().total_calories
            for i in range(min(len(elf_inventory), num_fatest_elfs))
        ],
        0,
    )

    print(f"The total calories of the is {total_calories}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
