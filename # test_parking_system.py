# test_parking_system.py

import unittest
from parking_system import ParkingSystem, WeeklyPass, MonthlyPass, SingleEntryPass


class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        self.system = ParkingSystem()

    def test_add_weekly_pass(self):
        wp = WeeklyPass("W1")
        self.system.add_pass(wp)
        self.assertEqual(self.system.sales_report["Weekly Pass"], 1)

    def test_add_monthly_pass(self):
        mp = MonthlyPass("M1")
        self.system.add_pass(mp)
        self.assertEqual(self.system.sales_report["Monthly Pass"], 1)

    def test_add_single_entry_pass(self):
        sp = SingleEntryPass("S1")
        self.system.add_pass(sp)
        self.assertEqual(self.system.sales_report["Single Entry Pass"], 1)

    def test_total_passes(self):
        self.system.add_pass(WeeklyPass("W1"))
        self.system.add_pass(MonthlyPass("M1"))
        self.system.add_pass(SingleEntryPass("S1"))

        self.assertEqual(len(self.system.passes), 3)


if __name__ == "__main__":
    unittest.main()
