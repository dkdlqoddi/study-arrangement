<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 전 차시 강의 개요 모음 (1/2)

> 원본: `docs/week*/study_guide_*.md` · 변환 방식: compiled · 생성일: 2026-10-25 · 8개 차시
> [다음 부분 ▶](overviews_part02.md) · [주차 인덱스](../../INDEX.md) · [전체 인덱스](../../INDEX.md)

---
> 각 차시 학습자료의 '강의 개요' 절만 모았습니다. 학기 흐름을 한눈에 볼 때. 각 차시 학습자료(요약본, 없으면 전체판)에서 자동 추출 · 생성일 2026-10-25 · [전체 인덱스](../../INDEX.md)


## 1차시 (2026-09-02) — 과목 소개 · Chap1 Introduction · Chap2 Part I (Statistical Learning)

_출처: [study_guide_summary.md](../week01_20260902/study_guide_summary.md) · [주차 인덱스](../week01_20260902/README.md)_

### 1. 강의 개요

1차시(2026-09-02)는 과목 소개 → Chap1 Introduction → Chap2 Part I(Statistical Learning)까지 진행됐다. 녹음은 세 토막이며, 강의노트 18쪽과 슬라이드(Intro, Chap1, Chap2_Part1)를 함께 정리했다.

| 구간 | 녹음 | 다룬 자료 | 핵심 주제 |
| --- | --- | --- | --- |
| 강의1 | 오후 6:34 시작, 약 47분 | Intro 슬라이드 | 과목 소개, 교재(ISLR 주교재, Prince 딥러닝 부교재, ESL 참고), 프로젝트와 평가, AI 도구 사용 원칙, 통계학 vs 기계학습 비교 |
| 강의2 | 오후 7:31 시작, 약 51분 | Intro 후반, Chap1 | 보건학에서 ML이 주목받는 이유(Tailoring, 건강 불평등, 공정성, 프라이버시), supervised / unsupervised / reinforcement learning |
| 강의3 | 오후 8:32 시작, 약 38분 | Chap2 Part I | 통계적 학습 = f 추정, 손실함수와 최적 예측자 E[Y\|X], Prediction vs Inference, Parametric vs Non-parametric, 차원의 저주, 유연성-해석력 trade-off |

**수업 운영 메모(시험·프로젝트)**

15주 과정, 7주차 중간고사, 15주차 기말고사. 주교재 ISLR(James, Witten, Hastie, Tibshirani) 순서를 따라가며 10주차쯤 딥러닝은 Prince 책에서 가져온다.

학기말 팀 프로젝트: 3~4명씩 약 8개 조, 9월 말 난수로 랜덤 배정. 특정 데이터셋을 분석해 마지막 수업에서 20분 이상 발표, 동료 평가 포함.

AI 도구 사용은 허용하되 반드시 보고: 어떤 도구를, 어떤 목적으로, 어느 범위까지 썼는지 명시. 코딩 에이전트(Codex 등)까지 허용.

읽기 과제: Efron(2020) "Prediction, Estimation, and Attribution"(Int. Statistical Review 2021)과 Shmueli의 "To Explain or to Predict?"는 읽어 보라고 권함. Shmueli 논문은 5~10분 발표 지원자를 받음.

필요한 수학: 선형대수(벡터·행렬 연산)와 기초 미적분(로그·지수 미분, 적분). 프로그래밍은 R 또는 Python.


## 2차시 (2026-09-09) — Chap2 Part I 복습(f 추정, parametric/non-parametric, KNN·차원의 저주) · Chap2 Part II(MSE, Bias-Variance, Bayes classifier) · Efron 논문 발표

_출처: [study_guide_summary_part01.md](../week02_20260909/study_guide_summary_part01.md) · [주차 인덱스](../week02_20260909/README.md)_

### 1. 강의 개요

2차시(2026-09-09)는 1차시에 시작한 Chap2 Part I(Statistical Learning)의 뒷부분인 "f를 어떻게 추정하나(parametric vs non-parametric)", K-최근접이웃(KNN)과 차원의 저주, 예측 정확도와 해석력의 trade-off를 마치고, 학생발표 뒤 Chap2 Part II(Assessing Model Accuracy)로 넘어가 MSE와 training/test 구분, overfitting, bias-variance 분해, 분류 설정(0-1 loss, Bayes classifier, KNN), 현대판 bias-variance trade-off(double descent)까지 진행했다. 교재로는 ISLR 1판 2장(p.15~42) 전체에 해당한다.

