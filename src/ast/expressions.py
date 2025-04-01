from abc import ABC, abstractmethod

class Expr(ABC):
	@abstractmethod
	def accept(self, visitor):
		pass

