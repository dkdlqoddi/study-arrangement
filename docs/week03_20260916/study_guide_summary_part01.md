<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 3차시 시험대비 학습자료 (요약본) (1/2)

> 원본: `machine_learning_for_health_science/20260916/3차시 시험대비 학습자료.pdf` · 변환 방식: pdf-text · 생성일: 2026-10-24 · 원본 13쪽
> [다음 부분 ▶](study_guide_summary_part02.md) · [주차 인덱스](README.md) · [전체 인덱스](../../INDEX.md)

---
<!-- page 1 -->

## ML for Health Science 3차시 시험 대비 학습자료 (요약본)

2026-10-10 작성 · 보건학을 위한 기계학습 (서울대 보건대학원, 이우주 교수) · 3차시 2026-09-16 강의노트·슬라이드·녹음·칠판

·교재(ISLR) 기반 · 전체판(118쪽)의 축약본. 출처 표기: [노트 p.N] 강의노트, [녹음k mm:ss] 녹음, [칠판 hh:mm], [교재 p.N] ISLR 1판, [추가] AI 보충(교수님 말씀 아님).

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

### 2. 핵심 개념 정리

진행 순서대로 2.1~2.10. 각 항목 끝의 괄호는 전체판 슬라이드 번호.

<!-- page 2 -->

#### 2.1 Chap.2 Part II 복습 — 모델 정확도 평가 (S001–S022)

훈련 MSE vs 테스트 MSE: 방법은 훈련 MSE를 줄이도록 설계되지만 관심은 새 데이터의 테스트 MSE. 유연성 ↑ → 훈련 MSE 단조 감소, 테스트 MSE U자형. 훈련 MSE가 작은데 테스트 MSE가 크면 overfitting [교재 p.30–32].

분해식(S012): E(Y − f̂(x₀))² = Bias² + Var(f̂(x₀)) + Var(ε). Var(ε)는 축소 불가능한 하한 [교재 p.34]. 교수님: "Universal한 result임. 거의 모든 machine learning의 fundamental한 picture" [노트 p.5]. "outcome 유형과 loss 타입에 따라 함수 형태는 조금 달라질 수 있지만 전체적으로 그렇게 성립" [녹음1 01:06].

분류 설정(S014): 오류율 = Σ1(yᵢ ≠ ŷᵢ)/n (0-1 loss의 평균) [교재 p.37].

Bayes classifier(S015–S016): h(x) = 1(P(Y=1|x) ≥ 1/2). "Zero one loss에 대해서는 이거를 이길 수가 없음" [노트 p.6]; 그 오류율이 Bayes error rate = 1 − E[maxⱼ P(Y=j|X)] [교재 p.38]. 회귀에서 E(Y|X)가 하는 역할을 분류에서 P(Y=1|X)가 한다. "이 Bayes classifier를 따라한다면 안에 있는 p(y=1|x)를 따라하면 — logistic regression 같은 게 잘 적합하면 1/2 이상인 것을 예측" 또는 "가까운 거 k개 average(KNN)" [노트 p.6][녹음1 03:23–05:31].

KNN(S017–S021): P̂(Y=j|x₀) = (1/K)Σ_{N₀}1(yᵢ=j); K 작을수록 유연(저bias·고variance). K=1 훈련오류 0이지만 테스트오류 0.1695, K=100은 0.1925, K=10이 Bayes(0.1304)에 근접(0.1363) [교재 p.39–40].

Brier score vs 0-1 loss(S022): 이진 Y에서 (Y − p̂)²(Brier)를 쓰면 제곱오차처럼 irreducible + bias² + variance 로 분해된다. "0-1에 대한 분해는 아직까지 unsolved" — 그래도 bias류·variance류 양으로 fundamental picture 는 성립 [노트 p.8][녹음1 08:30–10:59].

#### 2.2 Double descent — Belkin et al. (PNAS 2019) (S023, 논문발표)

