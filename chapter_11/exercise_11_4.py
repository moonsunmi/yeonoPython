from pathlib import Path


def cp(src, dst):
    src_obj = Path(src)
    dst_obj = Path(dst)

    if not src_obj.exists():
        raise FileNotFoundError

    with open(src_obj, 'r') as file:
        all_text = file.read()

    with open(dst_obj, 'w') as file:
        file.write(all_text)


cp('original.txt', 'clone.txt')
