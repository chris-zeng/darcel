import expression_parser
import os
import unittest

class ExpressionParserUnitTest(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_1(self):
        input=[]
        input.append("class()")
        input.append("1+1")
        input.append("1+1+1+1+1")
        input.append("1+1--1+1")
        input.append("class(a)")
        input.append("class(a, b)")
        input.append("class(True, c)")
        input.append("class(1+1+1+1+1)")
        input.append("class(1+1+1+1+1, b)")
        input.append("c<=B&&False&&True")
        input.append("C>=B&&C==False||B<=D")
        EP = expression_parser.ExpressionParser()
        result=[]
        for i in input:
            result.append(str(EP.parse_expression(i)))
        self.assertEquals("[['class']]",result[0])
        self.assertEquals("[['1', '+', '1']]", result[1])
        self.assertEquals("[['1', '+', '1', '+', '1', '+', "+\
            "'1', '+', '1']]", result[2])
        self.assertEquals("[['1', '+', '1', '-', '-1', '+', '1']]", 
            result[3])
        self.assertEquals("[['class', 'a']]", result[4])
        self.assertEquals("[['class', 'a', 'b']]", result[5])
        self.assertEquals("[['class', 'True', 'c']]", result[6])
        self.assertEquals("[['class', '1', '+', '1', '+', '1',"
            " '+', '1', '+', '1']]", result[7])
        self.assertEquals("[['class', '1', '+', '1', '+', '1', "
            "'+', '1', '+', '1', 'b']]", result[8])
        self.assertEquals("[['c', '<=', 'B', '&&', 'False', '&&', 'True']]",
            result[9])
        self.assertEquals("[['C', '>=', 'B', '&&', 'C', '==', 'False', '||', "
            "'B', '<=', 'D']]", result[10])

def main():
    unittest.main()

if __name__ == '__main__':
    main()