자료는 강의노트(OneNote 내보내기 20260909.pdf 44쪽: 슬라이드 캡처 아래 학생이 타이핑한 교수님 말씀), 슬라이드 54장(Part I 31장 + Part II 23장), 녹음 3개(20260909-1/2/3.wma, 약 51 + 21 + 41분), 교재 ISLR 1판 2장이다. Part I 슬라이드 1~17(노트 p.1~17)은 1차시에 다룬 내용이라 메모가 없고, 이날 메모는 p.18 "How Do We Estimate f?"부터 시작한다. 노트 p.35, 40~42에도 메모가 없고 칠판·판서 사진은 한 장도 없다. 녹음은 강의실 녹음이라 음질이 낮아 알아들은 구절만 인용했다(예: 녹음1 16:07~22:58은 판독 불가).

이날을 관통하는 틀은 P1 슬7의 "제곱오차 손실 아래 최적 예측자는 회귀함수 f(x) = E(Y|X=x)"이다[추가]. KNN은 이를 이웃 평균으로 근사하고(2.3), 분류에서는 0-1 손실 아래 최적 분류기가 P(Y=1|X=x) ≥ 1/2이면 1로 예측하는 Bayes classifier가 된다(2.7). 그 사이에 "f̂을 구할 때 쓰지 않은 자료로 평가해야 한다"는 원칙(test MSE, 2.5)과 test MSE가 U자를 그리는 이론적 근거인 bias-variance 분해(2.6)가 놓인다.

| 구간 | 녹음 | 다룬 자료 | 핵심 주제 |
|---|---|---|---|
| 강의 1 | 오후 6:35 시작, 녹음1 51.3분 | Chap2 Part I 슬18~31 (노트 p.18~28) | parametric vs non-parametric, 선형모형 ≠ 직선, Taylor 근사, KNN 이웃 평균과 k, 차원의 저주(단위 입방체, 고차원 거리·각도), 유연성–해석력 trade-off, 표본 수와 허용 복잡도 |
| 학생발표 | 오후 7:35 시작, 녹음 파일 없음 | 전체판에 발표 내용 기록 없음 | OneNote 머리에만 기록. 강의 2는 발표 직후 "세 분이 몇 가지 얘기를 드렸었는데"로 시작 [녹음2 00:05] |
| 강의 2 | 오후 8:11 시작, 녹음2 20.7분 | Chap2 Part II 슬1~6 (노트 p.28~32) | 통계(βⱼ·s.e.·CI) vs ML(Ŷ), MSE와 loss function, training vs test, generalization vs generalizability, interpolation과 overfitting, test MSE의 U자 |
| 강의 3 | 오후 8:40 시작, 녹음3 41.2분 | Chap2 Part II 슬6~23 (노트 p.32~44) | 세 예(그림 2.9~2.11), bias-variance 분해 유도, fundamental picture, 0-1 loss, Bayes classifier 유도와 두 갈래(확률 vs 결정경계), KNN 분류, double descent(노트 메모만) |

**수업 운영 메모**

- 녹음 구성: 노트 p.1(OneNote 머리)에 "강의 1 오후 6:35 / 학생발표 7:35 / 강의 2 8:11 / 강의 3 8:40"의 네 토막이 기록돼 있지만 폴더의 녹음 파일은 3개이고 학생발표 녹음은 없다.
- 학생발표의 발표자·주제는 전체판에 기록되어 있지 않다. 강의 2는 발표를 받아 "통계(하는 사람)은 β에 … 관심이 많아요"로 이어 갔다[녹음2 00:05].
- 시험·평가·과제에 대한 직접 언급은 이날 녹음 세 개에서 확인되지 않았다(→ 5절).
- 진도 예고: k를 정하는 방법은 "뒤쪽에서 배움", 커널·스플라인은 "다음 챕터에서 배우게 됨"[노트 p.23]. 강의는 KNN 분류에서 "다음 시간에 (계속하겠습니다)"로 마쳤다[녹음3 40:37]. 교재상 시험 MSE 추정(교차검증)은 5장, spline은 7장이다[교재 p.24, 33].
- 읽을거리: P2 슬23의 Belkin 외(2019) 그림은 "약간 technical 함. 수리적이거나 통계 background 있는 사람 추천"[노트 p.44].
- 강의 폴더에 kNN.txt(R 코드 12줄, k=1 KNN 회귀 vs 선형회귀 시연)가 있다[추가].


## 3차시 (2026-09-16) — Chap2 Part II 마무리 · Double descent 발표 · Chap3 Linear Regression(두 관점·likelihood·추론·변수선택·KNN 비교) · 회귀→경사하강→신경망 · Chap4 분류 시작(로지스틱, MLE·cross-entropy)