고전적 U자(under/over-fitting) 뒤에, capacity가 interpolation threshold(모든 훈련점을 지나 훈련오차 0이 되는 순간)를 넘으면 테스트 risk가 다시 내려갈 수 있다. "급작스럽게 변하는 순간이 그 순간임. 예전에는 이거의 이후를 볼 생각을 안 했음" [노트 p.8].

왜 가능한가: p > n이면 Xβ = y가 부정방정식이라 보간해가 무수히 많다. 그중 노름(계수 벡터 길이)이 최소인해를 고르면 "bias는 없다고 봐야 하고 variance는 regularize를 가장 세게 함. 그 작업만 잘하면 prediction risk 가 좋은 게 나타날 수 있다" [노트 p.9][녹음1 15:37–18:53].

단서: "항상 이런 건 아니고… 오른쪽이 안 나타나거나 왼쪽보다 더 높을 수도"; "반드시 여기를 찾으라는 얘기는 절대 아님. 찾아서 fitting하고 평가해야 함"; 학생 질문(A/B 어느 기준?)에 "문제에 따라 다르다" [노트 p.9] [녹음1 22:26]. 비판: regularization을 고려하면 파라미터 수 ≠ complexity → "complexity를 잘못 이해한 데서 온 artifact" [노트 p.9][녹음1 21:17].

의의: "sample size 이상의 파라미터를 쓰고 regularization을 잘하면 유용한 모델을 얻을 가능성 — 이론적 설명이 처음" [녹음1 23:12]; "training error가 0이 되어도 나쁜 것은 없다는 문을 열어준 것" [노트 p.9][녹음3 01:39].

논문발표 메모: interpolation(h(x)=y, training error 0), model class H와 inductive bias, capacity 계량(random Fourier feature N 조절), 최소노름 inductive bias, MNIST; random forest는 애매 → 모든 모델에서 나오진 않음; deep double descent(epoch·sample 수에 따른 비단조, peak 대신 plateau) [노트 p.1].

[추가] ISLR 1판에는 없음(2판 10.8절). 최소노름 보간해 β = Xᵀ(XXᵀ)⁻¹y는 0에서 시작한 경사하강이 수렴하는 해 (implicit regularization).

#### 2.3 선형회귀를 보는 두 관점 (S024–S026)

|  | True model view | Projection view |
| --- | --- | --- |
| 주장 | E(Y∣X=x) = xᵀβ가 실제 데이터 생성 메커니즘; β는 고정 미지 참값 | β* = argmin b E(Y − Xᵀb)² — 최선의 선형 근사(정사영); 생성 메커니즘 _ 과 무관 |
| 누가 | 통계학(학부 회귀분석): 계수 검정·신뢰구간·해석 | 기계학습: "기계학습에서의 Xβ는 E[Y∣X]를 근사한 것… ŷ = xβ으̂ 로 했을 때 얼마나 예측을 잘하나 봄" [노트 p.10] |

<!-- page 3 -->

|  | True model view | Projection view |
| --- | --- | --- |
| 도구 | likelihood(분포 가정) → s.e., CI, Fisher information | squared error loss 최소화(분포 가정 없음) |

녹음2 01:35–03:28: "데이터 생성 메커니즘이 진짜 이런 선형식을 따른다고 생각하는 사람들… 한국에서 들은 통계학 회귀분석은 그 관점"; "기계학습에서의 Xβ는 그냥 근사시킬 모델일 뿐… 이것을 projection view라고 함". 노트의 "prediction view"는 슬라이드의 projection view [추가].

교재: "많은 교과서가 말하는 것과 달리 참 관계가 선형이라고 믿는 일은 드물다"(p.63 각주); 선형모형은 참 곡면의 최선의 선형 근사 = model bias(p.82).

S027 주석: "(true model view를 가정할 때) inference는 prediction의 부분집합이 아니다."

