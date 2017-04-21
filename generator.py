import argparse
from collections import defaultdict
import pprint
import re
import sys, string

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
        self.body = None
    
    def generate_body(self):
        body_text = re.search(r"\{(.*)\}", self.file_text, re.DOTALL).group(0)
        matches = re.finditer(r"^(.*)\;", body_text, re.MULTILINE)
        self.body=[]
        for match in matches:
            self.body.append(str(match.group(0)))
    
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
        self.generate_body()
        for line in self.body:
            if "->" in line:
                source_name = re.search(r"(.*)->", line).group(1).strip()
                destination_name = re.search(r"-> (.*) \[", line).\
                    group(1).strip()
                labels = re.search(r"\"(.*?)\"", line).group(1)
                labels = ''.join(labels.split(' '))
                weights = self.extract_weights(labels)            
                self.add_edge(source_name, destination_name, weights, labels)
        self.state_graph.print_graph()
        self.generate_code()
        
    def generate_code(self):
        c = CodeGenerator()
        c.begin(tab="    ")
        c.write("import beam\n")
        c.write("import nexus\n")
        c.write("class {0}:\n".format(self.header))
        c.indent()
        c.write("def __init__(self):\n")
        c.write("###States###\n")
        states = sorted(self.state_graph.states, key=lambda state: int(
                                                    filter(str.isdigit, state)))
        conditions = sorted(self.state_graph.conditions, key=lambda condition:\
                                            int(filter(str.isdigit, condition)))
        events = sorted(self.state_graph.events, key=lambda event:\
                                            int(filter(str.isdigit, event)))
        for state in states:
            c.write("def "+state+"(self):\n")
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
                                edge=edge.replace(match.group(0), "self."+\
                                    match.group(0)+"()")
                                temp_hash.add(match.group(0))
                        c.indent()
                        c.write("if {0}:\n".format(edge))
                        c.indent()
                        c.write("return self.{0}()\n".format(destination_state))
                        c.dedent()
                        c.dedent()
                    elif edge == "&#949;":
                        c.indent()
                        c.write("return self.{0}()\n".format(destination_state))
                        c.dedent()
            c.write("\n")
        c.write("###Conditions###\n")
        for condition in conditions:
            c.write("def {0}(self):\n".format(condition))
            c.write("\n")
        c.write("###Events###\n")  
        for event in events:
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
            c.write("\n")
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