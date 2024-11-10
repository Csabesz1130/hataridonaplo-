import unittest
from datetime import date
from src.esemeny import Esemeny

class TestEsemeny(unittest.TestCase):
    def test_esemeny_letrehozas(self):
        """Esemény létrehozásának tesztelése"""
        esemeny = Esemeny(1, date(2024, 3, 15), "10:00", "Iroda", "Megbeszélés")
        self.assertEqual(esemeny.azonosito, 1)
        self.assertEqual(esemeny.nev, "Megbeszélés")
        self.assertEqual(esemeny.helyszin, "Iroda")

    def test_esemeny_str(self):
        """Esemény string reprezentációjának tesztelése"""
        esemeny = Esemeny(1, date(2024, 3, 15), "10:00", "Iroda", "Megbeszélés")
        str_repr = str(esemeny)
        self.assertIn("Megbeszélés", str_repr)
        self.assertIn("Iroda", str_repr)

if __name__ == '__main__':
    unittest.main()
