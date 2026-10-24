<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 3차시 시험대비 학습자료 (요약본) (2/2)

> 원본: `machine_learning_for_health_science/20260916/3차시 시험대비 학습자료.pdf` · 변환 방식: pdf-text · 생성일: 2026-10-24 · 원본 13쪽
> [◀ 이전 부분](study_guide_summary_part01.md) · [주차 인덱스](README.md) · [전체 인덱스](../../INDEX.md)

---
### 5. 예상 시험 문제와 모범 답안

근거 출처 표시: [노트] 강의노트, [녹음] 녹음, [교재] ISLR, [추가] AI 보충.

#### 5.1 객관식

Q1. 기대 테스트 MSE의 분해에서 어떤 방법으로도 줄일 수 없는 항은? ① Bias² ② Var(f̂(x₀)) ③ Var(ε) ④ 훈련 MSE

답 ③. Var(ε)는 irreducible error로 테스트 MSE의 하한이다. [교재 p.34][노트 p.5] (S012)

Q2. 다음 중 교수님이 "universal한 결과"라고 한 것은? ① 선형회귀의 불편성 ② bias-variance trade-off 그림 ③ double descent ④ KNN의 일관성

답 ②. loss·outcome 종류에 따라 형태는 달라도 복잡도↑ → bias↓·variance↑ → test error U자형은 항상 성립. double descent는 "항상 나타나는 것은 아니다"라고 했다. [녹음1 01:06][노트 p.5, p.9] (S012, S023)

Q3. Bayes classifier에 대한 설명으로 틀린 것은? ① P(Y=1|X=x) ≥ 1/2이면 1로 분류한다 ② 0-1 loss에서 최소 오류율을 낸다 ③ 실제 데이터에서 직접 계산할 수 있다 ④ 그 오류율을 Bayes error rate라 한다

답 ③. 조건부분포를 모르므로 계산 불가능한 "도달할 수 없는 금본위"다. [교재 p.39][녹음1 02:56] (S015–S016)

Q4. Belkin et al.(2019)의 double descent에서 테스트 risk가 치솟는 지점은? ① sweet spot ② interpolation threshold ③ under-parameterized 영역의 시작 ④ 훈련 risk의 최소점

답 ②. 모든 훈련 데이터를 지나는(훈련오차 0) 순간이며, 그 너머에서 다시 내려갈 수 있다. [노트 p.8][녹음1 12:02] (S023)

Q5. 정규오차 선형회귀에서 최대우도 추정치와 같은 것은? ① ridge 추정치 ② 최소제곱 추정치 ③ KNN 예측 ④ 중앙값 회귀

답 ②. ℓ(β) = const − (1/2σ²)Σ(yᵢ−xᵢᵀβ)²이므로 최대화 = RSS 최소화. [노트 p.11][녹음2 24:29][교재 p.133] (S027)

Q6. 로지스틱 회귀에서 exp(β₁)의 해석은? ① X 한 단위 증가 시 확률의 증가량 ② X 한 단위 증가 시 odds ratio

③ X 한 단위 증가 시 log odds의 증가량 ④ 절편의 odds

답 ②. β₁은 log odds의 변화, exp(β₁)은 odds의 배수(OR). ③은 β₁ 자체. [녹음4 28:36–29:28][교재 p.132–133] (S085)

Q7. 경사하강법 β^(t+1) = β^(t) − η∇L(β^(t))에 대한 설명으로 옳은 것은? ① ∇L은 손실이 가장 빠르게 감소하는 방향이다 ② η가 클수록 항상 빨리 수렴한다 ③ 볼록 함수에서는 초기값과 무관하게 전역 최소로 수렴한다(충분히 작은 η) ④ Hessian의 역행렬이 필요하다

<!-- page 10 -->

답 ③. ∇L은 가장 빠른 증가 방향(①×), η가 너무 크면 발산(②×), 역행렬은 뉴턴법(④×). [노트 p.25–26][녹음3 11:08] (S069–S072)