#### 2.4 Likelihood — 통계학의 핵심 엔진 (S027, 칠판 19:26)

정의: "분포를 지정한 다음 데이터를 집어넣어서 모수의 함수로 본 다음 그걸 그려 낸 것 — 이게 likelihood의 개념. 이 개념은 꼭 익혀야 하고, 가장 높은 값으로 추정한다는 것이 통계학의 방식" [녹음2 24:02–24:29]. "Likelihood function은 통계학에서 핵심적인 엔진" [노트 p.10].

정규 선형모형: Yᵢ = xᵢᵀβ + εᵢ, εᵢ ~ N(0,σ²) → L(β) = Πᵢ(2πσ²)^{-1/2}exp{−(yᵢ − xᵢᵀβ)²/2σ²} [칠판 19:26]. 로그는 단조변환이라 최대점을 바꾸지 않고 곱을 합으로 바꿔 계산이 쉬워진다 → ℓ(β) = const − (1/2σ²)Σ(yᵢ − xᵢᵀβ)².

MLE = OLS: "로그 라이클리후드를 maximize하는 건 −log likelihood를 minimize하는 것과 같음… 정확히 정규분포를 가정한 다음에 maximize한 문제와 같은 것" [노트 p.11][녹음2 25:39–25:58]. 교재: 최소제곱은 최대우도의 특수한 경우(p.133).

뾰족함 = Fisher information: y = ax² + bx + c에서 두 번 미분하면 a만 남듯, "log likelihood를 두 번 미분하는 게 confidence(precision)… 그걸 피셔 인포메이션이라고 함" [노트 p.11][녹음2 21:38–23:57]. I(β) = −E[∂²ℓ/∂β∂βᵀ] = XᵀX/σ² → Var(β̂) ≈ σ²(XᵀX)⁻¹ → s.e., CI, 검정이 모두 여기서 나온다. "회귀분석에서 배운 여러 검정이 모두 다 likelihood test… 노말 가정하고 likelihood (ratio) test" [노트 p.11, p.14][녹음2 30:00–31:08].

";" vs "|": "Conditioning(|)이 있으면 (random으로 보고); semicolon은 fixed unknown" [노트 p.10][녹음2 06:00]. 동전 앞면 확률은 모르지만 고정 → frequentist. "아시안게임 8강 진출 확률"은 같은 조건에서 반복 불가 → 빈도의 극한으로 정의 불가 → 개인의 믿음 → Bayesian. 백신 부작용 확률은 비율로 봄. prior = "데이터를 관찰하기 이전에 문제에 대해 갖는 정보의 표현" [녹음2 08:12–12:01]. 베이지안은 1990년대 MCMC 이후 급성장, 지금은 "실용주의적" [노트 p.10–11].

ML의 관점: "ML 쪽에서는 분포를 지정하지 않음. 알레르기 반응이 있음… squared error loss를 최소화" [노트 p.11]. "통계가 하는 일을 ML은 negative log-likelihood를 loss function으로 놓고 minimize하는 문제로 본다"; 다만 통계는 s.e.·CI에 더 관심. 어떤 분포에도 대응되지 않는 loss도 있다 — SVM의 hinge loss [녹음2 27:41–29:57].

#### 2.5 Ch.3 나머지 — 추론·변수선택·R²·KNN 비교 (S028–S063, 교수님 코멘트 위주)

신뢰구간 β̂₁ ± 2·SE(β̂₁), t = β̂ⱼ/SE, F = [(TSS−RSS)/p]/[RSS/(n−p−1)]: "신뢰구간 만드는 것은 통계학에서 너무 잘 알려진 사실", "Likelihood ratio test. 새로운 것은 없다" [노트 p.14]. 개별 t-검정만 보면 p가 클 때 우연한 유의가 생기므로 F-검정이 필요(교재 p.77). 단순회귀에서 유의하던 newspaper가 다중회귀에서 비유의 — radio와의 상관(교재 p.74–75).

