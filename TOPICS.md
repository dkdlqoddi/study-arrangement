# 주제별 찾기 — 키워드 → 어느 차시, 어느 문서

> 각 차시 「시험대비 학습자료(요약본)」의 절 번호(§)를 기준으로 정리했습니다. 2차시 요약본은 전체판에서 새로 작성한 것(2026-10-25)입니다. 전체판·슬라이드·코드 등 **(비공개)** 표시 자료는 GitHub에 없고 로컬 `private/` 폴더에만 있습니다. ChatGPT에 물을 때는 [llms.txt](llms.txt) URL 하나만 주면 됩니다. 2026-10-28 중간고사 대비 문서(예상 질문·프롬프트 북·채점표)는 8절 첫 세 행에 있습니다. 학기 전체를 한 파일로 보려면 [docs/compiled/](docs/compiled/)(용어집·예상문제·강조 포인트·체크리스트·요약표)를 쓰세요. 작성 2026-10-24.

표기: `요약본 §2.3` = 해당 주차 `study_guide_summary.md`의 2.3절 · `전체판` = `study_guide_full/` · `S0xx/M0x/B0x/T0x/V0x/AB0x/OP0x` = 전체판의 슬라이드 번호(S=Ch.4, M=Ch.6 ModelSelection, B=Binary classifier, T=Bootstrap, V=CV, AB=AIC/BIC, OP=Other penalties)

## 1. 통계적 학습의 기초 (ISLR Ch.1–2)

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 통계학 vs 기계학습, Two cultures, Breiman | 1 | [요약본 §2.1](docs/week01_20260902/study_guide_summary.md) | Intro 슬라이드 (비공개) |
| 보건학에서 ML이 주목받는 이유, 공정성·프라이버시 | 1 | [요약본 §2.2](docs/week01_20260902/study_guide_summary.md) | |
| supervised / unsupervised / reinforcement learning | 1 | [요약본 §2.3](docs/week01_20260902/study_guide_summary.md) | Chap1 슬라이드 (비공개) |
| 통계적 학습 = f 추정, Prediction vs Inference | 1 · 2 | [1차시 요약본 §2.4–2.5](docs/week01_20260902/study_guide_summary.md) · [2차시 요약본 §2.1](docs/week02_20260909/study_guide_summary.md) | Chap2 Part1 슬라이드 (비공개) |
| 손실함수, 최적 예측자 E[Y\|X] | 1 | [요약본 §2.6](docs/week01_20260902/study_guide_summary.md) | |
| Parametric vs Non-parametric | 1 · 2 | [1차시 요약본 §2.7](docs/week01_20260902/study_guide_summary.md) · [2차시 요약본 §2.2](docs/week02_20260909/study_guide_summary.md) | |
| KNN 회귀, 차원의 저주(curse of dimensionality) | 1 · 2 | [1차시 요약본 §2.8](docs/week01_20260902/study_guide_summary.md) · [2차시 요약본 §2.3](docs/week02_20260909/study_guide_summary.md) | R: KNN 회귀 데모 (비공개) |
| 예측 정확도 vs 해석력 trade-off | 1 · 2 | [1차시 요약본 §2.9](docs/week01_20260902/study_guide_summary.md) · [2차시 요약본 §2.4](docs/week02_20260909/study_guide_summary.md) | |
| MSE, training vs test error, overfitting | 2 · 3 | [2차시 요약본 §2.5](docs/week02_20260909/study_guide_summary.md) · [3차시 요약본 §2.1](docs/week03_20260916/study_guide_summary.md) | Chap2 Part2 슬라이드 (비공개) |
| Bias–Variance trade-off, 분해식 | 2 · 3 | [2차시 요약본 §2.6](docs/week02_20260909/study_guide_summary.md) · [3차시 요약본 §2.1](docs/week03_20260916/study_guide_summary.md) | |
| 0-1 loss, Bayes classifier, Bayes error, KNN 분류 | 2 | [2차시 요약본 §2.7](docs/week02_20260909/study_guide_summary.md) | |
| Double descent (Belkin et al. 2019) | 3 | [요약본 §2.2](docs/week03_20260916/study_guide_summary.md) | 참고 링크 (비공개) |

