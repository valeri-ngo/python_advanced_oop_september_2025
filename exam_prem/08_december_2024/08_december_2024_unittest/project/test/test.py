from project.senior_student import SeniorStudent
from unittest import TestCase, main

class TestSeniorStudent(TestCase):
    def test_init(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        self.assertEqual('id123', test.student_id)
        self.assertEqual('testname', test.name)
        self.assertEqual(2.0, test.student_gpa)
        self.assertEqual(set(), test.colleges)


    def test_student_id_less_than_4_raises(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        with self.assertRaises(ValueError) as ex:
            test.student_id = '123'
        self.assertEqual('Student ID must be at least 4 digits long!', str(ex.exception))


    def test_student_id_if_valid(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        test.student_id = 'id12345'
        self.assertEqual('id12345', test.student_id)


    def test_student_name_null_or_empty_raises(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        with self.assertRaises(ValueError) as ex:
            test.name = ''
        self.assertEqual('Student name cannot be null or empty!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            test.name = ' '
        self.assertEqual('Student name cannot be null or empty!', str(ex.exception))


    def test_student_name_if_valid(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        test.name = 'validname'
        self.assertEqual('validname', test.name)


    def test_student_gpa_below_1_raises(self):
        test = SeniorStudent('id123', 'testname', 2.0)

        with self.assertRaises(ValueError) as ex:
            test.student_gpa = -0.5
        self.assertEqual('Student GPA must be more than 1.0!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            test.student_gpa = 0
        self.assertEqual('Student GPA must be more than 1.0!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            test.student_gpa = 0.9
        self.assertEqual('Student GPA must be more than 1.0!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            test.student_gpa = 1.0
        self.assertEqual('Student GPA must be more than 1.0!', str(ex.exception))


    def test_student_gpa_above_1(self):
        test = SeniorStudent('id123', 'testname', 2.0)
        test.student_gpa = 3.0
        self.assertEqual(3.0, test.student_gpa)

        test.student_gpa = 2.0
        self.assertEqual(2.0, test.student_gpa)


    def test_apply_to_college_lower_gpa_vs_actual_gpa_returns(self):
        test = SeniorStudent('id123', 'testname', 2.5)

        result = test.apply_to_college(3.0, 'Harvard')
        self.assertEqual('Application failed!', result)


    def test_apply_to_college_if_valid(self):
        test = SeniorStudent('id123', 'testname', 2.8)

        result = test.apply_to_college(2.0, 'MIT')
        self.assertEqual('testname successfully applied to MIT.', result)
        self.assertIn('MIT', test.colleges)


    def test_update_gpa_below_one(self):
        test = SeniorStudent('id123', 'testname', 2.0)

        result = test.update_gpa(1.0)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(2.0, test.student_gpa)

        result = test.update_gpa(0.5)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(2.0, test.student_gpa)

        result = test.update_gpa(0.0)
        self.assertEqual('The GPA has not been changed!', result)
        self.assertEqual(2.0, test.student_gpa)


    def test_update_gpa_when_valid(self):
        test = SeniorStudent('id123', 'testname', 2.0)

        result = test.update_gpa(1.5)
        self.assertEqual('Student GPA was successfully updated.', result)
        self.assertEqual(1.5, test.student_gpa)

        result = test.update_gpa(2.5)
        self.assertEqual('Student GPA was successfully updated.', result)
        self.assertEqual(2.5, test.student_gpa)


    def test_eq(self):
        student_gpa = SeniorStudent('id123', 'testname', 2.0)
        other_student_gpa = SeniorStudent('id456', 'othername', 3.0)
        self.assertFalse(student_gpa == other_student_gpa)

        other_student_gpa.student_gpa = 2.0
        self.assertTrue(student_gpa == other_student_gpa)


if __name__ == '__main__':
    main()
