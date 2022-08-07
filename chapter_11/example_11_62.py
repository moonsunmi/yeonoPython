from pathlib import Path
def ls(path):
    path_obj = Path(path)

    for item in path_obj.iterdir():
        print(item)

print(ls('/Users')) # macOS라서 다르게 실습
