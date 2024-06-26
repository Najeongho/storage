import os
import shutil
from pathlib import Path

# 지정된 경로에 다중 레벨 디렉토리를 생성하고, 마지막 레벨 디렉토리에 파일을 복사하는 메소드
def create_directories_and_files(base_path, depth1_count, depth2_count, depth3_count, depth4_count, depth5_count, file_count, source_file_path):
    """
    Args:
        base_path (str): 기본 디렉토리 경로
        depth1_count (int): depth1 디렉토리 개수
        depth2_count (int): depth2 디렉토리 개수
        depth3_count (int): depth3 디렉토리 개수
        depth4_count (int): depth4 디렉토리 개수
        depth5_count (int): depth5 디렉토리 개수
        file_count (int): 각 depth5 디렉토리에 복사할 파일 개수
        source_file_path (str): 복사할 원본 파일 경로
    """
    for i in range(1, depth1_count + 1):
        depth1_path = Path(base_path) / f"tab{i}"
        depth1_path.mkdir(exist_ok=True)
        for j in range(1, depth2_count + 1):
            depth2_path = depth1_path / f"{j}Line"
            depth2_path.mkdir(exist_ok=True)
            for k in range(1, depth3_count + 1):
                depth3_path = depth2_path / f"202{k+2}"
                depth3_path.mkdir(exist_ok=True)
                for l in range(1, depth4_count + 1):
                    depth4_path = depth3_path / f"01{l:02}"
                    depth4_path.mkdir(exist_ok=True)
                    for m in range(1, depth5_count + 1):
                        depth5_path = depth4_path / f"{m:02}"
                        depth5_path.mkdir(exist_ok=True)
                        for n in range(1, file_count + 1):
                            file_name = f"TAB_Q{k}WE{l}RA{m}SD{n}F_202{k+2}01{l:02}{m:02}{n:02}_VISION PC_OK.png"
                            destination_file_path = depth5_path / file_name
                            shutil.copy(source_file_path, destination_file_path)

if __name__ == "__main__":
    base_path = r"\\172.16.20.195\testimagedata"  # 네트워크 드라이브 경로
    source_file_path = r"C:\test\pouch.png"  # 복사할 원본 파일 경로

    create_directories_and_files(base_path, 2, 3, 1, 30, 24, 60, source_file_path)
