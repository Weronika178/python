import random 

life = 100
mana = 50
gold = 0 
sadzonki = 3
eliksir = 2 
ogrod = []
dzien = 1
def gra() :
    while life > 0 :
        print("1 - sadz rosliny")
        print("2 - omin dzien")
        print("3 - idz do sklepu")
        print("4 - idz do domu")
        print("5 - idz do lasu")
        print("6 - zakoncz gre")
        wybor = input("wybierz opcje")
        if wybor == "1" :
            sadzenie_roslin()
        elif wybor == "2" :
            ilosc_dni()
        elif wybor == "3" :
            sklep()
        elif wybor == "4" :
            dom()
        elif wybor == "5" :
            wyprawa_do_lasu()
        elif wybor == "6":
            print("koniec gry")
            break 
        else: 
            print("wybrales zla opcje")



def sadzenie_roslin() :
    global sadzonki, ogrod 
    if sadzonki > 0:
        czas_wzrostu = random.randint (3,5)
        ogrod.append(czas_wzrostu)
        sadzonki -= 1
        print("-" *30)
        print(f"zasadziles rosline i bedzie rosnac przez {czas_wzrostu} dni")
        print("-" *30)
        print(f"stan ogrodu (dni wzrostu roslin): {ogrod}")
        print(f"zasoby : sadzonki - {sadzonki}, eliksiry - {eliksir}, zloto - {gold}, zycie - {life}, mana - {mana}")
    else:
        print("nie masz wiecej sadzonek")

def sprawdz_ogrod() :
    global ogrod, gold 
    nowy_ogrod = []
    for czas in ogrod:
        if czas == 0 :
            print("jedna roslina jest gotowa, sprzedajesz ja za 10 zlota")
            gold += 10 
        else:
            nowy_ogrod.append(czas)
    ogrod = nowy_ogrod

def walka() :
    global life, mana, eliksir 
    print("Atakuje cie potwor")
    life_potwora = random.randint(20,40) 
    while life_potwora > 0 and life > 0 :
        print(f"Potwor ma {life_potwora} zycia. Ty masz {life} zycia i {mana} many.")
        print("wybierz opcje: a - atak, m - magiczna, e - eliksir")
        wybor = input("twoj wybor:").upper()
        if wybor == 'a' :
            obrazenia = random.randint(5,15) 
            life_potwora -= obrazenia 
            print(f"Zadales {obrazenia} obrazen")
        elif wybor == 'm' :
            if mana >= 10 : 
                obrazenia = random.randint(15,30)
                life_potwora -= obrazenia 
                mana -= 10 
                print(f"Zadales {obrazenia} obrazen")
            else:
                print("Nie masz wystarczajaco many")
        elif wybor == 'e' :
            if eliksir > 0 :
                hp = random.randint(20,40)
                life += hp 
                eliksir -= 1
                print(f"uzyles eliksiru i odzyskales {hp} zycia")
            else:
                print("nie masz eliksirow")
        else:
            print("Nieprawidlowy wybor")

        if life_potwora > 0:
            obrazenia_potwora = random.randint(5,12)
            life -= obrazenia_potwora
            print(f"Potwor zadal ci {obrazenia} obrazen") 
    if life > 0 : 
        print("Pokonales potwora")
    else:
        print("Zostales pokonany przez potwora")

def ilosc_dni() :
    global dzien,ogrod,sadzonki 
    print(f"=== dzien {dzien} ===")
    for i in range(len(ogrod)) :
        if ogrod [i] > 0 :
            ogrod [i] -= 1 
        else:
            ogrod [i] = 0 
    losowe = random.randint(1,10) 
    if losowe <= 4: 
        walka()
    elif losowe > 4:
        sadzonki += 1 
        print("Znalazles nowa sadzonke")
    sprawdz_ogrod()
    print(f"stan ogrodu (dni wzrostu roslin): {ogrod}")
    print(f"zasoby : sadzonki - {sadzonki}, eliksiry - {eliksir}, zloto - {gold}, zycie - {life}, mana - {mana}")
    dzien += 1
    

def sklep() :
    global gold, sadzonki,eliksir
    print("=== sklep ===")
    print("1 - kup sadzonke(10 zlota)")
    print("2 - kup eliksir(20 zlota)")
    print("3 - wyjdz")
    while True :
        wybor = input("wybierz opcje")
        if wybor == "1" :
            if gold >= 10 :
                sadzonki += 1 
                gold -= 10
                print("kupiles sadzonke")
            else: 
                print("nie masz wystarczajaco zlota")
        elif wybor == "2" :
            if gold >= 20 :
                eliksir += 1
                gold -= 20
                print("kupiles eliksiir")
            else:
                print("nie masz wystarczajaco zlota")
        elif wybor == "3" :
            print("wychodzisz ze sklepu")
            break 
        else:
            print("nieprawidlowy wybor")
    print(f"zasoby : sadzonki - {sadzonki}, eliksiry - {eliksir}, zloto - {gold}")