변수선택: "요즘 잘 안 함… 큰 데이터에서는 automation할 수 있는 lasso나 ridge나 ensemble 같은 것들이 tool box에서 더 중요" [노트 p.16].

R²: "설명변수 넣으면 기계적으로 커짐. 절대 모델 선택의 criteria가 될 수 없음. 음수가 나오면 intercept가 없는 모델을 fitting한 것… 컴퓨터 문제가 아니라 여러분 모델이 별로 좋지 않다는 뜻" [노트 p.16][교재 p.79–80].

질적 예측변수·상호작용·다항회귀(S043–S054): "학부 때 많이 다루니까 책과 슬라이드로 대체" [노트 p.21]. 핵심: dummy는 수준 수 − 1개, baseline; 상호작용은 additive 가정 완화(Y = β₀ + (β₁+β₃X₂)X₁ + …); 다항회귀도

<!-- page 4 -->

선형모형(교재 p.82–92).

KNN 회귀 vs 선형회귀(S056–S062): 참 관계가 선형이면 선형회귀가 모든 K를 이김; 비선형이면 KNN 유리; p가 커지면 차원의 저주로 KNN이 급격히 나빠짐 — 예측변수당 관측이 적으면 모수적 방법(교재 p.104–109).

#### 2.6 One Idea, Many Models — 제곱오차에서 경사하강, 신경망까지 (S064–S076, 칠판 20:08)

목적함수 L(β₀,β₁) = (1/2n)Σ(yᵢ − β₀ − β₁xᵢ)²: 데이터가 아니라 모수의 함수로 읽는다. 2차식이라 "밥그릇(bowl) 처럼 생긴" 볼록 함수 → 미분이 0인 점이 유일한 최소. "다행스럽게 제곱이라서 미분하면 손으로 풀 수 있음"(닫힌 해 (XᵀX)⁻¹Xᵀy) [노트 p.24][녹음3 06:06–07:40]. 등고선 그림에서 "별표는 loss function을 minimize하는 점".

왜 경사하강을 배우나: "저 방식(gradient)은 완전히 일반적으로 적용할 수 있는 방식. 이해하기 쉬운 경우라서 gradient descent를 설명" [노트 p.13]. 닫힌 해는 L이 2차식이라 생긴 특수한 경우일 뿐(S068).

Gradient: ∇L = (∂L/∂β₀, ∂L/∂β₁)ᵀ — "1학년 미적분 내용, 각 변수로 미분한 것을 쌓은 벡터"; "등고선이 가장 빠르게 증가하는 방향. 앞에 마이너스가 붙어 가장 빠르게 감소하는 방향으로 움직임" [노트 p.25][녹음3 10:03–11:33][칠판 20:08]. 회귀에서는 ∇L = −(1/n)Xᵀ(y − Xβ)(잔차의 가중합).

갱신식 β^(t+1) = β^(t) − η∇L(β^(t)). η(learning rate, 노트 "러닝 레이트"): "얼마만큼 움직여야 할지는 모름… 너무 작게 잡으면 비효율적, 잘 잡으면 한 번에 훅훅 감(너무 크면 발산). 적절하게 잡는 것은 art이자 노하우"[노트 p.25–26]. 정지: 이전·다음 β 차이가 없을 때(∇L ≈ 0). "현재 거의 대부분의 ML 문제가 이런 식으로 풀림. 딥러닝도 loss를 정하고 gradient 벡터를 계속 반복하는 꼴로 학습". "시간이 되면 딱 한 번만 연습해 보세요"(간단한 함수로 경사하강 돌려 보기) [노트 p.25].

볼록 vs 비볼록: 볼록이면 초기치 무관; 오르락내리락하면 출발점에 따라 local min에 빠짐 — 초기화가 어려웠던 시기, "empirical하지만 성공률 높은" 해법들 [노트 p.25].

