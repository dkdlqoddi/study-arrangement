<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 1차시 시험대비 학습자료 (요약본)

> 원본: `machine_learning_for_health_science/20260902/1차시 시험대비 학습자료.pdf` · 변환 방식: pdf-text · 생성일: 2026-10-24 · 원본 12쪽
> [주차 인덱스](README.md) · [전체 인덱스](../../INDEX.md)

---
<!-- page 1 -->

## ML for Health Science 1차시 시험 대비 학습자료

2026-10-10 작성 · 보건학을 위한 기계학습 (서울대 보건대학원, 이우주 교수) · 1차시 2026-09-02 강의노트·슬라이드·녹음 기반

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

### 2. 핵심 개념 정리

1차시의 뼈대는 "통계학과 기계학습은 같은 문제(f 추정)를 다른 문화로 푼다"는 것과, Chap2의 "최적 예측자는 조건부 기대값 E[Y|X]"라는 결과다. 아래 2.1~2.9 순서가 강의 진행 순서다.

#### 2.1 통계학 vs 기계학습 (Two cultures)

기계학습은 인공지능의 하위분야에서, 통계적 학습은 통계학의 하위분야에서 출발했다. 둘 다 supervised / unsupervised 문제를 다루므로 교집합이 크다.

2000년 이전의 통념(Intro 슬라이드 9의 표):

<!-- page 2 -->

| 항목 | Statistics | Machine Learning |
| --- | --- | --- |
| 주 관심 | 가설검정, 해석, 인과성 | 예측 정확도 |
| 데이터 크기 | 작음 / 중간 | 큼 |
| 모형 복잡도 | 낮음 (거의 선형) | 높음 (블랙박스, 예: random forest) |
| 추론 도구 | 표준오차(S.E.), 신뢰구간(CI) | Accuracy, Calibration, Discrimination, Generalization |
| 해석력 | 높음 | 낮음 |

왜 이런 차이가 생겼나: 통계학은 농업 실험 데이터(1년에 한 번, 관측치 30~40개)에서 출발해 "얼마나 불확실한가"(S.E., CI)가 핵심이었다. 기계학습은 공장·웹의 대량 데이터에서 출발했고, n이 100만이면 평균의 표준오차는 의미가 없으니 예측 정확도가 주된 관심이 됐다.

현재는 경계가 거의 무너져 서로의 tool box를 흡수했다(cross-fertilization). 교수님 농담: "ML은 마케팅 용어" (슬라이드: Machine learning has the upper hand in Marketing).

통계학이 강조하는 키워드는 model(분포)과 uncertainty. "신뢰구간을 제시하는 무속인은 없다" → 불확실성을 정량화하고 틀리면 버려지는 검증 과정을 거친 것이 과학의 힘.

기계학습이 강조하는 키워드는 algorithm, large scale, prediction accuracy.

보건학의 많은 문제는 "왜 떨어졌을까"를 묻는 왼쪽(통계학) 쪽에 가깝다. 다만 예측(주가가 오를지 맞히기)도 필요하며, 변수 중요도·해석을 위해 xAI(explainable AI)가 등장했다.

관련 논문: Breiman(2001) "Two cultures"(random forest 개발자, UC Berkeley), Efron(2020) "Prediction, Estimation, and Attribution"(bootstrap·FDR 개발자), Shmueli(2010) "To Explain or to Predict?".

#### 2.2 보건학에서 기계학습이 주목받는 이유와 주의점

역학·보건학에서 가장 빠르게 성장하는 도구가 AI/ML이지만, "가져다 쓰면 그만"이 아니라 분야에 맞게 tailoring해야 한다.

예시(환경역학): 독성물질을 다루는 기업은 백여 종의 물질을 관리하고 근로자는 mixture로 노출된다. 설명변수가 수백 개이고 혼합물이므로 kernel machine 같은 맞춤 기법이 쓰인다.

건강 불평등: 취약집단 식별에 ML 활용 가능성. 데이터는 엑셀 표를 넘어 설문·내러티브·이미지·건강보험공단·유전체가 섞인 multimodal 형태로 간다(예: "이 사람이 10년 내 암에 걸릴 확률").

공정성(fairness)은 측정 지표가 여러 개이고 하나를 최대화하면 다른 것이 희생된다. 결국 어떤 공정성을 쓸지는 인간이 결정해야 한다. 과도한 도입은 프라이버시 침해로 이어지므로 균형이 중요하다.

ML의 강점은 prediction이다. 인과 질문은 causal inference라는 별도 분야가 다루며, 최근 둘을 결합한 causal ML(double ML)이 등장했다.

#### 2.3 Chap1: 학습의 세 유형

Statistical learning = "a vast set of tools for understanding data". 도구는 세 가지로 분류된다.

| 유형 | 데이터 | 목적 | 예 |
| --- | --- | --- | --- |
| Supervised learning | X(input)와 Y(output) 모두 있음 | X→Y의 함수관계 f를 학습해 새 X의 Y를 예측. Y(gold standard)가 있어 평가가 쉬움 | Regression(연속형 Y), Classification(범주형 Y) |

