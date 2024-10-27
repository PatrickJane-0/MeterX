from abc import abstractmethod

class controllerBasic:
    @abstractmethod
    def queryCurrent(self):
        pass

    @abstractmethod
    def queryVoltage(self):
        pass

    @abstractmethod
    def queryPower(self):
        pass

    @abstractmethod
    def powerOff(self):
        pass

    @abstractmethod
    def powerOn(self):
        pass

    @abstractmethod
    def isConsuming(self):
        pass
    
