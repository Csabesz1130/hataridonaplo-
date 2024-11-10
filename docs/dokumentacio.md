# Határidőnapló - Félkész Változat Dokumentációja

## Jelenlegi Funkcionalitás

### Működő funkciók:
1. Események kezelése
   - Új esemény generálása, létrehozása
   - Mai események listázása
   - Egyszerű adattárolás (események paraméterei)

2. Fájlkezelés
   - Események mentése JSON formátumban
   - Események betöltése JSON fájlból
   - Alapszintű hibakezelés

3. Felhasználói felület
   - Parancssoros menürendszer
   - Alapvető interakció az eseményekkel
   - Művelet visszajelzések: success, error

## Fájlok és függvények

### src/esemeny.py
- Esemeny osztály: Események tárolása
  - Attribútumok: azonosító, dátum, időpont, helyszín, név, megjegyzés
  - Ezeket tároljuk az egyes eseményekről

### src/esemenykezelo.py
- EsemenyKezelo osztály: Események kezelése, manipulációja
  - uj_esemeny(): Létrehozás
  - lista_nap(): Napi lista
  - mentes_fajlba(): JSON fájlba mentés
  - etoltes_fajlbol(): JSON betöltés, megjelenítés

### src/main.py
- Főprogram és menürendszer
- Felhasználói interakció
- Alapvető hibakezelés

## Továbbfejlesztési lehetőségek
1. Eseménykezelés bővítése
2. Hibakezelés fejlesztése (hibás adatok bevitelére)
3. Grafikus felület (végső verzióban egy egyszerű asztali felület)
4. Keresési funkciók