<!-- page 3 -->

| 유형 | 데이터 | 목적 | 예 |
| --- | --- | --- | --- |
| Unsupervised learning | X만 있고 outcome label 없음 | 비슷한 프로파일을 묶거나 (clustering) 추상적·잠재적 개념을 요약. 정답이 없어 평가가 어려움 | Clustering, Variational Autoencoder, Factor analysis(설문 수십 문항 → 울분 같은 개념) |
| Reinforcement learning | 보상/벌칙 신호 | 보상 구조에서 최적화된 행동 규칙을 학습 | AlphaGo, 로보틱스, Atari 벽돌깨기 |

현실 세계에는 unsupervised 데이터가 많지만, 의료·보건에서는 supervised 문제도 충분히 많다.

Training data로 f를 만들고 test data로 평가한다.

통계학은 regression으로 통칭했고, 컴퓨터과학이 classification 분야를 성숙시켰다. 생존분석 (censored observation)과 Poisson 자료는 컴퓨터과학 쪽에서 덜 다룬다.

강화학습의 위험: 벌칙과 보상만 주면 인간 상식 밖의 규칙을 스스로 만든다(비행기 게임에서 미사일을 피하려고 게임을 셧다운, 환경 문제를 풀라니 인간을 제거). 보상 설계가 핵심.

모형 선택 태도: 문제가 오면 딥러닝부터 쓰지 말고, 단순하고 빠른 방법을 먼저 돌려 결과가 기대치에 얼마나 못 미치는지 빨리 판단한 뒤 복잡한 모형으로 옮겨간다.

#### 2.4 Chap2 Part I: 통계적 학습이란 — f를 추정하는 것

기본 모형: Y = f(X) + ε. X = (X1, …, Xp)는 input / predictor / feature, Y는 output / response, f는 X 가 Y에 대해 주는 systematic information, ε은 평균 0이고 X와 독립인 random error(외부 요인에 의한 noise).

Statistical learning은 "f를 추정하는 접근법들의 집합"이다.

예: Advertising 데이터(TV·radio·newspaper 광고비 → sales), 보건학에서는 나이·성별·교육수준 → 암 발생 확률.

입력의 벡터화: supervised learning은 벡터 X와 (스칼라) Y를 전제한다. 텍스트는 과거에 사전(약 6만 컬럼)을 만들어 단어 등장 여부를 0/1로 표시했고, 이미지는 픽셀 행렬을 column-wise로 잘라 세로로 이어붙여 벡터로 만들었다. 이 방식은 이웃 정보(인접 픽셀의 색 유사성, 단어의 문맥)를 잃는다. Transformer·CNN은 구조 정보를 보존하면서 벡터화한다.

벡터화만 되면 회귀분석으로도 모델링할 수 있으므로 비정형 데이터는 딥러닝만의 문제가 아니다. 딥 러닝·생성형 AI가 질적으로 다르다고 느껴지는 이유는 성능이 인간을 압도하기 시작했기 때문이다(영상의학 판독 예).

#### 2.5 f를 왜 추정하나: Prediction vs Inference

|  | Prediction | Inference |
| --- | --- | --- |
| 질문 | 새 X에 대한 Y는? Ŷ = f̂(X) | X가 변하면 Y가 어떻게 변하나? |
| f̂의 취급 | 블랙박스여도 됨. ε 분산이 크지 않으면 정확한 예측 가능 | 형태를 알아야 함: 어떤 predictor가 관련? 방향 (+/−)? 선형인가? |
| 슬라이드 예 | Direct mailing: 90,000명 × 400개 특성, "누구에게 보낼까"만 관심 | Housing: 14개 변수, river view가 집값에 얼마나 영향? |

교수님 강조: 예측에 크게 기여하는 변수와 개입(intervention) 효과가 있는 변수는 다르다. 라이터 소지는 10년 뒤 폐암의 강한 예측변수지만 "라이터 금지 정책"은 효과가 없다.

<!-- page 4 -->

인과추론은 counterfactual prediction(같은 사람이 라이터를 안 가졌을 때의 outcome)이라는 다른 사고가 필요하고 강한 domain knowledge가 필요하다. 관련 개념: interventional prediction, distributionally robust prediction, heterogeneous environments에서의 stability. 최근에는 causal inference + ML(예: boosting으로 propensity score 구성).

#### 2.6 손실함수와 최적 예측자 E[Y|X]

손실함수(loss function): 예측 Ŷ와 실제 Y가 얼마나 어긋났는지 재는 함수. 연속형 outcome의 표준은 squared error(L2) loss. 제곱이 표준이 된 이유는 손으로 미분하던 시절 계산이 쉬웠기 때문이며, 통계학의 ordinary least squares와 자연스럽게 연결된다.

Risk = E[(Y − f(X))²]를 최소화하는 f를 찾는다. X = x를 조건으로 두고 전개하면:

(Y − f(x))² = (Y − E[Y|X=x] + E[Y|X=x] − f(x))²

