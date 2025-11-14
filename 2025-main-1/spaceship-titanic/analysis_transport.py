#!/usr/bin/env python3
"""Spaceship Titanic 분석 스크립트

기능:
- `train.csv`와 `test.csv`를 읽고 병합
- 전체 행 수를 출력
- `Transported`와 관련성이 높은 특성(mutual information) 계산 (train 기준)
- 연령대(10대~70대)별 Transported 비율을 그래프로 저장
"""
import os
from pathlib import Path
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif

# 터미널 출력을 깔끔하게 만들기 위해 일부 경고를 무시합니다.
warnings.filterwarnings("ignore", category=FutureWarning)
# matplotlib의 글리프(폰트) 관련 경고도 숨깁니다(한글 폰트가 없을 때 발생).
warnings.filterwarnings("ignore", message="Glyph .* missing from font.*")


BASE = Path(__file__).resolve().parent


def read_data():
    """`train.csv`와 `test.csv`를 읽어 DataFrame으로 반환합니다."""
    train_path = BASE / "train.csv"
    test_path = BASE / "test.csv"
    if not train_path.exists() or not test_path.exists():
        raise FileNotFoundError(f"{BASE}에 train.csv 또는 test.csv가 없습니다.")
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test


def merge_data(train, test):
    merged = pd.concat([train, test], axis=0, ignore_index=True, sort=False)
    return merged


def feature_importance_mi(train_df, target_col="Transported", top_n=10):
    """train_df에서 target_col과의 상관성을 mutual information으로 계산해 상위 top_n을 반환합니다.

    단순한 전처리(문자열 컬럼 레이블 인코딩, 숫자 결측값 중앙값 대체)를 수행합니다.
    """
    df = train_df.copy()
    if target_col not in df.columns:
        raise ValueError(f"데이터프레임에 {target_col} 컬럼이 없습니다.")
    y = df[target_col].astype(bool).map({False: 0, True: 1}).astype(int)
    X = df.drop(columns=[target_col])

    # 식별자처럼 보이는 컬럼(passenger로 시작)을 제외
    drop_cols = [c for c in X.columns if c.lower().startswith("passenger")]
    X = X.drop(columns=drop_cols, errors="ignore")

    # 간단한 인코딩: 범주형은 LabelEncoder, 숫자는 중앙값으로 결측치 채움
    X_enc = X.copy()
    discrete_mask = []
    for col in X_enc.columns:
        if X_enc[col].dtype == object or X_enc[col].dtype.name == 'category':
            X_enc[col] = X_enc[col].fillna("<NA>")
            le = LabelEncoder()
            X_enc[col] = le.fit_transform(X_enc[col].astype(str))
            discrete_mask.append(True)
        else:
            X_enc[col] = X_enc[col].fillna(X_enc[col].median())
            discrete_mask.append(False)

    if X_enc.shape[1] == 0:
        return []

    mi = mutual_info_classif(X_enc.values, y.values, discrete_features=np.array(discrete_mask))
    mi_scores = pd.Series(mi, index=X_enc.columns).sort_values(ascending=False)
    return mi_scores.head(top_n)


def plot_transported_by_decade(df, target_col="Transported", output_path=None):
    """연령대(10대~70대)별로 Transported 비율을 막대그래프로 그려 파일로 저장합니다."""
    d = df.copy()
    if target_col not in d.columns:
        raise ValueError(f"플롯을 위한 데이터프레임에 {target_col} 컬럼이 없습니다.")
    # 숫자형 Age 보장
    d = d[pd.notnull(d["Age"])].copy()
    d["Age"] = pd.to_numeric(d["Age"], errors="coerce")
    d = d[pd.notnull(d["Age"])].copy()

    # 10대~70대 레이블 생성
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    labels = ["0대", "10대", "20대", "30대", "40대", "50대", "60대", "70대"]
    d["decade"] = pd.cut(d["Age"], bins=bins, labels=labels, right=False)

    wanted = ["10대", "20대", "30대", "40대", "50대", "60대", "70대"]
    plot_df = d[d["decade"].isin(wanted)].copy()
    plot_df["Transported_bin"] = plot_df[target_col].astype(bool).map({False: 0, True: 1}).astype(int)

    agg = plot_df.groupby("decade")["Transported_bin"].agg(["mean", "count"]).reindex(wanted)

    sns.set(style="whitegrid")
    plt.figure(figsize=(9, 5))
    ax = sns.barplot(x=agg.index, y=agg["mean"].values)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Transported 비율 (0-1)")
    ax.set_xlabel("연령대")
    ax.set_title("연령대별 Transported 비율 (10대~70대)")
    # 막대 위에 비율과 개수 주석 추가
    for i, (mean_val, cnt) in enumerate(zip(agg["mean"].values, agg["count"].values)):
        ax.text(i, mean_val + 0.02, f"{mean_val:.2f}\n(n={int(cnt)})", ha="center")

    plt.tight_layout()
    if output_path is None:
        output_path = BASE / "transported_by_decade.png"
    else:
        output_path = Path(output_path)
    plt.savefig(output_path)
    plt.close()
    return output_path


def main():
    print("데이터 읽는 중...")
    train, test = read_data()
    print(f"train 행 수: {len(train):,}  test 행 수: {len(test):,}")

    merged = merge_data(train, test)
    print(f"병합 후 총 행 수: {len(merged):,}")

    print("\nTransported와의 관련성 계산 (mutual information) 중... (train 기준)")
    try:
        mi = feature_importance_mi(train, target_col="Transported", top_n=15)
        if len(mi) > 0:
            print("상위 mutual information 특성:")
            for feat, score in mi.items():
                print(f"  {feat}: {score:.6f}")
        else:
            print("평가할 특성이 없습니다.")
    except Exception as e:
        print("특성 중요도 계산 실패:", e)

    print("\n연령대(10대~70대)별 Transported 비율 그래프 생성 중...")
    try:
        out = plot_transported_by_decade(train, target_col="Transported")
        print(f"그래프 파일 저장 위치: {out}")
    except Exception as e:
        print("연령대별 그래프 생성 실패:", e)


if __name__ == '__main__':
    main()
