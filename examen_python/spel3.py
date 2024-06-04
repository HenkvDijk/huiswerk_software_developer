import random
import time

def spel():
    # Vraag de namen van de twee spelers
    while True:
        speler1 = input("Voer de naam van speler 1 in: ")
        speler2 = input("Voer de naam van speler 2 in: ")
        if speler1 == speler2:
            print("De namen van de spelers moeten verschillend zijn. Probeer het opnieuw.")
        else:
            break

    while True:
        try:
            level = int(input("Welk level (1 - 10) wil je spelen? "))
            if level < 1 or level > 10:
                raise ValueError
            break
        except ValueError:
            # Zorg ervoor dat alleen geldige gehele getallen worden geaccepteerd
            print("Voer een geldig getal tussen 1 en 10 in.")
    
    # Bedenk een willekeurig getal tussen 1 en level * 100
    geheim_getal = random.randint(1, level * 100)
    print("Het spel is begonnen! Raad het geheime getal!")
    
    # Variabelen om de starttijd van het spel en de starttijd van elke speler bij te houden
    start_tijd_spel = time.time()
        
    # Initialiseer de beurten voor beide spelers
    beurten1 = 0
    beurten2 = 0

    # Bepaal welke speler begint
    huidige_speler = random.choice([speler1, speler2])

    # Variabele om bij te houden of het getal is geraden
    gevonden = False

    while not gevonden:
        
        # Vraag de speler om een gok te doen
        try:
            gok = int(input(f"{huidige_speler}, raad het getal: "))
            # Verhoog het aantal pogingen (beurten) voor de huidige speler
            if huidige_speler == speler1:
                beurten1 += 1
            else:
                beurten2 += 1
        except ValueError:
            # Zorg ervoor dat alleen geldige gehele getallen worden geaccepteerd
            print("Voer een geldig getal in.")
            continue

        # Controleer of de gok juist, te laag of te hoog is
        if gok < geheim_getal:
            print("Hoger!")
        elif gok > geheim_getal:
            print("Lager!")
        else:
            # Als het juiste getal is geraden, feliciteer de speler en beëindig het spel
            eind_tijd_spel = time.time()
            totale_tijd = eind_tijd_spel - start_tijd_spel
            print(f"Gefeliciteerd {huidige_speler}, je hebt het juiste getal geraden in {totale_tijd:.2f} seconden!")
            gevonden = True

            # Bereken de totale tijd die de speler heeft genomen om het juiste getal te raden
            
            if huidige_speler == speler1:
                print(f"{speler2} heeft {beurten2} pogingen gedaan, maar helaas niet gewonnen.")
                print(f"{speler1} heeft in {beurten1} pogingen het juiste getal geraden en is de winnaar")
            else:
                print(f"{speler1} heeft {beurten1} pogingen gedaan, maar het getal helaas niet geraden.")
                print(f"{speler2} heeft in {beurten2} pogingen het juiste getal geraden en is de winnaar")

        
        
        # Wissel van speler
        huidige_speler = speler2 if huidige_speler == speler1 else speler1
    
# Voer de spel-functie uit als het script wordt gestart
if __name__ == "__main__":
    spel()
