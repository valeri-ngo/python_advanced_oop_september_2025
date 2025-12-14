from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.m = Mammal('mammalname', 'mammaltype', 'mammalsound')

    def test_init(self):
        self.assertEqual('mammalname', self.m.name)
        self.assertEqual('mammaltype', self.m.type)
        self.assertEqual('mammalsound', self.m.sound)

    def test_make_sound(self):
        self.assertEqual('mammalname makes mammalsound', self.m.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.m.get_kingdom())

    def test_info(self):
        self.assertEqual('mammalname is of type mammaltype', self.m.info())


if __name__ == "__main__":
    main()