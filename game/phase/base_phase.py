from abc import ABC, abstractclassmethod


class BasePhase(ABC):
    @abstractclassmethod
    def condition_to_play():
        ...

    @abstractclassmethod
    def start_phase():
        ...
