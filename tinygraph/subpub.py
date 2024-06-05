from __future__ import annotations

from abc import ABC,abstractmethod
from typing import Dict,List,Any
from tinygraph.component.base import Component

class ComponentObserver(Component):

    @abstractmethod
    def update(self, subject: Subject,comp_name:str) -> None:
        pass


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: ComponentObserver) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: ComponentObserver) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass   


class StateGraphSubject(Subject):

    
    _context:Dict = {}
    _observers: List[ComponentObserver] = []

    def attach(self, observer: ComponentObserver) -> None:
        self._observers.append(observer)
        
        self._context[observer.name] = observer

    def detach(self, observer: ComponentObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

   
