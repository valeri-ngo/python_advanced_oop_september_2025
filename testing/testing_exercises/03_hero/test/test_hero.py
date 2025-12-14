from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def test_init(self):
        h = Hero('Pesho', 99, 110, 300)
        self.assertEqual('Pesho', h.username)
        self.assertEqual(99, h.level)
        self.assertEqual(110, h.health)
        self.assertEqual(300, h.damage)

    def test_battle_with_self_name(self):
        with self.assertRaises(Exception) as ex:
            p1 = Hero('Pesho', 99, 110, 300)
            p2 = Hero('Pesho', 110, 150, 350)
            Hero.battle(p1, p2)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_below_or_equal_health_raises(self):
        with self.assertRaises(ValueError) as ex:
            p1 = Hero('Pesho', 99, -1, 300)
            p2 = Hero('Kaloyan', 110, 150, 350)
            p1.battle(p2)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            p1 = Hero('Pesho', 99, 0, 300)
            p2 = Hero('Kaloyan', 110, 150, 350)
            p1.battle(p2)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            p1 = Hero('Pesho', 99, 100, 300)
            p2 = Hero('Kaloyan', 110, -1, 350)
            p1.battle(p2)
        self.assertEqual('You cannot fight Kaloyan. He needs to rest', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            p1 = Hero('Pesho', 99, 100, 300)
            p2 = Hero('Kaloyan', 110, 0, 350)
            p1.battle(p2)
        self.assertEqual('You cannot fight Kaloyan. He needs to rest', str(ex.exception))

    def test_draw_battle(self):
        p1 = Hero('Pesho', 99, 110, 300)
        p2 = Hero('Kaloyan', 110, 150, 350)

        p1_dmg = p1.damage * p1.level
        p2_dmg = p2.damage * p2.level

        result = p1.battle(p2)

        self.assertEqual('Draw', result)
        self.assertEqual(110 - p2_dmg, p1.health)
        self.assertEqual(150 - p1_dmg, p2.health)

        self.assertEqual(99, p1.level)
        self.assertEqual(300, p1.damage)

        self.assertEqual(110, p2.level)
        self.assertEqual(350, p2.damage)

    def test_winner(self):
        p1 = Hero('Pesho', 120, 10_000, 45)
        p2 = Hero('Kaloyan', 110, 3800, 35)

        p1_dmg = p1.damage * p1.level
        p2_dmg = p2.damage * p2.level

        result = p1.battle(p2)

        self.assertEqual('You win', result)
        self.assertEqual(121, p1.level)
        self.assertEqual(10_000 - p2_dmg + 5, p1.health)
        self.assertEqual(45 + 5, p1.damage)

        self.assertEqual(3800 - p1_dmg, p2.health)
        self.assertEqual(110, p2.level)
        self.assertEqual(35, p2.damage)

    def test_loser(self):
        p1 = Hero('Pesho', 120, 3_800, 45)
        p2 = Hero('Kaloyan', 110, 10_000, 35)

        p1_dmg = p1.damage * p1.level
        p2_dmg = p2.damage * p2.level

        result = p1.battle(p2)

        self.assertEqual('You lose', result)
        self.assertEqual(111, p2.level)
        self.assertEqual(10_000 - p1_dmg + 5, p2.health)
        self.assertEqual(35 + 5, p2.damage)

        self.assertEqual(3_800 - p2_dmg, p1.health)
        self.assertEqual(120, p1.level)
        self.assertEqual(45, p1.damage)


    def test_str(self):
        hero = Hero('Pesho', 10, 100.5, 50.5)
        result = "Hero Pesho: 10 lvl\nHealth: 100.5\nDamage: 50.5\n"
        self.assertEqual(result, str(hero))


if __name__ == "__main__":
    main()