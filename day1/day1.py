# min 50 stars by dec 25th.

from util.get_content import get_content


def main() -> None:
    calories = get_content("day1.txt").splitlines()
    calories_by_elf = []

    temp = []
    for el in calories:
        if el != "":
            temp.append(el)
        else:
            calories_by_elf.append(temp)
            temp = []

    i_r = 0
    most_cal = 0
    mostcallist = []
    for _ in range(3):
        for j, elf in enumerate(calories_by_elf):
            current_elf = get_calories(elf)
            if current_elf >= most_cal:
                i_r = j
                most_cal = current_elf
        mostcallist.append(most_cal)
        calories_by_elf.pop(i_r)
        most_cal = 0

    print(sum(mostcallist))


def get_calories(calories):
    cal = 0
    for elf in calories:
        cal += int(elf)
    return cal


main()
