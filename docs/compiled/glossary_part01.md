<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 용어 정리 모음 (학기 용어집) (1/2)

> 원본: `docs/week*/study_guide_*.md` · 변환 방식: compiled · 생성일: 2026-10-24 · 8개 차시
> [다음 부분 ▶](glossary_part02.md) · [주차 인덱스](../../INDEX.md) · [전체 인덱스](../../INDEX.md)

---
> 각 차시의 용어 정리 절을 모은 학기 용어집. 각 차시 학습자료(요약본, 없으면 전체판)에서 자동 추출 · 생성일 2026-10-24 · [전체 인덱스](../../INDEX.md)


## 1차시 (2026-09-02) — 과목 소개 · Chap1 Introduction · Chap2 Part I (Statistical Learning)

_출처: [study_guide_summary.md](../week01_20260902/study_guide_summary.md) · [주차 인덱스](../week01_20260902/README.md)_

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


| 용어 | 정의 / 시험용 한 줄 |
| --- | --- |
| xAI (explainable AI) | 블랙박스 모형의 변수 중요도·예측 근거를 설명하려는 분야 |
| Kernel machine | 수백 개 혼합 노출 변수처럼 복잡한 입력을 다루는 비선형 방법. 환경역학 tailoring 예 |
| Multimodal data | 표·텍스트·이미지·유전체 등 서로 다른 형태의 데이터가 섞인 자료 |
| Vectorization | 텍스트·이미지 같은 비정형 입력을 벡터 X로 바꾸는 것. 이웃 정보 보존이 핵심 |
| Bootstrap, FDR | Efron이 개발한 재표본 방법과 다중검정 오류 통제(13주차 예정) |
| Calibration / Discrimination /Generalization | ML 쪽 성능 평가 개념: 예측확률의 정확성 / 양·음 구별력 / 새 자료에서의 성능 유지 |


## 2차시 (2026-09-09) — Chap2 Part I 복습(f 추정, parametric/non-parametric, KNN·차원의 저주) · Chap2 Part II(MSE, Bias-Variance, Bayes classifier) · Efron 논문 발표

_출처: 시험대비 학습자료(전체판)(비공개, 로컬 private/ 폴더) · [주차 인덱스](../week02_20260909/README.md)_

### 8. 핵심 개념 한 장 요약표 + 용어표

**추가 설명 (Claude 보충, 교수님 말씀 아님)**

이 장의 출처 — 아래 요약표와 용어표는 제가 1~7장의 내용(교수님 말씀 + 교재)을 시험용으로 압축한 것이다. 개별 문장의 원출처는 1~7장의 색 박스를 따른다. 출처 열의 "노트"는 강의노트 쪽수, "슬"은 슬라이드 번호, "ISLR"은 책 쪽수.

#### 8.1 한 장 요약