Q8. 0-1 loss를 직접 최소화하지 않는 가장 직접적인 이유는? ① 계산 비용이 O(p³)이기 때문 ② indicator가 step function이라 미분이 불가능하기 때문 ③ 확률을 추정할 수 없기 때문 ④ 과적합되기 때문

답 ②. 그래서 베르누이 NLL(cross-entropy) 같은 surrogate loss로 바꿔치기한다. [노트 p.32][녹음4 36:33–39:25] (S087)

Q9. R²에 대한 설명으로 옳은 것은? ① 변수를 추가하면 감소할 수 있다 ② 모델 선택의 좋은 기준이다 ③ 절편 없는 모델에서는 음수가 나올 수 있다 ④ 항상 테스트 데이터로 계산한다

답 ③. 변수 추가 시 기계적으로 증가하므로 모델 선택 기준이 될 수 없다. [노트 p.16][교재 p.79–80] (S042)

Q10. Default 데이터에서 student 계수가 단변량에서는 양수, balance를 포함한 다변량에서는 음수인 현상은? ① 상호작용 ② 다중공선성 ③ 교란(confounding) ④ 과적합

답 ③. 학생은 balance가 높아 전체적으로 default가 많지만 같은 balance에서는 덜 default한다. [교재 p.136] (S091)

#### 5.2 단답형

Q11. 분류 문제에서 classification risk를 수식으로 쓰고 empirical 버전을 쓰라.

R(h) = E[1(Y ≠ h(X))] = P(Y ≠ h(X)); R̂(h) = (1/n)Σᵢ 1(yᵢ ≠ h(xᵢ)). [칠판 21:00][노트 p.29] (S080)

Q12. Bayes error rate의 식을 쓰라.

1 − E[maxⱼ P(Y=j|X)]. [교재 p.38] (S015)

Q13. f(y; β)와 f(y|β) 표기의 차이를 한 줄로.

";"는 β가 고정된 미지수(frequentist), "|"는 β가 확률변수(Bayesian, conditioning). [녹음2 06:00][노트 p.10] (S026)

Q14. Fisher information의 정의와 그것이 큰 경우의 의미.

I(β) = −E[∂²ℓ(β)/∂β∂βᵀ]; 크면 log-likelihood가 뾰족해 추정 정밀도가 높고 s.e.·CI가 작다. [노트 p.11][녹음2 23:35] (S027)

Q15. p > n인 선형회귀에서 Belkin 논문이 택한 보간해는?

ℓ₂-노름이 최소인 보간해(minimum-norm interpolator; 계수 벡터 길이가 가장 짧은 해). [녹음1 15:51][노트 p.9] (S023)

Q16. logit link g(p)를 쓰고 그 역함수(sigmoid)를 쓰라.

g(p) = log(p/(1−p)); p = e^z/(1+e^z) = 1/(1+e^{−z}), z = β₀+β₁x. [칠판 21:10, 21:14][교재 p.132] (S085)

Q17. 로지스틱 회귀의 negative log-likelihood를 딥러닝에서 부르는 이름은? 다범주 버전은?

cross-entropy loss(log loss); 다범주는 softmax cross-entropy(multinomial likelihood). [녹음4 40:34–40:54][노트 p.32] (S087, S097)

Q18. 뉴턴–랩슨법을 거대 신경망에 쓰지 못하는 이유를 한 줄로.

p×p Hessian의 역행렬이 필요해 O(p³)이며 p가 수십억이면 행렬 자체를 만들 수 없다. [노트 p.26] (S072)

Q19. 교수님이 Ch.3에서 "수업에서 다룬 것은 사실상 이것뿐"이라고 한 내용은?

gradient method(경사하강법) — 머신러닝 관점에서 비교해 이해하기 쉬운 부분. 나머지(가설검정 등)는 교재로 자습. [녹음4 08:12–08:25]