## 2. 선형회귀 (ISLR Ch.3)

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 선형회귀를 보는 두 관점(최소제곱 vs 확률모형) | 3 | [요약본 §2.3](docs/week03_20260916/study_guide_summary.md) | Chap3 슬라이드 (비공개) |
| Likelihood — 통계학의 핵심 엔진 | 3 | [요약본 §2.4](docs/week03_20260916/study_guide_summary.md) | |
| 회귀 추론, 변수선택, R², KNN과 비교 | 3 | [요약본 §2.5](docs/week03_20260916/study_guide_summary.md) | |
| One Idea, Many Models — 제곱오차 → 경사하강 → 신경망 | 3 | [요약본 §2.6](docs/week03_20260916/study_guide_summary.md) | regression_to_neural_nets (비공개) · logistic_to_neural_nets (비공개) |

## 3. 분류: 로지스틱 회귀와 판별분석 (ISLR Ch.4)

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 분류 문제의 정의, risk | 3 | [요약본 §2.7](docs/week03_20260916/study_guide_summary.md) | Chap4 슬라이드 (비공개) |
| 선형회귀 vs 로지스틱 회귀, link 함수, 해석 | 3 · 4 | [3차시 요약본 §2.8](docs/week03_20260916/study_guide_summary.md) · [4차시 요약본 §2.1](docs/week04_20260923/study_guide_summary.md) | |
| MLE → cross-entropy, 0-1 loss와 surrogate loss | 3 · 4 | [3차시 요약본 §2.9](docs/week03_20260916/study_guide_summary.md) · [4차시 요약본 §2.2](docs/week04_20260923/study_guide_summary.md) | |
| 표준오차·z·p-value, Newton–Raphson | 4 | [요약본 §2.3](docs/week04_20260923/study_guide_summary.md) | |
| 예측, odds ratio, confounding | 4 | [요약본 §2.4](docs/week04_20260923/study_guide_summary.md) | |
| 유병률 vs 환자 비율, 코호트 vs 환자-대조군(남아공 심장병 자료) | 4 | [요약본 §2.5](docs/week04_20260923/study_guide_summary.md) | |
| 환자-대조군 로지스틱 회귀의 정당화(선택지표 S) | 4 | [요약본 §2.6](docs/week04_20260923/study_guide_summary.md) | |
| 다항 로지스틱, baseline category logit | 4 | [요약본 §2.7](docs/week04_20260923/study_guide_summary.md) | |
| 판별분석의 출발점 — Bayes 정리로 뒤집기, complete separation | 4 · 5 | [4차시 요약본 §2.8–2.9](docs/week04_20260923/study_guide_summary.md) · [5차시 요약본 §2.1](docs/week05_20260930/study_guide_summary.md) | |
| LDA (p=1): 정규밀도 대입, 판별점수, 모수 추정 | 5 | [요약본 §2.2](docs/week05_20260930/study_guide_summary.md) | |
| LDA (p>1), 왜 다변량 정규인가, GEE·mixed effect 언급 | 5 | [요약본 §2.3](docs/week05_20260930/study_guide_summary.md) | |
| 다변량 정규분포(밀도식, Σ, 기하, 성질) | 5 | [요약본 §2.4](docs/week05_20260930/study_guide_summary.md) | Multivariate Gaussian 슬라이드 (비공개) |
| Naive Bayes, Laplace 평활 | 5 · 6 | [5차시 요약본 §2.5](docs/week05_20260930/study_guide_summary.md) · [6차시 요약본 §2.8](docs/week06_20261007/study_guide_summary.md) | R: naive Bayes (비공개) |
| K=3 분류, Fisher의 붓꽃, 확률로의 변환 | 5 | [요약본 §2.6](docs/week05_20260930/study_guide_summary.md) | |
| QDA, KNN 분류 등 Ch.4 후반(교재 요약) | 3 · 4 · 5 | [3차시 §2.10](docs/week03_20260916/study_guide_summary.md) · [4차시 §2.10](docs/week04_20260923/study_guide_summary.md) · [5차시 §2.9](docs/week05_20260930/study_guide_summary.md) | |

