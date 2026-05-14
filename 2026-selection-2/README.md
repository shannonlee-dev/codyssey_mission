# 2026 Selection 2

Python 콘솔 퀴즈 게임 과제입니다. 메뉴 기반 콘솔 UI, 퀴즈 데이터 모델, 파일 기반 상태 저장, 예외 입력 처리를 구현했습니다.

## Structure

```text
2026-selection-2/
├── docs/
│   └── screenshots/
├── main.py
├── quiz.py
├── quiz_game.py
└── state.json
```

## Contents

| Path | Summary |
| --- | --- |
| `main.py` | 프로그램 진입점 |
| `quiz.py` | 퀴즈 항목 데이터 모델 |
| `quiz_game.py` | 게임 진행, 입력 처리, 저장 로직 |
| `state.json` | 퀴즈 목록과 최고 점수 저장 파일 |
| `docs/screenshots/` | 실행 흐름과 예외 상황 검증 이미지 |

## Run

```bash
cd 2026-selection-2
python3 main.py
```

## Features

- 퀴즈 풀이, 퀴즈 추가, 퀴즈 목록 조회, 최고 점수 확인
- `state.json` 기반 데이터 저장 및 재실행 시 복구
- 잘못된 입력, 손상된 상태 파일, 누락된 상태 파일 처리

## Notes

- 기능별 역할을 `Quiz`와 `QuizGame` 클래스로 분리했습니다.
- 검증 이미지는 `docs/screenshots/`에 보관합니다.
