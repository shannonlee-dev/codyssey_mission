# CPU 보고서 (간략)

## 핵심 요약

- `CPU_MAX_OCCUPY=100`에서는 `CpuWorker`가 임계치를 넘겨 보호 종료.
- `CPU_MAX_OCCUPY=10`에서는 10% 도달 후 냉각 진입, 임계치 위반 없음.

## 증거 경로

- `runtime/evidence/cpu/cpu-max-100/app.log`
- `runtime/evidence/cpu/cpu-max-100/ps_top.log`
- `runtime/evidence/cpu/cpu-max-10/app.log`
- `runtime/evidence/cpu/cpu-max-10/ps_top.log`
- 요약: `runtime/blocked.log`

## 발췌

`cpu-max-100/app.log`:

```text
2026-05-12 12:57:50,676 [INFO] [CpuWorker] Current Load: 47.26%
2026-05-12 12:57:53,776 [INFO] [CpuWorker] Current Load: 50.74%
2026-05-12 12:57:53,877 [CRITICAL] [CpuWorker] CPU Threshold Violated! (50.739999999999995%).
```

`cpu-max-10/app.log`:

```text
2026-05-12 12:57:19,062 [INFO] [Scheduler] Registered Tasks: ['Thread-A', 'Thread-B', 'Thread-C']
2026-05-12 12:57:25,347 [INFO] [CpuWorker] Peak reached (10.00%). Starting cooldown...
```

`cpu-max-100/ps_top.log`:

```text
2026-05-12T12:57:28+09:00
	PID USER     STAT %CPU %MEM   RSS COMMAND         COMMAND
31985 maincod+ S     5.3  0.0  1920 agent-app-leak  /home/maincodex/harness/codex-harness/tasks/mission1_2/submission/agent-app-leak/agent-app-leak
```

## 스크린샷 증거 (시간 연관)

- `submission/screenshots/comman_top_before.png`
	- `TIME+ 0:08.88` 시점에 `%CPU 1.7` 확인
- `submission/screenshots/command_top_after.png`
	- `TIME+ 0:08.94` 시점에 `%CPU 2.0`로 급상승
- `submission/screenshots/command_ps.png`
	- 동일 PID에서 `%CPU 1.7` 확인 (ps 스냅샷)

## 결론

- CPU 가드는 설정된 임계치에 따라 정상적으로 보호 종료 또는 냉각 동작을 수행한다.
- 동일 PID 기준으로 `TIME+ 0:08.88 -> 0:08.94` 사이에 `%CPU 1.7 -> 2.0` 상승이 관측된다.

