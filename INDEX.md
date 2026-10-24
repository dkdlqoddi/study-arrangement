# 전체 문서 인덱스 — 보건학을 위한 기계학습 (2026-2)

> 자동 생성 2026-10-25 (`python3 tools/convert_sources.py --index-only`) · 공개 문서 49개 · 총 425,832 tokens · 파일 하나는 최대 12,000 tokens(ChatGPT 웹에서 한 번에 읽히는 크기) · 공개 범위: 시험대비 학습자료 **요약본**과 **모아보기**만 (전체판·강의노트·슬라이드·받아쓰기·논문과제는 비공개)

> **ChatGPT에는 URL 하나만**: `https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/llms.txt` 를 주면 그 안의 색인을 보고 알맞은 문서를 찾아 읽습니다(README의 질문 템플릿 참고).

## 0. 모아보기 (학기 전체를 한 파일로)

| 문서 | 내용 | 파트 |
|---|---|---|
| **전 차시 강의 개요 모음** | 각 차시 학습자료의 '강의 개요' 절만 모았습니다. 학기 흐름을 한눈에 볼 때. | [목차](docs/compiled/overviews.md) · [1부](docs/compiled/overviews_part01.md) · [2부](docs/compiled/overviews_part02.md) |
| **핵심 개념 한 장 요약표 모음** | 질문/한 줄 답/출처 형식의 요약표. 시험 직전 복습용. | [목차](docs/compiled/summary_tables.md) · [1부](docs/compiled/summary_tables_part01.md) · [2부](docs/compiled/summary_tables_part02.md) · [3부](docs/compiled/summary_tables_part03.md) |
| **용어 정리 모음 (학기 용어집)** | 각 차시의 용어 정리 절을 모은 학기 용어집. | [목차](docs/compiled/glossary.md) · [1부](docs/compiled/glossary_part01.md) · [2부](docs/compiled/glossary_part02.md) |
| **교수님이 강조한 포인트 모음** | 녹음·강의노트에서 교수님이 반복·강조한 내용(시험 관련 발언 포함). | [목차](docs/compiled/key_points.md) · [1부](docs/compiled/key_points_part01.md) · [2부](docs/compiled/key_points_part02.md) · [3부](docs/compiled/key_points_part03.md) · [4부](docs/compiled/key_points_part04.md) · [5부](docs/compiled/key_points_part05.md) |
| **예상 시험 문제와 모범 답안 모음** | 객관식·단답·서술형 예상문제와 답. 근거 출처 표시 [노트]/[녹음]/[교재]/[추가]. | [목차](docs/compiled/exam_questions.md) · [1부](docs/compiled/exam_questions_part01.md) · [2부](docs/compiled/exam_questions_part02.md) · [3부](docs/compiled/exam_questions_part03.md) · [4부](docs/compiled/exam_questions_part04.md) · [5부](docs/compiled/exam_questions_part05.md) · [6부](docs/compiled/exam_questions_part06.md) · [7부](docs/compiled/exam_questions_part07.md) |
| **셀프 체크리스트 모음** | ☐ 항목으로 된 자가 점검표. | [목차](docs/compiled/checklists.md) · [1부](docs/compiled/checklists_part01.md) · [2부](docs/compiled/checklists_part02.md) |
| **핵심 수식 정리 (LaTeX)** | 수업에서 다룬 핵심 수식을 LaTeX로 정리하고 어느 차시 요약본 절에 나오는지 표시. AI 정리본(교수님 말씀 아님). | [formulas.md](docs/compiled/formulas.md) |

## 1. 주차별 요약본

