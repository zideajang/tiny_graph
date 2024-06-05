from typing import List
from tinygraph.component.base import Component
from tinygraph.graph.base_graph import BaseGraph

class SimpleGraph(BaseGraph):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._path:List[str] = []

    def add_component(self,comp):
        if comp.name in self.components:
            raise ValueError(f"{comp.name} already existed in components")
        self.components[comp.name] = comp
    
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

    def run(self,input):
        for compont_name in self._path:
            if compont_name == self.start_comp_name:
                self.components[compont_name].run(input)
            else:
                comp = self.components[compont_name]
                if comp.type == "common":
                    print(comp.parent[0].context["output"])
                    comp.run(comp.parent[0].context["output"])
                if comp.type == "aggregate":
                    input = [p.context["output"] for p in comp.parent]
                    comp.run(input)

        print(self.components)
        return self.components[self.end_comp_name].context["output"]