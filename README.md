# Codyssey Monorepo

Codyssey 과제 결과물을 모아 관리하는 monorepo입니다.

`codyssey_mission` 레포의 내용을 이 레포로 가져와 하위 디렉터리별로 관리합니다.

## 구조

각 과제는 루트 아래 별도 디렉터리로 관리합니다.

```text
.
├── 2025-main-1/
├── 2025-selection-1/
├── 2025-selection-2/
├── 2025-selection-team/
├── 2026-selection-1/
├── 2026-selection-2/
├── 2026-selection-3/
└── 2026-selection-term/
```

## 문서

- [레포 import 매뉴얼](docs/import-guide.md)

## Import 방식

`https://github.com/shannonlee-dev/codyssey_mission.git` 레포를 `git-filter-repo`로 하위 디렉터리로 이동한 뒤, 이 레포(`https://github.com/shannonlee-dev/codyssey`)의 `main`에 merge합니다.

원본 브랜치는 `import/codyssey_mission-<가져올-경로>/<브랜치명>` 형식의 브랜치로 보존합니다.