뉴턴법의 한계: "지금 이야기하는 gradient method보다 훨씬 빠르고 효능이 좋음"이지만 p×p 행렬의 역행렬 (O(p³))이 필요 — "1750억 개… 현실적으로 불가능. 5만×5만을 못 넘음. 10배 커지면 시간 1000배" → "두 번미분이 없는 훨씬 simple한 문제를 푸는 것을 선호" [노트 p.26]. 로지스틱·포아송 등도 같은 틀로 푼다.

Mini-batch: "n개를 100등분해서… random하게 선택, 일부분만 써서 업데이트. 기본 framework는 유지하고 아이디어를 접목" [노트 p.26].

신경망: θ가 수십만~수백만; "한 번에 미분이 안 되고 꼬리에 꼬리를 미분하는 chain(rule)" = 역전파. "딥러닝이라고 해서 새로운 것은 별로 없다. principle은 거의 다르지 않음. mini batch 문제만 풀고 chain rule을 쓰며 ReLU(노트 '레구') 같은 함수를 사용" [노트 p.27]. 비볼록 지형(국소최소·안장점·고원) → Hinton 도구상자: 사전 학습(2006), SGD+모멘텀, RMSProp, dropout/ReLU (S075).

전체 실(S076): Define(목적함수) → Seek(argmin) → Descend(θ ← θ − η∇L) → Beware(볼록이면 보장, 신경망은 아님) → Cope(Hinton).

#### 2.7 분류 문제의 정의와 risk (S077–S081, 칠판 20:55·21:00)

h: X(feature) → Y ∈ {0,…,K−1}; K=2면 binary. "feature를 집어넣어 categorical value를 주는 함수 = classifier(classification rule)". discrimination, pattern recognition 등 다른 이름도 쓰인다 [노트 p.29][녹음4 09:24–11:28].

"h(x)=0인 x의 집합과 1인 집합을 선으로 갈라… 설명변수 공간을 파티션하는 땅따먹기"; 그 선이 decision boundary, 선형이면 linear decision boundary [노트 p.29][칠판 20:55]. 보건 문제에는 multi-label(복지 서비스 중복 제공)처럼 파티션이 아닌 문제도 있지만 교재는 상호배타 문제만 다룸.

0-1 loss 1(Y≠h(X)) → 기댓값 = classification risk = P(Y≠h(X)) → empirical risk (1/n)Σ1(yᵢ≠h(xᵢ)). 이를 minimize하는 h가 Bayes classifier(조건부확률 ≥ 1/2) [노트 p.29][칠판 21:00].

통계 vs ML 접근: "Stat은 data generation model(확률모델)에 관심… p(y=1|x)를 구성해 1/2보다 크냐 작냐로 분류"; "ML은 확률을 타깃팅할 필요가 없으니 h(x) 자체를 구해 버림". 교재 저자들이 확률 추정에 관심이 많은

<!-- page 5 -->

건 통계 배경 때문. 확률이 필요한 순간: 은행이 "어느 정도로 갚을 거냐"를 볼 때 [노트 p.29][녹음4 19:22–21:36].

Default 데이터: balance(결제되지 않고 남은 잔액)·income이 feature, 원 하나가 개인; balance 높으면 default 위험↑ [노트 p.29–30].

#### 2.8 선형회귀 vs 로지스틱 회귀 — link와 해석 (S082–S086, 칠판 21:10–21:14)

"Y가 0,1이면 습관적으로 logistic regression을 떠올리지만, 예측의 관점에서는 선형회귀를 써도 문제 되지 않음(모델 클래스임, 실제 많이 씀)". 다만 "값이 1을 넘거나 0 미만일 수 있어 역학과 임상에서는 좋아하지 않음"[노트 p.30][녹음4 24:20, 29:39–30:32]. 교재: 이진이면 선형회귀의 분류는 LDA와 동일(p.130).