| 차시 | 날짜 | 주제 | 요약본 | tokens |
|---|---|---|---|---|
| [1차시](docs/week01_20260902/README.md) | 2026-09-02 | 과목 소개 · Chap1 Introduction · Chap2 Part I (Statistical Learning) | [요약본](docs/week01_20260902/study_guide_summary.md) | 10,278 |
| [2차시](docs/week02_20260909/README.md) | 2026-09-09 | Chap2 Part I 복습(f 추정, parametric/non-parametric, KNN·차원의 저주) · Chap2 Part II(MSE, Bias-Variance, Bayes classifier) · Efron 논문 발표 | [3부](docs/week02_20260909/study_guide_summary.md) | 23,934 |
| [3차시](docs/week03_20260916/README.md) | 2026-09-16 | Chap2 Part II 마무리 · Double descent 발표 · Chap3 Linear Regression(두 관점·likelihood·추론·변수선택·KNN 비교) · 회귀→경사하강→신경망 · Chap4 분류 시작(로지스틱, MLE·cross-entropy) | [2부](docs/week03_20260916/study_guide_summary.md) | 16,373 |
| [4차시](docs/week04_20260923/README.md) | 2026-09-23 | 로지스틱 회귀 심화(우도·경사법·Newton–Raphson·odds ratio·confounding·환자-대조군) · 다항 로지스틱 · 판별분석의 출발점 · TRIPOD/PROBAST 발표 | [3부](docs/week04_20260923/study_guide_summary.md) | 23,462 |
| [5차시](docs/week05_20260930/README.md) | 2026-09-30 | 판별분석(LDA, p=1 → p>1) · 다변량 정규분포 · Naive Bayes·Laplace 평활 · 이진 분류기 성능(정확도 함정·임계값·민감도·특이도·ROC·AUC) | [3부](docs/week05_20260930/study_guide_summary.md) | 23,025 |
| [6차시](docs/week06_20261007/README.md) | 2026-10-07 | 분류기 성능 심화(c-통계량=AUC 증명·discrimination vs calibration·PPV/NPV) · Naive Bayes 재정리 · Bootstrap(원리·CI·회귀·OOB) · Cross-Validation 시작(검증셋·k-fold·LOOCV) | [3부](docs/week06_20261007/study_guide_summary.md) | 31,487 |
| [7차시](docs/week07_20261014/README.md) | 2026-10-14 | Cross-Validation 완결(k-fold·LOOCV 지름길·1-SE 규칙·올바른 CV) · Model Selection(subset selection·Cp/AIC/BIC/adjR²·AIC vs BIC 철학) · 축소법 시작(능형회귀·라쏘) | [5부](docs/week07_20261014/study_guide_summary.md) | 45,112 |
| [8차시](docs/week08_20261022/README.md) | 2026-10-21 | AIC·BIC 유도(KL 발산·Laplace 근사) · 능형회귀·라쏘 심화(해 경로·표준화·sparse·oracle·soft thresholding) · elastic net·bridge·fused lasso · LLM으로 능형·라쏘 돌릴 때 시험 주의 (Ch7 자료 배포) | [7부](docs/week08_20261022/study_guide_summary.md) | 62,694 |

## 2. 주차별 상세 (공개 파일)

### 1차시 (2026-09-02) — 과목 소개 · Chap1 Introduction · Chap2 Part I (Statistical Learning)

키워드: 통계학 vs 기계학습(Two cultures) · supervised/unsupervised/reinforcement · f 추정, Prediction vs Inference · 손실함수와 최적 예측자 E[Y|X] · Parametric vs Non-parametric · 차원의 저주 · 유연성-해석력 trade-off · 수업 운영(중간·기말, 팀 프로젝트, AI 도구 사용 보고)  
주차 인덱스: [docs/week01_20260902/README.md](docs/week01_20260902/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 1차시 시험대비 학습자료 (요약본) | [study_guide_summary.md](docs/week01_20260902/study_guide_summary.md) | 10,278 |

### 2차시 (2026-09-09) — Chap2 Part I 복습(f 추정, parametric/non-parametric, KNN·차원의 저주) · Chap2 Part II(MSE, Bias-Variance, Bayes classifier) · Efron 논문 발표

키워드: f를 왜·어떻게 추정하나 · parametric vs non-parametric · KNN과 차원의 저주 · 예측 정확도 vs 해석력 · MSE, training vs test error · Bias-Variance trade-off · 0-1 loss, Bayes classifier, KNN 분류 · Efron(2020) Prediction·Estimation·Attribution 발표 · Shmueli(2010) To Explain or to Predict? 동료 발표  
주차 인덱스: [docs/week02_20260909/README.md](docs/week02_20260909/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 2차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week02_20260909/study_guide_summary_part01.md) | 10,935 |
| 2차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week02_20260909/study_guide_summary_part02.md) | 11,271 |
| 2차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week02_20260909/study_guide_summary_part03.md) | 1,728 |

