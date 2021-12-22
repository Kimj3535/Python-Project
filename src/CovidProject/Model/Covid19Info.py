'''
Created on Jan 28, 2021

@author: Kim Johnson
'''

class MyClass(object):
    '''
    classdocs
    '''


    '''
     Constructor with variables
    '''
    def __init__(self, pruid,prname,prnameFR,date,numconf,numprob,numdeaths,numtotal,numtoday,ratetotal):
        self._pruid = pruid
        self._prname = prname
        self._prnameFR = prnameFR
        self._date = date
        self._numconf = numconf
        self._numprob = numprob
        self._numdeaths = numdeaths
        self._numtotal = numtotal
        self._numtoday = numtoday
        self._ratetotal = ratetotal
        
        ''' Getter method for pruid variable'''
        def get_pruid(self):
            return self._pruid
        
        '''Setter method for pruid variable'''
        def set_pruid(self,pruid):
            self._pruid = pruid
            
        '''Getter method for prname variable'''
        def get_prname(self):
                return self.prname
            
        '''Setter method for prname variable'''
        def set_prname(self,prname):
            self._prname = prname
            
        '''Getter method for prnameFR variable'''
        def get_prnameFR(self):
            return self._prnameFR
          
        '''Setter method for prnameFR variable'''
        def set_prnameFR(self,prnameFR):
            self._prnameFR = prnameFR
             
        '''Getter method for date variable'''
        def get_date(self):
            return self._date
        
        '''Setter method for date variable'''
        def set_date(self,date):
            self._date = date
            
        '''Getter method for numconf variable'''
        def get_numconf(self):
            return self._numconf
        
        '''Setter method for numconf variable'''
        def set_numconf(self,numconf):
            self._numconf = numconf
            
        '''Getter method for numprob variable'''
        def get_numprob(self):
            return self._numprob
        
        '''Setter method for numprob variable'''
        def set_numprob(self,numprob):
            self._numprob = numprob
            
        '''Getter method for numdeaths variable'''
        def get_numdeaths(self):
            return self._numdeaths
        
        '''Setter method for numdeaths variable'''
        def set_numdeaths(self,numdeaths):
            self._numdeaths = numdeaths
            
        '''Getter method for numtotal variable'''
        def get_numtotal(self):
            return self._numtotal
        
        '''Setter method for numtotal variable'''
        def set_numtotal(self,numtotal):
            self._numtotal = numtotal
            
        '''Getter method for numtoday variable'''
        def get_numtoday(self):
            return self._numtoday
           
        '''Setter method for numtoday variable'''
        def set_numtoday(self,numtoday):
            self._numtoday = numtoday
            
        '''Getter method for ratetotal variable'''
        def get_ratetotal(self):
            return self._ratetotal
        
        '''Setter method for ratetotal variable'''
        def set_ratetotal(self,ratetotal):
            self._ratetotal = ratetotal
            
                
        x = getattr(MyClass, 'prname')
        print(prname)
          
               
           
           
            
            
           
        
        
        
        