_출처: [study_guide_summary_part01.md](../week03_20260916/study_guide_summary_part01.md) · [주차 인덱스](../week03_20260916/README.md)_

### 1. 강의 개요

3차시(2026-09-16)는 Chap.2 Part II 마무리 → Belkin(2019) double descent 학생 발표 → Chap.3 선형회귀(두 관점·likelihood) → 교수님 자작 슬라이드 "One Idea, Many Models"(제곱오차 → 경사하강 → 신경망) → Ch.4 분류 (정의·0-1 loss·로지스틱 회귀·MLE)까지 진행됐다. 녹음은 다섯 토막, 강의노트 43쪽(슬라이드 121장 포함), 칠판 사진 16장을 함께 정리했다.

| 구간 | 시각 | 다룬 자료 | 핵심 주제 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의 1 | 18:35–(26.6분) | Chap2 Part2 (23장) _ | 훈련/테스트 MSE, bias-variance 분해의 보편성, Bayes classifier, KNN, Brier score vs 0-1 loss, double descent 소개 | 없음 |
| 강의 2 | 19:02–(31.7분) | Chap03 Lec (40장) _ | 선형회귀의 두 관점, likelihood·log-likelihood·MLE, Fisher information, frequentist vs Bayesian, likelihood ↔ loss | 19:26 ×3 |
| 논문 발표 | 19:45–(12.5분) | Belkin et al. 2019 | interpolation, model class, inductive bias, random Fourier feature, deep double descent | 없음 |
| 강의 3-1 | 19:57–(36.4분) | regression to neural nets (13 _ _ _ 장) | 목적함수·볼록성, gradient와 경사하강, 학습률, 뉴턴법의 한계, mini-batch SGD, 신경망·역전파·비볼록 | 20:08 ×2 |
| 강의 3-2 | 20:42–(43.8분) | Ch04-Classification (45장 중 ~S089까지) | 분류의 정의, classification risk, 선형회귀 vs 로지스틱, link·logit·OR, 베르누이 likelihood = cross-entropy, softmax | 20:55–21:24 ×11 |

**수업 운영 메모(시험·평가 관련, 녹음4 00:59–08:46, 41:39–43:44)**

발표 슬라이드는 게시판 업로드가 원칙이며 가능하면 영어로 준비(외국인 수강생 배려).

정기 숙제는 없다("대학원이니 공부는 알아서"). 대신 교재 exercise를 LLM(GPT·Claude·Gemini)에 풀게 해 보고 LLM 답의 오류를 찾아 정리해 이메일로 제출하면 성적으로 보답하겠다. 의미 있는 것은 다음 시간에 짧게 발표.

교재 ISLR에는 R lab·Python lab(ISLP)·exercise가 있고 코드·데이터가 공개되어 있다.

Ch.3은 "이미 끝난 것"으로 간주 — 수업에서는 두 관점·likelihood·gradient method만 다뤘고 가설검정 등은 교재로 직접 공부(시험 범위 제외 언급은 없음).

다음 차시 발표 모집: TRIPOD(+AI) 예측모형 보고 체크리스트(20~25항목)를 사례와 함께 소개.

Ch.4의 다변량 로지스틱 이후(confounding·LDA·QDA·naive Bayes·KNN 비교)는 이번 차시에 다루지 않았다(다음 차시 예상).


## 4차시 (2026-09-23) — 로지스틱 회귀 심화(우도·경사법·Newton–Raphson·odds ratio·confounding·환자-대조군) · 다항 로지스틱 · 판별분석의 출발점 · TRIPOD/PROBAST 발표

_출처: [study_guide_summary_part01.md](../week04_20260923/study_guide_summary_part01.md) · [주차 인덱스](../week04_20260923/README.md)_

### 1. 강의 개요

4차시(2026-09-23)는 Ch.4 Classification을 로지스틱 회귀 복습부터 판별분석 도입(S26, complete separation)까지 진행했다. 중간에 학생 논문발표 2건(TRIPOD, PROBAST)이 있었다. 녹음 3개(60.0·55.8·37.0분), 강의노트 25쪽(슬라이드 45장 캡처), 칠판 사진 29장을 함께 정리했다. 녹음3 36:50 "오늘 여기까지, 다음 시간에 계속"으로 끝났으므로 S27(LDA p=1) 이후는 다음 차시 범위이다.

