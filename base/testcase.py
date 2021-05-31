from unittest import TestCase
from ast import literal_eval as parse


class CodilityTestCase(TestCase):
    """This is a base class for your tests. Derive your test cases from it."""

    def extract_test_data(self, test_input_file, exp_res_file):
        """Reads test input and expected results data from standard text files."""
        with open(test_input_file) as test_data_file:
            self.test_data = [parse(data_str) for data_str in test_data_file.readlines()]

        with open(exp_res_file) as expected_results_file:
            self.expected_results = [parse(exp_res) for exp_res in expected_results_file.readlines()]

        if len(self.test_data) != len(self.expected_results):
            raise ValueError(
                f'Number of data lines in files {test_input_file} and {exp_res_file} shall match'
            )