Q20. 다음 차시 발표 요청 주제와 그 항목 수.

<!-- page 11 -->

TRIPOD(+AI) 예측모형 보고 체크리스트, 약 20~25개 항목. [녹음4 42:11–42:59]

#### 5.3 서술형

Q21. 기대 테스트 MSE의 bias-variance 분해를 유도하고, 교수님이 이를 "universal"하다고 한 의미와 0-1 loss의 경우를 비교하라.

Y = f(x₀)+ε, E(ε)=0, Var(ε)=σ², f̂ ⊥ ε. E(Y−f̂)² = E(f−f̂)² + σ² (교차항 E[(f−f̂)ε]=0). E(f−f̂)² = (f − Ef̂)² + E(f̂ − Ef̂)² = Bias² + Var. 따라서 Bias² + Var + σ². [추가][교재 p.34] "universal"의 의미: 제곱오차처럼 깔끔한 덧셈 분해는 Brier score(확률 예측의 제곱오차)에도 그대로 성립하지만, 0-1 loss(지시함수)는 제곱 구조가 없어 표준 분해가 없다(unsolved). 그럼에도 "복잡도가 커지면 bias류 양은 줄고 variance류 양은 늘어 test error가 U자"라는 fundamental picture는 loss·outcome 종류에 관계없이 성립한다는 것이 교수님의 요지. [녹음1 01:06, 08:30–10:59][노트 p.5, p.8] (S012, S022)

Q22. 선형회귀를 보는 두 관점(true model view, projection view)을 설명하고, 각 관점에서 통계학과 기계학습이 "같은 식"을 어떻게 다르게 다루는지 likelihood와 loss function의 관계를 중심으로 서술하라.

(1) True model view: E(Y|X=x) = xᵀβ가 실제 데이터 생성 메커니즘이고 β는 고정 미지 참값. 관심은 β의 추론(검정·CI·해석). 정규오차를 가정하면 likelihood L(β,σ²) = Π(2πσ²)^{-1/2}exp{−(yᵢ−xᵢᵀβ)²/2σ²}를 최대화(MLE)하며, log-likelihood의 2차 미분(Fisher information)에서 s.e.·CI·검정이 나온다. (2) Projection view: 선형식은 E(Y|X)의 최선의 선형 근사 β* = argmin E(Y−Xᵀb)²일 뿐, 데이터 생성 메커니즘과 무관. 관심은 ŷ = xᵀβ̂의 예측 성능. 분포를 지정하지 않고 squared error loss를 최소화한다. (3) 연결: 정규 가정 하 ℓ(β) = const − (1/2σ²)Σ(yᵢ−xᵢᵀβ)²이므로 MLE = OLS, 즉 "−log-likelihood = loss". ML은 분포 지정에 "알레르기"가 있어 loss로 표현하지만, 통계가 보기엔 negative log-likelihood를 최소화하는 것과 같다. 다만 통계는 s.e.·CI 등 불확실성 정량화에 더 관심이 있고, ML에는 hinge loss처럼 분포에 대응하지 않는 loss도 있다. [녹음2 01:35–29:57][노트 p.10–11][칠판 19:26] (S026–S027)

Q23. Belkin et al.(2019)의 double descent를 설명하고, p > n 선형회귀에서 왜 훈련오차 0인 해가 무수히 많은지, 그중 최소노름 해가 bias·variance에 어떤 효과를 주는지, 그리고 이 현상에 대한 비판과 교수님의 입장을 서술하라.

