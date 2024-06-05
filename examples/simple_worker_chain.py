
from tinygraph.graph.simple_graph import SimpleGraph
from tinygraph.component.base import Component

class StartComp(Component):
    def run(self,input):
        self.context = {
            "input":input,
            "output":input
        }
        return input

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

class SumComp(Component):
    def run(self,input_list):
        res = 0
        for input in input_list:
            res += input
        self.context = {
            "input":input_list,
            "output":res
        }
        return res


start_comp = StartComp("start")

add_one_comp = AddComp("add_1")
mul_one_comp = MulComp("mul_1")
add_two_comp = AddComp("add_2")

sum_comp = SumComp("sum",type="aggregate")

simple_workers_chain = SimpleGraph("simple_workers_chain")

simple_workers_chain.add_component(start_comp)

simple_workers_chain.add_component(add_one_comp)
simple_workers_chain.add_component(mul_one_comp)
simple_workers_chain.add_component(add_two_comp)

simple_workers_chain.add_component(sum_comp)

simple_workers_chain.start_comp_name = "start"
simple_workers_chain.end_comp_name = "sum"

simple_workers_chain.add_connect(start_comp,add_one_comp)
simple_workers_chain.add_connect(start_comp,mul_one_comp)
simple_workers_chain.add_connect(start_comp,add_two_comp)


simple_workers_chain.add_connect(add_one_comp,sum_comp)
simple_workers_chain.add_connect(mul_one_comp,sum_comp)
simple_workers_chain.add_connect(add_two_comp,sum_comp)


simple_workers_chain.compile('start')
res = simple_workers_chain.run(2)
print(res)