## 4. 분류기 성능 평가

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 정확도의 함정, 오류 비용, 임계값 | 5 | [요약본 §2.7](docs/week05_20260930/study_guide_summary.md) | Binary Classifier Performance 슬라이드 (비공개) |
| 민감도·특이도, ROC 곡선, AUC, 임계값 선택 | 5 · 6 | [5차시 요약본 §2.8](docs/week05_20260930/study_guide_summary.md) · [6차시 요약본 §2.1](docs/week06_20261007/study_guide_summary.md) | |
| c-통계량(쌍의 확률, 동점 ½, 순위 불변), AUC = c-통계량 증명 | 6 | [요약본 §2.2–2.3](docs/week06_20261007/study_guide_summary.md) | |
| Discrimination vs Calibration | 6 | [요약본 §2.4](docs/week06_20261007/study_guide_summary.md) | |
| AUC의 네 가지 한계 | 6 | [요약본 §2.5](docs/week06_20261007/study_guide_summary.md) | |
| 민감도·특이도 vs PPV·NPV — 유병률의 영향 | 6 | [요약본 §2.6](docs/week06_20261007/study_guide_summary.md) | |
| 학습 손실 vs 평가지표, 보고 세트 | 6 | [요약본 §2.7](docs/week06_20261007/study_guide_summary.md) | |
| TRIPOD, PROBAST (예측모형 보고·편향 평가) | 4 | [요약본 §2.11](docs/week04_20260923/study_guide_summary.md) | |

## 5. Resampling: Bootstrap과 Cross-Validation (ISLR Ch.5)

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 부트스트랩의 원리 — F 대신 F̂ | 6 | [요약본 §2.9](docs/week06_20261007/study_guide_summary.md) | bootstrap 슬라이드 (비공개) |
| 부트스트랩 알고리즘, B=1000, 두 가지 신뢰구간 | 6 | [요약본 §2.10](docs/week06_20261007/study_guide_summary.md) | |
| 회귀에서의 부트스트랩, resampling unit | 6 | [요약본 §2.11](docs/week06_20261007/study_guide_summary.md) | |
| 부트스트랩으로 예측오차? (1−1/n)ⁿ, OOB | 6 | [요약본 §2.12](docs/week06_20261007/study_guide_summary.md) | |
| 교차검증 대원칙, 검증셋 접근 | 6 · 7 | [6차시 요약본 §2.13](docs/week06_20261007/study_guide_summary.md) · [7차시 요약본 §2.1](docs/week07_20261014/study_guide_summary.md) | CrossValidation 슬라이드 (비공개) |
| k-fold CV, CV₍ₖ₎ 식, 10-fold의 안정성 | 6 · 7 | [6차시 §2.14](docs/week06_20261007/study_guide_summary.md) · [7차시 §2.2](docs/week07_20261014/study_guide_summary.md) | |
| LOOCV, 지름길 공식(hᵢ), 항등식과 AIC, k의 편향–분산 | 6 · 7 | [6차시 §2.14](docs/week06_20261007/study_guide_summary.md) · [7차시 §2.3](docs/week07_20261014/study_guide_summary.md) | |
| CV 곡선 vs 참 검정곡선, 분류 문제의 CV, 1-SE 규칙 | 7 | [요약본 §2.4](docs/week07_20261014/study_guide_summary.md) | |
| 올바른 CV vs 틀린 CV (p=5000, n=50, 변수 선택을 CV 밖에서 하면) | 7 | [요약본 §2.5](docs/week07_20261014/study_guide_summary.md) | |

