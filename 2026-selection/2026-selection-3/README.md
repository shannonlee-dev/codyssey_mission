# 2026 Selection 3

Mini NPU 교육용 시뮬레이터 과제입니다. 실제 NPU 하드웨어를 재현하기보다는, 패턴과 필터의 원소별 곱셈 및 누산 과정을 통해 AI 가속기가 다루는 기본 계산을 설명하는 콘솔 프로그램입니다.

## Structure

```text
2026-selection-3/
├── benchmark_mac.py
├── cpu-gpu-npu-journey.html
├── data.json
├── main.py
└── videos/
```

## Contents

| Path | Summary |
| --- | --- |
| `main.py` | 3x3 패턴 입력, JSON 분석, 성능 측정 실행 |
| `data.json` | 일괄 분석용 패턴 데이터 |
| `benchmark_mac.py` | MAC 연산 벤치마크 보조 스크립트 |
| `cpu-gpu-npu-journey.html` | CPU/GPU/NPU 설명용 시각 자료 |
| `videos/` | 발표 또는 설명용 영상 및 GIF 자료 |

## Run

```bash
cd 2026-selection-3
python3 main.py
```

벤치마크만 확인하려면 다음을 실행합니다.

```bash
python3 benchmark_mac.py
```

## Notes

- 프로그램 내부 라벨은 `Cross`와 `X`로 정규화합니다.
- 성능 수치는 교육용 비교 지표이며 실제 NPU 성능을 직접 모델링하지 않습니다.
