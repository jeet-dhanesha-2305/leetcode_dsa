
class MyCalendar:

    def __init__(self):
        self.__events = []
        

    def book(self, start: int, end: int) -> bool:
        for event in self.__events:
            startEvent = event[0]
            endEvent = event[1]
            
            if (start < startEvent and end <= startEvent) or (start >= endEvent and end >= endEvent):
                pass
            else:
                return False
            
        self.__events.append( (start, end) )
        return True