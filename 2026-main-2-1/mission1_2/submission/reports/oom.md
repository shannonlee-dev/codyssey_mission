# OOM 보고서 (간략)

## 핵심 요약

- 메모리 워커가 힙을 증가시키며 `MEMORY_LIMIT` 도달 시 MemoryGuard가 종료.
- `MEMORY_LIMIT=128`은 종료를 지연시켜 관측 샘플이 더 많음.

## 증거 경로

- `runtime/evidence/oom/memory-50/app.log`
- `runtime/evidence/oom/memory-50/monitor.log`
- `runtime/evidence/oom/memory-128/app.log`
- `runtime/evidence/oom/memory-128/monitor.log`
- 요약: `runtime/blocked.log`

## 발췌

`memory-50/app.log`:

```text
2026-05-12 12:56:58,470 [CRITICAL] [MemoryGuard] Memory limit exceeded (50MB >= 50MB) / (Recommend Over 256MB)
2026-05-12 12:56:58,470 [CRITICAL] [MemoryGuard] Self-terminating process 31219 to prevent system instability.
```

`memory-128/app.log`:

```text
2026-05-12 12:57:16,699 [CRITICAL] [MemoryGuard] Memory limit exceeded (150MB >= 128MB) / (Recommend Over 256MB)
2026-05-12 12:57:16,699 [CRITICAL] [MemoryGuard] Self-terminating process 31363 to prevent system instability.
```

`memory-50/monitor.log`:

```text
[2026-05-12 12:56:54] PID:31219 CPU:4.4% MEM:0.2% RSS_MB:20.8 DISK_USED:3%
[2026-05-12 12:56:55] PID:31219 CPU:1.5% MEM:0.5% RSS_MB:45.8 DISK_USED:3%
```

`memory-128/monitor.log`:

```text
[2026-05-12 12:57:04] PID:31363 CPU:2.0% MEM:0.8% RSS_MB:70.8 DISK_USED:3%
[2026-05-12 12:57:08] PID:31363 CPU:1.5% MEM:1.2% RSS_MB:95.8 DISK_USED:3%
```

## 결론

- 종료 원인은 MemoryGuard의 설정된 한계 초과이며, 한계 상향은 임시 완화만 제공.