## 6. 모형 선택과 정규화 (ISLR Ch.6)

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| 왜 모형 선택인가 — 세 방법군, AIC vs BIC의 철학 | 7 | [요약본 §2.6](docs/week07_20261014/study_guide_summary.md) | ModelSelection 슬라이드 (비공개) |
| Best subset, forward/backward stepwise | 7 | [요약본 §2.7](docs/week07_20261014/study_guide_summary.md) | |
| RSS·R²로 고르면 안 되는 이유 | 7 | [요약본 §2.8](docs/week07_20261014/study_guide_summary.md) | |
| Cp, AIC, BIC, adjusted R² — 식, d, 2 vs log n | 7 · 8 | [7차시 §2.9](docs/week07_20261014/study_guide_summary.md) · [8차시 §2.1](docs/week08_20261022/study_guide_summary.md) | |
| 변환한 y의 AIC와 자코비안, Credit 자료의 CV | 7 | [요약본 §2.10](docs/week07_20261014/study_guide_summary.md) | |
| AIC 유도 — KL 발산, tr(J⁻¹I) → p | 8 | [요약본 §2.2–2.3](docs/week08_20261022/study_guide_summary.md) | AIC/BIC 유도 슬라이드 (비공개) |
| BIC 유도 — 사후 모형확률의 Laplace 근사 → p·log n | 8 | [요약본 §2.4](docs/week08_20261022/study_guide_summary.md) | |
| 축소(shrinkage)의 발상 — 편향을 내주고 분산을 줄인다; 제약 ⟺ 벌점(라그랑지안) | 7 · 8 | [7차시 §2.11–2.12](docs/week07_20261014/study_guide_summary.md) · [8차시 §2.5](docs/week08_20261022/study_guide_summary.md) | |
| 능형회귀(ridge) — 해, 해 경로, 척도와 표준화, λ의 CV 선택 | 7 · 8 | [7차시 §2.12](docs/week07_20261014/study_guide_summary.md) · [8차시 §2.6](docs/week08_20261022/study_guide_summary.md) | |
| 1차원 능형 β̂ = y/(1+λ) — 편향↑ 분산↓ | 8 | [요약본 §2.8](docs/week08_20261022/study_guide_summary.md) | |
| 라쏘(lasso) — ℓ1 벌점, 정확한 0, sparse vs dense, oracle property | 7 · 8 | [7차시 §2.13](docs/week07_20261014/study_guide_summary.md) · [8차시 §2.9](docs/week08_20261022/study_guide_summary.md) | |
| 1차원 라쏘의 해 — soft thresholding | 8 | [요약본 §2.12](docs/week08_20261022/study_guide_summary.md) | 기타 벌점 함수 슬라이드 (비공개) |
| Elastic net, 튜닝 파라미터 2개, grouping effect | 8 | [요약본 §2.10, §2.13](docs/week08_20261022/study_guide_summary.md) | |
| Bridge 벌점, generalized·fused lasso | 8 | [요약본 §2.11, §2.13](docs/week08_20261022/study_guide_summary.md) | |
| 차원축소 PCR·PLS (교재 기준, 미진행) | 7 · 8 | [7차시 §2.14](docs/week07_20261014/study_guide_summary.md) · [8차시 §2.15](docs/week08_20261022/study_guide_summary.md) | |
| Moving Beyond Linearity (Ch.7) — 배포만 됨 | 8 | — | Ch7 슬라이드 (비공개) · 보충 증명 (비공개) |

## 7. 논문 읽기·발표

