def get_acc_num():
    nr_rachunku = ""
    while len(nr_rachunku) != 26 or not nr_rachunku.isnumeric():
        nr_rachunku = input("Podaj nr rachunku bankowego: ")
    return nr_rachunku


def print_acc_num_spaced(nr_rachunku):
    out = f"{nr_rachunku[:2]}"
    for i in range(2, 23, 4):
        out += f" {nr_rachunku[i : i + 4]}"
    print(f"Nr rachunku: {out}")


nr_rachunku = get_acc_num()
print_acc_num_spaced(nr_rachunku)