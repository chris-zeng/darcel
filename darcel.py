import argparse
from collections import defaultdict
import pprint
from pyparsing import *
import re
import string
import StringIO
import sys

class CodeGenerator:
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return string.join(self.code, "")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

class StateGraph:
    def __init__ (self, name):
        self.name = name
        self.adjacency_list = defaultdict(list)
        self.states = set()
        self.events = defaultdict(list)
        self.conditions = set()

    def print_graph(self):
        pp = pprint.PrettyPrinter(indent=4)
        print "all states"
        pp.pprint(self.states)
        print "all events"
        pp.pprint(dict(self.events))
        print "all conditions"
        pp.pprint(self.conditions)
        print "graph"
        pp.pprint(dict(self.adjacency_list))

class StateMachineGenerator:
    def __init__(self, input_filename, output_filename):
        self.file_text = open(input_filename, "r").read()
        self.output_filename = output_filename
        self.header = None
        self.dot_block = None
        self.body = None
        ParserElement.setDefaultWhitespaceChars(" \t")

    def extract_dot_block(self):
        dot_block_text = re.search(r"\{(.*)\}", self.file_text, 
                                    re.DOTALL).group(0)
        matches = re.finditer(r"^(.*)\;", dot_block_text, re.MULTILINE)
        self.dot_block = []
        for match in matches:
            self.dot_block.append(str(match.group(0)))

    def extract_body(self):
        regex = r"}(.*)"
        matches = re.search(regex, self.file_text, re.DOTALL)
        self.body = matches.group(1)
        self.body = self.body.lstrip()

    def extract_weights(self, labels):
        weights = []
        regex = r"E+\d*|C+\d*|&#949"
        matches = re.finditer(regex, labels)
        for match in matches:
            weights.append(match.group())
        return weights

    def add_edge(self, source, destination, weights, labels):
        self.state_graph.states.add(source)
        self.state_graph.states.add(destination)
        for weight in weights:
            if weight[0] =='E':
                self.state_graph.events[weight].append([source, destination])
            elif weight[0] == 'C':
                self.state_graph.conditions.add(weight)
        labels = ''.join(labels.split(','))
        labels = labels.replace("&&", " and ")
        labels = labels.replace("||", " or ")
        labels = labels.replace("!", "not ")
        labels = labels.replace("~","not ")
        self.state_graph.adjacency_list[source].append(
                                                [destination, weights, labels])

    def generate_graph(self):
        header_regex = re.compile("(.*?)\s*\{")
        self.header = header_regex.match(self.file_text).group(1)
        self.header = self.header.replace('digraph','')
        self.header = ''.join(self.header.split(' '))
        self.state_graph = StateGraph(self.header)
        self.extract_dot_block()
        self.extract_body()
        for line in self.dot_block:
            if "->" in line:
                source_name = re.search(r"(.*)->", line).group(1).strip()
                destination_name = re.search(r"-> (.*) \[", line).\
                    group(1).strip()
                labels = re.search(r"\"(.*?)\"", line).group(1)
                labels = ''.join(labels.split(' '))
                weights = self.extract_weights(labels)            
                self.add_edge(source_name, destination_name, weights, labels)
        self.generate_code()

    def parse_parameter(self):
        word = Word(alphanums + '_')
        newline = Suppress('\n')
        colon = Suppress(':')
        arrow = Suppress('->')
        left_square_bracket = Suppress('[')
        right_square_bracket = Suppress(']')
        parameter_field_name = Literal('[Parameters]')
        attribute = word+colon+word + newline
        parameter_field = parameter_field_name + newline + Group(OneOrMore(Group(attribute)))
        parsed_parameter = parameter_field.scanString(self.body)
        parameters=[]
        for p in parsed_parameter:
            for a in p[0][1]:
                parameters.append((a[0], a[1]))
        return parameters

    def parse_variables(self):
        word = Word(alphanums + '_')
        newline = Suppress('\n')
        colon = Suppress(':')
        arrow = Suppress('->')
        left_square_bracket = Suppress('[')
        right_square_bracket = Suppress(']')
        variable_field_name = Literal('[Variables]')
        attribute = word+colon+word + newline
        variable_field = variable_field_name + newline + Group(OneOrMore(Group(attribute)))
        parsed_variables = variable_field.scanString(self.body)
        variables=[]
        for p in parsed_variables:
            for a in p[0][1]:
                variables.append((a[0], a[1]))
        return variables

    def generate_constructor(self, c):
        c.indent()
        parameters = self.parse_parameter()
        init_func_decl = "def __init__(self, service_clients"
        for param in parameters:
            init_func_decl += ", {0}".format(param[0].rstrip())
        init_func_decl += "):\n"
        c.write(init_func_decl)
        c.indent()   
        c.write("self.service_clients = service_clients\n")
        for param in parameters:
            c.write("self.{0} = {0}\n".format(param[0].rstrip()))
        variables = self.parse_variables()
        for var in variables:
            c.write("self.{0} = None\n".format(var[0].rstrip()))        
        c.write("self.state = None\n")
        c.write("self.tasks = beam.RoutineTaskQueue()\n")
        c.write("self.completion_queue = beam.Queue()\n")
        c.dedent()
        c.dedent()
        c.write("\n")
        return

    def generate_states_code(self, c):
        states = sorted(self.state_graph.states, key = lambda state: int(
                            filter(str.isdigit, state)))
        for state in states:
            c.indent()
            c.write("def "+state+"(self):\n")
            c.indent()
            c.write("self.state = {0}\n".format(
                int(filter(str.isdigit, state))))
            destinations = self.state_graph.adjacency_list[state]
            for destination in destinations:
                destination_state = destination[0]
                destination_edges = destination[2]
                for edge in destination_edges.split(','):
                    if 'C' in edge:
                        regex = r'C\d+'
                        matches = re.finditer(regex, edge)
                        temp_hash = set()
                        for match in matches:
                            if match.group(0) not in temp_hash:
                                edge = edge.replace(match.group(0), "self."+\
                                    match.group(0)+"()")
                                temp_hash.add(match.group(0))
                        c.write("if {0}:\n".format(edge))
                        c.indent()
                        c.write("return self.{0}()\n".format(destination_state))
                        c.dedent()
                    elif edge == "&#949;":
                        #c.indent()
                        c.write("return self.{0}()\n".format(destination_state))
                        #c.dedent()
            c.dedent()
            c.dedent()
            c.write("\n")

    def generate_conditions_code(self, c):
        conditions = sorted(self.state_graph.conditions, 
                                key = lambda condition:\
                                int(filter(str.isdigit, condition)))
        for condition in conditions:
            c.indent()
            c.write("def {0}(self):\n".format(condition))
            c.indent()
            c.write("pass")
            c.dedent()
            c.dedent()
            c.write("\n")

    def generate_events_code(self, c):
        events = sorted(self.state_graph.events, key = lambda event:\
                                            int(filter(str.isdigit, event)))
        for event in events:
            c.indent()
            c.write("def {0}(self):\n".format(event))
            for source_destination in self.state_graph.events[event]:
                source = source_destination[0]
                destination = source_destination[1]
                c.indent()
                c.write("if self.state == {0}:\n".format(int(filter(
                    str.isdigit, source))))
                c.indent()
                c.write("return self.{0}()\n".format(destination))
                c.dedent()
                c.dedent()
            c.dedent()
            c.write("\n")

    def generate_code(self): 
        c = CodeGenerator()
        c.begin(tab = "    ")
        c.write("import beam\n")
        c.write("import nexus\n")
        c.write("\n")
        c.write("class {0}:\n".format(self.header))
        self.generate_constructor(c)
        c.indent()
        c.write("def start(self):\n")
        c.indent()
        c.write("self.tasks.push(self.S0)\n")
        c.dedent()
        c.dedent()
        c.write("\n")
        c.indent()
        c.write("def wait(self):\n")
        c.indent()
        c.write("self.completion_queue.top()\n")
        c.dedent()
        c.dedent()
        c.write("\n")
        self.generate_states_code(c)
        self.generate_conditions_code(c)
        self.generate_events_code(c)
        f = open(self.output_filename,'w')
        f.write(c.end())
        f.close()

def parse_inputs():
    parser = argparse.ArgumentParser(description = 'State machine generator')
    parser.add_argument('-i', '--input', dest = 'input_filename', 
                        required = True)
    parser.add_argument('-o', '--output', dest = 'output_filename', 
                        required = True)
    args = parser.parse_args()
    return args

def main():
    args = parse_inputs()
    smg = StateMachineGenerator(args.input_filename, args.output_filename)
    smg.generate_graph()

if __name__=='__main__':
    main()