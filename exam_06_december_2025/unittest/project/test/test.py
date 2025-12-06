from unittest import TestCase, main
from project.star_system import StarSystem


class TestStarSystem(TestCase):

    def test_constants_are_defined(self):
        self.assertTrue(StarSystem._STAR_TYPES)
        self.assertTrue(StarSystem._STAR_SYSTEM_TYPES)

    def test_init(self):
        s = StarSystem('testname', 'Yellow dwarf', 'Triple', 3, None)
        self.assertEqual('testname', s.name)
        self.assertEqual('Yellow dwarf', s.star_type)
        self.assertEqual('Triple', s.system_type)
        self.assertEqual(3, s.num_planets)
        self.assertIsNone(s.habitable_zone_range)

    def test_star_types_contains_examples(self):
        self.assertIn("Red giant", StarSystem._STAR_TYPES)
        self.assertIn("Red dwarf", StarSystem._STAR_TYPES)

    def test_system_types_contains_examples(self):
        self.assertIn("Single", StarSystem._STAR_SYSTEM_TYPES)
        self.assertIn("Binary", StarSystem._STAR_SYSTEM_TYPES)

    def test_name_not_string_raises(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        with self.assertRaises(ValueError) as ex:
            s.name = ''
        self.assertEqual('Name must be a non-empty string.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            s.name = ' '
        self.assertEqual('Name must be a non-empty string.', str(ex.exception))

    def test_name_if_valid(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)
        self.assertEqual('testname', s.name)

    def test_star_type_no_type_raises(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        with self.assertRaises(ValueError) as ex:
            s.star_type = 'Big Red sun'
        self.assertEqual(f"Star type must be one of {sorted(StarSystem._STAR_TYPES)}.",str(ex.exception))

    def test_star_type_when_type_is_valid(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        s.star_type = 'Blue giant'
        self.assertEqual('Blue giant', s.star_type)

    def test_system_type_no_type_raises(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        with self.assertRaises(ValueError) as ex:
            s.system_type = 'testsystemtype'
        self.assertEqual(f'System type must be one of {sorted(StarSystem._STAR_SYSTEM_TYPES)}.', str(ex.exception))

    def test_system_type_when_type_is_valid(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)
        s.system_type = 'Multiple'
        self.assertEqual('Multiple', s.system_type)

    def test_num_planets_below_zero_raises(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        with self.assertRaises(ValueError) as ex:
            s.num_planets = -1
        self.assertEqual('Number of planets must be a non-negative integer.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            s.num_planets = -10
        self.assertEqual('Number of planets must be a non-negative integer.', str(ex.exception))

    def test_num_planets_above_zero(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)
        s.num_planets = 50
        self.assertEqual(50, s.num_planets)

    def test_habitable_zone_range_if_not_none_raises(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        with self.assertRaises(ValueError) as ex:
            s.habitable_zone_range = (10, 5)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            s.habitable_zone_range = (10, 3, 1)
        self.assertEqual("Habitable zone range must be a tuple of two numbers (start, end) where start < end.", str(ex.exception))

    def test_habitable_zone_range(self):
        s = StarSystem('testname', 'Red giant', 'Single', 3, None)

        s.habitable_zone_range = (1, 2)
        self.assertEqual((1, 2), s.habitable_zone_range)

    def test_gt_returns_true_when_self_has_wider_zone(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 6))
        s2 = StarSystem("B", "Red giant", "Single", 2, (1, 4))

        self.assertTrue(s1 > s2)

    def test_gt_returns_false_when_self_has_narrower_or_equal_zone(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 4))
        s2 = StarSystem("B", "Red giant", "Single", 2, (1, 6))

        self.assertFalse(s1 > s2)

    def test_gt_raises_when_one_system_not_habitable(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, None)
        s2 = StarSystem("B", "Red giant", "Single", 2, (1, 4))

        with self.assertRaises(ValueError) as ex:
            _ = s1 > s2

        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            str(ex.exception)
        )
    def test_compare_star_systems_returns_correct_message_when_first_is_wider(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, (1, 6))
        s2 = StarSystem("B", "Red giant", "Single", 2, (1, 4))

        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("A has a wider habitable zone than B.", result)

    def test_compare_star_systems_equal_ranges(self):
        s1 = StarSystem("A", "Red giant", "Single", 1, (1, 4))
        s2 = StarSystem("B", "Red giant", "Single", 1, (2, 5))

        result = StarSystem.compare_star_systems(s1, s2)
        self.assertEqual("B has a wider or equal habitable zone compared to A.", result)

    def test_compare_star_systems_returns_error_message_when_comparison_not_possible(self):
        s1 = StarSystem("A", "Red giant", "Single", 3, None)
        s2 = StarSystem("B", "Red giant", "Single", 2, (1, 4))

        result = StarSystem.compare_star_systems(s1, s2)

        self.assertEqual(
            "Comparison not possible: One or both systems lack a defined habitable zone or planets.",
            result
        )

if __name__ == "__main__":
    main()