| 질문 | 답 (시험용 한 줄) | 출처 |
| --- | --- | --- |
| 회귀함수 f(x)는 무엇이고 왜 "최적"인가? | f(x) = E(Y\|X=x). 제곱오차 E[(Y−g(X))²\|X=x]를 모든 g 중에서 최소화하는 함수 | Part I 슬7, 노트 p.18 |
| Parametric 방법의 2단계는? | ① f의 함수형 가정(예: 선형 f = β0+β1X1+…+βpXp) ② 훈련자료로 모수 추정(보통 OLS). f 추정이 p+1개 계수 추정으로 축소 | 슬20~21, ISLR p.21 |
| "선형"모형이 직선만 뜻하나? | 아니다. 계수에 대해 선형이면 된다. x², log x, √x, 교호항을 넣으면 곡선·곡면도 표현. 단, 그러면 "x1이 1 증가 → y가 β1 증가"식 해석은 깨진다 | 노트 p.19 |
| ML 관점에서 회귀 문제는? | Ŷ = f(x), L(y,f(x)) = (y−f(x))²의 총합(평균)을 최소화하는 f를 찾는 문제. 손실 함수를 갈아 끼우면 다른 문제가 된다 | 노트 p.19, 30 |
| Non-parametric 방법의 장단점? | 함수형 가정 없음 → 넓은 형태 적합(장점). 매우 많은 관측치 필요, 고차원에서 취약(단점). 데이터가 많으면 non-parametric | 슬23, 노트 p.21, ISLR p.23 |
| 왜 non-parametric이 결국 선형모형처럼 표현되나? | 함수가 매끄러우면 Taylor 전개 f(x) ≈ f(0)+f'(0)x+f''(0)x²/2+…로 적절한 차수의 다항식(=선형모형)으로 근사되기 때문 | 노트 p.21 |
| KNN 회귀란? | x에서 가장 가까운 k개 관측의 y 평균으로 E(Y\|X=x)를 추정: f̂(x) = Ave(Y\|X∈N(x)). k는 hyperparameter(tuning parameter) | 슬25, 노트 p.22~23 |
| k가 작을 때/클 때? | k=1: 점을 잇는 지그재그(과적합, low bias·high variance). k=n: 전체 평균의 평평한 선(high bias·low variance) | 노트 p.23, ISLR p.40 |
| 차원의 저주란? | p가 크면 "가까운 이웃"이 local하지 않다. 단위 입방체에서 자료의 r 비율을 잡으려면 변의 길이 r^(1/p): r=0.1, p=2→0.32, p=3→0.46, p=10→0.79, p=100→0.98 | 슬26~27, 노트 p.23~24 |
| 고차원에서 거리·각도는? | 성분이 N(0,1)이면 d(X,0)≈√p, d(X,Y)≈√(2p), 두 벡터는 거의 직교(90°). LLN(과 CLT)로 설명. 모든 점이 비슷하게 멀어 이웃 평균이 부담 | 슬28, 노트 p.25 |
| 유연한 방법을 항상 쓰지 않는 두 이유? | ① 해석력: 선형모형의 βⱼ = 다른 변수 고정 시 Xⱼ 1단위 증가당 Y 평균 증가 ② 예측만 목적이어도 단순 모형이 더 정확할 수 있음(과적합·표본 수) | 슬29~30, 노트 p.26~28, ISLR p.25~26 |
| 유연성–해석력 지도 순서? | Subset selection·Lasso(해석↑) → Least squares → GAM·Trees → Bagging·Boosting → SVM(유연↑). 딥러닝은 더 오른쪽 | 슬31, 노트 p.27 |
| 교수님이 강조한 표본 수 이야기? | 표본 수에 따라 허용되는 모형 복잡도가 제한된다. 50~100개면 유연한 모형은 돌아가도 성능 기대 못 함. 암·희귀질환처럼 표본이 적으면 단순 모형이 잘 작동할 때가 많다 | 노트 p.28 |
| 통계학 vs ML이 보는 회귀의 차이? | Stat: βⱼ, β,̂ s.e., 신뢰구간. ML: Ŷ = xβ(̂예측) | 노트 p.29 |
| 문헌을 읽을 때 가장 먼저 볼 것? | Loss function. 연구자가 어떤 오차를 줄이려 하는지, 문제를 어떻게 정의했는지가 거기 있다 | 노트 p.30 |


