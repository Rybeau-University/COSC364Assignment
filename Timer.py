import RoutingTable

import datetime
import random

import time
import threading

#routing update - 30 sec
#triggered update - when topology changes 1 - 5 sec
#timeout - 180 sec
#garbage collection - 120 sec  



""" EITHER MAKE A THREAD FOR ROUTING & TRIGGERED UPDATE OR MAKE FOR LOOP """



"""Maintains router and RTE timers"""
class Timer:
    
    last_routing_update_time = 0            # last time a routing update was sent(30 sec update)
    next_available_triggerd_update = 0      # time when a triggerd update can be performed
    
    timeout_bin = []                        # list of RTE's timeout time
    garbage_bin = []                        # list of RTE's pending garbage collection
    
    

    
    """Check if a RTE in 'timeout_bin' list has reached it's 180 sec"""
    def checkTimeoutTimers(self):
        #not sure if I should pop the timeout if its time expired
        
        timeout_bin = self.timeout_bin      # local 'timeout_bin' list
        
        while True:
            i = 0
            while i < len(timeout_bin):
                
                RTE_id = timeout_bin[i][0]
                RTE_timeout_time = timeout_bin[i][1]
                
                
                if (RTE_timeout_time <= self.getDateTime()):        # if RTE's timeout time has expired
                    self.addToGarbageBin(RTE_id)
                    self.popTimeoutBin(RTE_id)
                    
                    
                i += 1
                
            garbage_bin = self.garbage_bin      # set local 'garbage_bin' equal to global 'garbage_bin'
            
        
    
    
    
    
    """Check if a RTE in 'garbage_bin' list has reached it's 120 sec"""
    def checkGarbageTimers(self):
        # using local 'garbage_bin' to check each RTE since the global 'garbage_bin' can change during loop
        
        garbage_bin = self.garbage_bin      # local 'garbage_bin' list
        
        while True:
            i = 0
            while i < len(garbage_bin):
                
                RTE_id = garbage_bin[i][0]
                RTE_garbage_time = garbage_bin[i][1]
                
                
                if (RTE_garbage_time <= self.getDateTime()):        # if RTE's garbage time has expired
                    self.collectGarbage(RTE_id)
                    self.popGarbageBin(i)
                    
                    
                i += 1
                
            garbage_bin = self.garbage_bin      # set local 'garbage_bin' equal to global 'garbage_bin'
            
            
    
    
    """Get current date & time"""
    def getDateTime(self):
        return datetime.datetime.now()
    
    
    
    """Return 'timeDelta' in 'datetime' syntax"""
    def getIncrementDateTime(self, timeDelta):
        return datetime.timedelta(seconds = timeDelta)
    
    
    
    
    """Append new RTE to 'timeout_bin' list"""
    def addToTimeoutBin(self, RTE_id):
        pass
    
    
    
    """Pop a RTE off the global 'timeout_bin' list"""
    def popTimeoutBin(self, RTE_id):
        pass
    
    
    
    
    """Append timed out RTE to global 'garbage_bin' list"""
    def addToGarbageBin(self, RTE_id):
        
        RTE_garbage_timeout_time = self.getDateTime() + self.getIncrementDateTime(120)
        garbage_RTE = tuple([RTE_id, RTE_garbage_timeout_time])
        
        self.garbage_bin.append(garbage_RTE)
    
    
    
    """Pop a RTE off the global 'garbage_bin' list"""
    def popGarbageBin(self, RTE_id):
        pass
    
    
    
    """Remove RTE from 'RoutingTable'"""
    def collectGarbage(self, RTE_id):
        pass
    
    
    
    
    """Return a random time inteval between 1 to 5 sec inclusive"""
    def getOffsetTime(self):
        return random.randint(1, 5)
    
    



#t = Timer()

##make a check if thread is running
#x = threading.Thread(target=t.checkGarbageTimers)
#x.start()


#t.addToGarbageBin("0000")

#time.sleep(10)
#t.addToGarbageBin("1111")
