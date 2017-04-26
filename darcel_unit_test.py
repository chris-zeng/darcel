import darcel
import filecmp
import os
import unittest

class DarcelUnitTest(unittest.TestCase):
    def setUp(self):
        self.input_files_folder_path = os.path.relpath("test/input_files/")
        self.output_files_folder_path = os.path.relpath("test/output_files/")
        self.expected_files_folder_path = os.path.relpath("test/expected_files/")
        return

    def tearDown(self):
        return

    def test_case_1(self):
        input_file_path = self.input_files_folder_path + "/test1.txt"
        output_file_path = self.output_files_folder_path + "/test1_out.txt"
        expected_file_path = self.expected_files_folder_path + \
            "/test1_expected.txt"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_case_2(self):
        input_file_path = self.input_files_folder_path + "/credit_trader.gv"
        output_file_path = self.output_files_folder_path + "/credit_trader.py"
        expected_file_path = self.expected_files_folder_path + \
            "/credit_trader.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_case_3(self):
        input_file_path = self.input_files_folder_path + "/testcase3.txt"
        output_file_path = self.output_files_folder_path + "/testcase3.py"
        expected_file_path = self.expected_files_folder_path + \
            "/testcase3_expected.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

    def test_case_4(self):
        input_file_path = self.input_files_folder_path + "/testcase4.txt"
        output_file_path = self.output_files_folder_path + "/testcase4.py"
        expected_file_path = self.expected_files_folder_path + \
            "/testcase4_expected.py"
        d = darcel.StateMachineGenerator(input_file_path, output_file_path)
        d.generate_graph()
        self.assertTrue(filecmp.cmp(output_file_path,expected_file_path))

def main():
    unittest.main()

if __name__ == '__main__':
    main()