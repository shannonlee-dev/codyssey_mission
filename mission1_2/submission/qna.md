# Q&A (Mission 1-2)

## Q1. 메모리 구조를 이해하고, 메모리 누수가 시스템 전체에 미치는 영향을 설명할 수 있다.

A. 이 프로젝트의 `agent-app-leak`는 힙을 단계적으로 증가시키며, `MemoryGuard`가 `MEMORY_LIMIT`을 넘으면 프로세스를 종료한다. `runtime/evidence/oom/memory-50/app.log`와 `monitor.log`에서 RSS가 20.8MB -> 45.8MB로 증가한 뒤 즉시 종료되는 흐름이 보인다. 한계를 올린 `memory-128`에서도 RSS가 70.8MB -> 95.8MB로 계속 증가하고 결국 150MB에서 종료된다. 이는 누수가 장시간 지속되면 시스템 전체 메모리를 잠식해 다른 프로세스에 압박을 주고, 스왑 사용이나 OOM 등 전반적 성능 저하로 확장될 수 있음을 보여준다.

## Q2. 특정 프로세스의 CPU 과점유가 시스템 지연을 유발하는 원리를 설명할 수 있다.

A. CPU가 특정 프로세스에 과도하게 할당되면 스케줄러가 다른 작업에 충분한 CPU 시간을 배정하지 못해 대기 시간이 늘어난다. 본 프로젝트의 CPU 케이스에서 `CpuWorker`는 로드가 50% 수준까지 증가하면 보호 종료를 수행한다(`runtime/evidence/cpu/cpu-max-100/app.log`). 또 스크린샷에서 동일 PID가 `TIME+ 0:08.88`에서 `%CPU 1.7`, `TIME+ 0:08.94`에서 `%CPU 2.0`으로 상승하는 순간이 확인된다. 이는 작은 상승이라도 연속되면 시스템 응답 지연으로 이어질 수 있음을 보여주는 관제 근거다.

## Q3. 자원 경쟁으로 인해 발생하는 교착상태(Deadlock)의 개념을 이해하고, 프로세스가 멈춘 상태를 시스템 도구로 식별하여 진단할 수 있다.

A. 데드락은 서로 다른 작업자가 각자 보유한 자원을 놓지 않은 채, 상대가 보유한 자원을 기다리는 순환 대기 상태다. `runtime/evidence/deadlock/multi-true/app.log`에서는 Worker-Thread-1이 `Socket_Pool_B`를 기다리고, Worker-Thread-2가 `Shared_Memory_A`를 기다리는 로그가 연속으로 나타난다. `thread_samples.log`에서는 로그 바이트가 고정된 채 `stagnant_count`가 증가하며 PID가 계속 존재한다. 이는 프로세스가 살아 있으나 진행이 멈춘 상태를 시스템 도구와 로그로 동시에 확인한 사례다.

## Q4. 로그와 관제 데이터를 증거로 제시하여 육하원칙에 맞게 장애 상황을 기술하고, GitHub Issue를 통해 동료 개발자와 명확하게 소통할 수 있다.

A. 다음은 본 프로젝트 맥락의 육하원칙 기반 기술 예시다.

- 언제(When): 2026-05-12 12:57:53
- 어디서(Where): `runtime/evidence/cpu/cpu-max-100/app.log`
- 누가(Who): `CpuWorker`
- 무엇을(What): `CPU Threshold Violated` 경고 발생 후 보호 종료
- 왜(Why): CPU 부하가 설정된 한계를 초과
- 어떻게(How): `CPU_MAX_OCCUPY=100` 실행 중 로드가 50.74%까지 상승

이와 같이 증거 경로와 핵심 로그를 함께 제시하면, GitHub Issue에서 재현 조건, 관측 데이터, 결론을 짧고 명확하게 공유할 수 있다.