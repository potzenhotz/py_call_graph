from __future__ import annotations
from typing import Optional
import pydot
from dataclasses import dataclass, field


filename = "py_call_graph/resources/test.scala"
with open(filename) as f:
    content = f.read()

list = list(filter(None, content.split(" ")))
print(list)


@dataclass
class FunctionProperties:
    name: str
    index_start: Optional[int] = None
    index_end: Optional[int] = None
    content: Optional[str] = None
    calling_function: list[str] = field(default_factory=lambda: [])


function_list: list[FunctionProperties] = []
function_list_index = 0
counter_bracket = 0
for index, line in enumerate(list):
    if "def" in line:
        current_function_name = list[index + 1].partition("(")[0]
        function_list_index += 1
        function_list.append(
            FunctionProperties(name=current_function_name, index_start=index)
        )
        counter_bracket = 0
    if "{" in line:
        counter_bracket += 1
    if "}" in line and counter_bracket == 1:
        function_list[function_list_index - 1].index_end = index
    if "}" in line:
        counter_bracket -= 1

for function in function_list:
    function.content = " ".join(list[function.index_start : function.index_end])

function_names = [x.name for x in function_list]

for function in function_list:
    for index, function_name in enumerate(function_names):
        if function_name in function.content and function_name != function.name:
            function.calling_function.append(function_names[index])


function_extract = [(i.name, i.calling_function) for i in function_list]
print(f"FUNCTIONS: {function_extract}")

# https://github.com/pydot/pydot
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

# Add nodes
for index, function in enumerate(function_extract):
    node = pydot.Node(index, label=function[0], shape="box")
    graph.add_node(node)
    for children in function[1]:
        edge = pydot.Edge(function[0], children)
        graph.add_edge(edge)
graph.write_svg("output/test.svg")
