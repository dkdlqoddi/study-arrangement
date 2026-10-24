# 보건학을 위한 기계학습 — 학기 학습자료 (Markdown)

서울대 보건대학원 「보건학을 위한 기계학습」(2026-2학기) 수업에서 배운 내용을 **ChatGPT 웹사이트에서 URL로 바로 읽을 수 있는 Markdown**으로 정리한 저장소입니다. 주교재는 ISLR(*An Introduction to Statistical Learning*, 1판)입니다.

- **공개 범위는 각 차시 「시험대비 학습자료 요약본」과 학기 「모아보기」 문서만**입니다. 전체판·강의노트·슬라이드·녹음 받아쓰기·논문읽기과제·R 코드는 저작권과 개인정보 때문에 공개하지 않고 로컬 `private/` 폴더(git 제외)에만 둡니다. 원본(PDF·PPTX·녹음·사진)과 교재·논문 원문도 올리지 않습니다(아래 참고 링크).
- 모든 문서는 **파일당 12,000 tokens 이하**로 나뉘어 있어 ChatGPT가 한 번에 읽을 수 있습니다. 긴 문서는 `_part01.md`, `_part02.md` … 로 이어지고, 각 파트 머리에 이전/다음 링크가 있습니다.
- 학습자료·받아쓰기·OCR은 자동 생성물이므로 오류가 있을 수 있습니다. 문서 머리의 ⚠️ 주의 문구를 확인하세요.
- **ChatGPT에는 URL 하나만 주면 됩니다.** `llms.txt`가 질문 유형별 안내와 차시별 절 색인을 담은 허브라서, ChatGPT가 알맞은 문서를 스스로 찾아 읽습니다(아래 "ChatGPT에서 쓰는 법").

## 문서를 빨리 찾아가는 방법 (추천 순)

| # | 방법 | 이런 때 쓴다 | 어떻게 | 예 |
|---|---|---|---|---|
| 1 | **허브 URL 하나로 질문** [llms.txt](llms.txt) | ChatGPT에 물을 때 (기본) | 아래 템플릿처럼 `llms.txt` raw URL과 질문만 보낸다. ChatGPT가 허브의 색인을 읽고 알맞은 문서를 열어 답한다 | "…/llms.txt 를 읽고 안내에 따라 자료를 찾아 답해줘. 질문: LOOCV 지름길 공식이 왜 성립해?" |
| 2 | **모아보기** `docs/compiled/` | 시험 직전, 또는 개념 하나를 **학기 전체에서** 찾을 때 | [용어집](docs/compiled/glossary.md) · [예상문제](docs/compiled/exam_questions.md) · [교수님 강조 포인트](docs/compiled/key_points.md) · [체크리스트](docs/compiled/checklists.md) · [요약표](docs/compiled/summary_tables.md) · [강의 개요](docs/compiled/overviews.md) 중 하나를 연다 | ChatGPT에 `glossary.md` raw URL을 주고 "lasso와 ridge의 차이를 이 용어집 기준으로 설명해줘" |
| 3 | **주제별 인덱스** [TOPICS.md](TOPICS.md) | 키워드는 아는데 **몇 차시**인지 모를 때 | 키워드 행 → 차시·문서 링크 | "ROC/AUC" → 4차시 요약본, `slides/binary_classifier_performance.md` |
| 4 | **주차 인덱스** [INDEX.md](INDEX.md) → `docs/weekNN_*/README.md` | 특정 차시의 요약본을 볼 때 | 주차별 요약본 표에서 클릭. 여러 부로 나뉜 요약본은 `study_guide_summary.md` 목차 파일에서 절 위치를 확인 | 6차시 → 요약본 3부 |
| 5 | **모아보기 문서 직접 지정** `docs/compiled/` | 허브를 거치지 않고 특정 모아보기 파트만 읽히고 싶을 때 | 해당 파트의 raw URL을 직접 준다 | 아래 템플릿 B |
| 6 | **GitHub 검색** | 정확한 문구·수식 이름·영문 용어로 찾을 때 | 저장소 페이지 위쪽 검색창에 `repo:dkdlqoddi/study-arrangement "LOOCV"` 또는 파일 목록에서 `t` 키 | `"double descent"` |
| 7 | **로컬 ripgrep/grep** | 터미널에서 즉시 찾을 때 | `rg -n "bootstrap" docs/` · `rg -l "교수님 말씀 · 녹음" docs/week05*` | |
| 8 | **받아쓰기 시각으로 녹음 위치 찾기** (로컬 전용) | 교수님이 **실제로 어떻게 말했는지** 확인할 때 | 요약본의 `[녹음2 31:40]` 표기 → `private/docs/weekNN_*/transcripts/rec2.md`의 `## 30:00 – 35:00` 절 → 원본 녹음 파일의 그 시각 | 비공개 자료라 GitHub에는 없음 |
| 9 | **전체판 박스 라벨로 출처별 읽기** (로컬 전용) | 교수님 말씀만/교재 보충만 골라 볼 때 | `private/docs/…/study_guide_full/`에서 `**교수님 말씀 · 강의노트`, `**교재 보충 · ISLR`, `**예상문제**` 라벨을 검색 | `rg -n "교수님 말씀 · 녹음" private/docs/week03*/study_guide_full/` |
| 10 | **ChatGPT Projects / Custom GPT에 업로드** (선택) | URL 없이 매 대화에서 자동 검색하고 싶을 때, 또는 비공개 자료(전체판·받아쓰기)까지 쓰고 싶을 때 | `docs/`(공개)나 `private/docs/`(로컬)를 zip으로 묶어 Project 파일로 추가 | 업로드한 파일은 공개되지 않음 |

