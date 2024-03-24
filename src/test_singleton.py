class Test:
    _instance = None
    prop = 0

    def __new__(cls):
        print('new')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.prop = 2
        return cls._instance

    def increment(self):
        self.prop += 1


test = Test()
print(test.prop)
test.increment()
print(test.prop)
test2 = Test()
print(test2.prop)
