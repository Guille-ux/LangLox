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
    