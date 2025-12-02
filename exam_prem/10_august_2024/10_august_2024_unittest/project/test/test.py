from unittest import TestCase, main

from project.soccer_player import SoccerPlayer

class TestSoccerPlayer(TestCase):


    def test_init(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        self.assertEqual('testname', sp.name)
        self.assertEqual(20, sp.age)
        self.assertEqual(3, sp.goals)
        self.assertEqual('Barcelona', sp.team)
        self.assertEqual({}, sp.achievements)


    def test_VALID_TEAMS(self):
        valid_teams = ['Barcelona', 'Real Madrid', 'Manchester United', 'Juventus', 'PSG']
        self.assertEqual(valid_teams, SoccerPlayer._VALID_TEAMS)


    def test_name(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        with self.assertRaises(ValueError) as ex:
            sp.name = 'test'
        self.assertEqual('Name should be more than 5 symbols!', str(ex.exception))


    def test_age(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        with self.assertRaises(ValueError) as ex:
            sp.age = 15
        self.assertEqual('Players must be at least 16 years of age!', str(ex.exception))


    def test_goals(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        sp.goals = -1
        self.assertEqual(0, sp.goals)


    def test_team_if_not_valid_raises(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        with self.assertRaises(ValueError) as ex:
            sp.team = 'Bulgaria'
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!",
                         str(ex.exception))


    def test_change_team_not_valid_raises(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        result = sp.change_team('Bulgaria')
        self.assertEqual('Invalid team name!', result)


    def test_change_team_is_valid(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        result = sp.change_team('PSG')
        self.assertEqual('Team successfully changed!', result)
        self.assertEqual('PSG', sp.team)


    def test_new_achievement(self):
        sp = SoccerPlayer('testname', 20, 3, 'Barcelona')
        result = sp.add_new_achievement('test')

        self.assertEqual('test has been successfully added to the achievements collection!', result)

        self.assertIn('test', sp.achievements)
        self.assertEqual(1, sp.achievements['test'])

        sp.add_new_achievement('test')
        self.assertEqual(2, sp.achievements['test'])


    def test_lt(self):
        team1 = SoccerPlayer('testname1', 20, 3, 'Barcelona')
        team2 = SoccerPlayer('testname2', 23, 4, 'PSG')

        result = team1 < team2
        self.assertEqual('testname2 is a top goal scorer! S/he scored more than testname1.', result)

        team1 = SoccerPlayer('testname1', 20, 4, 'Barcelona')
        team2 = SoccerPlayer('testname2', 20, 3, 'PSG')

        result = team1 < team2
        self.assertEqual('testname1 is a better goal scorer than testname2.', result)


if __name__ == '__main__':
    main()