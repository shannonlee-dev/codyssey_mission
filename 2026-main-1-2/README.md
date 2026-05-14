# 2026 Main 1-2

2026 메인 1-2 과제 산출물입니다. 제공 애플리케이션 또는 재현용 애플리케이션을 대상으로 OOM, CPU spike, deadlock, scheduling 동작을 관찰하고 증거와 보고서를 정리했습니다.

## 참고 사항

본 미션은 제공 애플리케이션이 주어지지 않은 환경에서 시작했습니다.

따라서 보너스 과제 중 스케줄링 알고리즘 추론 부분은 당시 문제의 예시를 참고해 직접 제작한 재현용 애플리케이션의 로그를 기준으로 수행했습니다. 해당 애플리케이션은 **라운드 로빈** 방식의 작업 로그가 발생하도록 구성되어 있어, ./submission/reports/scheduling.md 는 이 점을 감안하여 확인해주시기 바랍니다. (실제 앱은 FCFS)

프로젝트 후반부에는 제공된 `agent-app-leak` 바이너리를 확보하여 OOM, CPU Spike, Deadlock 관련 로그와 리포트를 생성했습니다. 이로 인해 일부 산출물에는 직접 제작한 앱 기준의 로그와 제공 바이너리 기준의 로그가 함께 포함되어 있습니다.

## Structure

```text
2026-main-1-2/
├── 98_PROCEDURE_MANUAL.md
├── README.md
└── submission/
    ├── agent-app-leak/
    ├── evidence/
    ├── reports/
    ├── screenshots/
    └── tools/
```

## Contents

| Path | Summary |
| --- | --- |
| `submission/reports/` | CPU, OOM, deadlock, scheduling 분석 보고서 |
| `submission/evidence/` | 실험별 stdout, stderr, monitor, process 로그 |
| `submission/screenshots/` | 명령 실행 및 상태 확인 스크린샷 |
| `submission/tools/` | CPU spike 분석과 샘플링 보조 도구 |
| `submission/agent-app-leak/` | 제공 또는 확보된 분석 대상 바이너리 |

## Run

기본 환경값을 확인한 뒤 모니터링 스크립트를 실행합니다.

```bash
cd 2026-main-1-2/submission
cat env-default.sh
./monitor.sh
```

## Notes

- 기존 `mission1_2/` 래퍼 폴더는 제거하고 과제 루트에서 바로 README와 제출물을 확인할 수 있게 정리했습니다.
- 초기 일부 스케줄링 분석은 재현용 애플리케이션 로그를 기준으로 작성되었고, 이후 확보된 `agent-app-leak` 바이너리 기준 증거가 함께 보관되어 있습니다.
