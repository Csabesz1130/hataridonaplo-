from datetime import date
from src.esemenykezelo import EsemenyKezelo

def main():
    kezelo = EsemenyKezelo()
    
    while True:
        print("\nHatáridőnapló")
        print("1. Új esemény")
        print("2. Mai események")
        print("3. Mentés fájlba")
        print("4. Betöltés fájlból")
        print("5. Kilépés")
        
        valasztas = input("\nVálasszon (1-5): ")
        
        if valasztas == "1":
            print("\nÚj esemény létrehozása")
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            idopont = input("Időpont (ÓÓ:PP): ")
            helyszin = input("Helyszín: ")
            nev = input("Esemény neve: ")
            megjegyzes = input("Megjegyzés: ")
            
            if kezelo.uj_esemeny(datum, idopont, helyszin, nev, megjegyzes):
                print("Esemény sikeresen létrehozva!")
            else:
                print("Hiba történt az esemény létrehozásakor!")
                
        elif valasztas == "2":
            mai_esemenyek = kezelo.lista_nap(date.today())
            if mai_esemenyek:
                print("\nMai események:")
                for esemeny in mai_esemenyek:
                    print(esemeny)
            else:
                print("Nincsenek mai események!")
                
        elif valasztas == "3":
            fajlnev = input("Adja meg a fájlnevet: ")
            if kezelo.mentes_fajlba(fajlnev):
                print("Események sikeresen mentve!")
            else:
                print("Hiba történt a mentés során!")
                
        elif valasztas == "4":
            fajlnev = input("Adja meg a fájlnevet: ")
            if kezelo.betoltes_fajlbol(fajlnev):
                print("Események sikeresen betöltve!")
            else:
                print("Hiba történt a betöltés során!")
                
        elif valasztas == "5":
            break

if __name__ == "__main__":
    main()