Link function: "왼쪽(확률, 0~1)과 오른쪽(β₀+β₁x, 실수) 식의 범위를 일치시키기 위해 어떤 함수를 도입… link function. 가장 대표적인 함수가 g(x) = log(x/(1−x))" → 로지스틱 회귀. "아주 지대한 영향을 미침" [노트 p.30] [칠판 21:10 "link choice ⇒ interpretation"]. (R의 glm에서 family 옵션 [추가])

해석: log(p/(1−p)) = β₀ + β₁X를 X로 미분하면 β₁ → "β₁의 의미는 log odds의 변화, exp(β₁) = odds ratio — 의료와 임상에서의 루틴" [노트 p.30][녹음4 28:36–29:28][칠판 21:12]. "x를 미분하면 linear 형태여야 이게 나옴"(logit이 X에 선형이라 OR이 상수) [노트 p.31].

Sigmoid: p = e^{xβ}/(1+e^{xβ}) = 1/(1+e^{−xβ}) — "분모가 항상 크기 때문에 아무리 커도 1을 못 넘고 음수가 안 됨. S자 커브"; 0.5 이상이면 1로 예측 [녹음4 31:15–32:07][칠판 21:14].

3범주(stroke/overdose/seizure)를 1,2,3으로 선형회귀하면 "stroke–overdose 차이가 overdose–seizure 차이와 같냐? 인위적인 초이스" → multinomial regression [노트 p.31][교재 p.129].

#### 2.9 MLE → cross-entropy, 0-1 loss와 surrogate (S087–S089, 칠판 21:23–21:24)

"지금까지의 모든 내용은 continuous outcome에서 해 왔던 모습을 binary outcome에 그대로 적용하면 어떻게 되는가" [녹음4 35:26]. 연속형: (Y − (β₀+β₁x))² → L → ∇L → 갱신. 0-1 loss는 미분 불가: "h로 미분하려고 하니까 괴팍함. indicator는 step function… 수학적으로 허용되지 않는 function. 실제 문제는 0-1으로 푸는 게 많지는 않음" [노트 p.32][녹음4 36:33–37:59]. 대신 계산 가능한 surrogate loss로 "바꿔치기" — "원래 문제를 잃어버렸다고 비판하는 분들도 있음"; mixed integer programming으로 직접 푸는 2020년 이후 연구도 있으나 "아직 주류를 형성했다고 보기 어려움" [녹음4 38:16–39:14].

로지스틱 회귀의 loss: 베르누이 likelihood L(β) = Π pᵢ^{yᵢ}(1−pᵢ)^{1−yᵢ}, pᵢ = σ(xᵢᵀβ)를 maximize = "로그를 취한 다음 마이너스를 붙이면 minimize 문제… 이것을 하나의 loss로 봄. 실제 cross-entropy loss라고 부르는데 알고 보면 베르누이 likelihood에 로그 취하고 마이너스 붙여 minimize하는 것과 똑같다" [녹음4 39:25–40:52] [칠판 21:23 "−ℓ(β) = Loss(β)"]. −ℓ = −Σ[yᵢ log pᵢ + (1−yᵢ)log(1−pᵢ)]; β에 볼록, 닫힌 해 없음 → 반복(IRLS 또는 경사하강), ∇L = (1/n)Xᵀ(σ(Xβ) − y) [추가].

다범주: "Multinomial likelihood → softmax" [노트 p.32][녹음4 40:54]. "통계의 likelihood에 로그를 취하고 마이너스를 붙여 loss로 보고 gradient method로 minimize — classification에서 진행되는 내용이며 신경망에서도 같다" [녹음4 41:05–41:33].

교재 수치: balance 계수 0.0055(z 24.9); balance $1000 → p̂ 0.006, $2000 → 0.586; student 단독 계수 +0.4049 [교재 p.133–135].

#### 2.10 이번 차시에 다루지 않은 Ch.4 후반 (S090–S121) — 교재 요약 [교재]

