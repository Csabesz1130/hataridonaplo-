from typing import List, Optional
import json
from datetime import datetime, date, timedelta
from src.esemeny import Esemeny

class EsemenyKezelo:
    """Események kezelését végző osztály"""
    def __init__(self):
        self.esemenyek: List[Esemeny] = []
        self.kovetkezo_azonosito = 1

    def uj_esemeny(self, datum: str, idopont: str, helyszin: str, 
                   nev: str, megjegyzes: str = "") -> bool:
        """Új esemény létrehozása"""
        try:
            datum_obj = datetime.strptime(datum, "%Y-%m-%d").date()
            esemeny = Esemeny(
                azonosito=self.kovetkezo_azonosito,
                datum=datum_obj,
                idopont=idopont,
                helyszin=helyszin,
                nev=nev,
                megjegyzes=megjegyzes
            )
            self.esemenyek.append(esemeny)
            self.kovetkezo_azonosito += 1
            return True
        except ValueError:
            return False

    def lista_nap(self, datum: date) -> List[Esemeny]:
        """Adott napi események listázása"""
        return [e for e in self.esemenyek if e.datum == datum]

    def mentes_fajlba(self, fajlnev: str) -> bool:
        """Események mentése JSON fájlba"""
        try:
            with open(fajlnev, 'w', encoding='utf-8') as f:
                adatok = []
                for esemeny in self.esemenyek:
                    adatok.append({
                        'azonosito': esemeny.azonosito,
                        'datum': esemeny.datum.isoformat(),
                        'idopont': esemeny.idopont,
                        'helyszin': esemeny.helyszin,
                        'nev': esemeny.nev,
                        'megjegyzes': esemeny.megjegyzes
                    })
                json.dump(adatok, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Hiba a mentés során: {e}")
            return False

    def betoltes_fajlbol(self, fajlnev: str) -> bool:
        """Események betöltése JSON fájlból"""
        try:
            with open(fajlnev, 'r', encoding='utf-8') as f:
                adatok = json.load(f)
            self.esemenyek = []
            max_azonosito = 0
            for adat in adatok:
                esemeny = Esemeny(
                    azonosito=adat['azonosito'],
                    datum=date.fromisoformat(adat['datum']),
                    idopont=adat['idopont'],
                    helyszin=adat['helyszin'],
                    nev=adat['nev'],
                    megjegyzes=adat['megjegyzes']
                )
                self.esemenyek.append(esemeny)
                max_azonosito = max(max_azonosito, esemeny.azonosito)
            self.kovetkezo_azonosito = max_azonosito + 1
            return True
        except Exception as e:
            print(f"Hiba a betöltés során: {e}")
            return False