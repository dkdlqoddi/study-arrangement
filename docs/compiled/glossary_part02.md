<!-- 자동 생성 파일: tools/convert_sources.py 가 원본에서 변환. 직접 수정하지 말고 원본/스크립트를 고치세요. -->
# 용어 정리 모음 (학기 용어집) (2/2)

> 원본: `docs/week*/study_guide_*.md` · 변환 방식: compiled · 생성일: 2026-10-25 · 8개 차시
> [◀ 이전 부분](glossary_part01.md) · [주차 인덱스](../../INDEX.md) · [전체 인덱스](../../INDEX.md)

---
## 7차시 (2026-10-14) — Cross-Validation 완결(k-fold·LOOCV 지름길·1-SE 규칙·올바른 CV) · Model Selection(subset selection·Cp/AIC/BIC/adjR²·AIC vs BIC 철학) · 축소법 시작(능형회귀·라쏘)

_출처: [study_guide_summary_part01.md](../week07_20261014/study_guide_summary_part01.md) · [주차 인덱스](../week07_20261014/README.md)_

### 4. 용어 정리

| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| training error / test error(훈련오차 /검정오차) | 학습에 쓴 자료로 잰 오차(과소추정) / 학습에 쓰지 않은 새 관측의 평균 오차 | V03 |
| model assessment / model selection(모형 평가 / 모형 선택) | 고른 모형의 성능(값) 추정 / 후보 중 고르기(최솟값의 위치) — CV의 두 용도 | V01, V07, V17 |
| validation(hold-out) set approach(검증셋 접근) | 무작위로 한 번 나눠 검증셋 오차로 검정오차를 추정 | V04–V08 |
| k-fold cross-validation, fold | K조각으로 나눠 하나씩 떼어 평가를 K번; fold = 한 조각 | V09–V11 |
| CV (K), C k, n k, MSE k _ _ _ _ | Σ(n k/n)·MSE k; C k = k번째 조각의 관측 번호, n k = 그 크기, _ _ _ _ MSE k = 그 조각의 평균제곱오차 _ | V10, 판서 18:49 |
| LOOCV(leave-one-out CV) | K = n — 한 점씩 빼고 n번 적합; 분할의 무작위성이 없음 | V12–V13 |
| leverage hᵢ / hat matrix H | H = X(XᵀX)⁻¹Xᵀ의 대각원소(1/n ~ 1); LOOCV 지름길의 분모 1 − hᵢ | V14 |
| randomness / seed | 분할(fold 배정)의 무작위성 / 난수의 시작값 — 같은 seed라도 섞는 대상이 다르면 분할이 달라짐 | V08, V12, 3 장 발표 |
| bias–variance trade-off of K | (교재) K↑ 편향↓·분산↑·계산↑, K = 5·10이 절충 | V14 |


| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| Err k(오분류율) _ | Σ I(yᵢ ≠ ŷᵢ)/n k i∈C _k _ | V18 |
| ŜE(CV K) _ | fold 오차의 표준편차 — fold 간 상관 때문에 엄밀히 타당하지 않음 | V18 |
| one-standard-error rule(1-SE 규칙) | 최솟값 + 1 SE 이내에서 가장 단순한 모형을 고름 | V18, M23 |
| Bayes decision boundary / Bayes error rate | 참 분포를 알 때의 최적 경계 / 그때의 오류율(예: 0.133) — 어떤 분류기도 못 내려가는 하한 | V19 |
| high-dimensional data(고차원 자료) | p ≫ n(자료 행렬이 옆으로 긺); 아래로 길면 표본이 많은 자료, 둘 다 크면 빅데이터 | V23, 노트 p.12 |
| information leakage / selection bias | 평가 자료의 정보가 학습(변수 선별 포함)에 새어 들어감 / 그 결과 오류 추정이 낙관적으로 치우침 | V23 |
| nested CV | 바깥 CV는 평가, 안쪽 CV는 선별·튜닝 — 계산량이 K배로 늘어남 | V23 |
| feature selection = variable selection ⊂ model selection | 변수 고르기; model selection은 함수 형태(X vs X²)까지 포함 | M04 |
| null model M₀ / full model M p _ | 예측변수 없음(ŷ = ȳ) / 모든 변수 포함 | M07, M13 |
| best subset selection | 2ᵖ개 모형을 모두 적합; 제약형으로는 Σ I(βⱼ ≠ 0) ≤ s(ℓ0) | M07, M34 |
| forward / backward stepwise selection | 영모형에서 하나씩 추가 / 완전모형에서 하나씩 제거 — 모형 수 1 + p(p+1)/2 | M10–M13 |
| RSS / TSS / R² | Σ(yᵢ − ŷᵢ)² / Σ(yᵢ − ȳ)² / 1 − RSS/TSS — 크기가 다른 모형의 비교에 쓰면 안 됨 | M08, M14, 판서 20:25 |
| predictive R² | 검정 자료에서 계산한 R² — 교수님 비추천("그냥 AIC랑 BIC") | M14 |
| Mallows' Cp | (1/n)(RSS + 2dσ̂²); 가우시안 오차 전용 — "쓰지 말아주세요" | M18 |
| AIC(Akaike information criterion) | −2logL + 2d; KL 발산에 근거한 예측 기준 | M18, 판서 20:25 |
| BIC(Bayesian IC) = SIC(Schwarz IC) | −2logL + (log n)·d; 참 모형 식별(일치성) 기준 | M16, M19, 판서 20:25 |
| goodness of fit / penalty term | −2logL(적합도 항) / 2d 또는 (log n)d(복잡도 벌점 항) | M18 |
| d(모수의 개수) | 추정한 모수의 수(절편 포함, 정규모형이면 σ²도) — 같은 비교 안에서는 일관되게 셈 | M18, 판서 20:25 |
| Kullback–Leibler divergence | 참 분포 f와 모형 g의 차이 E f[log f − log g]; 최소화 ⇔ 새 자료의 기 _ 대 로그가능도 최대화 → AIC | M05, 노트 p.15 |
| consistency(일치성) / efficiency(효율성) | n → ∞에서 참 모형을 고를 확률 → 1(BIC) / 참 모형이 없을 때 예측 손실 최소(AIC) | M05 |
| adjusted R² | 1 − [RSS/(n−d−1)]/[TSS/(n−1)] — 클수록 좋음, 벌점이 가장 약함 | M20 |
| Jacobian | 변수변환 때 밀도에 곱해지는 ∣dz/dy∣(z = log y면 1/y) — AIC 비교 시 2Σlog yᵢ 보정 | M21 |
| lognormal / gamma distribution | 양수·오른쪽 꼬리 분포 — log y가 정규 / 감마 GLM; 모양이 비슷해 같은 척도의 AIC도 비슷해야 정상 | M21 |
| shrinkage / regularization(축소 / 정칙화·규제) | 계수를 0 쪽으로 당겨 분산을 줄이는 기법; '정규화' 번역은 "단어가 올바르진 않습니다"(교수님) | M24–M25 |
| constrained optimization /Lagrangian | 영역 안에서의 최소화 / 제약식에 λ를 곱해 목적함수에 붙여 제약 없는 문제로 바꾸는 방법 | M25–M26, 판서 21:11 |
| ridge regression(능형회귀) | RSS + λΣβⱼ²(ℓ2 벌점) ⇔ Σβⱼ² ≤ C(원·구) | M26–M28 |


| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| lasso | RSS + λΣ∣βⱼ∣(ℓ1 벌점) ⇔ Σ∣βⱼ∣ ≤ s(마름모); Least Absolute Shrinkage and Selection Operator, 카우보이의 올가미 | M31–M35 |
| ℓ1 norm / ℓ2 norm | ‖β‖₁ = Σ∣βⱼ∣ / ‖β‖₂ = √(Σβⱼ²) | M28, M31 |
| tuning parameter λ(hyper-parameter) / budget s(C) | 적합도와 벌점의 균형을 정하는 값 — CV로 고름 / 제약의 크기(클수록 λ가 작음) | M26–M27, M37 |
| penalized likelihood / penalized regression | 로그가능도(또는 RSS)에 벌점을 더한 목적함수 — regularized regression과 같은 말 | M26 |
| solution path(해 경로) | λ에 따른 계수 곡선 — ridge는 0에 점근, lasso는 0에 닿아 머묾 | M28, M33 |
| standardization / scale equivariance | 변수를 표준편차 1로 맞춤 / 최소제곱은 단위를 바꿔도 Xⱼβ̂ⱼ가 불변 — ridge·lasso는 아님 | M29 |
| sparse model / soft-thresholding | 계수 대부분이 0인 모형 / sign(y)·max(∣y∣ − λ/2, 0) — X = I일 때의 lasso 해 | M32, M34 |
| elastic net / bridge | ℓ1·ℓ2 혼합 벌점(꼭짓점은 뾰족, 변은 볼록) / (AI 보충) Σ∣βⱼ∣^q 꼴로 일반화한 벌점 | M25, M53 |
| dimension reduction / PCR / PLS | M < p개 선형결합으로 회귀 / 주성분을 비지도로 / 반응을 반영한 방향을 지도로 | M40–M52 |


