"""
Silver service taxi test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    # SilverServiceTaxi("name, fuel, fanciness")
    prestige_taxi = SilverServiceTaxi("Prestige", 100, 5)
    prestige_taxi.drive(15)
    print(prestige_taxi)
    print(prestige_taxi.get_fare())


main()
