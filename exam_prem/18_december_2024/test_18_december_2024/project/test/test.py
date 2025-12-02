from project.gallery import Gallery
from unittest import TestCase, main

class TestGallery(TestCase):
    def test_init(self):
        g = Gallery('testname', 'testcity', 2.0)
        self.assertEqual('testname', g.gallery_name)
        self.assertEqual('testcity', g.city)
        self.assertEqual(2.0, g.area_sq_m)
        self.assertTrue(g.open_to_public)
        self.assertEqual({}, g.exhibitions)


    def test_gallery_name_raises(self):
        g = Gallery('testname', 'testcity', 2.0)
        with self.assertRaises(ValueError) as ex:
            g.gallery_name = 'test_name'
        self.assertEqual('Gallery name can contain letters and digits only!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            g.gallery_name = ''
        self.assertEqual('Gallery name can contain letters and digits only!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            g.gallery_name = ' '
        self.assertEqual('Gallery name can contain letters and digits only!', str(ex.exception))



    def test_city_name_starting_with_letter_raises(self):
        g = Gallery('testname', 'testcityname', 2.0)

        with self.assertRaises(ValueError) as ex:
            g.city = ''
        self.assertEqual('City name must start with a letter!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            g.city = '1testcity'
        self.assertEqual('City name must start with a letter!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            g.city = ' 1testcity'
        self.assertEqual('City name must start with a letter!', str(ex.exception))


    def test_sq_m_raises(self):
        g = Gallery('testname', "testcity", 2.0)
        with self.assertRaises(ValueError) as ex:
            g.area_sq_m = -1
        self.assertEqual('Gallery area must be a positive number!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            g.area_sq_m = 0
        self.assertEqual('Gallery area must be a positive number!', str(ex.exception))


    def test_add_exhibition(self):
        g = Gallery('testname', 'testcity', 2.0)
        self.assertEqual({}, g.exhibitions)

        result = g.add_exhibition('test1', 1999)

        self.assertEqual('Exhibition "test1" added for the year 1999.', result)
        self.assertEqual({'test1': 1999}, g.exhibitions)


    def test_add_exhibition_if_exists(self):
        g = Gallery('testname', 'testcity', 2.0)
        g.exhibitions = {'test1': 1999}

        result = g.add_exhibition('test1', 1999)

        self.assertEqual('Exhibition "test1" already exists.', result)
        self.assertEqual({'test1': 1999}, g.exhibitions)


    def test_remove_exhibition(self):
        g = Gallery('testname', 'testcity', 2.0)
        self.assertEqual({}, g.exhibitions)

        result = g.remove_exhibition('test1')

        self.assertEqual('Exhibition "test1" not found.', result)
        self.assertEqual({}, g.exhibitions)


    def test_remove_exhibition_if_exists(self):
        g = Gallery('testname', 'testcity', 2.0)
        g.exhibitions = {'test1': 1999, 'test2': 2000}

        result = g.remove_exhibition('test1')

        self.assertEqual('Exhibition "test1" removed.', result)
        self.assertEqual({'test2': 2000}, g.exhibitions)


    def test_open_for_public(self):
        g = Gallery('testname', 'testcity', 2.0)
        self.assertTrue(g.open_to_public)

        g.open_to_public = False
        self.assertFalse(g.open_to_public)


    def test_list_exhibitions_when_closed_to_public_returns_msg(self):
        g = Gallery('testname', 'testcity', 2.0)
        g.open_to_public = False

        result = g.list_exhibitions()

        self.assertEqual('Gallery testname is currently closed for public! Check for updates later on.', result)


    def test_list_exhibition_when_open_to_public_returns_list_of_exhibitions(self):
        g = Gallery('testname', 'testcity', 2.0)
        g.open_to_public = True
        g.add_exhibition('test1', 1999)
        g.add_exhibition('test2', 2000)

        result = g.list_exhibitions()

        self.assertEqual('test1: 1999\ntest2: 2000', result)


if __name__ == '__main__':
    main()
