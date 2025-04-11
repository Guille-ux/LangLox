class SymbolTable:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.symbols = {}

    def add(self, name, value):
        self.symbols[name] = value

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.enclosing:
            return self.enclosing.get(name)
        raise ValueError(f"Variable '{name}' not defined.")

    def remove(self, name):
        if name in self.symbols:
            del self.symbols[name]

    def __str__(self):
        return str(self.symbols)
class FuncTable:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.symbols = {}

    def add(self, name, value):
        self.symbols[name] = value

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.enclosing:
            return self.enclosing.get(name)
        raise ValueError(f"Function '{name}' not defined.")

    def remove(self, name):
        if name in self.symbols:
            del self.symbols[name]

    def __str__(self):
        return str(self.symbols)
class Memory:
    def __init__(self, enclosing=None):
        self.var_memory = SymbolTable(enclosing)
        self.func_memory = FuncTable(enclosing)
        self.classes = {}
        self.modules = {}
        self.enclosing = enclosing
    def add_function(self, name, func):
        self.func_memory[name] = func
    def add_class(self, name, class_):
        self.classes[name] = class_
    def add_module(self, name, module):
        self.modules[name] = module
    def get_function(self, name):
        self.func_memory.get(name)
    def get_class(self, name):
        if  name in self.classes:
            return self.classes[name]
        elif self.enclosing is not None:
            return self.enclosing.get_class(name)
        raise ValueError(f"Class '{name}' not defined.")
    def get_module(self, name):
        if name in self.modules:
            return self.modules[name]
        elif self.enclosing is not None:
            return self.enclosing.get_module(name)
        raise ValueError(f"Module '{name}' not defined.")
    def get_variable(self, name):
        self.var_memory.get(name)