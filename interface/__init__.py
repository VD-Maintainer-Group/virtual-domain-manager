#!/usr/bin/env python3
from abc import ABCMeta, abstractmethod

class SRC_API(metaclass=ABCMeta):
    @abstractmethod
    def onStart(self):
        return 0

    @abstractmethod
    def onStop(self):
        return 0

    @abstractmethod
    def onSave(self, stat_file):
        return 0

    @abstractmethod
    def onResume(self, stat_file):
        return 0

    @abstractmethod
    def onClose(self):
        return 0
    
    # @abstractmethod
    def onTrigger(self, *args):
        return 0

    pass