| 구간 | 시각 | 핵심 주제 | 슬라이드 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의1 | 18:34– (60.0분) | 로지스틱 함수·logit(링크), 0-1 손실 → 베르누이 우도 → −log 우도 → 경사법, Fisher 정보·Newton–Raphson·표준오차·z·p-value, 예측, student 변수와 odds ratio, 다변수 로지스틱, confounding, 남아공 심장병 자료, 코호트 vs 환자-대조군, iid와 p* vs P | S01–S18 | 18:40–18:51 ×6, 19:09 ×1 |
| 강의2 | 19:43– (20분) | 선택지표 S를 이용한 환자-대조군 증명(절편만 이동), 절편 보정식, matched design, 역학 설계와 머신러닝 | S19–S20 | 19:47–19:59 ×7 |
| 논문발표 | 20:03– (36분) | TRIPOD(+AI, LLM) 보고 체크리스트, PROBAST 편향·적용성 평가 도구, 교수님 코멘트 | — | 없음 |
| 강의3 | 20:46– (37.0분) | 다항 로지스틱(baseline category logit, softmax, 다항분포 손실, argmax), 판별분석 도입(Bayes 정리로 뒤집기, 생성 vs 판별, 최고 밀도 분류), complete separation, naive Bayes 팁 | S21–S26 | 20:48–21:22 ×15 |
| 미진행 | — | LDA(p=1, p>1)·모수 추정·혼동행렬·ROC·QDA·naive Bayes·로지스틱 vs LDA·KNN·요약 | S27–S45 | — |

**수업 운영 메모(평가·과제 관련)**

시험 범위나 유형을 직접 언급한 발언은 녹음 1·2·3에서 확인되지 않았다.

최종 프로젝트: 추석 지나면 3명씩 팀을 꾸리기 시작. 최종 프로젝트에 TRIPOD+AI 체크리스트를 제출하는 연습을 권함 [녹음2 54:28–54:59]. 예측모형 논문에는 TRIPOD+AI·PROBAST+AI가 현재 표준이고 임팩트 팩터 높은 저널엔 제출이 필수 [녹음2 21:14, 51:13].

연습 권유: 로지스틱 계수를 경사법으로 직접 구해 보기(코덱스·클로드에 "loss 최소화, gradient, 학습률, 데이터 생성, 수렴 과정 한 스텝씩" 시키기) [녹음1 25:33–26:23]; confounding 설명의 틀린 점을 10분 생각한 뒤 LLM 과 토론 [녹음1 38:27–39:20]; 다항 로지스틱 손실을 간단한 자료로 짜 보기 [녹음3 12:48].

교육관: "GPT·클로드 시대에는 짜는 것보다 결과가 틀렸는지 판단하는 능력이 중요하고, 짤 줄 아는 사람과 모르는 사람이 거기서 갈린다" [녹음1 24:36–25:33]; "당분간은 공부해서 인간이 좀 더 나은 척하고 살아야 되는 시기" [녹음3 26:13–26:55].

보충 덱 4종(regression/logistic → NN, Multivariate Gaussian, Binary Classifier Performance)은 폴더에 배포됐지만 이번 차시에 설명하지 않았다. 앞의 둘은 3차시에서 다룬 것과 같다.




## 5차시 (2026-09-30) — 판별분석(LDA, p=1 → p>1) · 다변량 정규분포 · Naive Bayes·Laplace 평활 · 이진 분류기 성능(정확도 함정·임계값·민감도·특이도·ROC·AUC)

_출처: [study_guide_summary_part01.md](../week05_20260930/study_guide_summary_part01.md) · [주차 인덱스](../week05_20260930/README.md)_

### 1. 강의 개요

5차시(2026-09-30)는 Ch.4 Classification의 판별분석(LDA)을 S23 복습에서 시작해 S39(ROC·AUC·임계값 선택)까지 진행했고, 중간에 교수님이 직접 만든 보충 덱 「Multivariate Gaussian Distribution」(28장)을 끼워 넣어 p차원 정규분포를 설명했다. 녹음 3개(62.8·46.6·37.7분), 강의노트 13쪽(슬라이드 73장 캡처), 칠판 사진 9장을 함께 정리했다. 녹음3 34:02 "오늘은 여기까지, 다음 시간에 계속"으로 끝났으므로 S40–S45(QDA·naive Bayes 슬라이드·로지스틱 vs LDA·KNN·요약)와 AUC의 한계는 다음 차시 범위이다. 강의 2 중간에 프로젝트 팀(8조)을 구성했다.