## 주차별 바로가기

| 차시 | 날짜 | 주제 | 바로가기 |
|---|---|---|---|
| 1 | 2026-09-02 | 과목 소개 · Chap1 Introduction · Chap2 Part I (Statistical Learning) | [인덱스](docs/week01_20260902/README.md) · [요약본](docs/week01_20260902/study_guide_summary.md) |
| 2 | 2026-09-09 | Chap2 Part I 복습(f 추정, parametric/non-parametric, KNN·차원의 저주) · Chap2 Part II(MSE, Bias-Variance, Bayes classifier) · Efron 논문 발표 | [인덱스](docs/week02_20260909/README.md) · [요약본](docs/week02_20260909/study_guide_summary.md) (전체판에서 2026-10-25 작성) |
| 3 | 2026-09-16 | Chap2 Part II 마무리 · Double descent 발표 · Chap3 Linear Regression · 회귀→경사하강→신경망 · Chap4 분류 시작(로지스틱, MLE) | [인덱스](docs/week03_20260916/README.md) · [요약본](docs/week03_20260916/study_guide_summary.md) |
| 4 | 2026-09-23 | 로지스틱 회귀 심화(우도·Newton–Raphson·odds ratio·환자-대조군) · 다항 로지스틱 · 판별분석의 출발점 · TRIPOD/PROBAST 발표 | [인덱스](docs/week04_20260923/README.md) · [요약본](docs/week04_20260923/study_guide_summary.md) |
| 5 | 2026-09-30 | 판별분석(LDA) · 다변량 정규분포 · Naive Bayes · 이진 분류기 성능(임계값·민감도·특이도·ROC·AUC) | [인덱스](docs/week05_20260930/README.md) · [요약본](docs/week05_20260930/study_guide_summary.md) |
| 6 | 2026-10-07 | 분류기 성능 심화(c-통계량·calibration·PPV/NPV) · Bootstrap · Cross-Validation 시작 | [인덱스](docs/week06_20261007/README.md) · [요약본](docs/week06_20261007/study_guide_summary.md) |
| 7 | 2026-10-14 | Cross-Validation 완결(LOOCV·1-SE·올바른 CV) · Model Selection(subset·Cp/AIC/BIC) · 능형회귀·라쏘 시작 | [인덱스](docs/week07_20261014/README.md) · [요약본](docs/week07_20261014/study_guide_summary.md) |
| 8 | 2026-10-21 | AIC·BIC 유도 · 능형회귀·라쏘 심화 · elastic net·bridge·fused lasso · LLM 사용 시 시험 주의 (Ch7 자료 배포) | [인덱스](docs/week08_20261022/README.md) · [요약본](docs/week08_20261022/study_guide_summary.md) |

전체 목록과 분량(tokens)은 [INDEX.md](INDEX.md)에 있습니다. 여러 부로 나뉜 요약본은 `study_guide_summary.md`가 목차(각 부에 든 절 제목과 raw URL) 역할을 합니다.

## ChatGPT에서 쓰는 법