| 질문 | 답 (시험용 한 줄) | 출처 |
| --- | --- | --- |
| MSE 정의와 training/test 구분? | MSE = (1/n)Σ(yᵢ−f̂(xᵢ))². 훈련자료로 계산하면 training MSE. 정말 중요한 것은 훈련에 쓰지 않은 (x0,y0)에 대한 test MSE = Ave(y0−f̂(x0))² | 슬3~4, ISLR p.29~30 |
| Generalization vs generalizability(교수님 용어)? | Generalization: 같은 분포의 자료를 나눠 훈련/시험했을 때 잘 되는 것. Generalizability: 다른 시기·다른 인구집단(2026→2027년, 한국→미국)에서도 잘 되는 것. 후자는 훨씬 어렵고 weighting·modification 전략이 필요 | 노트 p.30 |
| 유연성이 커질 때 training/test MSE? | training MSE는 단조 감소(변수를 늘리면 0까지 가능, interpolation). test MSE는 U자: 처음 감소 후 다시 증가. 최소점이 best prediction, 그 위치를 hyperparameter로 찾는 것이 과제 | 슬5~6, 노트 p.31~32, ISLR p.31~32 |
| Overfitting이란? | 교수님: 훈련자료를 너무 따라가 오차 ε까지 적합한 것. 교재: training MSE 는 작은데 test MSE가 큰 상태, 특히 덜 유연한 모형이 더 작은 test MSE를 줬을 경우 | 노트 p.32, ISLR p.32 |
| 세 예(그림 2.9~2.11)의 교훈? | 참 f가 거의 선형이면 선형회귀가 최선, 매우 비선형이면 유연한 모형이 최선. test MSE 최소점의 유연성은 자료마다 다르다 → 실제로는 교차검증(5 장)으로 추정 | 슬6~8, 노트 p.33, ISLR p.33 |
| Bias와 variance 정의? | Bias: 복잡한 실제 문제를 단순 모형으로 근사해 생기는 오차(유연할수록↓). Variance: 훈련자료가 바뀔 때 f̂이 변하는 정도(유연할수록↑) | 슬10~11, ISLR p.34~35 |
| 기대 test MSE 분해식? | E(y0−f̂(x0))² = [Bias(f̂(x0))]² + Var(f̂(x0)) + Var(ε). ε이 f̂과 독립·평균 0이라 교차항 0. test MSE는 Var(ε) 아래로 못 내려감. 교수님: "꼭 유도해 보라" | 슬12, 노트 p.36, ISLR p.34 |
| U자가 생기는 이유? | 유연성↑ 초기에는 bias가 variance 증가보다 빨리 줄어 test MSE↓, 이후 bias는 거의 안 줄고 variance가 크게 늘어 test MSE↑. "U shape은 universal" | 노트 p.34, 36, ISLR p.35 |
| 분류에서 정확도 척도? | Error rate = (1/n)ΣI(yᵢ≠ŷᵢ) (0-1 loss의 평균). 틀리면 1점 벌점. 미분 불가하지만 직관적. 문제 맥락에 맞는 loss를 고르는 것이 중요 | 슬14, 노트 p.37, ISLR p.37 |
| Bayes classifier와 Bayes error rate? | P(Y=j\|X=x0)가 가장 큰 범주로 분류(이진이면 P(Y=1\|x) > 1/2 → 1). 0-1 손실의 기대값을 최소화. 그 오류율 1−E[maxⱼP(Y=j\|X)]이 Bayes error rate(=분류판 irreducible error). 실제로는 계산 불가한 금본위. "베이즈 통계와는 상관없다" | 슬15~16, 노트 p.38, ISLR p.37~39 |
| 확률 추정 vs 결정경계 추정? | 확률 P(Y=1\|x)를 모형화하는 쪽(로지스틱 회귀와 그 변형) vs 경계만 찾는 쪽(SVM, 확률 해석 없음). "큰 역사의 분기점" | 노트 p.38 |
| KNN 분류란? | x0의 최근접 K개 중 범주 j의 비율로 P(Y=j\|x0)를 추정하고 다수결(k=5에서 1이 3개면 1). K가 작을수록 유연. K=1이면 훈련오류 0이지만 test error는 높을 수 있음 | 슬17~20, 노트 p.39, ISLR p.39~40 |
| 근본적인 그림 (fundamental picture)? | 가로 모형 복잡도, 세로 예측오차. 훈련오차는 계속 감소, 시험오차는 U자 (왼쪽 high bias·low variance, 오른쪽 low bias·high variance). "더 복잡한 것이 항상 더 좋지는 않다" | 슬21~22, 노트 p.37, 43 |
| 현대판(2019) trade-off? | Belkin 외: interpolation threshold(훈련오차 0)를 넘어 더 과모수화하면 test risk가 다시 내려가는 double descent. 교수님: "2019년에 (고전적 그림이) 깨짐, technical함" | 슬23, 노트 p.32, 44 |

#### 8.2 용어표

| 용어 | 뜻 | 출처 |
| --- | --- | --- |
| Training data (훈련자료) | f를 추정(train, 통계용어로 estimation)하는 데 쓰는 {(x1,y1),…,(xn,yn)} | 슬18, 노트 p.30, ISLR p.21 |


