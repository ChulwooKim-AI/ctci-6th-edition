"""Call Center

Imagine you have a call center with three levels of employees: respondent, manager,
and director. An incoming telephone call must be first allocated to a respondent who is free. If the
respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
free or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method dispatchCall() which assigns a call to
the first available employee.

Hints: 
#363
Before coding, make a list of the objects you need and walk through the common algorithms.
Picture the code. Do you have everything you need?
"""

'''
Core objects: Employee, Respondent, Manager, Director, Caller, Call, CallHandler
Relationship: Employee(Respondent, Manager, Director) - CallHandler - Call -> Caller
Key actions: Employee(receive_call, complete_call, assign_call, escalate_call, is_free, get_rank)

'''
class Employee:    
    def __init__(self, call_handler):
        self.call_handler = call_handler
        self.current_call = None
        self.rank = None
    
    def receive_call(self, call):
        self.current_call = call
    
    def complete_call(self):
        if self.current_call:
            self.current_call.disconnect()
            self.current_call = None
        self.assign_call()

    def assign_call(self):
        if not self.is_free():
            return False
        return self.call_handler.assign_call(self)
    
    def is_free(self):
        return self.current_call is None
    
    def escalate_call(self):
        if self.current_call:
            self.current_call.increament_rank()
            self.current_call.dispatch_call(self.current_call)
            self.current_call = None
        self.assign_call()

    def get_rank(self):
        return self.rank


class Respondent(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.Respondent


class Manager(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.Manager


class Director(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.Director


class Caller:
    def __init__(self, id):
        self.id = id


class Call:
    def __init__(self, caller):
        self.caller = caller
        self.rank = Rank.Respondent
        self.handler = None
    
    def set_handler(self, employee):
        self.handler = employee
    
    def set_rank(self, rank):
        self.rank = rank
    
    def get_rank(self):
        return self.rank
    
    def increament_rank(self):
        if self.rank == Rank.Respondent:
            self.rank = Rank.Manager
        elif self.rank == Rank.Manager:
            self.rank = Rank.Director
        return self.rank
    
    def disconnect(self):
        print("Thank you for calling")


class CallHandler:
    NUM_RESPONDENT = 3
    NUM_MANAGER = 2
    NUM_DIRECTOR = 1
    LEVEL = 3

    def __init__(self):
        self.call_queue = [[],[],[]]
        self.employee_levels = list()
        self.employee_levels.append([Respondent(self) for _ in range(self.NUM_RESPONDENT)])
        self.employee_levels.append([Manager(self) for _ in range(self.NUM_MANAGER)])
        self.employee_levels.append([Director(self) for _ in range(self.NUM_DIRECTOR)])
    
    def get_handler_for_call(self, call):
        for level in range(call.get_rank(), self.LEVEL):
            for employee in self.employee_levels[level]:
                if employee.is_free():
                    return employee
        return None

    def dispatch_call(self, caller):
        call = Call(caller)
        employee = self.get_handler_for_call(call)
        if employee:
            employee.receive_call(call)
            call.set_handler(employee)
        else:            
            self.call_queue[call.get_rank()].append(call)
            raise Exception("Every lines is full. Please wait for them.")

    def assign_call(self, employee):
        for rank in range(employee.get_rank(), 0, -1):
            queue = self.call_queue[rank]
            if queue:
                call = queue.pop(0)
                if call:
                    employee.receive_call(call)
                    return True
        return False


class Rank:
    Respondent = 0
    Manager = 1
    Director = 2


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.caller1 = Caller(1)
        self.caller2 = Caller(2)
        self.caller3 = Caller(3)
        self.caller4 = Caller(4)
        self.caller5 = Caller(5)
        self.caller6 = Caller(6)
        self.caller7 = Caller(7)
        self.call_handler = CallHandler()

    def test_full_line(self):
        for _ in range(6):
            self.call_handler.dispatch_call(self.caller1)
        self.assertRaises(Exception, self.call_handler.dispatch_call, self.caller1)
        


if __name__ == "__main__":
    unittest.main()