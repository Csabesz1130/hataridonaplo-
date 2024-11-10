from datetime import datetime, date

class Esemeny:
    """Egy esemény adatainak tárolására szolgáló osztály"""
    def __init__(self, azonosito: int, datum: date, idopont: str, 
                 helyszin: str, nev: str, megjegyzes: str = ""):
        self.azonosito = azonosito
        self.datum = datum
        self.idopont = idopont
        self.helyszin = helyszin
        self.nev = nev
        self.megjegyzes = megjegyzes

    def __str__(self) -> str:
        return (f"[{self.azonosito}] {self.datum} {self.idopont} - "
                f"{self.nev} ({self.helyszin})")