| 구간 | 시각 | 핵심 주제 | 슬라이드 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의1 전반 | 18:34– (34분) | 팀 구성 예고 → 판별분석 복습(likelihood ↔ Bayes 유추, p(Y∣X) ⇕ p(X∣Y)) → LDA p=1 유도(공통분산으로 항 상쇄 → 1차식) → 밀도 높이 비교 그림 → 분산이 다르면 QDA, "LDA·QDA는 밑밥, naive Bayes가 실무" → 모수 추정·산뜻한 식 vs 역행렬 비용 → p>1과 다변량 분포의 한계(GEE·mixed effect) | S22–S31 | 18:37–18:38 ×5, 18:47 ×2 |
| 강의1 후반 | 19:08– (29분) | 보충 덱: 왜 다변량 정규인가, 우도 vs 추정방정식 장단점, 평균벡터·공분산행렬·양반정치, 밀도식 바꿔치기, Σ 모수 p(p+1)/2, 대각 Σ = 독립, 등고선 타원과 고유벡터, [[2,1],[1,2]] 예, 네 성질("외우세요"), 나머지 읽기 | M01–M17 (M18–M28 읽기) | 19:22 ×2 |
| 강의2 | 19:45– (46.6분) | 판별함수 선형성 재정리 → K=3 땅따먹기 → Fisher 의 붓꽃 → "가장 힘든 파트는 Σ" → 유전체 자료 → 비대각 0 = naive Bayes → 이산 변수 count·Laplace 평활·R 코드 → 팀 구성(8조)·중간보고서 공지 → 혼동행렬·정확도의 함정·오류 비용·임계값 ½ | S31–S36 | 없음 |
| 강의3 | 20:48– (34분) | 프로젝트 Q&A(주제·방법·LLM·발표) → 의료 문맥의 두 오류 → 민감도·특이도·시소 → ROC의 (0,0)·(1,1)·(0,1), 원숭이 선 → 교차하는 ROC와 AUC → Youden 지수 → "오늘은 여기까지" | S37–S39 | 없음 |
| 미진행 | — | 판별분석의 다른 형태, QDA·naive Bayes 슬라이드, 로지스틱 vs LDA, KNN, 요약, AUC의 한계(보충 덱) | S40–S45, 부록 C | — |

**수업 운영 메모(평가·과제 관련)**

시험 범위·유형을 직접 언급한 발언은 녹음 1·2·3에서 확인되지 않았다. 다만 "이 슬라이드는 중요"(노트 p.2, M09), "Binary classifier의 성능. 중요함"(노트 p.10), "외우세요"(노트 p.4, M16 두 성질)가 명시적 강조다.

프로젝트 팀: 번호순 3명씩 8개 조 확정, 조장과 조원 학번·이름 제출 [녹음2 24:28–30:22]. "프로젝트에 한해서는 운명공동체".

중간보고서: A4 1–2쪽(제목, 데이터셋, 분석 목적, 봐야 할 이유, 구체적 데이터셋 한두 개), 중간고사 즈음 제출 [녹음2 30:31–31:27][녹음3 09:10]. 주제는 건강 문제 안에서 권장, 방법 제한 없음(LLM 가능하되 투명한 보고)


[녹음3 01:08–02:33].

최종: 5–6쪽 보고서(데이터·방법·결과·결론·보건학적 함의) + 조장 20분 발표 + 공격적 질문·디펜스(조원 공동 답변 가능, 한·영 가능), 기말 전후 미정 [녹음3 02:52–04:31]. "왜 로지스틱만 돌렸나요?"에 답을 준비하라 [녹음 3 03:56]. 인과추론과 기계학습을 버무리면 "가장 좋은 먹잇감" [녹음3 05:00]. LLM이 틀렸는데 맞다고 발표하다 걸리면 "많이 각오" [녹음3 10:54].

연습 권유: LDA 유도를 손으로 [녹음1 17:30]; 보충 덱 M18 이후 읽기 [녹음1 58:10]; R ?naiveBayes 의

laplace 설명 읽기 [녹음2 24:16].


## 6차시 (2026-10-07) — 분류기 성능 심화(c-통계량=AUC 증명·discrimination vs calibration·PPV/NPV) · Naive Bayes 재정리 · Bootstrap(원리·CI·회귀·OOB) · Cross-Validation 시작(검증셋·k-fold·LOOCV)

_출처: [study_guide_summary_part01.md](../week06_20261007/study_guide_summary_part01.md) · [주차 인덱스](../week06_20261007/README.md)_

### 1. 강의 개요

