print("=== ECHO RDZENIA LASU ===")
print("Legenda głosi, że gdzieś w sercu tego lasu znajduje się Rdzeń.")
print("Źródło mocy, które potrafi spełnić jedno życzenie.")
print("Wielu próbowało. Mało kto wrócił.\n")

imie = input("Podaj swoje imię, wędrowcze: ")
print(f"\nWitaj, {imie}. Las już wie, że tu jesteś...\n")

ekwipunek = []

print("Stoisz na rozdrożu.")
print("p - Kamienna ścieżka prowadząca w głąb lasu")
print("l - Zarośnięta droga w stronę bagien")
sciezka = input("Twój wybór: ")

# PIERWSZA ŚCIEŻKA
if sciezka == 'p':
    print("\nIdziesz kamienną ścieżką.")
    print("Powietrze robi się ciężkie, a ziemia lekko drży.")
    print("Napotykasz starego strażnika run.\n")

    wybor = input("r - porozmawiaj, a - zaatakuj, u - uciekaj: ")

    if wybor == 'r':
        print("\nStrażnik widzi w Tobie rozsądek.")
        print("Daje Ci amulet ochrony.")
        ekwipunek.append("amulet")

    elif wybor == 'a':
        print("\nZły pomysł.")
        print("Strażnik nie był tu przez wieki bez powodu.")
        print("Giniesz, a las zapamiętuje Twoją głupotę.")
        print("\nKONIEC GRY.")
        exit()

    elif wybor == 'u':
        print("\nUciekasz, ale potykasz się i gubisz zapasy.")

    else:
        print("\nLas nie rozumie niezdecydowanych.")
        print("\nKONIEC GRY.")
        exit()

elif sciezka == 'l':
    print("\nBagna bulgoczą pod Twoimi stopami.")
    print("Mgła odsłania cień ogromnej istoty.\n")

    wybor = input("w - walcz, s - skradaj się, c - cofaj się: ")

    if wybor == 's':
        print("\nUdaje Ci się przemknąć niezauważonym.")
        print("Znajdujesz stary miecz wbity w drzewo.")
        ekwipunek.append("miecz")

    elif wybor == 'w':
        print("\nWalczysz dzielnie, ale bez broni nie masz szans.")
        print("\nKONIEC GRY.")
        exit()

    elif wybor == 'c':
        print("\nWycofujesz się, zachowując życie.")

    else:
        print("\nBagna pochłaniają niezdecydowanych.")
        print("\nKONIEC GRY.")
        exit()

else:
    print("\nBłądzisz bez celu, aż las Cię pochłania.")
    print("\nKONIEC GRY.")
    exit()

print("\nWędrujesz dalej...\n")

# DRUGA DECYZJA (zawsze druga ścieżka)
if sciezka == 'p':
    print("\nBagna bulgoczą pod Twoimi stopami.")
    print("Mgła odsłania cień ogromnej istoty.\n")

    wybor = input("w - walcz, s - skradaj się, c - cofaj się: ")

    if wybor == 's':
        print("\nUdaje Ci się przemknąć niezauważonym.")
        print("Znajdujesz stary miecz wbity w drzewo.")
        ekwipunek.append("miecz")

    elif wybor == 'w':
        print("\nWalczysz dzielnie, ale bez broni nie masz szans.")
        print("\nKONIEC GRY.")
        exit()

    elif wybor == 'c':
        print("\nWycofujesz się, zachowując życie.")

    else:
        print("\nBagna pochłaniają niezdecydowanych.")
        print("\nKONIEC GRY.")
        exit()

else:
    print("\nIdziesz kamienną ścieżką.")
    print("Powietrze robi się ciężkie, a ziemia lekko drży.")
    print("Napotykasz starego strażnika run.\n")

    wybor = input("r - porozmawiaj, a - zaatakuj, u - uciekaj: ")

    if wybor == 'r':
        print("\nStrażnik widzi w Tobie rozsądek.")
        print("Daje Ci amulet ochrony.")
        ekwipunek.append("amulet")

    elif wybor == 'a':
        print("\nZły pomysł.")
        print("Strażnik nie był tu przez wieki bez powodu.")
        print("\nKONIEC GRY.")
        exit()

    elif wybor == 'u':
        print("\nUciekasz, ale potykasz się i gubisz zapasy.")

    else:
        print("\nLas nie rozumie niezdecydowanych.")
        print("\nKONIEC GRY.")
        exit()

# FINAŁ
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
