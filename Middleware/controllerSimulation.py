import sys,time,random,sched
import threading
from controllerInterface import controllerBasic
import colours
from repeatedTimer import RepeatedTimer

standardQuerySize = 100

voltageCurrentSamples = []

class controllerSimulation(controllerBasic):
    def __init__(self,conf) -> None:
        if "isConsuming" not in conf  or "current" not in conf  or "voltage" not in conf :
            colours.printRed("meter config miss!")
            sys.exit()
        self._isConsuming=conf["isConsuming"]
        if self._isConsuming==False:
            self._base_current=conf["current"]
        else:
            self._base_current=conf["current"]
        self._base_voltage=conf["voltage"]
        self._dynamic_current=self._base_current
        self._dynamic_voltage=self._base_voltage
        self._runing_task= RepeatedTimer(1000,self._update_task)
        self._is_runing =False
        colours.printLightGray("isConsuming :%d , current:%d, voltage:%d"%(self._isConsuming,self._base_current,self._base_voltage))
    
    def queryCurrent(self):
        return self._dynamic_current

    def queryVoltage(self):
        return self._dynamic_voltage

    def queryPower(self):
        return self.queryCurrent()*self.queryVoltage()

    def powerOff(self):
        self._runing_task.cancel()
        self._dynamic_current = 0
        self._dynamic_voltage = 0

    def powerOn(self):
        self._runing_task.start()

    def isConsuming(self):
        return self._isConsuming
    
    def _update_task(self):
        # self._runing_task.start()
        colours.printLightGray(f"_update_task {time.time()}")
        #
        self._dynamic_voltage = (1+random.choice([-1,1])*0.01)*self._dynamic_voltage
        if self._dynamic_voltage>self._base_voltage*1.1 :
            self._dynamic_voltage=self._base_voltage*1.1
        elif self._dynamic_voltage<self._base_voltage*0.9 :
            self._dynamic_voltage=self._base_voltage*0.9
        #
        self._dynamic_current = (1+random.choice([-1,1])*0.01)*self._dynamic_current
        if self._dynamic_current>self._base_current*1.1 :
            self._dynamic_current=self._base_current*1.1
        elif self._dynamic_current<self._base_current*0.9 :
            self._dynamic_current=self._base_current*0.9
    