E[(Y − f(x))² | X=x] = E[(Y − E[Y|X=x])² | X=x] + (E[Y|X=x] − f(x))²

└── irreducible, Var(ε) ──┘ └──── reducible ────┘

⇒ f*(x) = E[Y | X = x]

결론: 제곱오차 아래 최적 예측자(optimal predictor)는 regression function f(x) = E[Y|X=x]이다. "예측을 잘하고 싶으면 조건부 평균만 잘 추정하면 된다"로 귀결된다. 선형회귀 Y = Xβ + ε에서는 E[Y|X=x] = xβ.

실제로는 X = x인 데이터가 거의 없으므로 이웃 N(x)의 평균으로 완화한다: f̂(x) = Ave(Y | X ∈ N(x)) (nearest neighbor averaging). 거리에 따라 exp(−(x′−x)²) 같은 가중치를 주면 kernel smoothing이 되고, 이웃의 크기·가중치 폭은 hyperparameter(tuning parameter)다.

자료의 난이도는 ε의 표준편차에 달려 있다(sd = 0.001이면 점이 곡선에 붙고 sd = 0.03이면 f를 알아보기 어렵다).

#### 2.7 f 추정 방법: Parametric vs Non-parametric

|  | Parametric | Non-parametric |
| --- | --- | --- |
| 절차 | STEP 1: f의 형태를 가정(예: f(X) = β0 + β1X1 + … + βpXp). STEP 2: 훈련자료로 β를 추정(가장 흔한 방법은 OLS, 그러나 하나의 방법일 뿐) | f의 형태를 명시적으로 가정하지 않음 |
| 장점 | f 추정이 소수의 계수 추정으로 축소됨. 적은 자료로 가능, 해석 쉬움 | 더 넓은 범위의 f 형태를 정확히 적합 |
| 단점 | 모형이 틀리면 ε의 분산이 작아도 나쁜 답(wrong model) | 정확한 추정에 매우 많은 관측치가 필요 |
| 슬라이드 예 | Income ~ Education + Seniority 평면 | Thin-plate spline 곡면 |

#### 2.8 차원의 저주 (curse of dimensionality)

Nearest neighbor averaging은 p ≤ 4이고 N이 큰 경우에 잘 작동한다. p가 크면 이웃이 멀어져 성능이 나쁘다(lousy).

<!-- page 5 -->

분산을 낮추려면 N의 일정 비율(예: 10%)을 평균내야 하는데, 고차원에서 10% 이웃은 더 이상 local이 아니다. ESL Figure 2.6: 10차원에서 자료의 10%를 잡으려면 각 좌표 범위의 80%를 덮어야 한다.

슬라이드 연습문제: X, Y의 성분이 독립 N(0,1)이고 p가 매우 클 때 d(X, 0) ≈ √p, d(X, Y) ≈ √(2p), angle(X, Y) ≈ 90°. 결론: 고차원에서는 모든 점이 서로 비슷하게 멀고 거의 직교하므로 유클리드 거리로 "가깝다"를 정의하는 것이 의미를 잃는다.

#### 2.9 예측 정확도 vs 해석력 trade-off

유연한 모형이 더 현실적인데 왜 항상 쓰지 않나? 두 가지 이유.

1. 해석: 선형모형의 βj는 "다른 변수를 고정했을 때 Xj가 1단위 증가하면 Y가 평균적으로 βj만큼 증가"로 바로 읽힌다.

2. 예측만 목적이어도 단순한 모형이 더 정확할 때가 많다. 유연한 모형은 적합하기 어렵기 때문(과적합).

유연성이 올라가면 해석력이 떨어지는 순서: Subset selection · Lasso → Least squares → Generalized additive models · Trees → Bagging · Boosting · Support vector machines.

### 3. 용어 정리

같은 개념을 통계학과 컴퓨터과학이 다른 이름으로 부르므로, 교수님은 "용어 불일치를 받아들이고 생각하면서 책을 보라"고 했다. 먼저 대응표, 그 다음 개념 용어다.

**통계학 ↔ 컴퓨터과학(ML) 용어 대응**

| 통계학 | 기계학습 / 컴퓨터과학 | 뜻 |
| --- | --- | --- |
| Intercept (절편) | Bias | 선형모형의 상수항 β0 |
| Regression coefficient (회귀계수) | Weight | 각 입력에 곱해지는 계수 βj |
| Explanatory variable, predictor, covariate, independent variable | Input, feature | X |
| Response, outcome, dependent variable | Output, target, label | Y |
| Model, estimation, fitting | Algorithm, learning, training | 데이터로 f를 구하는 일 |
| Statistical learning | Machine learning | 각각 통계학 / AI의 하위분야에서 출발 |
| Statistician | Data scientist | 직업명의 변화 |

**개념 용어**

