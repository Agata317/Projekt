def intro():
    print("=== ECHO RDZENIA LASU ===")
    print("Legenda głosi, że gdzieś w sercu tego lasu znajduje się Rdzeń.")
    print("Źródło mocy, które potrafi spełnić jedno życzenie.")
    print("Wielu próbowało. Mało kto wrócił.\n")


def pobierz_imie():
    imie = input("Podaj swoje imię, wędrowcze: ")
    print(f"\nWitaj, {imie}. Las już wie, że tu jesteś...\n")
    return imie


def wybor_sciezki():
    print("Stoisz na rozdrożu.")
    print("p - Kamienna ścieżka prowadząca w głąb lasu")
    print("l - Zarośnięta droga w stronę bagien")
    return input("Twój wybór: ")


def kamienna_sciezka(imie):
    print("\nIdziesz kamienną ścieżką.")
    print("Powietrze robi się ciężkie, a ziemia lekko drży.")
    print("Napotykasz starego strażnika run.\n")

    wybor = input("r - porozmawiaj, a - zaatakuj, u - uciekaj: ")

    if wybor == 'r':
        print("\nStrażnik widzi w Tobie rozsądek.")
        print("Daje Ci amulet ochrony.")
        return "amulet"

    elif wybor == 'a':
        print("\nZły pomysł.")
        print("Strażnik nie był tu przez wieki bez powodu.")
        print("Giniesz, a las zapamiętuje Twoją głupotę.")
        return "smierc"

    elif wybor == 'u':
        print("\nUciekasz, ale potykasz się i gubisz zapasy.")
        return "nic"

    else:
        print("\nLas nie rozumie niezdecydowanych.")
        return "smierc"


def bagna(imie):
    print("\nBagna bulgoczą pod Twoimi stopami.")
    print("Mgła odsłania cień ogromnej istoty.\n")

    wybor = input("w - walcz, s - skradaj się, c - cofaj się: ")

    if wybor == 's':
        print("\nUdaje Ci się przemknąć niezauważonym.")
        print("Znajdujesz stary miecz wbity w drzewo.")
        return "miecz"

    elif wybor == 'w':
        print("\nWalczysz dzielnie, ale bez broni nie masz szans.")
        return "smierc"

    elif wybor == 'c':
        print("\nWycofujesz się, zachowując życie.")
        return "nic"

    else:
        print("\nBagna pochłaniają niezdecydowanych.")
        return "smierc"


def final(imie, ekwipunek):
    print("\nDocierasz do serca lasu.")
    print("Przed Tobą pulsuje Rdzeń.\n")

    if "amulet" in ekwipunek and "miecz" in ekwipunek:
        print("Dzięki amuletowi i mieczowi jesteś w stanie podejść bliżej.")
        print("Rdzeń spełnia Twoje życzenie.")
        print(f"{imie}, wracasz jako legenda.")
        print("=== DOBRE ZAKOŃCZENIE ===")

    elif "amulet" in ekwipunek or "miecz" in ekwipunek:
        print("Masz tylko część potrzebnej mocy.")
        print("Rdzeń Cię oszczędza, ale niczego nie daje.")
        print("Wracasz żywy. To już coś.")
        print("=== NEUTRALNE ZAKOŃCZENIE ===")

    else:
        print("Rdzeń uznaje Cię za niegodnego.")
        print("Las zamyka się za Tobą na zawsze.")
        print("=== ZŁE ZAKOŃCZENIE ===")


def main():
    intro()
    imie = pobierz_imie()
    ekwipunek = []

    sciezka = wybor_sciezki()

    if sciezka == 'p':
        wynik = kamienna_sciezka(imie)
    elif sciezka == 'l':
        wynik = bagna(imie)
    else:
        print("\nBłądzisz bez celu, aż las Cię pochłania.")
        return

    if wynik == "smierc":
        print("\nKONIEC GRY.")
        return
    elif wynik != "nic":
        ekwipunek.append(wynik)

    print("\nWędrujesz dalej...\n")

    # Druga decyzja – zawsze druga próba
    wynik2 = bagna(imie) if sciezka == 'p' else kamienna_sciezka(imie)

    if wynik2 == "smierc":
        print("\nKONIEC GRY.")
        return
    elif wynik2 != "nic":
        ekwipunek.append(wynik2)

    final(imie, ekwipunek)


main()