| 키워드 | 차시 | 어디에 | 함께 볼 것 |
|---|---|---|---|
| Efron (2020) Prediction, Estimation, and Attribution | 1 · 2 | 2차시 논문읽기과제 (비공개) — 발표 슬라이드(최종, 발표자 노트), 발제문, 3쪽 요약, 완전요약본, 입문자용 해설 | DOI (비공개) |
| Shmueli (2010) To Explain or to Predict? | 1 · 2 | [1차시 요약본 §1](docs/week01_20260902/study_guide_summary.md)(읽기 과제 안내) · 동료 발표자료 (비공개) | |
| Belkin et al. (2019) Double descent | 3 | [요약본 §2.2](docs/week03_20260916/study_guide_summary.md) | |
| TRIPOD / PROBAST 발표 | 4 | [요약본 §2.11](docs/week04_20260923/study_guide_summary.md) | |

## 8. 수업 운영·시험·AI 도구

| 키워드 | 차시 | 어디에 |
|---|---|---|
| **중간고사(2026-10-28) 예상 질문 Top 42 — 답안 핵심·근거 §·프롬프트 번호** | 1~8 | [docs/compiled/exam_predictions.md](docs/compiled/exam_predictions.md) |
| **시험용 프롬프트 북 — P0 세션 설정, 유형별 템플릿, 능형·라쏘 CV 코드, AI 사용 리포트 템플릿** | 전체 | [docs/compiled/prompt_book.md](docs/compiled/prompt_book.md) |
| **채점표·모의고사 — 10점 기준, AI 답 검증, 모의고사 A/B, 채점 프롬프트** | 전체 | [docs/compiled/rubric.md](docs/compiled/rubric.md) |
| 시험 공지 원문(일시·장소·AI 사용 규칙·AI 사용 리포트), AI 사용 경고 | 8 | [요약본 §1 시험·과제 공지, §5-0](docs/week08_20261022/study_guide_summary.md) |
| 평가 방식(중간·기말·프로젝트), AI 도구 사용 보고 원칙, 필요한 수학 | 1 | [요약본 §1 수업 운영 메모](docs/week01_20260902/study_guide_summary.md) · Intro 슬라이드(강의계획서) (비공개) |
| 수업 운영·평가 관련 발언(3차시) | 3 | [요약본 §4.1](docs/week03_20260916/study_guide_summary.md) |
| AI(LLM)로 능형·라쏘를 돌릴 때 — "시험 볼 때 주의하세요", 시험장 점검표 | 8 | [요약본 §2.7, §2.16](docs/week08_20261022/study_guide_summary.md) |
| 교수님이 강조한 포인트(전 차시) | 전체 | [docs/compiled/key_points.md](docs/compiled/key_points.md) |
| 예상 시험 문제와 모범 답안(전 차시) | 전체 | [docs/compiled/exam_questions.md](docs/compiled/exam_questions.md) |
| 용어집(전 차시) | 전체 | [docs/compiled/glossary.md](docs/compiled/glossary.md) |

## 9. 자료 유형으로 찾기

| 찾는 것 | 어디에 |
|---|---|
| 교수님이 말한 원문(강의노트 그대로) | 각 주차 전체판의 `**교수님 말씀 · 강의노트 p.N**` 박스, 또는 전체판 끝 '부록 A 강의노트 원문' |
| 녹음에서 확인된 발언(시각 포함) | 전체판의 `**교수님 말씀 · 녹음k mm:ss**` 박스 → `transcripts/reck.md` 같은 시각 절 |
| 영문 슬라이드의 번역·요약 | 전체판의 `**슬라이드 원문**` 박스 |
| 교재 대응 쪽수 | 전체판의 `**교재 보충 · ISLR p.N**` 박스 (1판 기준) |
| 슬라이드 원문(영문) 텍스트 | 각 주차 `slides/*.md` (이미지 슬라이드는 OCR) |
| 수업 R 코드 | `private/docs/week02_20260909/code/knn_regression_demo.R`, `private/docs/week04_20260923/code/naive_bayes_default.R` (비공개, 로컬 전용) |
| 학습자료를 만들 때 쓴 프롬프트 | `private/docs/common/study_material_prompt.md` (비공개, 로컬 전용) |
