from abc import ABC,abstractmethod
from typing import List,Any,Dict,Literal
from pydantic import BaseModel,Field

class Component(ABC):

    def __init__(self,name,type:Literal["common", "condition","aggregate"]="common") -> None:
        self._name = name
        
        self._context:Dict = {
            "input":None,
            "output":None
        }
        self._parent:List[Component] = []
        self._children:List[Component] = []
        self._type: Literal["common", "condition","aggregate"] = type


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    # Property for '_context'
    @property
    def context(self) -> Dict:
        return self._context

    @context.setter
    def context(self, value: Dict) -> None:
        self._context = value

    # Property for '_parent'
    @property
    def parent(self) -> List['Component']:
        return self._parent

    @parent.setter
    def parent(self, value: List['Component']) -> None:
        self._parent = value

    # Property for '_children'
    @property
    def children(self) -> List['Component']:
        return self._children

    @children.setter
    def children(self, value: List['Component']) -> None:
        self._children = value

    # Property for '_type' with validation
    @property
    def type(self) -> Literal["common", "condition"]:
        return self._type

    @type.setter
    def type(self, value: Literal["common", "condition","aggregate"]) -> None:
        if value not in ["common", "condition","aggregate"]:
            raise ValueError(f"Invalid type {value}; type must be 'common' or 'condition'")
        self._type = value

    @abstractmethod
    def run(self,input):
        pass

    def __repr__(self) -> str:
        return f"'input': {self._context['input']}\t'output':{self._context['output']}"