def dom() :
    global gold, sadzonki, eliksir, mana, life, ogrod 
    level_domu = 0 
    max_level = 5
    koszt_zlota = [20,50,100,150,200]
    koszt_sadzonki = [2,3,5,8,11]
    koszt_eliksir = [0,1,2,3,5]
    nagrody = ["+ 10 life ", " + sadzonka", " + 25 many", "+ 20 gold" , " + 2 eliksiry"]
    print("=== ulepszaj swoj dom aby dostawac roznorodne nagrody ===")
    print(" kazdy poziom wymaga okreslonych zasobow i przynosi korzysci")
    while level_domu < max_level :
        print(f"aktualny level domu: {level_domu}")
        if level_domu > 0 :
            print(f"obecna nagroda: {nagrody[level_domu - 1]}")
        print("koszt ulepszenia na nastepny level: ")
        print(f"- gold: {koszt_zlota [level_domu]}")
        print(f"- sadzonki: {koszt_sadzonki [level_domu]}")
        print(f"- elksiry: {koszt_eliksir [level_domu]}")
        print("wybierz opcje")
        print("1 - ulepsz dom")
        print("2 - informacje")
        print("3 - wyjdz z domu")
        wybor = input() 
        if wybor == "1" :
            if (gold >= koszt_zlota [level_domu] and sadzonki >= koszt_sadzonki [level_domu] and eliksir >= koszt_eliksir [level_domu]):
                gold -= koszt_zlota [level_domu]
                sadzonki -= koszt_sadzonki [level_domu]
                eliksir -= koszt_eliksir [level_domu]
                level_domu += 1 
                print("Ulepszyles swoj dom")
                if level_domu <= max_level :
                    print(f"nagroda : {nagrody[level_domu - 1]} ")
                
                if level_domu == 1 :
                    life += 10 
                    print("Twoje zycie wzroslo o 10")
                elif level_domu == 2 :
                    sadzonki += 1 
                    print("Dostales sadzonke")
                elif level_domu == 3 :
                    mana += 25 
                    print("dostales 25 many")
                elif level_domu == 4 :
                    gold += 20 
                    print("dostales 20 gold")
                elif level_domu == 5 :
                    eliksir += 2 
                    print("dostales 2 eliksiry")
            else :
                print("Nie masz wystarczajaco duzo zasobow")
        elif wybor == "2" :
            print(f"aktualny level domu: {level_domu}")
            if level_domu > 0 :
                print(f"obecna nagroda: {nagrody[level_domu - 1]}")
            print(f"zasoby : sadzonki - {sadzonki}, eliksiry - {eliksir}, zloto - {gold}")
        elif wybor == "3" :
            print("Wychodzisz z domu")
            break
        else: 
            print("nieznana akcja")
    if level_domu == max_level :
        print("Twoj dom jest na maksymalnym poziomie")
def wyprawa_do_lasu() :
    global mana, life, gold, sadzonki, eliksir 
    print("=== wyprawa do lasu ===")
    print("Idac w las czekaja cie rozne sytuacje. Wybierz czy chcesz isc dalej czy wrocic")
    kroki = 0 
    zdobyte_zloto = 0
    zdobyte_sadzonki = 0 
    zdobyte_eliksiry = 0
    obrazenia = 0 
    while True :
        print("co chcesz zrobic?")
        print("1 - kontynuuj wyprawe")
        print("2 - wroc")
        wybor = input()
        if wybor == "1" :
            kroki += 1 
            print(f"kroki {kroki}")
            wydarzenie = random.randint(1,100)
            if wydarzenie <= 30 :
                rodzaj_zagrozen = random.choice(["atak wilkow", "zatruty owoc", "upadek z galezi"])
                if rodzaj_zagrozen == "atak wilkow" :
                    obrazenia = random.randint(10,20)
                    life -= obrazenia 
                    print(f"Zaatakowal cie wilk i tracisz{obrazenia} zycia")
                elif rodzaj_zagrozen ==  "zatruty owoc" :
                    obrazenia = random.randint(5,15)
                    life -= obrazenia 
                    print(f"Zjadles zatruty owoc i tracisz{obrazenia} zycia")
                elif rodzaj_zagrozen ==  "upadek z galezi":
                    obrazenia = random.randint(10,20)
                    life -= obrazenia 
                    print(f"Spadles z galezi i tracisz{obrazenia} zycia")
                if life <= 0:
                    print("UMARLES")
                    break 
            elif wydarzenie > 30 :
                rodzaj_zdarzenia = random.choice(["zloto", "sadzonki2", "eliksir many", "eliksir zycia", "eliksir"])
                if rodzaj_zdarzenia  == "zloto" :
                    zloto = random.randint 
                    gold += zloto 
                    print(f"Znalazles {zloto} zlota")
                elif rodzaj_zdarzenia == "sadzonki2":
                    sadzonki2 = random.randint(1,3)
                    sadzonki += sadzonki2 
                    print(f"Znalazles {sadzonki2} sadzonek")
                


        elif wybor == "2" :
            print("Wracasz do ogrodu") 
            break 
        else:
            print("Nieprawidlowa akcja. Wybierz ponownie")

                                       



