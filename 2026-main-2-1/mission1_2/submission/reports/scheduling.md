# 스케줄링 보고서 (간략)

## 핵심 요약

- 로그 순서가 A -> B -> C -> A -> B -> C로 반복되어 라운드로빈과 일치.
- 각 스레드가 선점 후 재개되는 패턴이 확인됨.

## 증거 경로

- `runtime/evidence/scheduling/round-robin/agent_app.log`

## 발췌

`round-robin/agent_app.log`:

```text
2026-05-12 12:58:33,166 [INFO] [Thread-A] Task Started. Calculating... (20%)
2026-05-12 12:58:33,267 [INFO] [Thread-A] Preempted. Progress saved at (40%)
2026-05-12 12:58:33,318 [INFO] [Thread-B] Task Started. Calculating... (20%)
2026-05-12 12:58:33,419 [INFO] [Thread-B] Preempted. Progress saved at (40%)
2026-05-12 12:58:33,469 [INFO] [Thread-C] Task Started. Calculating... (20%)
2026-05-12 12:58:33,571 [INFO] [Thread-C] Preempted. Progress saved at (40%)
```

## 결론

- 관찰된 스케줄링은 라운드로빈으로 판단된다.

