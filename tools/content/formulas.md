# 핵심 수식 정리 (LaTeX)

> 1~8차시 수업에서 다룬 핵심 수식을 LaTeX로 정리한 것입니다. 표기는 교재(ISLR 1판)와 수업 슬라이드를 따르되, 정리와 설명은 AI가 쓴 **[추가]** 성격의 자료라 교수님 말씀이 아닙니다. 각 항목의 "어디서" 열은 자세한 설명·유도·교수님 코멘트가 있는 차시 요약본 절(§)입니다. 수식은 GitHub에서 그대로 렌더링됩니다(`$$ … $$`).

## 1. 통계적 학습의 틀 (1~2차시)

| 이름 | 수식 | 뜻 | 어디서 |
|---|---|---|---|
| 모형 | $Y = f(X) + \varepsilon$ | $f$는 체계적 정보, $\varepsilon$은 평균 0·$X$와 독립인 오차 | 1차시 §2.4, 2차시 §2.1 |
| 회귀함수(최적 예측자) | $f(x) = E(Y \mid X = x)$ | 제곱오차 손실에서 평균제곱예측오차를 최소화하는 함수 | 1차시 §2.6, 2차시 §2.1 |
| 환원·비환원 오차 | $E(Y-\hat Y)^2 = \underbrace{[f(X)-\hat f(X)]^2}_{\text{reducible}} + \underbrace{\mathrm{Var}(\varepsilon)}_{\text{irreducible}}$ | 아무리 잘 추정해도 $\mathrm{Var}(\varepsilon)$ 아래로는 못 내려감 | 1차시 §2.5, 2차시 §2.1 |
| 모수적 모형 | $f(X) \approx \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p$ | $f$ 추정을 계수 $p+1$개 추정으로 축소 | 1차시 §2.7, 2차시 §2.2 |
| KNN 회귀 | $\hat f(x_0) = \dfrac{1}{K}\sum_{x_i \in \mathcal N_0} y_i$ | $x_0$에 가장 가까운 $K$개 이웃의 평균으로 $E(Y\mid X=x_0)$ 근사 | 1차시 §2.8, 2차시 §2.3 |

$$
\text{훈련 MSE} = \frac{1}{n}\sum_{i=1}^{n}\bigl(y_i - \hat f(x_i)\bigr)^2,
\qquad
\text{검정 MSE} = \mathrm{Ave}\bigl(y_0 - \hat f(x_0)\bigr)^2
$$

2차시 §2.5: 유연성이 커지면 훈련 MSE는 단조 감소하지만 검정 MSE는 U자형. 훈련 MSE가 작은데 검정 MSE가 크면 과적합.

## 2. Bias–Variance 분해 (2~3차시)

$$
E\bigl(y_0 - \hat f(x_0)\bigr)^2
= \mathrm{Var}\bigl(\hat f(x_0)\bigr) + \bigl[\mathrm{Bias}\bigl(\hat f(x_0)\bigr)\bigr]^2 + \mathrm{Var}(\varepsilon),
\qquad
\mathrm{Bias}\bigl(\hat f(x_0)\bigr) = E\hat f(x_0) - f(x_0)
$$

- 기대값은 "같은 분포에서 훈련셋을 반복 추출해 $x_0$에서 평가"한 평균. 유연한 방법은 분산↑ 편향↓, 경직된 방법은 그 반대. 2차시 §2.6, 3차시 §2.1.
- 3차시 §2.2: Belkin 외(2019)의 double descent — 보간(interpolation) 문턱을 넘은 뒤 검정오차가 다시 내려가는 현대판 trade-off.

## 3. 분류의 기초 (2~3차시)

| 이름 | 수식 | 뜻 | 어디서 |
|---|---|---|---|
| 훈련 오류율 | $\dfrac{1}{n}\sum_{i=1}^{n} I(y_i \neq \hat y_i)$ | 0-1 손실의 평균 | 2차시 §2.7, 3차시 §2.7 |
| Bayes 분류기 | $\hat y_0 = \arg\max_j \Pr(Y=j \mid X=x_0)$ | 조건부 확률이 가장 큰 범주. 2범주면 $\Pr(Y=1\mid X=x_0) > 1/2$ 이면 1 | 2차시 §2.7 |
| Bayes 오류율 | $1 - E\bigl[\max_j \Pr(Y=j \mid X)\bigr]$ | 분류의 비환원 오차(회귀의 $\mathrm{Var}(\varepsilon)$에 대응) | 2차시 §2.7 |
| KNN 분류 | $\Pr(Y=j \mid X=x_0) \approx \dfrac{1}{K}\sum_{i \in \mathcal N_0} I(y_i = j)$ | 이웃 비율로 조건부 확률 추정 후 최대 범주 선택 | 2차시 §2.7 |

## 4. 선형회귀 (3차시)