## 8차시 (2026-10-21) — AIC·BIC 유도(KL 발산·Laplace 근사) · 능형회귀·라쏘 심화(해 경로·표준화·sparse·oracle·soft thresholding) · elastic net·bridge·fused lasso · LLM으로 능형·라쏘 돌릴 때 시험 주의 (Ch7 자료 배포)

_출처: [study_guide_summary_part01.md](../week08_20261022/study_guide_summary_part01.md) · [주차 인덱스](../week08_20261022/README.md)_

### 4. 용어 정리

| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| best subset / forward·backward stepwise selection | 2ᵖ개 모형을 모두 적합 / 영모형에서 하나씩 추가·완전모형에서 하나씩 제거(모형 수 1 + p(p+1)/2, backward는 n > p 필요) | M07–M13 |
| 훈련오차 / 검정오차 | 적합에 쓴 자료의 오차(과소추정) / 새 자료에서의 오차 — RSS·R²는 훈련오차라 크기가 다른 모형 비교에 부적합 | M14 |
| 간접 추정 / 직접 추정 | 훈련오차에 벌점을 더해 보정(Cp·AIC·BIC·adjusted R²) / 검증셋·교차검증으로 직접 | M15 |
| RSS · TSS · R² | Σ(yᵢ − ŷᵢ)² · Σ(yᵢ − ȳ)² · 1 − RSS/TSS | M08, M14, M20 |
| Mallows' Cp | (1/n)(RSS + 2dσ̂²) — 가우시안 선형모형에서 AIC와 비례 | M18 |
| AIC(Akaike information criterion) | −2ℓ(θ̂) + 2p(= −2log L + 2d); 새 자료의 기대 로그가능도(기대 KL)의 추정(Akaike, 1973) | M18, AB04–AB11 |
| BIC(= SIC, Schwarz) | −2ℓ(θ̂) + p·log n; −2 × log 주변가능도의 O(1) 근사(Schwarz, 1978) | M19, AB12–AB16 |
| TIC(Takeuchi IC) | −2ℓ(θ̂) + 2tr(Ĵ⁻¹Î) — 오지정을 허용한 일반 편향을 그대로 쓴 기준 | AB10 |
| AICc | AIC + 2p(p + 1)/(n − p − 1) — 소표본(n/p < 40) 보정 | AB10 |
| adjusted R² | 1 − [RSS/(n − d − 1)]/[TSS/(n − 1)], 클수록 좋음; ≈ (RSS/n)(1 + d/n) 이라 모수당 벌점 ≈ 1 | M20, 판서 18:44 |


| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| d · p(모수의 개수) | 추정한 모수 수 — 슬라이드 M18–M19는 d, AB 덱은 p | M18, AB10 |
| σ̂²(오차분산 추정치) | Cp·BIC 식에 들어가고 AIC의 가능도 안에 숨어 있음; p ≫ n이면 Σ(yᵢ − ŷᵢ)²/n ≃ 0 | M21, 판서 18:44 |
| CV error · ŷ₋ᵢ | (1/n)ΣLoss(yᵢ, ŷ₋ᵢ) — ŷ₋ᵢ는 i(또는 그 fold)를 빼고 적합한 모형의 예측; σ²·d가 필요 없음 | M21, 판서 18:44 |
| one-standard-error rule | CV 최솟값 + 1 SE 이내의 모형 중 가장 단순한 모형을 고름 | M23 |
| 참 밀도 g / 후보 모형 f(·∣θ) /오지정 | 자료를 낳은 미지의 분포 / 모수족 / g가 모수족 안에 없는 경우(AIC 유도는 허용) | AB03 |
| KL 발산(Kullback–Leibler divergence) | KL(g‖f θ) = E g[log g] − E g[log f θ] ≥ 0, g = f일 때만 0; 비대칭이 _ _ _ _ 라 거리가 아닌 '발산' | AB03, 판서 18:59 |
| 의사 참값 θ₀(pseudo-true parameter) | arg min KL(g‖f θ) = arg max E g[log f(Z ∣ θ)] — 모형 안에서 g에 _ _ 가장 가까운 점, 오지정이어도 MLE가 수렴하는 곳 | AB03 |
| 목표량 η | E Y E Z[log f(Z ∣ θ̂(Y))] — MLE로 적합한 모형이 평균적으로 새 자료 _ _ 를 얼마나 잘 예측하나 | AB05 |
| 낙관 편향 b | E Y[ℓ(θ̂)] − nη > 0 ≈ tr(J⁻¹I) — "y를 두 번 쓴다"_ | AB05, AB09 |
| 정보행렬 J · I | J = −E[∂²log f/∂θ∂θᵀ] = 곡률(기대 헤시안), I = E[s sᵀ] = 점수의 분산 — 둘 다 θ₀에서 평가 | AB06 |
| 정보 항등식 | 모형이 맞으면 I = J → tr(J⁻¹I) = p — "이 하나의 항등식이 '2p'가 나오는 곳" | AB06 |
| 샌드위치 분산 | √n(θ̂ − θ₀) → N(0, J⁻¹IJ⁻¹)(White, 1982) — 모형이 맞으면 J⁻¹ | AB06 |
| 2차 테일러 전개 | 1차 항은 최대점에서 0, 2차 항 O(1)이 편향을 만들고 3차 이상은 n → ∞에서 사라짐 | AB07–AB09 |
| 사후 모형확률 / 주변가능도 | P(M k ∣ y) ∝ p(y ∣ M k)π(M k) / p(y ∣ M) = ∫f(y ∣ θ)π(θ)dθ — _ _ _ 사전 모형확률을 같게 주면 주변가능도만 비교 | AB13 |
| Laplace 근사 | h(θ) = ℓ(θ) + log π(θ)를 최빈값 주위에서 2차 전개 → ∫ ≈ exp{h(θ̃)} (2π)^(p/2)∣A∣^(−1/2), A ≈ nĴ, ∣nĴ∣ = nᵖ∣Ĵ∣ | AB14–AB15 |
| 베이즈 인자(Bayes factor) | BF₁₂ = p(y ∣ M₁)/p(y ∣ M₂), log BF₁₂ ≈ −½(BIC₁ − BIC₂) | AB16 |
| 일치성 / 효율성 | 참 모형이 후보에 있을 때 그것을 확률 → 1로 고름(BIC) / 참 모형이 없을 때 예측 손실을 점근적으로 최소화(AIC) | M05, AB16–AB17 |
| 상대적 기준(relative criterion) | AIC 값 자체는 의미가 없고 같은 자료의 모형 간 차이만 의미 — 후보가 garbage면 결과도 garbage | AB10 |
| 축소(shrinkage) / 정칙화 (regularization) | 계수를 0 쪽으로 당겨 분산을 크게 줄이는 기법(대가는 편향) | M24–M25 |
| 조절모수 λ(tuning parameter = hyperparameter) | RSS와 벌점의 상대적 영향을 정하는 값 — 모형을 기술하는 모수가 아니라 "연구자의 마음"; CV(또는 AIC·BIC)로 고름 | M26–M27, M37, 판서 19:24 |
| 예산 S(s) | 제약의 크기 — S가 클수록 대응하는 λ가 작음 | M34, 판서 19:24 |
| 라그랑지안(Lagrangian) | L(β, λ) = Loss + λ(P(β) − S); λ를 고정하면 −λS는 상수 → 제약 문제를 벌점 문제로 바꿈 | M26, 판서 19:24 |
| 벌점항(shrinkage penalty) /penalized = regularized regression | 손실 뒤에 더하는 λΣβⱼ² 등 / 그런 회귀의 두 이름 | M27, 판서 19:54 |
| 등고선(contour) | RSS 값이 같은 β들의 모임 — β̂ 중심의 타원; 처음 제약 영역에 닿는 점이 해 | M26, M35 |


| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| 능형회귀(ridge) / 능형 추정량 | RSS + λΣβⱼ² ⟺ Σβⱼ² ≤ s(원); β̂ᴿ = (XᵀX + λI)⁻¹XᵀY | M26–M29, 판서 19:54 |
| 라쏘(lasso) | RSS + λΣ∣βⱼ∣ ⟺ Σ∣βⱼ∣ ≤ s(마름모); Least Absolute Shrinkage and Selection Operator — 일부 계수가 정확히 0 | M31–M35 |
| ℓ1 노름 / ℓ2 노름 | ‖β‖₁ = Σ∣βⱼ∣ / ‖β‖₂ = √(Σβⱼ²) | M28, M31 |
| 해 경로(solution path) | λ에 따른 β̂ⱼ(λ) 곡선 — 능형은 0에 점근, 라쏘는 0에 닿아 머묾 | M28, M33 |
| 척도 동변성(scale equivariance) | Xⱼ를 c배 하면 β̂ⱼ는 1/c배, Xⱼβ̂ⱼ 불변 — OLS는 성립, 능형·라쏘는 깨짐 | M29, 노트 p.12 |
| 표준화 / 표준화 계수 | x̃ᵢⱼ = xᵢⱼ / √((1/n)Σᵢ(xᵢⱼ − x̄ⱼ)²) / 표준편차 1만큼 변할 때의 효과 | M28–M29 |
| 가변수(dummy variable) | 범주형 변수를 0/1 열로 바꿔 넣음 — "Fair하게 넣도록" | M29 |
| soft thresholding | sgn(y)(∣y∣ − λ/2)₊ — λ/2만큼 0 쪽으로 옮기고 [−λ/2, λ/2]는 0으로 자름 | M34, 판서 20:47 |
| sparse / dense | 소수의 계수만 0이 아님 / 거의 모든 계수가 작게 0이 아님 | M31, 판서 20:20 |
| oracle property | 참으로 0이 아닌 변수를 미리 안 것처럼(선택 일치성 + 점근 효율) 행동하는 성질 | M31 |
| adaptive lasso | 변수마다 벌점 가중치 1/∣β̂ⱼ(초기)∣^γ를 주어 oracle property를 갖게 한 라쏘(AI 보충) | M31 |
| elastic net | 칠판 RSS + λ(αΣ∣βⱼ∣ + (1 − α)Σβⱼ²) / 슬라이드 ‖y − Xβ‖² + λ₂‖β‖² + λ₁‖β‖₁ | M31, OP04–OP05, 판서 20:25 |
| grouping effect | 상관이 큰 변수들이 비슷한 계수를 나눠 가짐: ∣β̂ᵢ − β̂ⱼ∣/∣y∣ ≤ (√2/λ₂)√(1 − ρᵢⱼ) | OP06 |
| group lasso | 변수 묶음을 미리 알 때 묶음째 0으로 만들거나 함께 선택 | OP03 |
| bridge 벌점 | λΣ∣βⱼ∣^q(0 < q < 1) — 오목한 별 모양 영역, 선택은 더 강하지만 비볼록 | M39, 판서 20:34·20:37 |
| 볼록집합 / 볼록성(convexity) | 안의 두 점을 이은 선분이 집합 안에 있음 / 볼록 목적함수는 국소 최솟값 = 전역 최솟값 | M39 |
| generalized lasso | ½‖y − Xβ‖²₂ + λ‖Dβ‖₁(Tibshirani & Taylor, 2011) | OP08 |
| 벌점 행렬 D | 연구자가 정하는 행렬 — I면 표준 라쏘, 1차 차분이면 1-d fused, 간선 행렬이면 2-d fused | OP08–OP11, 판서 20:54 |
| fused lasso(1-d / 2-d) | 이웃 차이 ∣βᵢ₊₁ − βᵢ∣ 또는 간선 차이 ∣βᵢ − βⱼ∣에 ℓ1 벌점 → 계단 (점프)·덩어리(군집)로 융합 | OP09–OP12, 판서 20:56–21:01 |
| trend filtering | 차분 차수로 일반화한 방법 — 1차 차분(0차 trend filtering) = 1-d fused lasso, 2차 차분 = 구간별 직선 | OP10 |
| 부호 제약 회귀(sign-constrained) / 가능 집합 C | C = {β : cₖβₖ ≥ 0 for some k} 위에서 OLS·능형·라쏘를 푸는 것(C-Ridge, C-Lasso, C-EN) | OP18–OP20 |
| LUR(land-use regression, 토지 이용회귀) | 땅의 쓰임새(녹지·공장·도로 등) 변수로 대기오염 농도를 예측하는 환경역학 모형 | OP17 |
| λ min / λ 1se _ _ | CV 오차가 최소인 λ / 그 1 SE 안에서 가장 큰 λ(더 단순한 모형) — glmnet의 coef·predict 기본은 lambda.1se | M23, M37 |
| R glmnet · cv.glmnet 인자 | alpha(1 = 라쏘, 0 = 능형, 사이 = elastic net), lambda(λ 격자), standardize = TRUE(기본), nfolds(기본 10), foldid, family = "binomial" | M29, M37, 6장 6-7 |


| 용어 | 뜻 | 관련 슬라이드 |
| --- | --- | --- |
| scikit-learn 인자 | alpha = λ(벌점 크기), l1 ratio = 섞는 비율, RidgeCV 기본 alphas (0.1, _ 1, 10), LassoCV 기본 cv = 5, LogisticRegression 기본 C = 1(= 1/λ, ℓ2 벌점), 표준화는 StandardScaler | 6장 6-7 |
