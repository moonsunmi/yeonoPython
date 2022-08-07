from pathlib import Path
path = Path('/Users')
path_list = list(path.iterdir())
print(path_list)
print(path_list[0])
print(path_list[0].is_dir())