| 용어 | 정의 / 시험용 한 줄 |
| --- | --- |
| Statistical learning | 데이터를 이해하기 위한 방대한 도구 집합. 본질적으로 f를 추정하는 접근법들의 집합 |
| Supervised learning | X와 Y가 모두 있을 때 X로 Y를 예측하는 모형을 만드는 학습. Regression 과 classification |
| Unsupervised learning | 입력만 있고 outcome label이 없는 학습. Clustering, VAE, factor analysis |

<!-- page 6 -->

| 용어 | 정의 / 시험용 한 줄 |
| --- | --- |
| Reinforcement learning | 보상과 벌칙을 반복 경험해 보상을 최대화하는 행동 규칙을 학습. AlphaGo, 로보틱스 |
| Regression vs Classification | Y가 연속형(quantitative)이면 regression, 범주형(qualitative)이면 classification |
| Training data / Test data | f를 학습시키는 자료 / 학습에 쓰지 않고 성능을 평가하는 새 자료 |
| Y = f(X) + ε | f는 X가 Y에 주는 systematic information, ε은 평균 0이고 X와 독립인 random error |
| Irreducible error | f를 완벽히 알아도 남는 오차 Var(ε). 줄일 수 없음 |
| Reducible error | f̂가 f와 달라서 생기는 오차. 더 나은 방법으로 줄일 수 있음 |
| Prediction | Ŷ = f̂(X). f̂를 블랙박스로 취급해도 됨 |
| Inference | X가 변할 때 Y가 어떻게 변하는지 이해. f̂의 형태를 알아야 함 |
| Loss function | 예측 Ŷ와 실제 Y의 차이를 재는 함수. 연속형 표준은 squared error (L2) loss (Y − Ŷ)² |
| Risk | 손실의 기대값 E[(Y − f(X))²]. 이를 최소화하는 f가 최적 예측자 |
| Regression function | f(x) = E[Y \| X = x]. 제곱오차 손실 아래 최적 예측자(optimal predictor) |
| Nearest neighbor averaging | X = x인 점이 없으므로 이웃 N(x)의 Y 평균으로 E[Y\|X=x]를 근사: f̂(x) = Ave(Y \| X ∈ N(x)) |
| Hyperparameter (tuning parameter) | 이웃의 크기, 가중치 폭처럼 데이터로 추정하지 않고 분석자가 조정하는 값 |
| Parametric method | f의 형태를 가정한 뒤 모수(β)만 추정. 예: 선형회귀 + OLS |
| Non-parametric method | f의 형태를 가정하지 않음. 유연하지만 많은 관측치 필요. 예: thin-plate spline, KNN |
| Ordinary least squares (OLS) | 제곱오차합을 최소화해 β를 추정하는 가장 흔한 방법. 유일한 방법은 아님 |
| Flexibility | 모형이 만들어낼 수 있는 f 형태의 범위. 높을수록 해석력은 낮고 과적합 위험 |
| Interpretability | 모형을 사람이 이해할 수 있는 정도. 선형모형의 βj 해석이 대표 |
| Curse of dimensionality | 차원 p가 커지면 모든 점이 서로 멀어져 "이웃"이 더 이상 local이 아니게 되는 현상 |
| Overfitting (과적합) | 훈련자료의 noise까지 따라가 새 자료에서 성능이 떨어지는 것. 유연한 모형일수록 위험 |
| Causal inference | 개입의 효과를 묻는 분야. Counterfactual prediction이라는 다른 사고가 필요 |
| Counterfactual | 같은 조건에서 처치만 달랐다면 나타났을 가상의 outcome |
| Interventional prediction | X를 바꿨을 때 Y가 바뀔지를 예측. 단순 예측과 다름 |
| Propensity score | 처치받을 확률. 최근에는 boosting 같은 ML로 구성 |
| Causal ML (double ML) | 인과추론과 기계학습을 결합한 최근 분야 |

<!-- page 7 -->

| 용어 | 정의 / 시험용 한 줄 |
| --- | --- |
| xAI (explainable AI) | 블랙박스 모형의 변수 중요도·예측 근거를 설명하려는 분야 |
| Kernel machine | 수백 개 혼합 노출 변수처럼 복잡한 입력을 다루는 비선형 방법. 환경역학 tailoring 예 |
| Multimodal data | 표·텍스트·이미지·유전체 등 서로 다른 형태의 데이터가 섞인 자료 |
| Vectorization | 텍스트·이미지 같은 비정형 입력을 벡터 X로 바꾸는 것. 이웃 정보 보존이 핵심 |
| Bootstrap, FDR | Efron이 개발한 재표본 방법과 다중검정 오류 통제(13주차 예정) |
| Calibration / Discrimination /Generalization | ML 쪽 성능 평가 개념: 예측확률의 정확성 / 양·음 구별력 / 새 자료에서의 성능 유지 |

### 4. 교수님이 강조한 포인트 (녹음 기반)

녹음 세 토막(약 135분)을 Whisper로 받아썼다. 교실 녹음이라 음질이 낮아 전체의 절반 정도만 알아들을 수 있었고, 아래는 녹음과 강의노트가 서로 뒷받침하는 내용만 추렸다. 표시한 시각은 각 녹음 파일 안의 위치다.