| 용어 | 뜻 | 출처 |
| --- | --- | --- |
| Test data (시험자료) | f̂을 구할 때 쓰지 않은 새 자료 (x0,y0); 노트에서는 별표(*)로 표시 | 슬4, 노트 p.30 |
| Parametric / Non-parametric | f의 함수형을 가정하고 모수를 추정 / 함수형을 가정하지 않고 데이터를 따라감 | 슬20, 23 |
| OLS (ordinary least squares) | 잔차 제곱합을 최소화해 선형모형 계수를 구하는 가장 흔한 방법 | 슬21 |
| L2 loss, squared error loss | L(y,f(x)) = (y−f(x))². 회귀의 표준 손실 | 노트 p.19 |
| Loss function (손실함수) | 예측이 틀렸을 때의 벌점을 정의하는 함수. 연구자가 문제를 정의하는 곳. 문헌에서 가장 먼저 확인 | 노트 p.30, 37 |
| Hyperparameter / tuning parameter | KNN의 k, spline의 매끄러움처럼 모형 복잡도를 조절하는 값. 기분이 아니라 test MSE 최소화로 정함 | 노트 p.23, 32 |
| Neighborhood N(x) | x 근방의 관측 집합. KNN에서는 가장 가까운 k개 | 슬25 |
| Curse of dimensionality (차원의 저주) | p가 크면 국소 이웃이 더 이상 local하지 않고, 거리·각도가 모두 비슷해지는 현상 | 슬26~28, 노트 p.23~25 |
| LLN / CLT | 큰수의 법칙(표본평균→기댓값) / 중심극한정리. 교수님: "둘은 알아두라" | 노트 p.25 |
| Interpretability (해석력) | 변수 변화가 Y에 주는 효과를 사람이 읽을 수 있는 정도. 공식 정의는 없음(교수님) | 슬29, 노트 p.27 |
| Explainable AI, LIME | 유연한 모형의 예측을 국소적으로 설명하는 기법. LIME은 특정 점 근처에서 lasso 등 단순 모형을 적합 | 노트 p.28 |
| MSE (mean squared error) | (1/n)Σ(yᵢ−ŷᵢ)². training MSE와 test MSE를 구분 | 슬3, ISLR p.29 |
| Overfitting (과적합) | 오차까지 적합해 새 자료를 못 맞히는 상태; training MSE 작고 test MSE 큼 | 노트 p.32, ISLR p.32 |
| Interpolation (내삽) | f̂이 모든 훈련점을 정확히 지나 training MSE = 0이 된 상태 | 노트 p.32, 슬23 |
| Generalization / Generalizability | 같은 분포 안에서의 일반화 / 다른 시기·집단으로의 이전 가능성 (교수님 구분) | 노트 p.30 |
| Bias / Variance | 단순화에서 오는 체계적 오차 / 훈련자료 변화에 따른 f̂의 변동 | 슬10~11 |
| Irreducible error Var(ε) | f를 완벽히 알아도 남는 오차. test MSE의 하한(점선) | 슬6, 12, ISLR p.18, 34 |
| Error rate (오분류율) | (1/n)ΣI(yᵢ≠ŷᵢ). 0-1 loss의 평균 | 슬14 |
| 0-1 loss | 틀리면 1, 맞으면 0. 미분 불가. 표준적이지만 유일한 선택은 아님 | 노트 p.37 |
| Bayes classifier / Bayes decision boundary / Bayes error rate | 조건부확률 최대 범주로 분류 / P=1/2인 점들의 경계 / 그때의 최소 오류율 | 슬15~16, ISLR p.37~39 |
| Decision boundary | 두 범주의 예측이 갈리는 경계. SVM 등은 확률 없이 경계만 추정 | 노트 p.38 |
| KNN (K-nearest neighbors) | 회귀: 이웃 평균 / 분류: 이웃 다수결. K가 작을수록 유연 | 슬17, 25 |
| Double descent | 보간 임계점 이후 test risk가 다시 감소하는 현대적 현상 (Belkin 외 2019) | 슬23 |




## 3차시 (2026-09-16) — Chap2 Part II 마무리 · Double descent 발표 · Chap3 Linear Regression(두 관점·likelihood·추론·변수선택·KNN 비교) · 회귀→경사하강→신경망 · Chap4 분류 시작(로지스틱, MLE·cross-entropy)

_출처: [study_guide_summary_part01.md](../week03_20260916/study_guide_summary_part01.md) · [주차 인덱스](../week03_20260916/README.md)_

### 3. 용어 정리

| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| MSE (mean squared error) | (1/n)Σ(yᵢ−ŷᵢ)²; 훈련 MSE vs 테스트 MSE | S003 |
| Flexibility / complexity / capacity | 모델이 만들 수 있는 함수 모양의 다양성(자유도); KNN 은 1/K | S005, S023 |
| Irreducible error | Var(ε); 어떤 방법도 넘을 수 없는 하한 | S006, S012 |
| Bias / Variance | 단순화에 의한 체계적 오차 / 훈련셋 변화에 따른 f̂의 변동 | S010–S011 |
| Overfitting | 훈련 오차는 작지만 테스트 오차가 큰 상태 | S005 |
| Error rate / 0-1 loss | Σ1(yᵢ≠ŷᵢ)/n ; 1(Y≠h(X)) | S014, S080 |
| Bayes classifier / Bayes decision boundary / Bayes error rate | 조건부확률 최대 클래스로 분류 / P=1/2인 경계 / 그 오류율 | S015–S016 |
| KNN | 가장 가까운 K개 이웃의 다수결(분류) 또는 평균(회귀) | S017, S057 |
| Brier score | (Y − p̂)²; 확률 예측의 제곱오차 | S022 |
| Interpolation (threshold) | 훈련 데이터를 완전히 맞춤(훈련오차 0); 그 경계 | S023 |
| Double descent | capacity↑에 따라 테스트 risk가 내려갔다 올라갔다 다시 내려가는 현상 | S023 |
| Inductive bias | 무수한 해 중 특정 해(예: 최소노름)를 선호하는 학습 알고리즘의 편향 | 논문발표 |
| True model view / Projection view | 선형식이 실제 E(Y∣X)라는 관점 / 최선의 선형 근사라는 관점 | S026 |
| Likelihood / log-likelihood / MLE | 데이터 대입 후 모수의 함수 / 그 로그 / 최대화 해 | S027, S087 |
| Fisher information | −E[∂²ℓ/∂β∂βᵀ]; 추정 정밀도 | S027 |
| Frequentist / Bayesian / prior / MCMC | 확률=장기 비율 / 확률=믿음 / 사전 정보 / 베이지안 계산 알고리즘 | S026–S027 |
| RSS / TSS / R² / RSE | 잔차제곱합 / 총제곱합 / 1−RSS/TSS / √(RSS/(n−p−1)) | S031, S042 |
| F-statistic / t-statistic / p-value | 전체 계수 검정 / 개별 계수 검정 / 귀무가설 하 확률 | S036, S038 |
| Forward / Backward / Best subset selection | 변수 추가 / 제거 / 전체 탐색 | S040–S041 |


| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| Dummy variable / baseline | 질적 변수의 0/1 코딩 / 더미가 없는 기준 수준 | S044–S045 |
| Interaction / additive assumption | X₁X₂ 항 / 효과가 다른 변수에 무관하다는 가정 | S048 |
| Parametric / Non-parametric | 함수 형태 가정 O / X | S056 |
| Curse of dimensionality | p가 커지면 이웃이 멀어져 KNN 등이 나빠짐 | S062 |
| Objective / loss / cost function | 최소화하고 싶은 양 | S066 |
| Convex | 국소 최소 = 전역 최소인 밥그릇 모양 | S066 |
| Gradient ∇L / learning rate η | 편미분 벡터(최대 증가 방향) / step 크기 | S069 |
| Closed form / normal equations | β ̂ = (XᵀX)⁻¹Xᵀy | S068, S070 |
| Newton–Raphson / Hessian | 2차 미분 행렬을 쓰는 반복법 | S072 |
| SGD / mini-batch / epoch | 확률적 경사하강 / 데이터 일부 / 전체 1회 통과 | S072 |
| Backpropagation / chain rule | 합성함수의 gradient를 역방향으로 계산 | S073 |
| Local minimum / saddle point / plateau | 비볼록 지형의 정류점 유형 | S074 |
| Pre-training / momentum / RMSProp / dropout /ReLU | 비볼록 최적화 요령(Hinton) | S075 |
| Classifier h(x) / decision boundary / linear decision boundary | 분류 함수 / 0·1 영역의 경계 / 선형 경계 | S080 |
| Classification risk / empirical risk | P(Y≠h(X)) / 표본 오분류율 | S080 |
| Multi-class / multi-label | 상호배타 범주 / 중복 레이블 가능 | S080 |
| Link function / logit / odds / odds ratio | 확률↔선형식 연결 / log(p/(1−p)) / p/(1−p) / e^{β} | S082–S085 |
| Sigmoid (logistic function) | σ(z) = e^z/(1+e^z) = 1/(1+e^{−z}) | S085 |
| Surrogate loss | 0-1 loss 대신 쓰는 미분 가능한 손실 | S087 |
| Cross-entropy / softmax | −Σ[y log p + (1−y)log(1−p)] / 다범주 확률 e^{zₖ}/Σe^{zₗ} | S087, S097 |
| Confounding | 제3변수(balance)가 노출(student)과 결과(default) 관계를 왜곡 | S091 |
| Case-control sampling | 사례·대조를 따로 표집; 기울기는 추정 가능, 절편은 보정 필요 | S095 |
| LDA / QDA / Naive Bayes | 클래스별 정규(공통 Σ / Σₖ / 대각)로 X∣Y를 모델링해 Bayes 정리로 분류 | S099–S118 |
| Discriminant function δₖ(x) | 클래스 k의 점수; 최대인 클래스로 분류 | S104, S107 |
| Confusion matrix / FPR / FNR / sensitivity /specificity / ROC / AUC | 분류 성능 지표들 | S112–S115 |
| Discriminative / Generative learning | P(Y∣X) 직접 모델링 / P(X,Y) 모델링 | S119 |
| TRIPOD | 예측모형 보고 체크리스트 | 녹음4 끝 |




