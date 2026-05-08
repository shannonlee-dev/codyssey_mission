# 레포 import 매뉴얼

`codyssey_mission` 레포를 Codyssey monorepo의 하위 디렉터리로 가져오는 절차입니다.

## 목표

원본 레포의 파일과 히스토리를 유지한 채 Codyssey monorepo의 지정한 하위 경로로 옮깁니다.

```text
codyssey_mission.git
└── <원본 파일>

codyssey/
└── <가져올 경로>/
    └── <원본 파일>
```

원본 브랜치는 다음 형식으로 보존합니다.

```text
main
import/codyssey_mission-<가져올-경로>/<원본 브랜치>
```

원본 `main` 브랜치는 monorepo의 `main`에 merge합니다. 필요하면 보존용 `import/.../main` 브랜치는 push 후 삭제할 수 있습니다.

## 전제

현재 monorepo 로컬 경로:

```bash
~/__dev/monorepo
```

임시 import 작업 경로:

```bash
~/__dev/tmp/mono-imports
```

monorepo의 GitHub 원격 이름:

```bash
origin
```

monorepo의 기본 브랜치:

```bash
main
```

가져올 원본 레포:

```bash
https://github.com/shannonlee-dev/codyssey_mission.git
```

병합 대상 레포:

```bash
https://github.com/shannonlee-dev/codyssey
```

`git-filter-repo`가 설치되어 있어야 합니다.

```bash
git filter-repo --help
```

## 핵심 흐름

```text
1. 원본 레포를 mirror clone 한다.
2. git filter-repo로 모든 파일 경로를 monorepo 하위 경로로 재작성한다.
3. 원본 브랜치들을 import/<이름>/<브랜치> 형태로 가져온다.
4. 원본 main 브랜치를 monorepo main에 merge한다.
5. monorepo main과 import 브랜치들을 GitHub에 push한다.
```

## Import 절차

### 1. 변수 설정

```bash
export SOURCE_REPO=codyssey_mission
export TARGET_PATH=<가져올-경로>
export REMOTE_NAME=$SOURCE_REPO-$(echo "$TARGET_PATH" | tr '/' '-')
export URL=https://github.com/shannonlee-dev/codyssey_mission.git
```

예:

```bash
export SOURCE_REPO=codyssey_mission
export TARGET_PATH=2026-selection-3
export REMOTE_NAME=$SOURCE_REPO-$(echo "$TARGET_PATH" | tr '/' '-')
export URL=https://github.com/shannonlee-dev/codyssey_mission.git
```

### 2. monorepo 상태 확인

```bash
cd ~/__dev/monorepo
git switch main
git status
```

작업 트리가 깨끗해야 합니다.

```text
nothing to commit, working tree clean
```

### 3. 원본 레포 mirror clone

```bash
rm -rf ~/__dev/tmp/mono-imports/$REMOTE_NAME.git
git clone --mirror "$URL" ~/__dev/tmp/mono-imports/$REMOTE_NAME.git
```

### 4. 원본 레포의 파일 경로 재작성

```bash
cd ~/__dev/tmp/mono-imports/$REMOTE_NAME.git

git filter-repo \
  --to-subdirectory-filter "$TARGET_PATH" \
  --tag-rename '':"$REMOTE_NAME-"
```

이 작업 후 원본 레포의 파일들은 히스토리 전체에서 다음 경로 아래로 이동합니다.

```text
2026-selection-3/
```

### 5. monorepo로 가져오기

```bash
cd ~/__dev/monorepo

git remote add "$REMOTE_NAME" ~/__dev/tmp/mono-imports/$REMOTE_NAME.git

git fetch "$REMOTE_NAME" \
  "+refs/heads/*:refs/heads/import/$REMOTE_NAME/*" \
  "+refs/tags/*:refs/tags/*"
```

예상 브랜치:

```text
import/codyssey_mission-2026-selection-3/main
import/codyssey_mission-2026-selection-3/dev
import/codyssey_mission-2026-selection-3/feature-x
```

### 6. 원본 main을 monorepo main에 merge

```bash
git switch main

git merge "import/$REMOTE_NAME/main" \
  --allow-unrelated-histories \
  --no-ff \
  -m "chore: import $TARGET_PATH from $SOURCE_REPO"
```

예상 merge commit 메시지:

```text
chore: import 2026-selection-3 from codyssey_mission
```

### 7. 임시 remote 제거

```bash
git remote remove "$REMOTE_NAME"
```

### 8. GitHub에 push

monorepo `main` push:

```bash
git push origin main
```

보존용 import 브랜치 전체 push:

```bash
git push origin "refs/heads/import/$REMOTE_NAME/*:refs/heads/import/$REMOTE_NAME/*"
```

## 선택 사항: 원격 import main 브랜치 삭제

원본 `main` 브랜치는 이미 monorepo의 `main`에 merge되었으므로, GitHub에서 보존용 `import/.../main` 브랜치는 삭제해도 됩니다.

삭제하지 않아도 문제는 없습니다.

삭제하려면:

```bash
git push origin :refs/heads/import/$REMOTE_NAME/main
```