$$
\hat\beta = (X^\top X)^{-1} X^\top y,
\qquad
\mathrm{RSS} = \sum_{i=1}^{n}(y_i - \hat y_i)^2,
\qquad
R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}},\ \ \mathrm{TSS} = \sum_{i=1}^{n}(y_i - \bar y)^2
$$

$$
\mathrm{SE}(\hat\beta_1)^2 = \frac{\sigma^2}{\sum_{i=1}^{n}(x_i - \bar x)^2},
\qquad
\hat\sigma^2 = \frac{\mathrm{RSS}}{n-p-1}
$$

- 두 관점(3차시 §2.3): 기하적 최소제곱(RSS 최소화) vs 확률모형 $Y \mid X \sim N(X\beta, \sigma^2)$의 최대가능도. 정규오차에서는 두 답이 같다.
- 가능도(3차시 §2.4): $L(\beta,\sigma^2) = \prod_i \phi\bigl(y_i; x_i^\top\beta, \sigma^2\bigr)$, 로그가능도를 최대화 ⇔ RSS 최소화.
- 경사하강(3차시 §2.6): $\beta^{(t+1)} = \beta^{(t)} - \eta\,\nabla_\beta \mathrm{RSS}$, $\nabla_\beta \mathrm{RSS} = -2X^\top(y - X\beta)$. 같은 손실에 비선형 층을 쌓으면 신경망("One idea, many models").

## 5. 로지스틱 회귀 (3~4차시)

$$
p(X) = \Pr(Y=1 \mid X) = \frac{e^{\beta_0 + \beta_1 X}}{1 + e^{\beta_0 + \beta_1 X}},
\qquad
\log\frac{p(X)}{1-p(X)} = \beta_0 + \beta_1 X
$$

$$
\ell(\beta) = \prod_{i=1}^{n} p(x_i)^{y_i}\bigl(1-p(x_i)\bigr)^{1-y_i},
\qquad
-\log \ell(\beta) = -\sum_{i=1}^{n}\Bigl[y_i \log p(x_i) + (1-y_i)\log\bigl(1-p(x_i)\bigr)\Bigr]
$$

| 이름 | 수식 | 뜻 | 어디서 |
|---|---|---|---|
| 0-1 손실과 대리 손실 | $I(y \neq \hat y)$ 대신 $-\log$ 우도(cross-entropy)를 최소화 | 0-1 손실은 미분 불가 → 볼록한 대리(surrogate) 손실 | 3차시 §2.9, 4차시 §2.2 |
| odds ratio | $\mathrm{OR} = e^{\beta_1}$ | $X$가 1 증가할 때 odds가 $e^{\beta_1}$배 | 4차시 §2.4 |
| 추론 | $z = \hat\beta_1 / \mathrm{SE}(\hat\beta_1)$ | 정규근사 p-value; SE는 관측 정보행렬의 역행렬 대각 | 4차시 §2.3 |
| Newton–Raphson | $\beta^{(t+1)} = \beta^{(t)} - \bigl[\nabla^2 \ell\bigr]^{-1}\nabla \ell$ | 로그우도의 2차 근사로 반복 갱신(IRLS) | 4차시 §2.3 |
| 다항 로지스틱 | $\log\dfrac{\Pr(Y=k\mid x)}{\Pr(Y=K\mid x)} = \beta_{k0} + \beta_k^\top x$ | 기준 범주 $K$ 대비 로짓(baseline category logit) | 4차시 §2.7 |

- 환자-대조군 자료(4차시 §2.5–2.6): 표본 추출이 $Y$에 의존해도 로지스틱 회귀의 기울기 $\beta_1$은 불변, 절편만 $\log(\pi_1/\pi_0)$ 만큼 이동. 유병률은 코호트에서만 추정 가능.

## 6. 판별분석과 다변량 정규분포 (4~5차시)

$$
p_k(x) = \Pr(Y=k \mid X=x) = \frac{\pi_k f_k(x)}{\sum_{l=1}^{K} \pi_l f_l(x)}
$$

$p=1$, $f_k \sim N(\mu_k, \sigma^2)$ (공통 분산)일 때 판별점수:

$$
\delta_k(x) = x\cdot\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log \pi_k,
\qquad
\hat\mu_k = \frac{1}{n_k}\sum_{i:y_i=k} x_i,\quad
\hat\sigma^2 = \frac{1}{n-K}\sum_{k}\sum_{i:y_i=k}(x_i-\hat\mu_k)^2,\quad
\hat\pi_k = \frac{n_k}{n}
$$

$p>1$, 다변량 정규 $N(\mu, \Sigma)$:

$$
f(x) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}} \exp\Bigl(-\tfrac12 (x-\mu)^\top \Sigma^{-1}(x-\mu)\Bigr),
\qquad
\delta_k(x) = x^\top\Sigma^{-1}\mu_k - \tfrac12 \mu_k^\top\Sigma^{-1}\mu_k + \log\pi_k
$$