(1) 고전적 U자(under/over-fitting, sweet spot)에 더해 capacity가 interpolation threshold(훈련 risk 0)를 넘는 over-parameterized 영역에서 test risk가 다시 하강할 수 있다는 관찰. (2) Xβ = y는 n개 식, p개 미지수이므로 p > n이면 부정방정식 → 해가 (p−n)차원 아핀 공간. (3) 그중 ‖β‖가 최소인 해를 택하면 보간(bias ≈ 0)을 유지하면서 계수 크기를 가장 강하게 억제(variance regularize) → 조건이 맞으면 sweet spot보다 좋은 예측 risk. 항상은 아니고 오른쪽이 안 나타나거나 더 높을 수도 있다. (4) 비판: regularization을 고려하면 파라미터 수가 곧 complexity가 아니므로 "complexity를 잘못 표현해 생긴 artifact"라는 견해; 아직 잘 이해되지 않음. (5) 교수님 입장: 훈련오차 0이 곧 나쁜 것은 아니라는 문을 열었고 sample size 이상의 파라미터+좋은 regularization이 유용할 가능성을 이론적으로 처음 설명했지만, "반드시 여기를 찾으라는 얘기는 절대 아님", 비용이 들고 보장이 없으며 "문제에 따라 다르다". [녹음1 11:12–23:28][녹음3 00:05–02:58][노트 p.8–9] (S023)

Q24. 경사하강법의 원리를 선형회귀의 제곱오차 손실로 설명하고, (a) 닫힌 해가 있는데도 경사하강을 배우는 이 유, (b) 학습률의 역할, (c) 뉴턴법과의 비교, (d) mini-batch SGD, (e) 신경망으로의 확장(역전파·비볼록성)을 서술하라.

L(β) = (1/2n)‖y−Xβ‖²는 볼록한 밥그릇. ∇L = −(1/n)Xᵀ(y−Xβ)는 손실이 가장 빠르게 증가하는 방향이므로 β ← β − η∇L로 반대 방향으로 조금씩 내려가면 ∇L = 0인 유일한 최소점(= (XᵀX)⁻¹Xᵀy)에 수렴. (a) 닫힌 해는 L이 2차 식이라 생긴 특수한 행운; 로지스틱 회귀·신경망에는 없다. 레시피는 "목적함수 값 + gradient"만 요구하므로 일반적. (b) η(learning rate)는 step 크기: 너무 작으면 비효율, 너무 크면 overshoot·발산 — 선택이 "art". (c) 뉴턴법 θ ← θ − H⁻¹∇L은 훨씬 빠르지만 p×p Hessian 역행렬(O(p³))이 필요해 파라미터가 수십억이면 불가능 → 1차 방법 선호. (d) n개를 배치로 나눠 일부로 gradient를 근사해 갱신(잡음 있지만 싸다) — 기본 틀은 유지. (e) f(x;θ)가 비선형 층의 합성이면 ∇L은 chain rule을 역방향으로 조직한 역전파로 구하고, 지형이 비볼록이라 국소최소·안장

<!-- page 12 -->

점·고원이 생겨 초기화와 잡음이 중요 → 사전학습·모멘텀·RMSProp·dropout·ReLU(Hinton). "딥러닝이라고 새로운 것은 별로 없다 — 원리는 같다." [노트 p.24–27][녹음3 06:06–13:46][칠판 20:08] (S066–S076)

Q25. 이진 outcome에서 선형회귀 대신 로지스틱 회귀를 쓰는 이유를 link function의 관점에서 설명하고, 로지스틱 회귀의 모수 추정(MLE)이 왜 cross-entropy 최소화와 같은지, 그리고 이것이 Ch.3의 "likelihood ↔ loss" 논의와 어떻게 이어지는지 서술하라.

