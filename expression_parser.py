from pyparsing import *

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
assign_op = Literal('=')
greater_op = Literal('>')
less_op = Literal('<')
greater_equal_op = Literal('>=')
less_equal_op = Literal('<=')
equal_equal_op = Literal('==')
not_equal_op = Literal('!=')
comp_op = (greater_op | less_op | greater_equal_op | less_equal_op |
    equal_equal_op | not_equal_op)
left_paren = Literal('(')
right_paren = Literal(')')
identifier = Combine(alpha + ZeroOrMore(alpha|number))
qualified_name = Combine(identifier + ZeroOrMore(point+identifier))

atom = integer | money | decimal | boolean
exp = Forward()

exp << atom + arithmetic_op + atom | atom + comp_op + atom

#bnf = Optional(identifier + assign_op)+expr

input = "$1.0--1"

print exp.parseString(input)