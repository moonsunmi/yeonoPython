from pathlib import Path
def mv(src, dst):
    """src 경로의 파일을 dst 경로로 이동한다."""
    src_obj = Path(src)
    dst_obj = Path(dst)

    if dst_obj.exists():
        raise FileExistsError
    src_obj.replace(dst_obj)

mv('dir2', 'dir88')