(1) 예측·분류만 목적이면 Y∈{0,1}에 선형회귀를 써도 되지만(LDA와 동등), E(Y|X)=P(Y=1|X)는 (0,1)인데 우변 β₀+β₁X는 ℝ이라 확률이 [0,1]을 벗어난다. 좌·우변의 범위를 잇는 link g를 도입: logit g(p)=log(p/(1−p)) → p = e^{xβ}/(1+e^{xβ}) (S자, 항상 (0,1)). link 선택이 곧 해석: logit이 X에 선형이므로 ∂logit/∂X = β₁, exp(β₁) = odds ratio — 역학·임상의 루틴. (2) 0-1 loss는 step function이라 미분 불가 → surrogate로 베르누이 likelihood L(β) = Πpᵢ^{yᵢ}(1−pᵢ)^{1−yᵢ}를 최대화. −log를 취하면 −Σ[yᵢlog pᵢ + (1−yᵢ)log(1−pᵢ)] = cross-entropy loss. 따라서 MLE = cross-entropy 최소화이며, 볼록이지만 닫힌 해가 없어 gradient method(또는 IRLS)로 푼다. (3) Ch.3에서 정규 likelihood의 −log가 제곱오차였듯, 여기서는 베르누이의 −log가 cross-entropy, 다범주에서는 multinomial의 −log가 softmax cross-entropy. "통계의 likelihood에 로그를 취하고 마이너스를 붙여 loss로 보고 gradient method로 최소화" — continuous에서 한 것을 binary에 그대로 적용한 것이며 신경망에서도 같다. [녹음4 24:20–41:33][노트 p.30–32][칠판 21:10–21:24] (S082–S087)

Q26. (보건학 응용) Default 데이터의 LDA 혼동행렬(예측 No/Yes × 실제 No/Yes = 9644, 252 / 23, 81)을 이용해 전체 오류율·민감도·특이도를 계산하고, 전체 오류율이 낮은데도 이 분류기가 부적절할 수 있는 이유와 개선 방법을 Bayes classifier의 성질과 연결해 서술하라.

전체 오류 = (23+252)/10000 = 2.75%. 민감도 = 81/333 = 24.3%, 특이도 = 9644/9667 = 99.8%, FNR = 75.7%, FPR = 0.2%. Bayes classifier(threshold 0.5)는 어느 클래스의 오류인지 구분하지 않고 전체 오류율만 최소화하므로, 소수 클래스(default 3.3%)를 대부분 놓친다 — 항상 No라고 해도 3.33% 오류라 2.75%는 거의 이득이 없다. 카드사·임상처럼 FN 비용이 크면 threshold를 0.2나 0.1로 낮춰 민감도를 높이고(FP 증가 감수), ROC·AUC로 모든 threshold의 trade-off를 보며 도메인 지식(비용)으로 결정한다. 즉 손실이 비대칭이면 0-1 loss 대신 비용 가중 loss가 맞다. [교재 p.144–147] (S112–S115)

### 6. 셀프 체크리스트

학습을 마친 뒤 스스로 답할 수 있으면 ☑ 표시. 괄호는 해당 슬라이드.

- [ ] 훈련 MSE와 테스트 MSE의 차이, overfitting의 정의를 말할 수 있다 (S003–S005)

- [ ] 기대 테스트 MSE의 세 성분 분해식을 쓰고 유도 개요를 설명할 수 있다 (S012)

- [ ] bias·variance가 유연성에 따라 어떻게 변하는지, 세 예시 그림을 그릴 수 있다 (S006–S013)

- [ ] 0-1 loss, 오류율, Bayes classifier, Bayes error rate(1−E[max P])를 정의할 수 있다 (S014–S016)

- [ ] "Bayes classifier를 따라하는" 두 가지 접근(확률 추정 / h 직접)을 예와 함께 말할 수 있다 (S016, S080)

- [ ] KNN의 확률 추정식과 K에 따른 bias·variance 변화를 설명할 수 있다 (S017–S021)

- [ ] Brier score의 분해와 0-1 loss 분해가 "unsolved"인 이유를 말할 수 있다 (S022)

- [ ] double descent 곡선, interpolation threshold, p>n의 최소노름 해, "항상은 아님"을 설명할 수 있다 (S023)

- [ ] 논문발표의 키워드(interpolation, model class H, inductive bias, RFF)를 설명할 수 있다 (논문발표)

- [ ] 선형회귀의 두 관점을 표로 비교할 수 있다 (S026)

