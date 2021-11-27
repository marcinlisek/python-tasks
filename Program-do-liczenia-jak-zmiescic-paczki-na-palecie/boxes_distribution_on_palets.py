def boxes_distribution():

    pallet_width = int(input("Wprowadz szerokosc palety: "))
    pallet_lenght = int(input("Wprowadz dlugosc palety: "))
    box_width = int(input("Wprowadz szerokosc gry: "))
    box_lenght = int(input("Wprowadz dlugosc gry: "))

    lenght_varian1 = pallet_lenght / box_lenght
    lenght_varian2 = pallet_lenght / box_width

    width_variant1 = pallet_width / box_lenght
    width_variant2 = pallet_width / box_width

    total_varinat1 = round(lenght_varian1 * width_variant1)
    total_varinat2 = round(lenght_varian2 * width_variant2)

    if total_varinat1 >= total_varinat2:
        return ("wzdluz", total_varinat1)

    else:
        return ("wszerz", total_varinat2)


result = boxes_distribution()

if result[0] == "wzdluz":
    print(f"Gry nalezy ulozyc po dlugosci na palecie po dlugosci. Gier na palecie zmiesci sie {result[1]}.")

else:
    print(f"Gry nalezy ulozyc po szerokosci na palecie po dlugosci. Gier na palecie zmiesci sie {result[1]}.")
