
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import site
import shutil
from pathlib import Path

def print_header(title):
    print(f"\n{'='*10} {title} {'='*10}\n")

def check_python_info():
    print_header("파이썬 인터프리터 정보")
    print(f"실행 중인 Python 경로: {sys.executable}")
    print(f"site-packages 경로 목록:")
    for path in site.getsitepackages():
        print(f"  - {path}")

def check_pip_module_path(module_name):
    print_header(f"pip로 설치된 '{module_name}' 모듈 경로")
    try:
        result = subprocess.run(["pip", "show", module_name], capture_output=True, text=True, check=True)
        for line in result.stdout.splitlines():
            if line.startswith("Location:"):
                print(line)
                break
        else:
            print("모듈 위치 정보를 찾을 수 없습니다.")
    except subprocess.CalledProcessError:
        print(f"모듈 '{module_name}' 이(가) 설치되지 않았습니다.")

def remove_idea_folder(project_root):
    print_header(".idea 폴더 삭제")
    idea_path = Path(project_root) / ".idea"
    if idea_path.exists() and idea_path.is_dir():
        try:
            shutil.rmtree(idea_path)
            print(f"삭제 완료: {idea_path}")
        except Exception as e:
            print(f"삭제 실패: {e}")
    else:
        print(f".idea 폴더가 존재하지 않거나 디렉토리가 아닙니다: {idea_path}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="PyCharm 환경 문제 진단 도구")
    parser.add_argument("--module", help="pip로 설치된 모듈명 확인", required=False)
    parser.add_argument("--remove-idea", help=".idea 폴더 삭제할 프로젝트 루트 경로", required=False)
    args = parser.parse_args()

    check_python_info()

    if args.module:
        check_pip_module_path(args.module)

    if args.remove_idea:
        remove_idea_folder(args.remove_idea)

if __name__ == "__main__":
    main()
