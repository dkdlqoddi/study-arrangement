# 7차시 (2026-10-14) — Cross-Validation 완결(k-fold·LOOCV 지름길·1-SE 규칙·올바른 CV) · Model Selection(subset selection·Cp/AIC/BIC/adjR²·AIC vs BIC 철학) · 축소법 시작(능형회귀·라쏘)

> 변환 생성일 2026-10-25 · [전체 인덱스](../../INDEX.md) · [주제별 찾기](../../TOPICS.md) · [모아보기](../compiled/)

## 이번 차시 키워드

`CV의 목적·검증셋 접근` · `k-fold CV 식` · `LOOCV 지름길 공식(hᵢ), k의 편향–분산` · `CV 곡선, 분류 문제의 CV, 1-SE 규칙` · `올바른 CV vs 틀린 CV(p=5000, n=50)` · `모형 선택 세 방법군, AIC vs BIC 철학` · `best subset·forward·backward` · `Cp·AIC·BIC·adjusted R²` · `자코비안과 변환한 y의 AIC` · `축소의 발상, 능형회귀(λ의 CV 선택)` · `라쏘(ℓ1, 변수 선택)` · `PCR·PLS(교재, 미진행)`

## 시험 포인트 (2026-10-28 중간고사)

올바른 CV vs 틀린 CV(V23 퀴즈, 정답 0.5) · LOOCV 지름길·K의 편향–분산 · AIC vs BIC 철학 · R² 금지·자코비안 함정 · 제약 ⟺ 벌점(라그랑지안) — 문항별 답안 핵심은 [예상 시험 질문](../compiled/exam_predictions.md), 보낼 프롬프트는 [프롬프트 북](../compiled/prompt_book.md), 자기 채점은 [채점표](../compiled/rubric.md).

## 공개 문서 (시험대비 학습자료 요약본)

| 유형 | 문서 | 파트 | 분량(tokens) | 원본 | 비고 |
|---|---|---|---|---|---|
| 시험대비 학습자료(요약본) | 7차시 시험대비 학습자료 (요약본) | [목차](study_guide_summary.md) · [1부](study_guide_summary_part01.md) · [2부](study_guide_summary_part02.md) · [3부](study_guide_summary_part03.md) · [4부](study_guide_summary_part04.md) · [5부](study_guide_summary_part05.md) | 45,112 | `7차시 시험대비 학습자료.pdf` |  |

## 비공개 자료

전체판·강의노트·슬라이드·녹음 받아쓰기·논문과제·코드는 저작권과 개인정보 때문에 공개하지 않습니다 (로컬 `private/` 폴더에 시험대비 학습자료(전체판) 1건, 강의노트 1건, 녹음 받아쓰기 3건).