### 3차시 (2026-09-16) — Chap2 Part II 마무리 · Double descent 발표 · Chap3 Linear Regression(두 관점·likelihood·추론·변수선택·KNN 비교) · 회귀→경사하강→신경망 · Chap4 분류 시작(로지스틱, MLE·cross-entropy)

키워드: 모델 정확도 평가 복습 · Double descent(Belkin 2019) · 선형회귀의 두 관점 · likelihood · 추론·변수선택·R²·KNN 비교 · 제곱오차 → 경사하강 → 신경망(One Idea, Many Models) · 분류 문제의 정의와 risk · 선형회귀 vs 로지스틱 회귀(link) · MLE → cross-entropy, 0-1 loss와 surrogate · 다변량 정규분포 보충 덱  
주차 인덱스: [docs/week03_20260916/README.md](docs/week03_20260916/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 3차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week03_20260916/study_guide_summary_part01.md) | 10,344 |
| 3차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week03_20260916/study_guide_summary_part02.md) | 6,029 |

### 4차시 (2026-09-23) — 로지스틱 회귀 심화(우도·경사법·Newton–Raphson·odds ratio·confounding·환자-대조군) · 다항 로지스틱 · 판별분석의 출발점 · TRIPOD/PROBAST 발표

키워드: 로지스틱 회귀 모형과 링크 함수 · 0-1 손실 → 우도 → −log 우도 → 경사법 · 표준오차·z·p-value, Newton–Raphson · odds ratio, confounding · 유병률 vs 환자 비율, 코호트 vs 환자-대조군 · 환자-대조군 로지스틱 회귀(선택지표 S) · 다항 로지스틱(baseline category logit) · 판별분석의 출발점(Bayes 정리) · complete separation · TRIPOD·PROBAST 논문 발표  
주차 인덱스: [docs/week04_20260923/README.md](docs/week04_20260923/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 4차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week04_20260923/study_guide_summary_part01.md) | 10,501 |
| 4차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week04_20260923/study_guide_summary_part02.md) | 11,243 |
| 4차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week04_20260923/study_guide_summary_part03.md) | 1,718 |

### 5차시 (2026-09-30) — 판별분석(LDA, p=1 → p>1) · 다변량 정규분포 · Naive Bayes·Laplace 평활 · 이진 분류기 성능(정확도 함정·임계값·민감도·특이도·ROC·AUC)

키워드: 판별분석: p(Y|X) ⇕ p(X|Y) · LDA p=1 판별점수·모수 추정 · p>1 다변량 정규, GEE·mixed effect 언급 · Multivariate Gaussian(밀도식, Σ, 기하) · naive Bayes, Laplace 평활 · K=3 분류, Fisher 붓꽃 · 정확도의 함정, 오류 비용, 임계값 · 민감도·특이도, ROC, AUC  
주차 인덱스: [docs/week05_20260930/README.md](docs/week05_20260930/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 5차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week05_20260930/study_guide_summary_part01.md) | 11,005 |
| 5차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week05_20260930/study_guide_summary_part02.md) | 9,968 |
| 5차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week05_20260930/study_guide_summary_part03.md) | 2,052 |

### 6차시 (2026-10-07) — 분류기 성능 심화(c-통계량=AUC 증명·discrimination vs calibration·PPV/NPV) · Naive Bayes 재정리 · Bootstrap(원리·CI·회귀·OOB) · Cross-Validation 시작(검증셋·k-fold·LOOCV)