6차시(2026-10-07)는 지난 차시 끝(S36–S39 혼동행렬·ROC·AUC)을 5분 복습한 뒤 교수님이 만든 보충 덱 「Binary classifier performance」(19장)로 AUC = c-통계량 증명, 판별 vs 보정, AUC의 한계, PPV·NPV, 학습 손실 vs 평가 지표를 강의 1에서 다루었고(18:36–19:24), 수강생의 논문발표(LLM 보건의료 평가 리뷰, JAMA 2025; 19:34–20:09) 뒤 강의 2에서 부트스트랩(bootstrap_en 덱 T01–T14; 20:09–20:41), 강의 3에서 부트스트랩 마무리(T15–T18)와 교차검증(CrossValidation 덱 V01–V16; 21:01–21:25)을 진행했다. 녹음 3개(48.8·66.9·24.4분), 강의노트 51쪽(슬라이드 105장 캡처), 칠판 사진 17장을 함께 정리했다. 녹음3 23:51 "다음 시간에 이어서"로 끝났으므로 V17–V23(분류 문제의 CV, 다항 차수·KNN K 선택, right and wrong)은 다음 차시 범위이고, 폴더의 6장 덱 3종(모델 선택·정규화, AIC/BIC 유도, 다른 벌점함수)은 이번 차시에 설명되지 않았다.

| 구간 | 시각 | 핵심 주제 | 슬라이드 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의1 | 18:36– (48.8분) | 복습(2×2표·민감도·특이도·점수·임계값·ROC·AUC) → c-통계량 정의, 동점 ½, 순위 불변(+5·×2) → 구분구적법으로 AUC = c 증명 → Mann–Whitney → 판별 vs 보정, 10 등분·Brier → AUC의 한계(부분 AUC, odds ratio, 비용) → 민감도·특이도 vs PPV·NPV, 유병률 0.0000… → 개표 방송 일화 → 학습 손실 vs AUC "철학적 issue" → 보고 세트·TRIPOD → naive Bayes 재정리 → "10분 휴식" | S36–S42, B01–B19 | 18:51 ×4, 19:03–19:08 ×7, 19:20 ×2 |
| 논문발표 | 19:34– (35분) | 교수님 도입("LLM이 이겼다는 건 무슨 measure로?") → 발표: LLM 보건의료 적용의 testing & evaluation 체계적 문헌고찰(519편, 실제 환자 자료 5%, accuracy 95%, calibration 최소 측정, 6가지 권고, 한국 맥락) → 코멘트 (AI 구독·"족쇄 전략", GPU 세금, 보건 AI는 더디다, fairness는 이후 수업) | 없음 | 없음 |
| 강의2 | 20:09– (32분) | "Bootstrap = inference 최강, CV = model selection 최강" → 최후의 보루·Efron·신발끈 → inference = uncertainty = s.e./CI, Xᵢ~F → sampling distribution → F 를 모른다 → F̂ₙ(경험분포, 1/n 계단, 복원추출 항아리) → real vs bootstrap world, B=1000, 알고리즘 4단계, median 예, "공짜가 아니다" → normal interval vs percentile interval("무조건 좋다") → 회귀·상관계수: resampling unit = (xᵢ,yᵢ) 쌍, index → 휴식 | T01–T14 | 20:17, 20:20 |


| 구간 | 시각 | 핵심 주제 | 슬라이드 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의3 | 21:01– (24.4분) | 부트스트랩으로 예측오차? training set이 평가셋에 → (1−1/n)ⁿ → e⁻¹, 63%/37%, OOB → "무조건 cross validation" → 대원칙: 평가 자료는 학습에 절대 사용 금지 → 검증셋 접근·분할 비율·셔플링 → CV의 목적 = model selection, "R²는 금기", AIC/BIC → seed별 변동, swapping → "cross" → k-fold (k−1)/k, 10→5·3 → LOOCV(randomness 없음, 느림) → 1−hᵢ 항등식, AIC = LOOCV를 빨리 한 것 → 10-fold의 안정성 → "다음 시간에", "28일 시험" | T15–T18, V01–V16 | 21:04 ×2 |
| 미진행 | — | 분류 문제의 CV(Err k·SE), 다항 로지스틱 차수·KNN K 선 _ 택, CV right and wrong; 6장 덱 3종 | V17–V23, 부록 C(전체판) | — |

**수업 운영 메모(평가·과제 관련)**

시험일 10월 28일(수): "아까 시험 저희 언제 보고요? 28일? 네. 28일날 시험은 잘 기억해 주시길 바랍니다" [녹음3 24:07–24:10]. 범위: "시험은 아마도 라스토[= lasso로 들림, 불명확] 위치까지는 아마 들어가야 된다고 하거든요" [녹음3 23:58] — 다음 차시(6장 모델 선택·정규화)까지 포함될 가능성.

