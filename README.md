# 🧠 pycharm_env_checker

**PyCharm에서 Python 모듈 import 오류 발생 시 진단과 초기화를 도와주는 CLI 도구**

---

## 📦 개요

이 스크립트는 다음과 같은 PyCharm 관련 문제를 진단하고 해결할 수 있도록 도와줍니다:

- `No module named xxx` 또는 `Unresolved reference` 오류 발생 시 환경 정보 확인
- pip로 설치한 모듈이 현재 인터프리터에서 접근 가능한지 확인
- `.idea` 폴더를 삭제하여 PyCharm 프로젝트 설정을 초기화

---

## ✅ 주요 기능

| 기능 | 설명 |
|------|------|
| Python 인터프리터 정보 출력 | 현재 실행 중인 인터프리터 경로 및 site-packages 확인 |
| pip 설치 경로 확인 | pip로 설치된 모듈의 실제 경로 확인 |
| .idea 폴더 삭제 | PyCharm의 프로젝트 설정을 초기화 |

---

## 🚀 사용법

### 1. 현재 파이썬 환경 확인
```bash
python pycharm_env_checker.py

출력 예시:
```swift
실행 중인 Python 경로: C:/Users/사용자명/AppData/Local/Programs/Python/Python311/python.exe
site-packages 경로 목록:
  - C:/Users/사용자명/AppData/Local/Programs/Python/Python311/Lib/site-packages


### 2. 특정 모듈의 설치 경로 확인
```bash
python pycharm_env_checker.py --module <모듈명>

예시:
```bash
python pycharm_env_checker.py --module heroes

출력 예시:
```swift
Location: C:/Users/사용자명/AppData/Local/Programs/Python/Python311/Lib/site-packages


### 3. .idea 폴더 삭제
```bash
python pycharm_env_checker.py --remove-idea "C:/Users/사용자명/PycharmProjects/project-name"

### 4. 모든 기능 한 번에 사용
```bash
python pycharm_env_checker.py --module heroes --remove-idea "C:/Users/사용자명/PycharmProjects/project-name"


---

## 💻 개발 환경

- Python 3.6+
- OS: Windows (PyCharm 사용자 기준)
