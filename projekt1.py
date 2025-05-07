# Projekt 1 - Task Manager - Martin Papež

# Seznam s úkoly
ukoly = [] 

# Definování funkcí 
def hlavni_menu():
    """Spustí hlavní menu."""
    while True:
        print ("\nSprávce úkolů - Hlavní menu 📝") 
        print ("1. Přidat nový úkol")
        print ("2. Zobrazit všechny úkoly")
        print ("3. Odstranit úkol")
        print ("4. Konec programu")

        volba = input ("Vyberte možnost (1-4): ") # vstupní volba z hlavního menu
        if  volba == "1":
            print() # čistý řádek pro přehlednost při spuštění (lze jinak??)
            pridat_ukol()
        elif volba == "2":
            print()
            zobrazit_ukoly()
        elif volba == "3":
            print()
            odstranit_ukol()
        elif volba == "4":
            print()
            print("Konec programu.👋")
            break
        else:
            print("❌ Neplatná volba. Zkuste to znovu.")


def pridat_ukol():
    """Přidá úkol, popis úkolu a uloží do seznamu."""
    global ukoly # Seznam je mimo funkci tak se musím na ni odkazat skrz příkaz "global"! (globální)
    while True:
        nazev = input ("Zadejte název úkolu: ").strip() # strip() zamezí přidávání nežádoucích mezer či mezer bez textu
        if not nazev:
            print("❓ Nic jste nezadal! Zadejte prosím znova.")
            continue
        else:
            break

    while True:
        popis = input ("Zadejte popis úkolu: ").strip()
        if not popis:
            print("❓ Nic jste nezadal! Zadejte prosím znova.")
            continue 
        else:
            break

    # Přidání úkolu do seznamu
    ukoly.append({"Název": nazev, "Popis": popis})
    print(f"✅ Úkol '{nazev}' byl úspěšně přidán!")
    
def zobrazit_ukoly():
    """Zobrazí úkoly v seznamu"""
    global ukoly
    if not ukoly:
        print("❌ Seznam úkolů je prázdný!")
        return
    else:
        print("📋 Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"📌 {i}. {ukol['Název']} - {ukol['Popis']}")
        

def odstranit_ukol():
    """Odstraní úkol ze seznamu"""
    global ukoly
    if not ukoly:
        print("❌ Seznam úkolů je prázdný!")
        return
     
    # Tímto si zobrazím úkoly v seznamu
    while True:
        print("\n📋 Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"📌 {i}. {ukol['Název']} - {ukol['Popis']}")

        try:
            volba = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if volba in range(1, len(ukoly) + 1):
                odstraneny = ukoly.pop(volba - 1)
                print(f"✅ Úkol \"{odstraneny['Název']}\" byl odstraněn.")
                break  # Break aby po odstranění úkolu se vrátilo do menu!
            else:
                print("⚠️  Úkol s tímto číslem neexistuje. Zkuste to znovu.")
        except ValueError:
            print("❗Zadejte platné číslo.")
   
hlavni_menu()


