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
and_op = Literal("&&")
or_op = Literal("||")
binary_op = and_op | or_op
left_paren = Suppress(Literal('('))
right_paren = Suppress(Literal(')'))
identifier = Combine(alpha + ZeroOrMore(alpha|number))
qualified_name = Combine(identifier + ZeroOrMore(point+identifier))
ops = arithmetic_op|multi_op|comp_op|assign_op|binary_op

expr = Forward()
atom = integer | money | decimal | boolean| expr | qualified_name

expr << ((identifier + assign_op + atom + ZeroOrMore(ops + atom)) | \
        (qualified_name + left_paren + Optional(atom + ZeroOrMore(Suppress(',')+atom)) + right_paren))

#bnf = Optional(identifier + assign_op)+expr

input=[]
input.append("class()")
input.append("a=1+1")
input.append("a=1+1+1+1+1")
input.append("a=1+1--1+1")
input.append("class(a)")
input.append("class(a, b)")
input.append("class(a, c)")

for i in input:
    print expr.parseString(i)