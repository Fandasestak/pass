while True:
    vztup = int(input("- uhadni číslo, které si myslím, a které jsem vidělil čtyřkou (1-30): "))
    if vztup <= 20:
        print("typni si znova🫠")
        pass
    elif 20 < vztup < 30:
        print(f"  Výsledek: {vztup} / 4 =", vztup / 4, "bodů")
        print("     Gratuluji nasel jsi ho!🎉")
        break
    else:
        print(f"co jsi to sakra zadal? znova😭")