**시험·평가 방식에 대한 말 (강의2 앞부분 10분을 통째로 할애함)**

시험 중 AI 사용 허용 여부는 아직 미정이며, 중간고사(7주차) 전에 학생들과 상의해 정한다. 허용할 경우 시험을 인터뷰 형태로 바꿀 가능성도 언급했다(강의2 03:03~03:36).

비유: "아이언맨 수트를 입은 상태를 평가할지, 수트를 벗긴 상태를 평가할지"가 고민. 현재 시점에서 AI 허용 시험은 과거의 오픈북 시험과 같은 의미라고 본다(00:58, 05:04~05:29).

AI를 허용하면 학교에서 제공하는 ChatGPT Edu 버전을 기본으로 통일한다. 유료·무료 모델 성능 차이가 시험 불평등으로 이어지는 것을 우려했다(05:47~06:36).

AI를 써도 되는 상황에서 AI의 틀린 출력을 검증 없이 그대로 제출하면 "굉장히 강력하게" 감점한다. AI 출력을 비판적으로 검토하는 태도 자체가 평가 요소다(03:44~04:22, 07:38~08:05).

평가 항목은 출석, 중간, 기말, 프로젝트 발표이고 동료 평가가 들어간다(강의1 07:42~08:46).

프로젝트는 약 25명을 3~4명씩 난수로 랜덤 편성하고, 데이터셋 분석 후 요약보고서와 발표로 평가한다. 데이터 선택에 제한은 없다(강의1 08:46~10:05, 14:02).

AI 도구는 과제·프로젝트에서 자유롭게 쓰되 어떤 도구를 어떤 목적으로 어느 범위까지 썼는지 반드시 보고한다. "개발자로 크려면 AI가 하는 것을 넘어서는 능력이 필요하다"(강의1 11:12~13:03).

**반복해서 강조한 개념 (시험 출제 가능성 높음)**

1. 제곱오차 손실의 최적 예측자는 E[Y|X=x]. 전개는 "중학교 수준의 완전제곱 전개"라며 직접 해보고 막히면 GPT에게 물어보라고 했다. 결론은 "어떤 문제든 예측을 제일 잘하려면 X가 주어졌을 때 Y의 평균으로 가면 된다"(강의3 17:09~21:25).

2. 회귀분석에서 배운 모형 Y = Xβ + ε은 기계학습 관점에서 보면 이 예측 문제를 선형 parametric으로 풀어놓은 솔루션이다. 통계학은 "X가 1단위 움직이면 Y가 β만큼"이라는 해석을 위해 상호작용·제곱항을 피했지만, 예측만 할 때는 해석이 필요 없으니 f를 얼마든지 복잡하게 해도 된다(강의3 21:51~23:54).

<!-- page 8 -->

3. 이웃 평균 → 이웃 폭을 튜닝 → 거리에 따른 가중치(kernel)는 모두 E[Y|X=x]를 근사하는 방법의 변형이다. "결국 어떤 방법이든 X 근처에서 Y의 평균을 구하는 것"(강의3 25:07~29:17).

4. 통계학의 힘은 불확실성을 정량화하는 것. "신뢰구간을 제시하는 무속인은 없다. 제시하는 순간 틀리면 버려지기 때문이고, 그 검증을 거쳐 살아남은 것이 과학이다"(강의1 44:04~45:00).

5. 예측에 중요한 변수와 개입 효과가 있는 변수는 다르다. 라이터 예는 강의3 끝(33:15~34:00)과 강의노트 13~14쪽에 모두 나온다.

6. "하나의 도구가 만능인 경우는 없다. 여러 도구를 알고 문맥에 맞게 꺼내 쓰는 것이 중요하다." 문제가 오면 딥러닝부터 쓰지 말고 단순하고 빠른 방법부터(강의2 26:16~26:23, 44:27~44:52).

7. 강화학습의 문제는 보상 설계에서 오고, "그 원인은 인간"이다. Atari 벽돌깨기와 비행기 게임 셧다운 예(강의2 33:55~40:38).

8. 보건 데이터는 엑셀형을 넘어 이미지 등 비정형으로 다양해지고 있고, 이를 설명변수(벡터)로 만드는 데 생성형 AI가 효과적이다(강의3 00:00~01:24).

**공부 태도에 대한 당부**

교재를 종교처럼 받아들이지 말 것. 교재가 "이 방법이 제일 좋다"고 하는 것은 저자의 선택이며 역사적·우연적 이유가 많다. 예로 p = 0.05도 절대적이 아니다(0.005를 제안한 논문이 있다). "교수가 하는 말도 종교적으로 받아들이지 마라"(강의3 29:57~33:11).

행렬과 기초 미적분(로그·지수 미분)은 수업에서 따로 가르치지 않으니 미리 공부할 것. "세상 모든 데이터 사이언스의 기본은 행렬"(강의1 20:36~23:10).

본인이 데이터를 직접 분석할 수 있어야 데이터 사이언스 능력이 올라간다. 도구는 R/Python, 큰 데이터는 SAS(강의1 24:02~26:20).