다중 로지스틱: student 계수가 단독 +0.40 → balance·income 포함 시 −0.65. Confounding: 학생은 잔액이 높아 전체 default율은 높지만 같은 balance에서는 덜 default(p.135–137).

사례-대조 표집: 기울기는 추정 가능, 절편은 π/π̃로 보정; 대조는 사례의 5배면 충분(강의 슬라이드).

<!-- page 6 -->

LDA: 클래스별 정규 + 공통 Σ → δₖ(x) = xᵀΣ⁻¹μₖ − ½μₖᵀΣ⁻¹μₖ + log πₖ(선형). QDA: Σₖ → 이차. Naive Bayes: feature 조건부 독립(대각 Σₖ). 로지스틱(discriminative, P(Y|X))과 LDA(generative, P(X,Y))는 같은 선형 경계, 추정 방식만 다름(p.138–151).

혼동행렬·민감도·특이도·threshold·ROC/AUC: Default LDA 전체 오류 2.75%지만 default 중 75.7% 놓침 → threshold를 0.2로 낮추면 41.4%로 개선(p.144–148). 결정경계가 선형이면 LDA/로지스틱, 중간 비선형이면 QDA, 복잡하면 KNN(p.154).

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

<!-- page 7 -->

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

<!-- page 8 -->

### 4. 교수님이 강조한 포인트 (녹음 기반 · 시험/평가 관련 발언 포함)

#### 4.1 수업 운영·평가 관련 (녹음4 00:59–08:46, 41:39–43:44)

1. 발표 슬라이드는 게시판에 업로드가 원칙(모두가 다운로드할 수 있게). 가능하면 영어로 준비하는 것이 외국인 수강생에 대한 배려.

2. 정기 숙제는 없다("대학원이니 공부는 알아서"). 대신 교재의 exercise를 LLM(GPT·Claude·Gemini)에 풀게 해 보고 LLM 답의 오류를 찾아 정리해 이메일로 제출하면 성적으로 보답하겠다. 의미 있는 것은 다음 시간에 짧게 발표할 기회.

3. 교재 ISLR에는 R lab·Python lab(ISLP)·exercise가 있고 코드·데이터가 모두 공개되어 있다 — 적극 활용하라.

4. Ch.3은 "이미 끝난 것"으로 간주 — 수업에서는 두 관점·likelihood·gradient method만 다뤘고, 가설검정 등 나머지는 교재로 직접 공부할 것(시험 범위 제외 언급 없음).

5. 다음 차시 발표 주제: TRIPOD(+AI) 체크리스트를 사례와 함께 소개할 발표자 1명 모집.

#### 4.2 학술적 강조점 (중요도 순, 녹음·노트 근거)

1. Bias-variance 그림은 universal — loss·outcome 종류와 무관하게 성립한다(녹음1 01:06, 10:36; 노트 p.5). "학습 방법을 고를 때 항상 이 그림을 염두에 두라"(S022).

2. Bayes classifier h(x)=1(P(Y=1|x)≥1/2)는 0-1 loss에서 이길 수 없다(녹음1 02:56; 노트 p.6). 분류 방법들은 이를 "따라하는" 것 — 안의 확률을 추정하거나(로지스틱) h를 직접 찾거나.

3. Brier score는 제곱오차처럼 분해되지만 0-1 loss의 분해는 unsolved(녹음1 08:30–10:32; 노트 p.8).

4. Double descent: interpolation threshold, p>n의 무수한 해 중 최소노름 해, regularization. "문제에 따라 다르다", "반드시 여기를 찾으라는 얘기는 절대 아님", complexity 오해라는 비판도 소개(녹음1 11:12–23:28; 노트 p.8–9). 훈련오차 0이 곧 나쁜 것은 아니라는 문을 열었다(녹음3 01:39).