- LDA는 공통 $\Sigma$(선형 경계), QDA는 범주별 $\Sigma_k$(2차 경계). 4차시 §2.8–2.9, 5차시 §2.1–2.4.
- Naive Bayes(5차시 §2.5, 6차시 §2.8): $f_k(x) = \prod_{j=1}^{p} f_{kj}(x_j)$ — 범주 안에서 변수들이 독립이라 가정해 $\Sigma$ 추정을 피함. 범주형 변수의 0 확률은 Laplace 평활 $\hat p = (c+1)/(n+m)$ 로 보정.

## 7. 이진 분류기의 성능 (5~6차시)

| 이름 | 수식 | 뜻 | 어디서 |
|---|---|---|---|
| 민감도(재현율, TPR) | $\dfrac{TP}{TP+FN}$ | 환자 중 양성으로 맞춘 비율 | 5차시 §2.8 |
| 특이도 | $\dfrac{TN}{TN+FP}$ | 비환자 중 음성으로 맞춘 비율 ($1-$FPR) | 5차시 §2.8 |
| PPV / NPV | $\dfrac{TP}{TP+FP}$, $\dfrac{TN}{TN+FN}$ | 양성(음성) 판정 중 실제 환자(비환자) 비율 — 유병률에 좌우 | 6차시 §2.6 |
| PPV와 유병률 | $\mathrm{PPV} = \dfrac{\mathrm{Se}\cdot\pi}{\mathrm{Se}\cdot\pi + (1-\mathrm{Sp})(1-\pi)}$ | Bayes 정리; 유병률 $\pi$가 낮으면 PPV가 급락 | 6차시 §2.6 |
| ROC / AUC | 임계값을 바꾸며 $(\mathrm{FPR}, \mathrm{TPR})$을 그린 곡선의 아래 면적 | 임계값과 무관한 판별력 지표 | 5차시 §2.8, 6차시 §2.1 |
| c-통계량 | $c = \Pr(S_D > S_{\bar D}) + \tfrac12 \Pr(S_D = S_{\bar D})$ | 환자 1명·비환자 1명을 뽑았을 때 환자 점수가 더 클 확률 | 6차시 §2.2 |
| AUC = c | $\mathrm{AUC} = \int_0^1 \mathrm{TPR}\,d(\mathrm{FPR}) = \Pr(S_D > S_{\bar D})$ | 구분구적법으로 증명; 순위 불변(점수에 단조변환 적용해도 같음) | 6차시 §2.3 |

- 판별(discrimination)과 보정(calibration)은 다른 성질(6차시 §2.4). 학습 손실(cross-entropy)과 평가지표(AUC·민감도 등)는 구분해 보고(6차시 §2.7).

## 8. Bootstrap과 교차검증 (6~7차시)

$$
\mathrm{SE}_B(\hat\alpha) = \sqrt{\frac{1}{B-1}\sum_{r=1}^{B}\bigl(\hat\alpha^{*r} - \bar{\hat\alpha}^{*}\bigr)^2},
\qquad
\Pr(\text{관측 } i \notin \text{부트스트랩 표본}) = \Bigl(1-\tfrac1n\Bigr)^n \xrightarrow{n\to\infty} e^{-1} \approx 0.368
$$

- 경험분포 $\hat F$를 참분포 $F$ 대신 쓰는 것이 원리(6차시 §2.9). 회귀에서는 (x, y) 쌍을 재표집(§2.11). 포함되지 않은 관측(OOB)으로 예측오차를 추정할 수 있지만 CV가 표준(§2.12).

$$
\mathrm{CV}_{(k)} = \frac{1}{k}\sum_{i=1}^{k} \mathrm{MSE}_i,
\qquad
\mathrm{CV}_{(n)} = \frac{1}{n}\sum_{i=1}^{n}\Bigl(\frac{y_i - \hat y_i}{1 - h_i}\Bigr)^2,
\qquad
\mathrm{CV}_{(k)}^{\text{분류}} = \frac{1}{k}\sum_{i=1}^{k}\mathrm{Err}_i,\ \ \mathrm{Err}_i = I(y_i \neq \hat y_i)
$$

- LOOCV 지름길(7차시 §2.3): 최소제곱 적합에서 $h_i = \frac1n + \frac{(x_i-\bar x)^2}{\sum_j (x_j-\bar x)^2}$ 는 leverage. 한 번의 적합으로 $n$번 적합과 같은 값.
- $k$의 편향–분산(7차시 §2.3): $k=n$은 편향이 작지만 분산이 크고, $k=5,10$이 경험적 절충. 1-SE 규칙은 최소 CV 오차의 1표준오차 안에서 가장 단순한 모형 선택(§2.4). 변수 선택을 CV 바깥에서 하면 과소추정(§2.5).