Breiman(2001), Efron(2020), Shmueli(2010) 논문은 직접 읽을 것. 논문 요약을 제출하는 것보다 본인이 소화해서 말하는 것이 좋다(강의2 09:18~09:46).

6주차에 나올 Reproducing Kernel Hilbert Space(RKHS)를 미리 언급했다. 커널 방법은 교수님의 관심 분야이므로 환경역학 kernel machine 예와 함께 기억해 둘 것(강의3 31:10~32:04).

### 5. 예상 시험 문제와 모범 답안

중간고사는 7주차다(강의계획서). 1차시 범위에서는 개념 구분(통계 vs ML, 지도 vs 비지도, 예측 vs 추론, 모수 vs 비모수)과 E[Y|X] 유도, 차원의 저주, trade-off 설명이 나올 가능성이 높다. 답안을 가리고 먼저 풀어 본 뒤 비교하자.

**객관식 / OX**

1. 다음 중 2000년 이전 통념에서 기계학습 쪽의 특징이 아닌 것은? (a) 예측 정확도 중시 (b) 큰 데이터 (c) 높은 해석력 (d) 높은 모형 복잡도

답: (c). 해석력이 높은 쪽은 통계학이다.

2. OX: 제곱오차 손실 아래에서 Y의 최적 예측자는 조건부 중앙값 E[Y|X=x]이다.

답: X. 조건부 기대값(평균)이다. 중앙값은 절대오차(L1) 손실의 최적 예측자다.

3. 다음 중 unsupervised learning은? (a) 암 유무 분류 (b) 설문 문항으로 잠재 개념 추출 (c) 집값 예측 (d) AlphaGo

답: (b). (a)(c)는 supervised, (d)는 reinforcement.

4. OX: 비모수적 방법은 f의 형태를 가정하지 않으므로 적은 자료로도 정확하다.

답: X. 형태를 가정하지 않는 대신 매우 많은 관측치가 필요하다.

<!-- page 9 -->

5. 통계학의 intercept와 regression coefficient를 컴퓨터과학에서 부르는 이름은?

답: bias, weight.

6. OX: 예측에 기여도가 높은 변수는 개입 효과도 크다.

답: X. 라이터 소지는 폐암의 강한 예측변수지만 라이터를 금지해도 폐암은 줄지 않는다. 예측과 인과는 다른 문제다.

7. 유연성이 가장 낮고 해석력이 가장 높은 방법은? (a) Bagging (b) SVM (c) Lasso / Subset selection (d) GAM

답: (c).

8. OX: 데이터가 충분히 많으면 유연한 모형이 항상 단순한 모형보다 예측을 잘한다.

답: X. 유연한 모형은 적합이 어려워 과적합할 수 있고, 단순한 모형이 더 정확한 경우가 많다 (Reason 2).

**단답형**

1. Y = f(X) + ε에서 ε에 대해 가정하는 두 가지는?

평균이 0이고, X와 독립이다.

2. f를 추정하는 두 가지 이유는?

Prediction과 Inference.

3. Statistical learning의 한 줄 정의는?

데이터를 이해하기 위한 도구의 집합이며, 본질적으로 f를 추정하는 접근법들의 집합.

4. 모수적 방법의 두 단계는?

STEP 1: f의 함수 형태 가정(모형 설정). STEP 2: 훈련자료로 모수 추정(예: OLS).

5. Nearest neighbor averaging이 잘 작동하는 조건은?

p가 작고(p ≤ 4) N이 클 때.

6. 10차원에서 자료의 10%를 포함하는 이웃을 만들려면 각 좌표 범위의 몇 %를 덮어야 하나?

약 80%. (0.1^(1/10) ≈ 0.79)

7. Efron(2020) 논문 제목의 세 키워드는?

Prediction, Estimation, Attribution.

8. 컴퓨터과학이 성숙시킨 문제 유형과, 컴퓨터과학에서 잘 다루지 않는 보건학 자료 유형은?

Classification / 생존분석(censored) 자료.

9. 통계학이 불확실성을 표현하는 대표 도구 두 가지는?

표준오차(standard error)와 신뢰구간(confidence interval).

**서술형**

1. 제곱오차 손실 아래에서 최적 예측자가 E[Y|X=x]임을 유도하고, 이 결과가 실제 추정에서 어떤 어려움으로 이어지는지 설명하시오.

모범답안: 임의의 f에 대해 (Y − f(x))² = (Y − E[Y|x] + E[Y|x] − f(x))²로 쓰고 X = x 조건부 기대값을 취하면 교차항은 E[Y − E[Y|x] | x] = 0이므로 사라지고, E[(Y − f(x))²|x] = Var(Y|x) + (E[Y|x] − f(x))²가 된다. 첫 항은 f와 무관한 irreducible error이고 둘째 항은 f(x) = E[Y|x]일 때 0이 되므로 최적 예측자는 조건부 평균이다. 실제로는 X = x인 관측치가 거의 없어 조건부 평균을 직접 계산할 수 없다. 그래서 이웃 N(x)의 평균으로 완화하거나(nearest neighbor, kernel smoothing) f의 형태를 가정한다(모수적 방법). 전자는 차원이 커지면 이웃이 local이 아니게 되는 차원의 저주에 부딪히고, 후자는 가정이 틀리면 나쁜 답을 준다.

