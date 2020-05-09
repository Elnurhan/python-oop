class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, t):
        self.t = t
    
    def command(self):
        return "GET"


class EventSet:
    def __init__(self, value):
        self.value = value
    
    def command(self):
        return "SET"


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.command() == "SET":
            if isinstance(event.value, int):
                obj.integer_field = event.value
                return

        elif event.command() == "GET":
            if event.t is int:
                return obj.integer_field

        return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.command() == "SET":
            if isinstance(event.value, float):
                obj.float_field = event.value
                return

        elif event.command() == "GET":
            if event.t is float:
                return obj.float_field

        return super().handle(obj, event)



class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.command() == "SET":
            if isinstance(event.value, str):
                obj.string_field = event.value
                return

        elif event.command() == "GET":
            if event.t is str:
                return obj.string_field

        return super().handle(obj, event)


if __name__ == "__main__":
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))
    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))

