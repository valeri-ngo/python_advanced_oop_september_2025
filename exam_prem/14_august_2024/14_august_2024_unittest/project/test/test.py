from unittest import TestCase, main
from project.furniture import Furniture


class TestFurniture(TestCase):

    def test_init(self):
        t = Furniture('woodenchair', 12.50, (3, 3, 3), True, None)
        self.assertEqual('woodenchair', t.model)
        self.assertEqual(12.50, t.price)
        self.assertEqual((3, 3, 3), t.dimensions)
        self.assertTrue(t.in_stock)
        self.assertIsNone(t.weight)


    def test_model_must_be_less_than_50_raises(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, None)

        with self.assertRaises(ValueError) as ex:
            t.model = 'testingthelengthforoverfiftycharslongexampleifitstooshortimputmoresymbols'
        self.assertEqual('Model must be a non-empty string with a maximum length of 50 characters.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.model = ' '
        self.assertEqual('Model must be a non-empty string with a maximum length of 50 characters.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.model = ''
        self.assertEqual('Model must be a non-empty string with a maximum length of 50 characters.', str(ex.exception))


    def test_model_when_valid(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        t.model = 'testmodelvalid'
        self.assertEqual('testmodelvalid', t.model)


    def test_price_below_zero_raises(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        with self.assertRaises(ValueError) as ex:
            t.price = -0.5
        self.assertEqual('Price must be a non-negative number.', str(ex.exception))


    def test_price_if_valid(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        t.price = 0.0
        self.assertEqual(0.0, t.price)

        t.price = 0.5
        self.assertEqual(0.5, t.price)


    def test_dimensions_less_than_three_integers_raises(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        with self.assertRaises(ValueError) as ex:
            t.dimensions = ()
        self.assertEqual('Dimensions tuple must contain 3 integers.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.dimensions = (0, 2)
        self.assertEqual('Dimensions tuple must contain 3 integers.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.dimensions = (2, 2, 2, 2)
        self.assertEqual('Dimensions tuple must contain 3 integers.', str(ex.exception))


    def test_dimensions_below_zero_raises(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)
        with self.assertRaises(ValueError) as ex:
            t.dimensions = (0, 0, 0)
        self.assertEqual('Dimensions tuple must contain integers greater than zero.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.dimensions = (-1, 0, -3)
        self.assertEqual('Dimensions tuple must contain integers greater than zero.', str(ex.exception))


    def test_dimensions_when_valid(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        t.dimensions = (1, 9, 1)
        self.assertEqual((1, 9, 1), t.dimensions)

        t.dimensions = (3, 1, 10)
        self.assertEqual((3, 1, 10), t.dimensions)


    def test_weight_if_none_or_below_zero_raises(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        with self.assertRaises(ValueError) as ex:
            t.weight = 0.0
        self.assertEqual('Weight must be greater than zero.', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            t.weight = -0.5
        self.assertEqual('Weight must be greater than zero.', str(ex.exception))


    def test_weight_above_zero(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3,), True, 30.50)

        t.weight = 1.5
        self.assertEqual(1.5, t.weight)

        t.weight = None
        self.assertEqual(None, t.weight)


    def test_get_available_status(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)

        self.assertEqual('Model: testmodel is currently in stock.', t.get_available_status())

        t = Furniture('testmodel', 12.50, (3, 3, 3), False, 30.50)
        self.assertEqual('Model: testmodel is currently unavailable.', t.get_available_status())


    def test_get_spec(self):
        t = Furniture('testmodel', 12.50, (3, 3, 3), True, 30.50)
        self.assertEqual('Model: testmodel has the following dimensions: 3mm x 3mm x 3mm and weighs: 30.5', t.get_specifications())

        t = Furniture('testmodel', 12.50, (1, 1, 1), True, None)
        self.assertEqual('Model: testmodel has the following dimensions: 1mm x 1mm x 1mm and weighs: N/A', t.get_specifications())


if __name__ == '__main__':
    main()