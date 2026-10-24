# 6차시 (2026-10-07) — 분류기 성능 심화(c-통계량=AUC 증명·discrimination vs calibration·PPV/NPV) · Naive Bayes 재정리 · Bootstrap(원리·CI·회귀·OOB) · Cross-Validation 시작(검증셋·k-fold·LOOCV)

> 변환 생성일 2026-10-25 · [전체 인덱스](../../INDEX.md) · [주제별 찾기](../../TOPICS.md) · [모아보기](../compiled/)

## 이번 차시 키워드

`ROC·AUC 복습` · `c-통계량, AUC = c-통계량 증명` · `discrimination vs calibration` · `AUC의 한계` · `민감도·특이도 vs PPV·NPV(유병률)` · `학습 손실 vs 평가지표` · `naive Bayes 재정리` · `부트스트랩 원리·알고리즘·신뢰구간` · `회귀에서의 부트스트랩, (1−1/n)ⁿ, OOB` · `교차검증 대원칙, 검증셋, k-fold, LOOCV`

## 시험 포인트 (2026-10-28 중간고사)

AUC = c-통계량 증명(구분구적법) · 판별 vs 보정, AUC 한계(증분) · PPV와 유병률 계산 · 부트스트랩 원리·백분위 구간 · (1−1/n)ⁿ → 예측오차는 CV — 문항별 답안 핵심은 [예상 시험 질문](../compiled/exam_predictions.md), 보낼 프롬프트는 [프롬프트 북](../compiled/prompt_book.md), 자기 채점은 [채점표](../compiled/rubric.md).

## 공개 문서 (시험대비 학습자료 요약본)

| 유형 | 문서 | 파트 | 분량(tokens) | 원본 | 비고 |
|---|---|---|---|---|---|
| 시험대비 학습자료(요약본) | 6차시 시험대비 학습자료 (요약본) | [목차](study_guide_summary.md) · [1부](study_guide_summary_part01.md) · [2부](study_guide_summary_part02.md) · [3부](study_guide_summary_part03.md) | 31,487 | `6차시 시험대비 학습자료.pdf` |  |

## 비공개 자료

전체판·강의노트·슬라이드·녹음 받아쓰기·논문과제·코드는 저작권과 개인정보 때문에 공개하지 않습니다 (로컬 `private/` 폴더에 시험대비 학습자료(전체판) 1건, 강의노트 1건, 슬라이드 3건, 녹음 받아쓰기 3건).

