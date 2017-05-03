from pyparsing import *

class ExpressionParser:
    def parse_expression(self, input):
        point = Literal('.')
        plus_op = Literal('+')
        minus_op = Literal('-')
        alpha = Word(alphas + '_')
        number = Word(nums)
        integer = Combine(Optional(plus_op|minus_op) + number)
        decimal = Combine(integer+Optional(point + Optional(number)))
        money = Combine('$' + decimal)
        true = Literal("True")
        false = Literal("False")
        boolean = true | false
        multi_op = Literal('*')
        divide_op = Literal('/')
        arithmetic_op = plus_op | minus_op | multi_op | divide_op
        greater_op = Literal('>')
        less_op = Literal('<')
        greater_equal_op = Literal('>=')
        less_equal_op = Literal('<=')
        equal_equal_op = Literal('==')
        not_equal_op = Literal('!=')
        comp_op = (greater_op ^ less_op ^ greater_equal_op ^ less_equal_op ^
            equal_equal_op ^ not_equal_op)
        and_op = Literal("&&")
        or_op = Literal("||")
        binary_op = and_op | or_op
        left_paren = Suppress(Literal('('))
        right_paren = Suppress(Literal(')'))
        identifier = Combine(alpha + ZeroOrMore(alpha|number))
        qualified_name = Combine(identifier + ZeroOrMore(point+identifier))
        ops = arithmetic_op|multi_op|comp_op|binary_op
        expr = Forward()
        atom = integer | money | decimal | boolean | qualified_name
        expr << (atom ^ (atom + ZeroOrMore(ops + atom)) ^ \
                (qualified_name + left_paren + Optional(
                 expr + ZeroOrMore(Suppress(',')+expr)) + right_paren))
        return expr.searchString(input)

#print ExpressionParser().parse_expression("A<=b")