**방법 1 (권장) — URL 하나와 질문만 보내기.** `llms.txt`는 AI용 허브입니다. 사용 규칙, 질문 유형별 안내, 모아보기 문서 목록, 차시별 요약본의 절(§) 색인과 raw URL이 들어 있어 ChatGPT가 스스로 알맞은 문서를 열어 읽습니다.

```
다음 URL의 안내 문서를 읽고, 그 안의 규칙대로 질문에 맞는 자료를 찾아 읽은 뒤 답해줘. 답 끝에 출처(차시·절)를 밝혀줘.
URL: https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/llms.txt
질문: LOOCV의 지름길 공식이 왜 성립하는지, 교수님이 어떻게 설명했는지 알려줘.
```

질문 예: "lasso와 ridge의 차이를 수업 내용 기준으로 비교해줘", "6차시 예상문제 중 서술형만 골라 내게 출제하고 채점해줘", "AUC가 c-통계량과 같다는 증명을 단계별로 설명해줘", "교수님이 시험에 대해 언급한 내용을 모두 모아줘".

**방법 2 — 문서를 직접 지정하기.** raw URL 규칙은 `https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/` + 저장소 안 경로입니다.

```
https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/docs/compiled/glossary_part01.md
https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/docs/week05_20260930/study_guide_summary_part01.md
```

- 문서 하나: "다음 URL의 문서를 읽고 ○○에 대해 설명해줘. 근거가 된 절 제목을 함께 알려줘. URL: …"
- 여러 파트: "이 문서는 N부로 나뉘어 있어. 1부부터 차례로 모두 읽은 뒤 ○○ 관련 내용을 정리해줘. URL: …_part01.md, …_part02.md, …"
- 시험 대비: "exam_questions_part01.md를 읽고 서술형 문제만 골라 하나씩 출제해줘. 내가 답하면 모범 답안과 비교해 채점해줘."

주의: ChatGPT가 긴 페이지를 앞부분만 읽는 경우가 있어 파일 크기를 12,000 tokens 이하로, 허브(`llms.txt`)도 10,000 tokens 이하로 유지합니다. 그래도 잘리면 "문서의 뒷부분(○○ 절)을 다시 읽어줘"라고 요청하세요.

## 다시 생성하기

원본 폴더가 있는 PC에서:

```bash
python3 -m pip install --user -r tools/requirements.txt
python3 tools/convert_sources.py                # 전체 변환 + 인덱스
python3 tools/convert_sources.py --only week09  # 한 주차만
python3 tools/convert_sources.py --index-only   # 인덱스·모아보기만 다시 생성
python3 tools/check_links.py                    # 깨진 링크·토큰 한도 초과 점검
```

주차를 쉼표로 여러 개 지정해(`--only week04,week05`) 터미널 여러 개에서 나눠 돌릴 수 있습니다. 주차별 결과는 `docs/weekNN_*/week_manifest.json`에 기록되고, 마지막에 `--index-only`로 합칩니다.

새 주차를 넣는 절차와 할 일 목록은 [PLAN.md](PLAN.md)를 보세요.

## 공개 범위와 출처

- **공개**: 각 차시 시험대비 학습자료 **요약본**(`docs/weekNN_*/study_guide_summary*.md`)과 **모아보기**(`docs/compiled/`). 사람 이름(발표 학생 등)은 `[발표자]`, `[발표 학생]`으로 치환했습니다.
- **비공개(로컬 `private/`, git 제외)**: 전체판, 강의노트, 교수님 슬라이드 텍스트, 녹음 받아쓰기, 논문읽기과제(Efron 발표·요약), R 코드, 학습자료 생성 프롬프트. 동료 학생의 발표자료도 여기에만 있습니다.
- 학습자료(요약본·전체판)는 수업 노트·녹음·슬라이드·교재를 바탕으로 AI 도구로 만든 2차 자료입니다. `추가 설명` 박스는 AI 보충(교수님 말씀 아님)입니다. 자동 생성물이므로 오류가 있을 수 있습니다.
- 교재와 논문 원문은 저작권 때문에 포함하지 않았습니다. 공식 링크: ISLR 1판 <https://www.statlearning.com/> · Efron (2020) <https://doi.org/10.1111/insr.12409> · Shmueli (2010) <https://doi.org/10.1214/10-STS330> · Belkin et al. (2019) <https://doi.org/10.1073/pnas.1903070116>
- 수업 자료의 저작권은 담당 교수님에게 있습니다. 개인 학습 목적으로만 사용하세요.
