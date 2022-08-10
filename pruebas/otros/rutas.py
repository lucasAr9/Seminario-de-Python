import os

print()
print(f"__file__: {__file__}")
print(f"os.getcwd(): {os.getcwd()}")

print(f"dirname(__file__): {os.path.dirname(__file__)}")
print(f"abspath(dirname('')) {os.path.abspath(os.path.dirname(''))}")
print(f"abspath(dirname(__file__)) {os.path.abspath(os.path.dirname(__file__))}")
print()
print(f"os.path.dirname(os.path.abspath(__file__)): {os.path.dirname(os.path.abspath(__file__))}")  # esta
print(f"os.path.abspath(os.path.dirname(__file__)): {os.path.abspath(os.path.dirname(__file__))}")