## 9. 모형 선택 기준 (7~8차시)

$$
C_p = \frac{1}{n}\bigl(\mathrm{RSS} + 2d\hat\sigma^2\bigr),
\qquad
\mathrm{AIC} = -2\log L + 2d,
\qquad
\mathrm{BIC} = -2\log L + d\log n
\ \ \Bigl(=\tfrac{1}{n}\bigl(\mathrm{RSS} + \log(n)\, d\,\hat\sigma^2\bigr)\text{ 정규오차}\Bigr)
$$

$$
\text{Adjusted } R^2 = 1 - \frac{\mathrm{RSS}/(n-d-1)}{\mathrm{TSS}/(n-1)}
$$

- $d$는 모수 개수, $\hat\sigma^2$은 전체 모형의 오차분산 추정. 벌점 $2$ vs $\log n$: $n>7$이면 BIC가 더 무겁게 벌해 작은 모형을 고름(7차시 §2.9, 8차시 §2.1).
- 반응변수를 변환한 모형끼리 AIC를 비교할 때는 자코비안 항 $\sum_i \log|g'(y_i)|$을 로그가능도에 더해야 함(7차시 §2.10).
- AIC 유도(8차시 §2.2–2.3): KL 발산 $\mathrm{KL}(g\,\|\,f_\theta) = E_g[\log g] - E_g[\log f_\theta]$ 의 추정에서 생기는 낙관 편향이 $\mathrm{tr}(J^{-1}I)$, 모형이 맞으면 $J=I$라 $\approx p$ → 벌점 $2p$.
- BIC 유도(8차시 §2.4): 사후 모형확률 $\Pr(M_k\mid \text{data}) \propto \int L(\theta)\pi(\theta)\,d\theta$ 를 Laplace 근사하면 $\log \approx \log L(\hat\theta) - \tfrac{p}{2}\log n$ → 벌점 $p\log n$.

## 10. 축소(정규화) 방법 (7~8차시)

$$
\hat\beta^{\mathrm{ridge}} = \arg\min_\beta\ \mathrm{RSS} + \lambda\sum_{j=1}^{p}\beta_j^2
= (X^\top X + \lambda I)^{-1}X^\top y,
\qquad
\hat\beta^{\mathrm{lasso}} = \arg\min_\beta\ \mathrm{RSS} + \lambda\sum_{j=1}^{p}|\beta_j|
$$

| 이름 | 수식 | 뜻 | 어디서 |
|---|---|---|---|
| 제약 형태 ⟺ 벌점 형태 | $\min \mathrm{RSS}\ \text{s.t.}\ \sum_j\beta_j^2 \le s$ (원), $\sum_j|\beta_j| \le s$ (마름모) | 라그랑지안으로 동치; 라쏘의 모서리가 정확한 0을 만듦 | 7차시 §2.12–2.13, 8차시 §2.5 |
| 1차원 능형 | $\hat\beta = \dfrac{y}{1+\lambda}$ | 편향은 늘고 분산은 줄어드는 축소의 가장 단순한 예 | 8차시 §2.8 |
| 1차원 라쏘(soft thresholding) | $\hat\beta = \mathrm{sign}(z)\bigl(|z| - \lambda\bigr)_+$ | $|z| \le \lambda$ 이면 정확히 0 → 변수 선택 | 8차시 §2.12 |
| 능형의 척도 의존성 | $\tilde x_{ij} = \dfrac{x_{ij}}{\sqrt{\frac1n\sum_i (x_{ij}-\bar x_j)^2}}$ | 벌점이 $\beta_j^2$에 걸리므로 표준화 뒤 적합 | 8차시 §2.6 |
| Elastic net | $\lambda\Bigl[\alpha\sum_j|\beta_j| + (1-\alpha)\sum_j\beta_j^2\Bigr]$ | 라쏘의 선택 + 능형의 안정성(grouping effect), 튜닝 모수 2개 | 8차시 §2.10, §2.13 |
| Bridge | $\lambda\sum_j|\beta_j|^q$ | $q=2$ 능형, $q=1$ 라쏘, $q<1$ 이면 비볼록·더 희소 | 8차시 §2.11 |
| Fused lasso | $\lambda_1\sum_j|\beta_j| + \lambda_2\sum_j|\beta_j - \beta_{j-1}|$ | 이웃한 계수를 같게 묶음(순서 있는 변수) | 8차시 §2.13 |

- $\lambda$는 CV로 고르고(7차시 §2.12), 라쏘는 sparse한 참모형에서, 능형은 dense한 참모형에서 유리(8차시 §2.9). 라쏘의 oracle property와 LLM으로 능형·라쏘를 돌릴 때의 주의(표준화·$\lambda$ 격자·seed)는 8차시 §2.7, §2.9, §2.16.
