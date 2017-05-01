from pyparsing import *
import pprint
ParserElement.setDefaultWhitespaceChars(" \t")
pp = pprint.PrettyPrinter(indent=4)

def parse_parameter(input):
    word = Word(alphanums + '_')
    newline = Suppress('\n')
    colon = Suppress(':')
    arrow = Suppress('->')
    left_square_bracket = Suppress('[')
    right_square_bracket = Suppress(']')
    parameter_field_name = Literal('[Parameters]')
    attribute = (word+colon+word + newline).setResultsName("attribute")
    parameter_field = parameter_field_name + newline + Group(OneOrMore(Group(attribute)))
    parsed_parameter = parameter_field.scanString(input)
    parameters=[]
    for p in parsed_parameter:
        for a in p[0][1]:
            parameters.append((a[0], a[1]))
    return parameters
    

input_text = open("testcase4.txt", "r").read()

parameters = parse_parameter(input_text)
for p in parameters:
    print p[0], p[1]