## 4차시 (2026-09-23) — 로지스틱 회귀 심화(우도·경사법·Newton–Raphson·odds ratio·confounding·환자-대조군) · 다항 로지스틱 · 판별분석의 출발점 · TRIPOD/PROBAST 발표

_출처: [study_guide_summary_part01.md](../week04_20260923/study_guide_summary_part01.md) · [주차 인덱스](../week04_20260923/README.md)_

### 4. 용어 정리

| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| classification(분류) / classifier | 질적 반응 Y ∈ 𝒞를 예측하는 함수 C(X) | S04 |
| qualitative(categorical) variable | 순서 없는 집합의 값을 갖는 변수 | S04 |
| logistic function / sigmoid | σ(z) = e^z/(1+e^z) = 1/(1+e^{−z}); 출력이 (0,1) | S09, X15 |
| logit / log odds / link function | log[p/(1−p)]; 로지스틱 회귀에서 X에 선형인 양 | S09 |
| odds | p/(1−p), 0~∞ | 노트 p.8 |
| odds ratio (OR) | 두 odds의 비; 더미변수 계수의 e^{β} | 노트 p.8 |
| likelihood(우도) | 관측 자료가 나올 확률을 모수의 함수로 본 것 ∏p(xᵢ)^{yᵢ} (1−p(xᵢ))^{1−yᵢ} | S11 |
| maximum likelihood (MLE) | 우도를 최대화하는 추정법; −log 우도 최소화와 동치 | S11, 노트 p.6 |
| 0-1 loss | 1(y ≠ ŷ)의 평균 = 오분류율; 미분 불가 | 판서 18:40 |
| surrogate(대리) loss | 0-1 손실 대신 쓰는 미분 가능한 손실(−log 우도, cross-entropy) | 노트 p.6 |
| cross-entropy / log loss | −[y log p + (1−y)log(1−p)]; 베르누이 −log 우도 | 판서 18:46, X15 |
| gradient descent(경사법) | β ← β − η∇L 반복; η 학습률 | 판서 18:51, X06 |
| Newton–Raphson / IRLS | β ← β − H⁻¹∇L; 2차 미분(Hessian) 역행렬로 걸음 결정; glm의 알고리즘 | 노트 p.7, X21 |
| Fisher information / Hessian | −log 우도의 2차 미분 행렬 F; F⁻¹ ≈ Var(β)̂ | 노트 p.7, 판서 19:09 |
| standard error / z-statistic / p-value | SE = √diag(F⁻¹), z = β/̂ SE, p = 2(1−Φ(∣z∣)) | 노트 p.7, ISLR p.134 |
| confounding(교란) | 노출과 결과 모두와 연관된 제3변수 때문에 단순 관계가 왜곡되는 현상 | S15, ISLR p.136 |
| prevalence(유병률) | 모집단에서 질병을 가진 사람의 비율 π | S16·S19 |
| cohort design | 노출 여부로 모집 → 추적 → 결과 관찰 | 노트 p.9 |
| case-control design | 결과(환자/대조군)로 모집 → 과거 노출 조사 | 노트 p.9–10 |
| selection indicator S | 표본에 뽑혔음(S=1)을 나타내는 지표; p(S=1∣y,x) 모형으로 설계를 표현 | 판서 19:47 |
| RCT / SCCS / matched design | 무작위 대조 시험 / 자기-대조 환자군(백신 연구) / 짝짓기 설계 | 노트 p.9·11 |
| iid | 독립·동일분포 가정; 환자-대조군은 iid이지만 모집단 분포 p가 아닌 p*에서 나옴 | 노트 p.11 |
| multinomial(다항) regression | K클래스 로지스틱; baseline category logit; softmax | S21 |
| baseline(reference) category | 비의 기준이 되는 범주(α J=β J=0) _ _ | 판서 20:48 |
| softmax | π j = e^{η j}/Σ ℓ e^{η ℓ} _ _ _ _ | S21, 판서 20:54 |
| argmax 분류 / Bayes classifier | 사후확률이 최대인 클래스 선택; 0-1 손실 최소 | 노트 p.13, ISLR p.139 |
| discriminative vs generative | P(Y∣X) 직접 모델링 vs P(X∣Y)P(Y) 모델링 후 Bayes 정리 | S23·S43 |
| prior π k / posterior p k(x) _ _ | 사전(클래스 주변) 확률 / X=x가 주어졌을 때 클래스 확률 | S24, ISLR p.139 |
| density f k(x) _ | 클래스 k에서 X의 밀도 P(X=x∣Y=k) | S24 |
| Bayes theorem (분류용) | Pr(Y=k∣X=x) = π k f k(x)/Σ ℓ π ℓ f ℓ(x) _ _ _ _ _ | S24 |


| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| decision boundary | 두 클래스의 사후확률이 같아지는 x의 집합; LDA 선형, QDA 이 차 | S25·S28·S41 |
| complete separation | 선형결합으로 y가 완전히 갈려 로지스틱 MLE가 발산하는 상황 | 노트 p.16 |
| LDA / QDA / naive Bayes | 가우스 공통 Σ / 가우스 클래스별 Σ k / 클래스 내 변수 독립 가 _ 정의 판별분석 | S27–S42 |
| discriminant score δ k(x) _ | 사후확률 비교와 동치인 점수; LDA에서 x의 선형함수 | S28·S31 |
| confusion matrix / sensitivity /specificity | 예측×실제 2×2표 / 실제 양성 중 양성 판정 비율 / 실제 음성 중 음성 판정 비율 | S36, ISLR p.145 |
| false positive rate / false negative rate | 1−특이도 / 1−민감도 | S37 |
| threshold(임계값) | 사후확률을 분류로 바꾸는 절단값(기본 0.5) | S37–S38 |
| ROC / AUC / c-statistic | FPR 대 TPR 곡선 / 곡선 아래 면적 / P(환자 점수 > 비환자 점수) = AUC | S39, X59–X64 |
| calibration(보정) | 예측 확률이 관측 빈도와 맞는 정도; AUC는 못 봄 | X68 |
| Mahalanobis distance | (x−μ)ᵀΣ⁻¹(x−μ)의 제곱근; 상관을 고려한 표준화 거리 | X34 |


## 5차시 (2026-09-30) — 판별분석(LDA, p=1 → p>1) · 다변량 정규분포 · Naive Bayes·Laplace 평활 · 이진 분류기 성능(정확도 함정·임계값·민감도·특이도·ROC·AUC)

_출처: [study_guide_summary_part01.md](../week05_20260930/study_guide_summary_part01.md) · [주차 인덱스](../week05_20260930/README.md)_

### 4. 용어 정리

| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| discriminant analysis(판별분석) | 클래스별 X의 분포 f k(x)와 사전확률 π k를 모델링한 뒤 Bayes 정리로 _ _ P(Y=k∣x)를 얻는 분류법 | S22–S24 |
| generative / discriminative | 생성적(P(X,Y) 모델링: LDA·QDA·NB) / 판별적(P(Y∣X) 직접: 로지스틱) | S23·S43, 판서 18:38 |
| prior π k / posterior p k(x) _ _ | 사전확률 P(Y=k) / 사후확률 P(Y=k∣X=x) | S24 |
| likelihood(우도) | 자료가 관찰된 뒤 모수 θ의 함수로 본 확률; probability와 대비 | 판서 18:38, 녹음1 02:53 |
| Bayes classifier | p k(x)가 최대인 클래스로 배정; 0-1 손실을 최소화 _ | S25, 녹음1 05:50 |
| discriminant score δ k(x) _ | 로그·약분 뒤 남는 k별 점수; 가장 큰 k로 분류 | S28·S31 |
| LDA / QDA | 공통 Σ(선형 경계) / 클래스별 Σ k(이차 경계) _ | S27·S41 |
| homogeneous (variance) assumption | 클래스별 분산(공분산)이 같다는 가정 | 녹음1 13:44 |
| pooled variance σ̂² (n−K) | K개 클래스 분산의 가중평균, 자유도 K 보정 | S30 |
| multivariate Gaussian N p(μ, _ Σ) | 평균벡터 μ, 공분산행렬 Σ를 갖는 p차원 정규분포 | M09 |
| covariance matrix Σ | Cov(X) = E[(X−μ)(X−μ)ᵀ]; 대칭, 양반정치, 모수 p(p+1)/2 | M07, 판서 19:22 |
| positive (semi-)definite | zᵀΣz ≥ 0 ∀z (반정치) / > 0 ∀z≠0 (정치, Σ⁻¹ 존재) | M07 |
| quadratic form / Mahalanobis 거리 | (x−μ)ᵀΣ⁻¹(x−μ): 상관을 고려한 표준화 거리의 제곱 | M08 |
| determinant | Σ |  |
| contour(등고선) | 밀도 값이 같은 x의 집합 = 타원; "칼로 자른 단면" | M13, 녹음1 53:27 |
| eigenvector eᵢ / eigenvalue λᵢ | Σ = EΛEᵀ; 타원의 축 방향 / 축 길이 c√λᵢ | M13–M14 |
| spectral decomposition | Σ = EΛEᵀ (회전–늘림–되돌림) | M14 |
| whitening Σ^{−1/2}(X−μ) | 타원을 구로 펴는 표준화; 결과는 N(0, I) | M18 |
| Schur complement Σ₁∣₂ | 조건부 공분산 Σ₁₁ − Σ₁₂Σ₂₂⁻¹Σ₂₁ | M23 |
| GEE(generalized estimating equation) | 분포 가정 없이 "어떤 식 = 0"을 풀어 β를 추정하는 접근 | 노트 p.1, 판서 19:22 |
| mixed / random effect model | 조건부분포(잠재변수)로 상관을 간접 모델링; multilevel, spatial 모형 포함 | 녹음1 32:18 |
| naive Bayes | 클래스 안에서 변수 독립(Σ k 대각) 가정; f k(x) = ∏j f(x j) _ _ _ | S42, 노트 p.9 |
| Laplace smoothing(라플라스평활) α | 빈도 0 범주의 확률을 (빈도+α)/(n+α·범주수)로 0이 아니게; e1071::naiveBayes(laplace=) | 노트 p.9, 녹음2 21:29 |
| LASSO / regularized regression | 고차원(p≫n)에서 로지스틱 회귀 쪽이 택한 해법(Stanford 그룹) | 녹음2 10:56 |
| confusion matrix(혼동행렬) | 예측 × 실제 2×2 표 | S36 |
| training / test error | 적합에 쓴 자료 / 쓰지 않은 자료의 오류율 | 노트 p.10 |
| accuracy / misclassification rate | 1 − 오분류율; 불균형 자료에서는 현혹되기 쉬움 | 노트 p.10 |
| imbalanced data | 클래스 비율이 매우 치우친 자료(default 3.33%) | 녹음2 40:03 |


| 용어 | 뜻 | 등장 |
| --- | --- | --- |
| sensitivity(민감도) = TPR = recall = 1−FNR | P(ŷ=1∣y=1) | S37, 노트 p.11 |
| specificity(특이도) = TNR = 1−FPR | P(ŷ=0∣y=0) | S37, 노트 p.11 |
| false positive / false negative rate | FP/N = 1−특이도 / FN/P = 1−민감도 | S37, ISLR Table 4.7 |
| PPV(precision) / NPV | TP/P / TN/N — 예측 양성(음성) 중 실제 비율 | ISLR Table 4.7 |
| threshold(임계값) c | P̂(Y=1∣x) ≥ c이면 1; 기본 ½; "여유 파라미터" | S37–S38, 녹음2 45:25 |
| ROC curve | 임계값을 바꿔 가며 (FPR, TPR)을 이은 곡선 | S39 |
| AUC | ROC 아래 면적; 0.5(우연)~1 | S39, 노트 p.11 |
| "monkey line"(원숭이 선) | 교수님 표현: ROC의 대각선(random guess) | 노트 p.11 |
| oracle / "신의 분류기" | (0,1)점 — 민감도·특이도 모두 1인 완벽 분류기 | 노트 p.11 |
| Youden's J index | 민감도 + 특이도 − 1이 최대인 임계값 선택법 | 노트 p.11 |
| KNN | 비모수 분류기; 경계가 매우 비선형일 때 유리, 계수 표 없음 | S44 |
| Charlson comorbidity index(CCI) | 동반질환 보정 지수 — 질환마다 처리 방식이 다르다는 예로 언급 | 녹음1 49:21 |
| quick and dirty | "더티하고 빠른 방법으로 윤곽부터" — naive Bayes가 선도주자 | 녹음1 27:17, 녹음 2 18:55 |
