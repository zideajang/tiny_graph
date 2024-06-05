

from tinygraph.graph.simple_graph import SimpleGraph
from tinygraph.component.base import Component


class AddComp(Component):

    def run(self,input):
        self.context = {
            "input":input,
            "output":input + 1
        }
        return input + 1
    
class MulComp(Component):
    def run(self,input):
        self.context = {
            "input":input,
            "output":input * 2
        }
        return input * 2

simple_graph = SimpleGraph("simple_chain")

add_one_comp = AddComp("add_1")
mul_two_comp = MulComp("mul_1")

simple_graph.add_component(add_one_comp)
simple_graph.add_component(mul_two_comp)

simple_graph.start_comp_name = "add_1"
simple_graph.end_comp_name = "mul_1"

simple_graph.add_connect(add_one_comp,mul_two_comp)

simple_graph.compile("add_1")
res = simple_graph.run(2)
print(f"{res=}")
