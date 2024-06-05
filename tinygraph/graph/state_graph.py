from typing import List
from tinygraph.component.base import Component
from tinygraph.graph.base_graph import BaseGraph

from tinygraph.subpub import StateGraphSubject

class StateGraph(BaseGraph):

    def __init__(self, name) -> None:
        super().__init__(name)
        self._subject = StateGraphSubject()

    def add_component(self,comp):
        if comp.name in self.components:
            raise ValueError(f"{comp.name} already existed in components")
        self.components[comp.name] = comp

        self._subject.attach(comp)

    def add_connect(self, start_comp: Component, end_comp: Component):
        # check
        if start_comp.name not in self.components:
            raise KeyError(f"The key '{start_comp.name}' does not exist in the dictionary.")
        
        if end_comp.name not in self.components:
            raise KeyError(f"The key '{end_comp.name}' does not exist in the dictionary.")

        start_comp.children.append(end_comp)
        end_comp.parent.append(start_comp)

        self.connections.append((start_comp.name,end_comp.name))

        if start_comp.name in self.graph:
            self.graph[start_comp.name].append(end_comp.name)
        else:
            self.graph[start_comp.name]= [end_comp.name]
    def bfs(self, start):
        path = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in path:
                path.append(vertex)
                if vertex in self.graph:
                    queue.extend(self.graph[vertex])
                else:
                    continue

        return path
    
    def compile(self,start:str):
        self._path = self.bfs(start)
        
    # def _path_generator(self):
    #     for p in self._path:
    #         yield p
    
    def run(self,input):
        # comp_path_list = self._path_generator()
        # print(next(comp_path_list))

        stack_size = len(self._path)
        print(f"{stack_size=}")
        current_pnt = 0
        while current_pnt < stack_size:
            if(current_pnt == 0):
                print(self.components[self.start_comp_name].context['input'])
                if self.components[self.start_comp_name].context['input']:
                    self.components[self.start_comp_name].run(self.components[self.start_comp_name].context['input'])
                else:
                    self.components[self.start_comp_name].run(input)
                print(self.components[self.start_comp_name].context['output'])
                current_pnt += 1
            else:
                current_comp_name = self._path[current_pnt]
                current_comp = self.components[current_comp_name]
                print(self.components[current_comp_name].context['input'])
                if current_comp.type == "condition":
                    res = current_comp.run(input)
                    current_pnt = self._path.index(res)
                    self.components[res].context['input'] = current_comp.context['output']
                    print(current_pnt)
                else:
                    current_comp.run(input)
                    current_pnt += 1    
            self._subject.notify()