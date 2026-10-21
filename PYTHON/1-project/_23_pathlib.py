from pathlib import Path

path = Path(r"D:\test.txt")

print(path.name)
print(repr(path.name))
print("#-----------------#")
# print(path)
# print(repr(path))
print(Path)
print(type(path))
print(isinstance(path, Path))