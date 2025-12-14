from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.v = Vehicle(50, 100)

    def test_init(self):
        self.assertEqual(50, self.v.fuel)
        self.assertEqual(50, self.v.capacity)
        self.assertEqual(100, self.v.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.v.fuel_consumption)

    def test_fuel_drive_when_enough_fuel(self):
        self.v = Vehicle(50, 100)

        self.v.drive(40)
        self.assertEqual(0, self.v.fuel)

        self.v = Vehicle(50, 100)

        self.v.drive(37.5)
        self.assertEqual(3.125, self.v.fuel)


    def test_fuel_drive_when_not_enough_fuel(self):
        self.v = Vehicle(50, 100)
        with self.assertRaises(Exception) as ex:
            self.v.drive(41)
        self.assertEqual('Not enough fuel', str(ex.exception))

        self.v = Vehicle(50, 100)
        with self.assertRaises(Exception) as ex:
            self.v.drive(40.5)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_above_capacity(self):
        v = Vehicle(50, 100)
        with self.assertRaises(Exception) as ex:
            v.refuel(1)
        self.assertEqual('Too much fuel', str(ex.exception))

        v = Vehicle(50, 100)
        v.drive(10)
        with self.assertRaises(Exception) as ex:
            v.refuel(13)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_in_range_capacity(self):
        v = Vehicle(50, 100)
        v.drive(10)
        v.refuel(12.5)
        self.assertEqual(50, v.fuel)

        v = Vehicle(100, 190)
        v.drive(20)
        v.refuel(25)
        self.assertEqual(100, v.fuel)

    def test_str(self):
        result = 'The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption'
        self.assertEqual(result, str(self.v))

if __name__ == '__main__':
    main()