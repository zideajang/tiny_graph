from typing import Dict,List,Tuple
from abc import ABC,abstractmethod

from tinygraph.component.base import Component

class BaseGraph(ABC):
    def __init__(self,name) -> None:
        self._name = name

        self._components:Dict[str,Component] = {}
        self._connections:List[Tuple[str,str]] = []

        self._graph:Dict[str,List[str]] = {}

        self.start_comp_name:str = None
        self.end_comp_name:str = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def components(self) -> Dict:
        return self._components

    @property
    def connections(self) -> List[Tuple[str, str]]:
        return self._connections

    @property
    def graph(self) -> Dict:
        return self._graph
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    @abstractmethod
    def add_component(self,comp:Component):
        pass  

    @abstractmethod
    def add_connect(self,start_comp:Component,end_comp:Component):
        pass  
    
    @abstractmethod
    def run(self,start_comp,input):
        pass

