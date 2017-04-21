# state_machine_generator
generates a python state machine code from graphviz

>>python generator.py -i "input.gv" -o "output.py"

There are certain rules the .GV file needs to follow for the script to properly generate a state machine:
1. Currently it only supports digraph. Subgraph and graphs with no direction do not work.
2. Each state transition must have an associate condition or event. For example:
    >>S1 -> S2; //Will not work since no condition is specified
3. There must be a space before and after '->' like this ' -> ', and ';' ending all transitions.
4. Only supports edges with labels starting with 'E', 'C' or '&#949;', and nodes starting with 'S'. Anything else will not work

Need to fix:
1. ~~Ordering of state needs to be fixed~~
2. Epsilon state must appear after conditional transitions
