class SymbolTable:
    def __init__(self, enclosing=None):
        self.enclosing = enclosing
        self.symbols = {}

    def add(self, name, value):
        self.symbols[name] = value

    def get(self, name):
        return self.symbols.get(name)

    def remove(self, name):
        if name in self.symbols:
            del self.symbols[name]

    def __str__(self):
        return str(self.symbols)
    