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
        input.append("a=1+1")
        input.append("a=1+1+1+1+1")
        input.append("a=1+1--1+1")
        input.append("class(a)")
        input.append("class(a, b)")
        input.append("class(a=True, c)")
        input.append("class(a=1+1+1+1+1)")
        input.append("class(a=1+1+1+1+1, b)")
        EP = expression_parser.ExpressionParser()
        result=[]
        for i in input:
            result.append(str(EP.parse_expression(i)))
        self.assertEquals("[['class']]",result[0])
        self.assertEquals("[['a', '=', '1', '+', '1']]", result[1])
        self.assertEquals("[['a', '=', '1', '+', '1', '+', '1', '+', "+\
            "'1', '+', '1']]", result[2])
        self.assertEquals("[['a', '=', '1', '+', '1', '-', '-1', '+', '1']]", 
            result[3])
        self.assertEquals("[['class', 'a']]", result[4])
        self.assertEquals("[['class', 'a', 'b']]", result[5])
        self.assertEquals("[['class', 'a', '=', 'True', 'c']]", result[6])
        self.assertEquals("[['class', 'a', '=', '1', '+', '1', '+', '1'," + \
            " '+', '1', '+', '1']]", result[7])
        self.assertEquals("[['class', 'a', '=', '1', '+', '1', '+', '1', " + \
            "'+', '1', '+', '1', 'b']]", result[8])

def main():
    unittest.main()

if __name__ == '__main__':
    main()