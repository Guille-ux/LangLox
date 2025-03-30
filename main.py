# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# Copyright (c) 2025 Guillermo Leira Temes
# 
import sys

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

