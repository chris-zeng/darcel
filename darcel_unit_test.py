import darcel
import filecmp
import os
import unittest

class DarcelUnitTest(unittest.TestCase):
    def setUp(self):
        self.input_files_folder_path = os.path.relpath("Test/input_files/")
        self.output_files_folder_path = os.path.relpath("Test/output_files/")
        self.expected_files_folder_path = os.path.relpath("Test/expected_files/")
        return

    def tearDown(self):
        return

    def test_epsilon(self):
        input_file_path = self.input_files_folder_path + "/test_epsilon.txt"
        output_file_path = self.output_files_folder_path + "/test_epsilon.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_epsilon_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path, shallow=True))

    def test_dot_only(self):
        input_file_path = self.input_files_folder_path + "/test_dot_only.txt"
        output_file_path = self.output_files_folder_path + "/test_dot_only.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_dot_only_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_dot_body(self):
        input_file_path = self.input_files_folder_path + "/test_dot_body.txt"
        output_file_path = self.output_files_folder_path + "/test_dot_body.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_dot_body_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_parameters(self):
        input_file_path = self.input_files_folder_path + "/test_parameters.txt"
        output_file_path = self.output_files_folder_path + "/test_parameters.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_parameters_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_variables(self):
        input_file_path = self.input_files_folder_path + "/test_variables.txt"
        output_file_path = self.output_files_folder_path + "/test_variables.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_variables_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))
        
    def test_conditions(self):
        input_file_path = self.input_files_folder_path + "/test_conditions.txt"
        output_file_path = self.output_files_folder_path + "/test_conditions.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        expected_file_path = self.expected_files_folder_path + \
            "/test_conditions_expected.py"
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

def main():
    unittest.main()

if __name__ == '__main__':
    main()