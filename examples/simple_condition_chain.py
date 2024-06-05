from typing import Literal
from tinygraph.graph.state_graph import StateGraph
from tinygraph.component.base import Component

from tinygraph.subpub import ComponentObserver,StateGraphSubject, Subject

class AddComp(ComponentObserver):

    def update(self, subject: Subject) -> None:
        if(self.parent):
            for comp in self.parent:
                print(subject._context[comp.name]._context['output'])
            

    def run(self,input):
        self.context = {
            "input":input,
            "output":input + 1
        }
        return input + 1
    
class EndComp(ComponentObserver):

    def update(self, subject: Subject,) -> None:

        for comp in self.parent:
            subject._context[comp.name]._context['output']


    def run(self,input):
        self.context = {
            "input":input,
            "output":input
        }
        return input
    
class GreaterThan10Comp(ComponentObserver):

    def __init__(self, 
                 name:str, 
                 t_comp:ComponentObserver,
                 f_comp:ComponentObserver,
                 type: Literal['common','condition','aggregate'] = "condition") -> None:
        
        super().__init__(name, type)

        self.true_comp:ComponentObserver = t_comp
        self.false_comp:ComponentObserver = f_comp

    def update(self, subject: Subject) -> None:
        for comp in self.parent:
            subject._context[comp.name]._context['output']

    def run(self,input):

        input = self.parent[0].context['output']

        self.context = {
            "input":input,
            "output":input
        }
        if (input  > 10):
            self.children.append(self.true_comp)
            return self.true_comp.name
        else:
            self.children.append(self.false_comp)
            return self.false_comp.name
        return input 

simple_state_graph = StateGraph("simple_state_chain")

add_one_comp = AddComp("add_1")
end_comp = EndComp("end")
greater_than_10_comp = GreaterThan10Comp("greater_than_10",end_comp,add_one_comp)

simple_state_graph.add_component(add_one_comp)
simple_state_graph.add_component(greater_than_10_comp)
simple_state_graph.add_component(end_comp)

simple_state_graph.start_comp_name = "add_1"
simple_state_graph.end_comp_name = "end"

simple_state_graph.add_connect(add_one_comp,greater_than_10_comp)
simple_state_graph.add_connect(greater_than_10_comp,end_comp)
simple_state_graph.compile("add_1")
res = simple_state_graph.run(2)
print(f"{res=}")
