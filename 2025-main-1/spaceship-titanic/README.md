# spaceship-titanic 분석

이 폴더에는 `analysis_transport.py`라는 간단한 분석 스크립트가 있습니다.

기능:
- `train.csv`와 `test.csv`를 읽습니다 (두 파일 모두 이 폴더에 있어야 합니다).
- 두 파일을 병합하고 총 행 수를 출력합니다.
- `Transported`와 관련성이 높은 특성(mutual information, train 기준)을 계산합니다.
- 연령대별(10대~70대) Transported 비율을 그래프로 그려 `transported_by_decade.png`로 저장합니다.

실행 방법:
```
python3 analysis_transport.py
```

필요한 패키지: pandas, matplotlib, seaborn, scikit-learn

생성되는 파일:
- `transported_by_decade.png` — 연령대별 Transported 비율 그래프