키워드: ROC·AUC 복습 · c-통계량, AUC = c-통계량 증명 · discrimination vs calibration · AUC의 한계 · 민감도·특이도 vs PPV·NPV(유병률) · 학습 손실 vs 평가지표 · naive Bayes 재정리 · 부트스트랩 원리·알고리즘·신뢰구간 · 회귀에서의 부트스트랩, (1−1/n)ⁿ, OOB · 교차검증 대원칙, 검증셋, k-fold, LOOCV  
주차 인덱스: [docs/week06_20261007/README.md](docs/week06_20261007/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 6차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week06_20261007/study_guide_summary_part01.md) | 9,867 |
| 6차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week06_20261007/study_guide_summary_part02.md) | 11,434 |
| 6차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week06_20261007/study_guide_summary_part03.md) | 10,186 |

### 7차시 (2026-10-14) — Cross-Validation 완결(k-fold·LOOCV 지름길·1-SE 규칙·올바른 CV) · Model Selection(subset selection·Cp/AIC/BIC/adjR²·AIC vs BIC 철학) · 축소법 시작(능형회귀·라쏘)

키워드: CV의 목적·검증셋 접근 · k-fold CV 식 · LOOCV 지름길 공식(hᵢ), k의 편향–분산 · CV 곡선, 분류 문제의 CV, 1-SE 규칙 · 올바른 CV vs 틀린 CV(p=5000, n=50) · 모형 선택 세 방법군, AIC vs BIC 철학 · best subset·forward·backward · Cp·AIC·BIC·adjusted R² · 자코비안과 변환한 y의 AIC · 축소의 발상, 능형회귀(λ의 CV 선택) · 라쏘(ℓ1, 변수 선택) · PCR·PLS(교재, 미진행)  
주차 인덱스: [docs/week07_20261014/README.md](docs/week07_20261014/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 7차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week07_20261014/study_guide_summary_part01.md) | 9,502 |
| 7차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week07_20261014/study_guide_summary_part02.md) | 9,773 |
| 7차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week07_20261014/study_guide_summary_part03.md) | 9,915 |
| 7차시 시험대비 학습자료 (요약본) | [study_guide_summary_part04.md](docs/week07_20261014/study_guide_summary_part04.md) | 6,346 |
| 7차시 시험대비 학습자료 (요약본) | [study_guide_summary_part05.md](docs/week07_20261014/study_guide_summary_part05.md) | 9,576 |

### 8차시 (2026-10-21) — AIC·BIC 유도(KL 발산·Laplace 근사) · 능형회귀·라쏘 심화(해 경로·표준화·sparse·oracle·soft thresholding) · elastic net·bridge·fused lasso · LLM으로 능형·라쏘 돌릴 때 시험 주의 (Ch7 자료 배포)

키워드: AIC·BIC 유도: KL 발산, tr(J⁻¹I) → p, Laplace 근사 → p·log n · 제약 형태 ⟺ 벌점 형태(원과 마름모) · 능형회귀 해·해 경로·표준화 · 1차원 능형 β̂ = y/(1+λ) · 라쏘: sparse vs dense, oracle property · elastic net, 튜닝 파라미터 2개 · bridge 벌점 · soft thresholding · grouping effect, generalized·fused lasso · 보건 응용과 LLM 시대의 메시지 · 시험장 점검표(AI로 능형·라쏘) · Chap7 Beyond Linearity 슬라이드(배포, 다음 차시)  
주차 인덱스: [docs/week08_20261022/README.md](docs/week08_20261022/README.md)

| 문서 | 파일 | tokens |
|---|---|---|
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part01.md](docs/week08_20261022/study_guide_summary_part01.md) | 10,192 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part02.md](docs/week08_20261022/study_guide_summary_part02.md) | 10,498 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part03.md](docs/week08_20261022/study_guide_summary_part03.md) | 10,503 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part04.md](docs/week08_20261022/study_guide_summary_part04.md) | 8,831 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part05.md](docs/week08_20261022/study_guide_summary_part05.md) | 8,336 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part06.md](docs/week08_20261022/study_guide_summary_part06.md) | 8,269 |
| 8차시 시험대비 학습자료 (요약본) | [study_guide_summary_part07.md](docs/week08_20261022/study_guide_summary_part07.md) | 6,065 |

## 3. ChatGPT에 붙여 넣을 raw URL 규칙

`https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/` + 위 표의 파일 경로. 예:

```
https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/docs/compiled/overviews_part01.md
```

