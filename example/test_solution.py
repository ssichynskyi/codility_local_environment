from base.testcase import CodilityTestCase
from solution import solution


class Test(CodilityTestCase):
    def setUp(self) -> None:
        test_input_file = 'test-input.txt'
        expected_result_file = 'test-expected.txt'
        self.extract_test_data(test_input_file, expected_result_file)

    def test_solution(self):
        for i in range(len(self.test_data)):
            self.assertEqual(
                self.expected_results[i],
                solution(*self.test_data[i])
            )