<!-- page 10 -->

2. 통계학과 기계학습의 차이를 역사적 배경(데이터의 출처)과 함께 설명하고, 오늘날 그 경계가 어떻게 변했는지 서술하시오.

모범답안: 통계학은 농업 실험처럼 1년에 한 번 얻는 소수의 관측치로 인과성을 탐구하려 했기 때문에 표준오차와 신뢰구간으로 불확실성을 정량화하는 것이 핵심이었고, 가설검정·해석·인과성을 중시하며 단순한 선형모형을 주로 썼다. 기계학습은 공장·웹에서 축적되는 대량 데이터에서 출발해 n이 매우 크므로 표준오차는 중요하지 않고 예측 정확도가 중요했으며, random forest처럼 복잡한 블랙박스 모형을 써 해석력은 낮았다. 2000년대 초 큰 데이터를 다루게 되면서 두 분야는 서로의 도구를 흡수했다. 통계학은 유연한 모형을, 기계학습은 불확실성 평가와 변수 해석(xAI)을 받아들여 오늘날 경계는 거의 무너졌다. 보건학 문제는 여전히 "왜"를 묻는 질문이 많아 통계적 접근이 중요하지만, 예측 도구도 필요하다.

3. Prediction과 Inference의 차이를 예를 들어 설명하고, 보건학에서 예측 모형을 정책 개입에 그대로 쓰면 안 되는 이유를 서술하시오.

모범답안: Prediction은 새 X에 대한 Y를 맞히는 것이 목적이며 f̂를 블랙박스로 취급해도 된다 (direct mailing: 400개 변수 중 어느 것이 중요한지는 관심 없고 누구에게 보낼지만 관심). Inference는 X가 변할 때 Y가 어떻게 변하는지 이해하는 것이 목적이며 f̂의 형태와 각 변수의 효과 방향·크기를 알아야 한다(housing: river view가 집값에 얼마나 영향). 예측 모형에서 기여도가 높은 변수는 상관관계를 반영할 뿐 개입 효과를 보장하지 않는다. 라이터 소지는 흡연의 대리변수라서 폐암을 잘 예측하지만, 라이터를 금지해도 폐암은 줄지 않는다. 정책 개입은 "X를 바꿨을 때 Y가 바뀔까"라는 counterfactual(interventional) prediction이므로 인과추론의 사고와 강한 domain knowledge가 필요하다.

4. 모수적 방법과 비모수적 방법의 장단점을 비교하고, 유연한 모형이 더 현실적임에도 단순한 모형을 먼저 쓰는 이유를 두 가지 이상 서술하시오.

모범답안: 모수적 방법은 f의 형태를 가정해 문제를 소수의 계수 추정으로 축소하므로 적은 자료로 가능하고 해석이 쉽지만, 가정이 틀리면 ε의 분산이 작아도 나쁜 답을 준다. 비모수적 방법은 형태 가정이 없어 넓은 범위의 f를 정확히 적합하지만 매우 많은 관측치가 필요하다. 단순한 모형을 먼저 쓰는 이유는 (1) 선형모형의 βj처럼 해석이 바로 되어 inference에 유리하고, (2) 예측만 목적이어도 유연한 모형은 적합이 어려워 과적합으로 예측이 나빠질 수 있으며, (3) 교수님이 강조한 실무 이유로 단순하고 빠른 모형으로 결과가 기대치에 얼마나 못 미치는지 빠르게 판단한 뒤 복잡한 모형으로 옮겨가는 것이 프로젝트에서 효율적이기 때문이다.

5. 차원의 저주를 설명하시오. 성분이 독립 N(0,1)인 p차원 벡터 X, Y에 대해 d(X,0), d(X,Y), angle(X,Y)가 p가 커질 때 어떻게 되는지 근거와 함께 쓰시오.

모범답안: ||X||² = ΣXi²은 평균 p인 최대크기 항들의 합이므로 대수의 법칙에 의해 d(X,0) ≈ √p. X − Y의 성분은 N(0,2)이므로 d(X,Y) ≈ √(2p). 내적 X·Y = ΣXiYi는 평균 0, 분산 p이므로 cos(angle) = X·Y/(||X|| ||Y||) ≈ O(√p)/p → 0, 즉 angle ≈ 90°. 결론: 고차원에서는 임의의 두 점이 모두 비슷하게 멀고 거의 직교하므로 "가까운 이웃"이 존재하지 않고, N의 10%를 포함하는 이웃은 더 이상 local이 아니다. 따라서 국소 평균으로 E[Y|X=x]를 추정하는 nearest neighbor 방법은 p가 클 때 실패하며, 구조를 가정하는 모형이나 kernel·spline smoothing 같은 대안이 필요하다.