이번 차시 명시적 강조: "C statistic은 rank에만 의존한다는 것만 일단 기억하도록" [녹음1 10:54–11:36]; "폭은 D가 아니라 D bar — 확대해서 보세요" [녹음1 12:34]; "저 개인적으로는 3번(odds ratio와 AUC)이 굉장히 중요" [녹음1 24:00]; "sens 0.99·spec 0.98에 유병률 0.0000…을 직접 넣어 보세요" [녹음1 30:58]; "Percentile interval이 무조건 좋음" [노트 p.35][녹음2 63:10]; "평가할 때 사용한 데이터셋은 모형의 학습에 절대 사용돼서는 안 된다" [녹음3 06:50]; "R²로 모델 고르는 건 금기" [노트 p.42][녹음3 10:46]; 예측오차는 "무조건 cross validation" [녹음3 06:03].

읽기 권유: JAMA 2025 LLM 평가 리뷰 "직접 한번 읽어 보시기를 추천" [녹음2 00:49]. 증명·코드는 "GPT·Claude 가 잘 해 준다" [녹음2 49:42, 66:19][녹음3 20:15] — 내용(원리)을 이해하는 데 집중하라는 취지.

예고: Nature·PNAS·JNCI에 실린 "평가 자료가 학습에 섞인" 실패 논문 사례를 나중에 보여 줄 것 [녹음3 06:50]; fairness·subgroup 성능은 이후 수업에서 [녹음2 34:31].

프로젝트·중간보고서에 관한 새 공지는 이번 차시 녹음에서 확인되지 않았다(5차시 공지 유지: 8개 조, A4 1–2 쪽 중간보고서를 중간고사 즈음 제출).


## 7차시 (2026-10-14) — Cross-Validation 완결(k-fold·LOOCV 지름길·1-SE 규칙·올바른 CV) · Model Selection(subset selection·Cp/AIC/BIC/adjR²·AIC vs BIC 철학) · 축소법 시작(능형회귀·라쏘)

_출처: [study_guide_summary_part01.md](../week07_20261014/study_guide_summary_part01.md) · [주차 인덱스](../week07_20261014/README.md)_

### 1. 강의 개요

7차시(2026-10-14)는 강의 1에서 6차시에 V16까지 진행한 교차검증 덱(V01–V23)을 처음부터 다시 정리하며 k-fold·LOOCV와 k의 편향–분산, 분류 문제의 CV와 1-SE 규칙, 올바른 CV와 틀린 CV까지 끝냈고(18:36–19:30), 강의 2에서 V23의 실제 사례 논문으로 마무리한 뒤 「Linear Model Selection and Regularization」 덱(M01–M53)으로 넘어가 세 방법군과 AIC vs BIC의 철학, 부분집합 선택, R² 금지, Cp·AIC·BIC·adjusted R², CV의 장점, 로그 변환과자코비안을 다루었다(19:41–20:38). 녹음3(20:48–)은 교수님 도입과 수강생 발표(ISLR 5장 연습문제 8번)로 시작해, 강의 3에서 축소(shrinkage) — 제약 영역의 모양, 능형회귀(라그랑지안, λ의 CV 선택), 라쏘(정확한 0과 변수 선택)를 진행했다(20:58–21:24). 녹음 3개(54.8·57.2·36.0분), 강의노트 39쪽(슬라이드 76장 캡처), 칠판 사진 10장을 함께 정리했다. 녹음3 35:44 "다음 시간에 계속 이어서 설명을 하겠습니다"로 끝났으므로 M34 이후(라쏘의 기하·λ 선택, PCR·PLS)는 다음 차시 범위이고, M29–M32는 화면만 넘기고 따로 설명하지 않았다.