5. 선형회귀의 두 관점 — 통계(true model, 추론)와 기계학습(projection, 예측)이 같은 식을 다르게 본다(녹음2 01:35–03:28; 노트 p.10).

6. Likelihood는 통계학의 핵심 엔진이고 "이 개념은 꼭 익혀야 한다"(녹음2 24:02–24:29). 분포 가정 → 데이터 대입 → 모수의 함수 → 최대화(MLE). 로그는 단조변환이라 최대점을 바꾸지 않고 계산을 쉽게 한다.

7. 정규분포 + MLE = squared error loss 최소화; "negative log-likelihood = loss"로 통계와 ML이 연결된다(녹음2 24:29–28:34; 노트 p.11; 칠판 19:26). ML은 "분포 지정에 알레르기"가 있고 hinge loss처럼 분포 없는 loss 도 있다.

8. log-likelihood의 뾰족함(2차 미분) = Fisher information → s.e., CI, 검정이 모두 여기서 나온다. 학부 회귀분석의 모든 검정은 정규 가정 하의 likelihood (ratio) test(녹음2 30:00–31:08; 노트 p.11, p.14).

9. ";"(fixed unknown, frequentist) vs "|"(random, Bayesian); 반복 불가능한 사건(아시안게임 8강)의 확률은 믿음 → Bayesian; prior = 데이터 전의 정보(녹음2 06:00–12:01; 노트 p.10).

10. R²는 절대 모델 선택 기준이 아니다; 음수 R²는 모델이 나쁘다는 뜻(노트 p.16). Stepwise 변수선택은 요즘 잘 안 하고 lasso·ridge·ensemble이 중요(노트 p.16).

11. 경사하강법: gradient = 가장 빠른 증가 방향, −η∇L로 이동, η는 learning rate이며 선택이 "art". "시간이 되면 딱 한 번만 연습해 보세요"(노트 p.25; 녹음3 10:03–13:46; 칠판 20:08).

12. 뉴턴법은 빠르지만 p×p 역행렬(O(p³))이 필요해 거대 모델에선 불가능 → 1차 방법 + mini-batch(노트 p.26).

13. "딥러닝이라고 해서 새로운 것은 별로 없다" — 원리는 같고 chain rule(역전파)·mini-batch·ReLU 같은 기술이 더해진 것(노트 p.27).

14. Classification = 설명변수 공간의 파티션(땅따먹기); 0-1 loss → classification risk P(Y≠h(X)) → empirical risk(녹음4 09:24–18:28; 칠판 20:55, 21:00). 보건 문제에는 multi-label 등 다양한 형태가 있다.

<!-- page 9 -->

15. 통계는 확률 모델(P(Y=1|X))을 먼저 세우고 threshold로 분류, ML은 h를 직접 — 교재 저자들은 통계 배경이라 확률 추정에 관심; 은행 대출처럼 "얼마나 갚을지"가 필요하면 확률이 필요(녹음4 19:22–21:36; 노트 p.29).

16. 이진 Y에 선형회귀도 예측용으로는 쓸 수 있지만, 확률이 [0,1]을 벗어나 역학·임상은 로지스틱을 선호. link function 선택이 곧 해석(exp(β₁)=OR) — 임상·역학의 루틴(녹음4 24:20–30:32; 노트 p.30; 칠판 21:10–21:14).

17. continuous에서 한 것(손실 → gradient descent)을 binary에 그대로 적용 — 0-1 loss는 step function이라 미분 불가 → surrogate(베르누이 NLL = cross-entropy)로 바꿔치기; 비판과 MIP 직접 최적화 연구도 소개하되 "아직 주류 아님"(녹음4 35:26–41:33; 노트 p.32; 칠판 21:23).

18. cross-entropy = 베르누이 likelihood의 −log; softmax = multinomial likelihood — "통계의 likelihood에 로그 취하고 마이너스 붙여 loss로 보고 gradient method로 푸는 것이 classification의 현재 모습"(녹음4 40:34–41:33).
