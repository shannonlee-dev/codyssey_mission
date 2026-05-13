# 데드락 보고서 (간략)

## 핵심 요약

- `MULTI_THREAD_ENABLE=true`에서 두 작업자가 서로의 리소스를 기다리며 정체.
- `MULTI_THREAD_ENABLE=false`에서는 정상 경로로 완료.

## 증거 경로

- `runtime/evidence/deadlock/multi-true/app.log`
- `runtime/evidence/deadlock/multi-true/thread_samples.log`
- `runtime/evidence/deadlock/multi-false/app.log`
- 요약: `runtime/blocked.log`

## 발췌

`multi-true/app.log`:

```text
2026-05-12 12:58:03,891 [INFO] [AgentWorker][Worker-Thread-1] Need resource [Socket_Pool_B] to finish job.
2026-05-12 12:58:03,892 [INFO] [AgentWorker][Worker-Thread-1] WAITING for [Socket_Pool_B]... (Status: BLOCKED)
2026-05-12 12:58:03,892 [INFO] [AgentWorker][Worker-Thread-2] Need resource [Shared_Memory_A] to write logs.
2026-05-12 12:58:03,892 [INFO] [AgentWorker][Worker-Thread-2] WAITING for [Shared_Memory_A]... (Status: BLOCKED)
```

`multi-true/thread_samples.log`:

```text
--- sample 1 pid=32744 app_log_bytes=1517 stagnant_count=0 ---
--- sample 4 pid=32744 app_log_bytes=1517 stagnant_count=3 ---
--- sample 6 pid=32744 app_log_bytes=1517 stagnant_count=5 ---
```

## 결론

- 순환 대기 패턴이 확인되며, 단일 스레드 실행으로 회피 가능.