| 구간 | 시각 | 핵심 주제 | 슬라이드 | 칠판 |
| --- | --- | --- | --- | --- |
| 강의1 | 18:36– (54.8분) | 도입 "bootstrap = 불확실성, CV = 예측 성능" → 훈련 vs 검정 오차 → 검증셋("법칙 없음"), 계수 검정 vs 예측 비교 → seed별 곡선(위치는 같고 값은 흔들림) → k-fold(10 → 5·3), CV₍ₖ₎ 식 → LOOCV(randomness 없음) → 여담(measurement error, selection bias) → 지름길 공식, K의 bias–variance → "값은 prediction error가 아님" → 분류 CV·SE·1-SE 규칙 → 로지스틱차수·KNN 1/K("order 주의") → V23 퀴즈(p = 5000, n = 50, "모두 틀린 방식", 올바른 CV, nested CV) → 휴식 | V01–V23 | 18:49 ×1 |
| 강의2 | 19:41– (57.2분) | V23 마무리(정답 0.5 vs 틀린 CV ≈ 0, Nature·PNAS 사례, Ambroise & McLachlan) → 08:08 M01 "딥러닝에서 다 쓰이는 아이디어" → 세 방법군, AIC(KL·참 모형 없음) vs BIC(참 모형·확률 1) → best subset 2ᵖ, forward ≈ p², backward(p > n 불가) → R² 금지, 간접 vs 직접 → "Cp 쓰지 마세요", Credit 4·6·7 → AIC·BIC 식(d = 3, log n = 10) → CV의 universal함 → 자코비안 함정(10만 vs 500만) → LOOCV ≈ AIC → 휴식 | V23, M01–M22 | 20:25 ×3 |
| 녹음3 | 20:48– (36.0분) | 교수님 도입(GPT·Claude는 "완벽하지는 않습니다", 혼동 사례 공유) → 수강생 발표(01:00–08:42): ISLR 5장 연습문제 8, 같은 seed인데 10-fold 결과가 다른 이유 = fold 배정 방식 → 코멘트 → 09:48 강의3: lasso의 역사 → 추정치 불안정, 제약 → variance ↓·bias ↑ → 사각형·원·마름모·elastic net·십자가 → ridge = sphere, 라그랑지안 → λ는 CV, 격자 범위 경고 → solution path → lasso path(정확한 0, 이름) → "다음 시간에 계속" | M24–M28 → M33 | 21:07 ×4, 21:11 ×2 |
| 미진행 | — | M23 1-SE 규칙(녹음2에서 설명 없음; 1-SE 규칙 자체는 녹음1 V18에서 설명), M29–M32(따로 설명 없음), M34–M39(라쏘의 기하·λ 선택), M40–M53(PCR·PLS·요약); 6장 관련 덱 2종(전체판 부록 C) | M23·M29–32·M34–53 | — |

**수업 운영 메모(평가·과제 관련)**


시험일 10월 28일(수)(지난 차시 공지): "28일날 시험은 잘 기억해 주시길", 범위 "시험은 아마도 라쏘 위치까지는 들어가야 된다고" [6차시 녹음3 23:58–24:10]. 이번 차시 녹음 3개에는 시험·과제 발언이 없다. 강의가 M33 에서 멈췄으므로 M34–M39도 다음 차시에 배운 뒤 범위에 들 가능성이 크다 [추가].

이번 차시 강조: "bootstrap은 불확실성, CV는 예측 성능 — 가장 중요한 메시지" [녹음1 01:03]; "R²로 절대 모델을 고르면 안 됩니다" [노트 p.20][녹음2 28:47]; BIC가 더 단순한 모형을 고른다 — "하나의 중요한 결론으로 기억" [녹음2 45:18]; "아무것도 안 떠오르고 cross validation만 떠오르면 공부를 제대로 한 겁니다" [노트 p.23][녹음2 48:31]; "세상에 공짜가 없습니다" [녹음3 15:42]; λ 범위의 경계값이 최적으로 나오면 "항상 의심"[녹음3 30:27].

비중을 낮춘 것: "Cp 같은 거 쓰지 말아주세요. 안 써요" [녹음2 33:54], "Adjusted R²는 안 써요. 공부하지 마세요" [노트 p.23][녹음2 45:25]; 1-SE 규칙이 헷갈리면 "그냥 최적 값을 주는 모델을 고르겠다고 생각하시면 돼요"[녹음1 32:22].

읽기 권유: Ambroise & McLachlan, "Selection bias in gene extraction on the basis of microarray gene-expression data"(PNAS 2002) — "각자 꼭 한 번씩 읽어보셔서 슬라이드 마지막 내용과 결부해서" [노트 p.13] [녹음2 07:52].

AI 도구: 라그랑지안은 "Claude나 GPT를 이용해서 'Lagrangian을 설명해줘'" [노트 p.26][녹음3 25:36], 자코비안 보정은 "GPT에 넣으면 … 한번 해보세요" [녹음2 55:16], LOOCV ≈ AIC는 "GPT나 Claude에 물어보세요" [녹음2 55:52]; 디폴트·AI가 고른 λ 범위는 "여러분이 검토해 주셨으면" [녹음3 29:41].

발표 시간: 코드는 GPT·Claude를 "많이 활용하세요 … 그런데 완벽하지는 않습니다" — 문제·혼동 사례를 함께 공유하는 시간이며 "오늘 첫 번째 시간" [녹음3 00:25–00:47]. V23 퀴즈는 "평가하는 퀴즈는 아니고 한번 생각해보세요 퀴즈" [녹음1 39:32]. 프로젝트 관련 새 공지 없음.
