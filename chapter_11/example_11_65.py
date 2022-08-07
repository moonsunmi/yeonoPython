from pathlib import Path
path = Path('/Users')
path_list = list(path.iterdir())

Path('dir1').mkdir()
Path('dir2').mkdir()
Path('file1').touch()

Path('dir2').replace('dir1/dir2')
Path('dir1/dir2').replace(Path('dir2'))
Path('dir2').replace('dir3')