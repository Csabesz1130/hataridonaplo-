
import pytest
from datetime import date, datetime

# Test helper functions
def create_test_esemeny(azonosito=1):
    """Teszt esemény létrehozása"""
    return {
        'azonosito': azonosito,
        'datum': date(2024, 3, 15),
        'idopont': '10:00',
        'helyszin': 'Iroda',
        'nev': 'Teszt esemény',
        'megjegyzes': 'Teszt megjegyzés'
    }

def create_test_data():
    """Több teszt esemény létrehozása"""
    return [
        {
            'azonosito': 1,
            'datum': date(2024, 3, 15),
            'idopont': '10:00',
            'helyszin': 'Iroda',
            'nev': 'Első esemény',
            'megjegyzes': 'Első teszt'
        },
        {
            'azonosito': 2,
            'datum': date(2024, 3, 15),
            'idopont': '14:00',
            'helyszin': 'Tárgyaló',
            'nev': 'Második esemény',
            'megjegyzes': 'Második teszt'
        }
    ]

# Constants for testing
TEST_FILE = 'test_events.json'

__all__ = ['create_test_esemeny', 'create_test_data', 'TEST_FILE']