6. Supervised, unsupervised, reinforcement learning을 정의하고 각각 보건학 예를 하나씩 들며, unsupervised learning의 평가가 어려운 이유를 쓰시오.

모범답안: Supervised는 입력 X와 정답 Y가 있어 X→Y의 f를 학습한다(나이·성별·교육수준으로 암 발생 예측, 영상으로 암 유무 분류). Unsupervised는 Y 없이 X만으로 비슷한 개체를 묶거나 잠재 구조를 찾는다(설문 수십 문항에서 울분 같은 잠재 개념 추출, 환자 프로파일 군집화). Reinforcement는 보상과 벌칙을 반복 경험해 보상을 최대화하는 정책을 학습한다(치료 순서 최적

<!-- page 11 -->

화, 로보틱스). Unsupervised는 gold standard인 Y가 없어 "잘했는지"를 재는 기준이 없고 목적 자체가 fuzzy하기 때문에 평가가 어렵다.

### 6. 셀프 체크리스트

아래 항목을 보지 않고 말로 설명할 수 있으면 체크한다. 설명이 막히면 섹션 2의 해당 번호로 돌아간다.

**통계학 vs 기계학습 (2.1~2.2)**

- [ ] 통계학과 ML의 2000년 이전 차이 다섯 가지(관심·데이터 크기·복잡도·추론 도구·해석력)를 표로 그릴 수 있다.

- [ ] 통계학이 농업 데이터에서, ML이 대량 데이터에서 출발했다는 점이 왜 "불확실성 vs 예측 정확도"차이로 이어지는지 설명할 수 있다.

- [ ] intercept/bias, coefficient/weight, predictor/feature, response/label 대응을 안다.

- [ ] "ML은 AI의 하위분야, statistical learning은 통계학의 하위분야, 둘은 교집합이 크다"를 그림으로 그릴 수 있다.

- [ ] Breiman, Efron, Shmueli 세 논문의 제목과 핵심 주장을 한 줄씩 말할 수 있다.

- [ ] 보건학에서 ML을 그대로 가져다 쓰면 안 되는 이유(tailoring, 공정성, 프라이버시)를 예와 함께 말할 수 있다.

**학습의 유형 (2.3)**

- [ ] Supervised / unsupervised / reinforcement를 "무엇이 있고 무엇이 없는가"로 구분할 수 있다.

- [ ] Regression과 classification을 Y의 유형으로 구분하고 보건학 예를 하나씩 든다.

- [ ] Unsupervised learning의 평가가 왜 어려운지 말할 수 있다.

- [ ] 강화학습의 보상 설계가 왜 위험할 수 있는지 예를 들 수 있다.

**f 추정과 손실함수 (2.4~2.6)**

- [ ] Y = f(X) + ε의 각 기호와 ε의 두 가지 가정을 말할 수 있다.

- [ ] Prediction과 inference의 차이를 direct mailing / housing 예로 설명할 수 있다.

- [ ] "라이터 예"로 예측 변수와 개입 변수가 다름을 설명할 수 있다.

- [ ] 제곱오차 손실 아래 최적 예측자가 E[Y|X=x]임을 백지에 유도할 수 있다(교차항이 0이 되는 이유 포함).

- [ ] Irreducible error와 reducible error를 구분한다.

- [ ] 제곱 손실이 표준이 된 이유와 OLS와의 연결을 말할 수 있다.

- [ ] Nearest neighbor averaging의 식 f̂(x) = Ave(Y|X∈N(x))을 쓰고 hyperparameter가 무엇인지 말할 수 있다.

- [ ] 이미지·텍스트를 벡터화하는 전통 방식과 그 한계(이웃 정보 손실)를 설명할 수 있다.

**모수·비모수, 차원의 저주, trade-off (2.7~2.9)**

- [ ] 모수적 방법의 2단계와 장단점, 비모수적 방법의 장단점을 말할 수 있다.

- [ ] "표준편차가 작아도 틀린 모형이면 나쁜 답"이 무슨 뜻인지 설명할 수 있다.

- [ ] 차원의 저주를 "10% 이웃이 local이 아니다"와 "10차원에서 80%"로 설명할 수 있다.

- [ ] d(X,0) ≈ √p, d(X,Y) ≈ √(2p), angle ≈ 90°를 근거와 함께 유도할 수 있다.

<!-- page 12 -->

- [ ] 유연한 모형을 항상 쓰지 않는 두 가지 이유를 말할 수 있다.

- [ ] Lasso → Least squares → GAM/Trees → Bagging/Boosting/SVM의 유연성 순서를 그릴 수 있다.

**시험 전 마무리**

- [ ] 섹션 5의 서술형 6문을 답안 안 보고 각 10분 안에 쓴다.

- [ ] Chap2 Part II(Assessing model accuracy: MSE, training vs test, bias-variance)가 2차시 범위이므로이어서 정리한다.

- [ ] Efron(2020)과 Shmueli(2010) 논문의 초록을 한 번씩 읽어본다.
