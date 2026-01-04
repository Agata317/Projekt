import { Input } from "postcss"

print("W starej stodole znalazłeś...")
print("wehikuł czasu")
imie = Input("Podaj swoje imię: ")
print("1 - Cofasz się do przeszłości.") 
print("2 - Idziesz do przyszłośći.")
wybor = Input("Wybierz 1 lub 2: ")
 if wybor == "1" then
    print("Jestes w epoce lodowcowej.")
    print("1- Idziesz do jaskini.")
    print("2- Ruszasz zwiedzać okolicę.")
    wybor = Input("Wybierz 1 lub 2: ")
    if wybor == "1" then
        print("W jaskini spotykasz grupę prymitywnych ludzi.")
        print("1- Probujesz sie z nimi porozumiec.")
        print("2- Pokazujesz im jak rozpalić ogień.")
        wybor = Input("Wybierz 1 lub 2: ")
        if wybor == "1" then 
             print(f"{imie}! Przecież oni cię nie rozumieją!")
             print("Czujac zagrozenie prymitywni ludzie zabijają cię.")
             print("Koniec gry.")
        if wybor == "2" then
            print("Prymitywni ludzie przestraszyli się ognia.")
            print("Czujac zagrozenie prymitywni ludzie zabijają cię.")
            print("Koniec gry.")
        else:
            print("Nieprawidłowy wybór.")
    if wybor == "2" then
         print("Idziesz przez zamarznieta doline.")
         print("Nagle przed tobą pojawia się mamut.")
         wybor = Input("Co robisz?/n" +
                 "w- walczę, u- uciekam:")
         if wybor == "w" then 
            print(f"{imie}! To zły pomysł napadać na mamuta bez broni!")
            print("Mamut cię zjada.")
            print("Koniec gry."))
         if wybor == "u" then 
            print("Udało ci się uciec!")
            print("Nagle przed tobą pojawia się dziura.")
            wybor == Input("Co robisz?/n" +
                           "s- skaczesz, k- kontynuujesz chodzenie:")
            if wybor == "s" then
                 print("Gratulacje udało ci się przeżyć!"
                 print("Wygrywasz grę!")
            if wybor == "k" then
                 print("Otoczony lodem zamarzasz na śmierć...")
                 print("Koniec gry.")
            else: print("Nieprawidłowy wybór.")
        else: print("Nieprawidłowy wybór.")
    else: print("Nieprawidłowy wybór.")
if wybor == "2" then 
    print("Jestes w przyszlosci.")
    print("1- Idziesz do miasta.")
    print("2- Ruszasz zwiedzać okolicę.")
    wybor = Input("Wybierz 1 lub 2: ")
    if wybor == "1" then 
        print("W miescie spotykasz grupe ludzi.")
        print("Dowiadujesz się od nich, że musisz na siebie uważać, bo na świecie panuje chaos.")
        print("1- Idziesz do sklepu.")
         print("2- Idziesz się schować.")
         wybor = Input("Wybierz 1 lub 2:")
         if wybor == "1" then
            print("W sklepie spotykasz zombie.")
            wybor == Input("Co robisz?/n" + 
                           "w- walczę, u- uciekam:")
                           if wybor == "w" then 
                             print(f"{imie}! To zły pomysł napadać na zombie bez broni!")
                               print("Zombie cię zjada.")
                                 print("Koniec gry.") 
                            if wybor == "u" then
                                print("Udało ci się uciec!")
                                 print("Nagle przed tobą pojawia się dziura.")
                                 wybor == Input("Co robisz?/n" +
                                                 "s- skaczesz, k- kontynuujesz chodzenie:")
                                                 if wybor == "s" then 
                                                    print("Gratulacje udało ci się przeżyć!")
                                                    print("Wygrywasz grę!")
                                                 if wybor == "k" then 
                                                  print("Dopada cię tuzin zombiaków...")
                                                  print("Koniec gry.")
                                                 else: print("Nieprawidłowy wybór.")
                            else: print("Nieprawidłowy wybór.")      
         if wybor == "2" then      
         print("Chowasz się w szopie.")
         print("Spotykasz dziewczynę, która mówi ci, że jest twoją córką.")
         print("1- Wierzę jej.")
         print("2- Uciekam od niej, bo mam złe przeczucie.")
         wybor = Input("Wybierz 1 lub 2:")              
         if wybor == "1" then  
            print("Okazuje się, że dziewczyna chce cię zabić.")
            print("Koniec gry.")  
         if wybor == "2" then  
            print("Udało ci się uciec!")  
            print("Nagle przed tobą pojawia się zombie.")
            print("Koniec gry!")
         else: print("Nieprawidłowy wybór.")  
    if wybor == "2" then    
        print("Idziesz do laboraturium.")
        print("W laboraturium spotykasz naukowca.")  
        print("1- Probujesz się z nim porozumieć i dowiedzieć się co stało się ze światem.")      
        print("2- Wolisz poznać prawdę o świecie na własną rękę.")
        wybor = Input("Wybierz 1 lub 2: ")  
          if wybor == "1" then  
          print("Naukowiec wyjaśnił ci, że świat został zniszczony przez wirusa.") 
          print("Naukowiec każe ci wrócić wehikułem czasu do teraźniejszości i wszystkiemu zapobiec")
          print("1- Wracasz do teraźniejszości.")
          print("2- Wolisz zostać w przyszłości.")
              wybor = Input("Wybierz 1 lub 2: ")    
              if wybor == "1" then  
              print("Gratulacje udało ci się przeżyć!")  
              print("Wygrywasz grę!")  
              if wybor == "2" then  
              print("Naukowiec zabija cię, bo nie chce cię tu trzymać.")
              print("Koniec gry.")
              else: print("Nieprawidłowy wybór.")  
        if wybor == "2" then  
            print("Szukasz w laboratorium informacji o wirusie.")
            print("Dowiadujesz się, że wirus rozprzestrzenił się dzięki zanieczyszczeniu środowiska.")
            print("1- Wracasz do teraźniejszości.")  
            print("2- Wolisz zostać w przyszłości.")      
            wybor = Input("Wybierz 1 lub 2: ")                      
            if wybor == "1" then              
             print("Gratulacje udało ci się przeżyć!")
             print("Wygrywasz grę i ratujesz świat przed wirusem!")    
            if wybor == "2" then  
             print("Zostajesz w przyszłości i umierasz z głodu.")          
             print("Koniec gry.")  
            else: print("Nieprawidłowy wybór.")    
        else: print("Nieprawidłowy wybór.")      
    else: print("Nieprawidłowy wybór.")        
else: print("Nieprawidłowy wybór.")
print("Koniec gry.")
print("Dziękuję za grę!")
                              


               
            