- [ ] likelihood의 정의(분포 가정 → 데이터 대입 → 모수의 함수)와 log를 취하는 이유를 말할 수 있다 (S027)

- [ ] 정규 선형회귀에서 MLE = OLS임을 식으로 보일 수 있다 (S027)

- [ ] Fisher information(2차 미분, 뾰족함)과 s.e.·CI·검정의 관계를 설명할 수 있다 (S027, S034–S039)

- [ ] ";"와 "|", frequentist와 Bayesian, prior의 뜻을 말할 수 있다 (S026–S027)

- [ ] F-검정과 개별 t-검정의 역할 차이, 왜 F-검정이 필요한지 설명할 수 있다 (S036–S039)

- [ ] R²가 모델 선택 기준이 될 수 없는 이유와 음수 R²의 의미를 말할 수 있다 (S042)

<!-- page 13 -->

- [ ] forward/backward selection 절차와 "요즘은 lasso·ridge·ensemble"이라는 교수님 입장을 안다 (S040–S041)

- [ ] dummy 변수·baseline·상호작용·다항회귀의 기본을 교재로 자습했다 (S043–S054)

- [ ] KNN 회귀 vs 선형회귀: 참 모형이 선형일 때·고차원일 때 누가 이기는지 설명할 수 있다 (S057–S062)

- [ ] 목적함수 L(β₀,β₁)이 볼록한 밥그릇이며 등고선·별표의 의미를 말할 수 있다 (S066–S067)

- [ ] gradient의 정의·성질과 경사하강 갱신식, η의 역할을 설명할 수 있다 (S068–S071)

- [ ] 단순회귀 손실의 편미분과 벡터형 ∇L = −(1/n)Xᵀ(y−Xβ)를 유도할 수 있다 (S070)

- [ ] 경사하강이 "일반적"인 이유, 뉴턴법의 한계(O(p³)), mini-batch SGD를 설명할 수 있다 (S072)

- [ ] 신경망의 학습이 같은 레시피인 이유와 역전파·비볼록성·Hinton 도구상자를 말할 수 있다 (S073–S076)

- [ ] classifier h, decision boundary, classification risk, empirical risk를 수식으로 쓸 수 있다 (S080)

- [ ] multi-class와 multi-label의 차이를 보건 예로 말할 수 있다 (S080)

- [ ] 이진 Y에 선형회귀를 쓸 때의 장단점과 역학·임상이 로지스틱을 선호하는 이유를 안다 (S082–S083)

- [ ] logit link, odds, odds ratio, sigmoid 식을 쓰고 "link choice ⇒ interpretation"을 설명할 수 있다 (S082–S086)

- [ ] 3범주를 1,2,3으로 코딩하면 안 되는 이유를 말할 수 있다 (S084)

- [ ] 0-1 loss가 미분 불가능한 이유와 surrogate loss, 그리고 직접 최적화 연구에 대한 교수님 평가를 안다 (S087)

- [ ] 베르누이 likelihood → cross-entropy, multinomial → softmax의 대응을 식으로 쓸 수 있다 (S087, S097)

- [ ] balance 1000·2000에서의 default 확률을 계산할 수 있다 (S088)

- [ ] confounding(student 계수 부호 반전)을 설명할 수 있다 (S090–S091)

- [ ] LDA·QDA·naive Bayes의 가정 차이와 판별함수의 형태(선형/이차)를 안다 (S099–S118)

- [ ] 혼동행렬에서 민감도·특이도·FPR·FNR·AUC를 계산·해석하고 threshold 조정의 효과를 안다 (S112–S115)

- [ ] 로지스틱 회귀 vs LDA(discriminative vs generative), KNN의 장단점을 비교할 수 있다 (S119–S121)

- [ ] 수업 운영 사항(슬라이드 업로드·영어, LLM 오류 찾기 과제 → 성적, TRIPOD 발표)을 안다 (녹음4)
