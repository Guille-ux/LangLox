import sys

class Token:
	def __init__(tipo, valor):
		self.type = tipo
		self.value = valor
		self.included = []
	def include(token):
		self.included.append(token)
	def __repr__(self):
		return f"Token(type={self.type}, value={self.value})"
	def __str__(self):
		pass
def main():
	if len(sys.argv) < 3:
		print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
		exit(1)

	command = sys.argv[1]
	filename = sys.argv[2]

	if command != "tokenize":
		print(f"Unknown command: {command}", file=sys.stderr)
		exit(1)

	with open(filename) as file:
		file_contents = file.read()

	if file_contents:
		raise NotImplementedError("Scanner not implemented")
	else:
		print("EOF  null") # Placeholder, remove this line when implementing the scanner


if __name__ == "__main__":
	main()

