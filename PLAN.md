# 계획 문서 — 「보건학을 위한 기계학습」 학습자료 공개 저장소

작성 2026-10-24 · 담당 Jae-Yul Woo · 저장소 <https://github.com/dkdlqoddi/study-arrangement> (이미 **PUBLIC**, 아직 커밋 0개)

## 1. 목표

- 한 학기(현재 1~8차시, 2026-09-02 ~ 2026-10-21) 동안 배운 내용을 **ChatGPT 웹사이트에서 URL만 주면 바로 읽히는 Markdown**으로 정리한다.
- 원본(PDF·PPTX·녹음·칠판 사진, 1.5 GB)은 로컬 `machine_learning_for_health_science/` 에만 두고 **GitHub에는 올리지 않는다**.
- 문서를 빨리 찾아갈 수 있는 인덱스(주차별·주제별·모아보기)를 함께 제공한다.
- **공개 범위(2026-10-24 결정)**: GitHub에는 각 차시 「시험대비 학습자료 요약본」과 학기 「모아보기」만 올린다. 전체판·강의노트·슬라이드·녹음 받아쓰기·논문읽기과제(Efron 발표·요약, 동료 Shmueli 발표자료)·R 코드·공통 자료는 로컬 `private/`(git 제외)에만 둔다. 교재·논문 원문은 링크만. 변환물 전체에서 사람 이름은 `[발표자]`, `[발표 학생]`으로 치환한다.

## 2. 현황 스냅샷 (2026-10-24)

| 항목 | 값 |
|---|---|
| 원본 | 8개 주차 폴더 + 공통 5개 파일, **267개 파일, 1.5 GB** (jpg 117, pdf 64, txt 29, m4a 18, wma 11, pptx 8, json/jsonl 14, html 3, docx 2, md 1) |
| 변환 결과 | Markdown **223개**(주차 문서 201 + 모아보기 20 + 공통 2), 약 186만 tokens, 가장 큰 파일 11,826 tokens. 분할 문서에는 목차 파일(`…/study_guide_summary.md` 등) 추가 |
| 공개(docs/) | **요약본 24파트 + 모아보기 20파트 = 44개 문서**, 목차 파일 11개, 주차 README 8개, manifest 1개 → 커밋 대상 **74개 파일**(루트 문서 6, tools 4 포함) |
| 비공개(private/) | 전체판 100파트, 강의노트 11파트, 슬라이드 18, 받아쓰기 38파트, 논문과제 8파트, R 코드 2, 공통 2 + 목차·README·INDEX·manifest. `.gitignore`의 `private/`로 제외 |
| 변환 내역 | 요약본 7건(24파트, 2차시는 요약본 없음) · 전체판 8건(100파트) · 강의노트 8건(11파트) · 슬라이드 18건 · 받아쓰기 26건(38파트) · 논문과제 6건(8파트) · R 코드 2건 · OCR 약 170쪽 |
| 파일 크기 한도 | 파일당 **12,000 tokens**(o200k_base) 이하로 분할 → ChatGPT 웹 브라우징이 한 번에 읽는 범위 안 |
| GitHub | 원격 저장소는 PUBLIC·빈 상태. 로컬에도 커밋 없음 → **첫 커밋부터 `.gitignore` 적용됨** |
| 로컬 환경 | WSL2 Ubuntu 22.04, Python 3.10, sudo 없음(pip --user 사용) |

## 3. 저장소 구조

```
.
├── README.md            시작점: 빠른 탐색 방법 표, 주차 요약, ChatGPT 사용법, 공개 범위
├── INDEX.md             공개 문서 인덱스 (자동 생성)
├── TOPICS.md            주제·키워드 → 문서 매핑 (비공개 자료는 '(비공개)'로 표시)
├── PLAN.md              이 문서 (완료/할 일)
├── llms.txt             공개 문서의 raw URL 목록 (ChatGPT에 한 줄로 전달용, 자동 생성)
├── .gitignore           원본 디렉토리, 원본 파일 형식, private/ 제외
├── tools/
│   ├── convert_sources.py   원본 → 변환 + 공개/비공개 분리 + 인덱스 생성 파이프라인
│   ├── pdfmd.py             PDF → Markdown (제목 복원·표·OCR·띄어쓰기 복원)
│   ├── check_links.py       깨진 링크·비공개 경로 누출·토큰 한도·manifest 누락 점검
│   └── requirements.txt
├── docs/                ← 공개 (GitHub에 올라감)
│   ├── compiled/            모아보기: 용어집·예상문제·강조 포인트·체크리스트·요약표·강의 개요 (+ 목차 파일)
│   ├── weekNN_YYYYMMDD/
│   │   ├── README.md                 주차 인덱스 (키워드, 공개 문서 표, 비공개 자료 건수)
│   │   ├── study_guide_summary.md    여러 부일 때 목차(각 부의 절 제목 + raw URL)
│   │   └── study_guide_summary_partNN.md   N차시 시험대비 학습자료(요약본)
│   └── manifest.json        공개 문서 목록 (경로·토큰 수)
├── private/             ← 비공개, git 제외 (로컬에서 ChatGPT 파일 업로드 등에 사용)
│   ├── INDEX.md             전체(공개+비공개) 인덱스
│   ├── manifest.json        전체 목록
│   └── docs/
│       ├── common/              학습자료 생성 프롬프트, 교재·논문 공식 링크
│       └── weekNN_YYYYMMDD/
│           ├── README.md                 주차 전체 목록, 미변환 원본과 사유
│           ├── week_manifest.json        주차 변환 결과
│           ├── study_guide_full/…_partNN.md   전체판
│           ├── lecture_notes*.md         OneNote 강의노트 텍스트(+OCR)
│           ├── slides/*.md               교수님 슬라이드 PDF 텍스트(+OCR), 동료 발표자료
│           ├── transcripts/recN*.md      녹음 받아쓰기
│           ├── code/*.R                  수업 배포 R 코드
│           └── paper_assignment/*.md     (2차시) Efron 논문 발표·요약 (이름 치환)
└── machine_learning_for_health_science/   원본 — git 제외
```

## 4. 완료된 작업

- [x] **원본 전수 조사** — 267개 파일의 형식·크기·중복(md5)·텍스트 추출 가능 여부 분석. 주요 발견:
  - 주차마다 `N차시 시험대비 학습자료(.pdf / (전체판).pdf)`, OneNote 강의노트 PDF, 슬라이드 PDF, Whisper 받아쓰기 txt, 녹음, 칠판 사진이 있음. 2차시만 요약본이 없고 전체판만 있음.
  - 슬라이드 PDF 중 Ch04·ModelSelection·OtherPenalty·Ch7_BeyondLinear·Intro·Chap1·CrossValidation(일부)은 **이미지 전용(텍스트 층 없음)** → OCR 필요.
  - 같은 슬라이드 PDF가 여러 주차에 중복(MVG 3회, NN 슬라이드 3회 등). 5차시 녹음 m4a는 폴더 안팎에 2벌.
  - `20261022_강의노트.pdf`(271쪽)는 1~8차시 **누적** 노트북. 8차시 부분은 p.236~271.
  - `20261014/20261014-notes.pdf`는 **다른 과목**(Topics in Biochemical Engineering, 10/13) 노트가 섞여 들어온 것 → 제외.
  - 학습자료 생성 작업 파일(`~/.cache/claude-work/`)은 남아 있지 않아 전체판은 PDF에서 역변환함.
- [x] **변환 파이프라인 작성** (`tools/convert_sources.py`, `tools/pdfmd.py`)
  - PDF: 글꼴 크기·굵기로 제목 단계 복원, 줄 간격으로 문단 경계 판단해 PDF 줄바꿈을 한 문단으로 합침, `find_tables()`로 표를 Markdown 표로(색 박스를 표로 오인한 것은 필터), 이미지 전용 페이지는 **RapidOCR(PP-OCRv4 한국어 모델)** 로 OCR.
  - 한글 줄바꿈 경계에서 사라진 띄어쓰기와 OneNote 내보내기에서 사라진 띄어쓰기는 **kiwipiepy**로 복원.
  - PPTX(제목·본문·표·발표자 노트), DOCX(문단·제목·표), HTML(markdownify), 받아쓰기 txt(5분 단위 소제목) 변환.
  - 모든 결과물을 **12,000 tokens 이하**로 제목 경계에서 분할(`_partNN.md`), 각 파트 머리에 이전/다음/인덱스 링크.
  - 이메일·전화번호 자동 제거, 프롬프트 문서의 Windows 사용자 이름 가림.
  - 중복 원본은 처음 등장한 주차에서만 변환하고 다른 주차 README에서 링크. 저작권 자료(ISLR 교재, Efron 논문 원문)는 변환하지 않고 공식 링크만 제공.
- [x] **1~8차시 전체 변환 실행** — 결과는 [INDEX.md](INDEX.md), 각 `docs/weekNN_*/README.md`.
- [x] **모아보기 문서 생성** (`docs/compiled/`) — 각 차시 학습자료의 용어 정리·강조 포인트·예상문제·체크리스트·요약표·강의 개요를 학기 단위 파일로 합침.
- [x] **공개/비공개 분리** — `PUBLIC_CATEGORIES = {요약본, 모아보기}`. 인덱스 단계에서 비공개 문서를 `private/docs/`로 옮기고, 공개 INDEX/README/llms.txt는 공개 문서만 가리키게 생성. `check_links.py`가 공개 문서→비공개 경로 링크(누출)를 0건으로 확인.
- [x] **사람 이름 치환** — 동료 학생(Shmueli 발표자)과 Efron 발표자 이름을 `[발표 학생]`, `[발표자]`로 치환(파일명·본문·manifest 포함, 띄어쓰기 복원으로 갈라진 경우까지). 공개·비공개 트리 모두 잔존 0건.
- [x] **`.gitignore`** — `machine_learning_for_health_science/` 전체 + `*.pdf *.pptx *.docx *.wma *.m4a *.jpg` 등 원본 형식 + `.fablize/` + `private/` 제외.
- [x] **탐색 보조 문서** — `README.md`(빠른 탐색 방법 표), `INDEX.md`, `TOPICS.md`, `llms.txt`, 주차별 `README.md`.
- [x] **점검 스크립트** `tools/check_links.py` — 모든 Markdown의 상대 링크가 실제 파일을 가리키는지, 파일이 토큰 한도를 넘지 않는지 확인.
- [x] **계획 문서(이 파일)** 작성.

## 5. 해야 할 작업

### 5.1 공개 전 확인 (2026-10-24 결정 반영)

- [x] **공개 범위 결정** — 요약본 + 모아보기만 공개. 전체판·강의노트·슬라이드·받아쓰기·논문과제·코드·공통은 `private/`(git 제외).
- [x] **동료 학생 자료** — Shmueli 발표자료는 비공개로 이동, 파일명·본문의 실명은 `[발표 학생]`으로 치환.
- [x] **Efron 발표 내용** — 발표자 이름을 `[발표자]`로 치환(비공개 폴더에 보관).
- [x] **교재·논문 원문** — 변환하지 않음. README에 공식 링크만.
- [ ] 첫 push 전에 공개 문서 44개를 한 번 훑어 **교수님 사담·수강생 언급**이 공개해도 괜찮은지 확인한다(`rg -n "교수님 농담|여담|학생" docs/`). 요약본에는 녹음 인용(교수님 발언 요약)이 들어 있으므로, 부담되면 PUBLIC_CATEGORIES에서 `study_guide_summary`를 빼고 모아보기만 공개하는 선택도 가능하다.
- [ ] 저장소 공개 상태 자체를 다시 확인한다: `gh repo view dkdlqoddi/study-arrangement --json visibility`. Private으로 바꾸려면 `gh repo edit dkdlqoddi/study-arrangement --visibility private --accept-visibility-change-consequences`.

### 5.2 GitHub 반영

- [ ] 첫 커밋 전 확인: `python3 tools/check_links.py` 가 깨진 링크 0·한도 초과 0을 보고하고, `git status --short | grep -v '^??'` 가 비어 있고, `git check-ignore -v machine_learning_for_health_science/ISLR_1stEd.pdf` 가 `.gitignore` 규칙을 가리키는지 확인.
- [ ] 커밋·푸시:
  ```bash
  git add .gitignore README.md INDEX.md TOPICS.md PLAN.md llms.txt tools/ docs/   # private/ 는 .gitignore 로 자동 제외
  git status --short | grep -c '^A'   # 74개여야 함
  git commit -m "Add ML for Health Science study summaries (weeks 1-8, public scope)"
  git push -u origin main
  ```
- [ ] 푸시 후 raw URL 확인: `curl -sI https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/INDEX.md | head -1` → `200`.
- [ ] ChatGPT에서 테스트: README의 "ChatGPT 질문 템플릿"대로 `docs/compiled/glossary_part01.md`와 한 주차 요약본 URL을 주고 답이 나오는지, 긴 파트 파일이 잘리지 않는지 확인. 잘리면 `--max-tokens 8000`으로 재생성.

### 5.3 다음 주차(9차시~) 추가 절차

1. 원본 폴더 `machine_learning_for_health_science/YYYYMMDD/`에 자료를 넣는다(학습자료 PDF, 강의노트 PDF, 슬라이드 PDF, 받아쓰기 txt).
2. `tools/convert_sources.py`의 `WEEKS` 목록에 항목을 추가한다(n, folder, date, slug, title, topics, summary_pdf, full_pdf, notes, slides, reuse, skip). 다른 주차에 이미 있는 슬라이드는 `slides`가 아니라 `reuse`에 적는다.
3. `python3 tools/convert_sources.py --only week09` 로 해당 주차만 변환한다. 요약본은 `docs/`, 나머지는 `private/`로 자동 분리되고 인덱스·모아보기·llms.txt가 갱신된다. 끝나면 `python3 tools/check_links.py`(깨진 링크 0, 비공개 누출 0, 한도 초과 0 확인).
4. `TOPICS.md`에 새 키워드 행을 추가하고, 5.1 점검 후 커밋·푸시한다.

### 5.4 품질 개선 (선택, 우선순위 순)

- [ ] **2차시 요약본 작성**: 2차시는 전체판만 있어 공개 범위에 요약본이 없다. 전체판(비공개)에서 요약본을 만들어 `20260909/2차시 시험대비 학습자료.pdf`로 저장하고 `WEEKS[1]["summary_pdf"]`에 적으면 자동으로 공개 범위에 들어온다.
- [ ] **TOPICS.md 보강**: 현재는 주차 키워드와 요약본 절 제목 기반. 전체판의 슬라이드 단위 제목(`#### S0xx …`)까지 색인하면 더 세밀해짐.
- [ ] **칠판 사진 117장**: 손글씨 OCR 신뢰도가 낮아 보류. 대안은 (a) 축소 썸네일 + 촬영 시각으로 해당 슬라이드 위치만 표시, (b) 시각 모델로 사진 설명문 생성.
- [ ] **강의노트 안의 슬라이드 캡처 이미지 OCR 전수**: 지금은 텍스트가 전혀 없는 페이지만 OCR. 텍스트와 이미지가 섞인 페이지의 이미지도 OCR하면 강의노트 단독으로도 슬라이드 내용 검색 가능(전체판에 이미 '슬라이드 원문' 박스가 있어 우선순위 낮음).
- [ ] **받아쓰기 교정본**: Whisper 오인식이 많음(특히 1~2차시). ChatGPT로 용어 교정본을 만들어 `transcripts/recN_corrected.md`로 추가.
- [ ] **수식 복원**: OCR·텍스트 추출에서 수식이 깨짐(β̂, Σ 등). 자주 쓰는 수식은 전체판의 '슬라이드 원문' 박스 기준으로 LaTeX로 정리한 `formulas.md`를 만들면 좋음.
- [ ] **ISLR 교재 텍스트**: 공개 저장소에는 넣지 않음(저작권). 개인용으로 필요하면 gitignore된 `private/` 폴더에 장별 텍스트를 뽑아 ChatGPT에 직접 업로드.
- [ ] 변환 스크립트에 단위 테스트(표 필터·분할 규칙) 추가.

## 6. 변환 규칙 (결정 사항)

| 규칙 | 내용 | 이유 |
|---|---|---|
| 파일 크기 | 파일당 ≤ 12,000 tokens (o200k_base, `tiktoken`으로 측정) | ChatGPT 웹 브라우징은 긴 페이지를 앞부분만 읽거나 잘라서 요약하는 경우가 있어, 한 번에 안전하게 읽히는 크기로 제한 |
| 분할 지점 | `##` → `###` → `####` 제목 경계 우선, 그래도 크면 문단(빈 줄) 경계 | 절이 중간에 끊기지 않게 |
| 파트 파일명 | `이름_part01.md`, `이름_part02.md` … + 각 파트 머리에 이전/다음 링크 | 순서대로 읽기 |
| 경로·파일명 | ASCII 소문자 slug (`week03_20260916/slides/cross_validation.md`) | raw URL에 한글이 들어가면 인코딩이 길어지고 복사 실수가 잦음 |
| 제목 표기 | 각 문서 첫 줄에 `#` 한국어 제목, 그 아래 원본 경로·변환 방식·생성일·주의 문구 | 출처 추적 |
| 중복 처리 | md5가 같은 원본은 처음 등장한 주차에서만 변환, 다른 주차는 README의 '다른 주차에서 이미 변환된 자료' 표로 링크 | 저장소 크기·검색 중복 방지 |
| 공개 범위 | `PUBLIC_CATEGORIES = {study_guide_summary, compiled}` 만 `docs/`, 나머지는 `private/docs/`(동일 구조, git 제외). 공개 문서는 비공개 경로를 링크하지 않음(`check_links.py`가 검사) | 교수님 노트 원문·녹음·슬라이드·동료 자료의 저작권·개인정보 |
| 이름 치환 | `REDACT` 목록(동료 학생, 발표자)을 본문·파일명·manifest에 적용. 띄어쓰기 복원으로 갈라진 이름도 정규식으로 잡음 | 공개 저장소에 실명이 남지 않도록 |
| 제외 | 녹음(wma/m4a), 칠판 사진, 교재·논문 원문 PDF, `.fablize/`, pptx 초안·템플릿, 다른 과목 노트 | 용량·저작권·중복 |
| 변환 불가 표시 | 이미지 전용 페이지는 `_(이미지 기반 페이지 → OCR …)_`, 전체판의 슬라이드 그림은 `_[그림/슬라이드 이미지 — 원본 PDF p.N 참고]_` | 어디가 누락됐는지 알 수 있게 |

## 7. 알려진 한계

- **한글 띄어쓰기**: PDF 줄 끝에서 단어 사이 공백이 사라진 경우를 kiwipiepy로 복원하지만 100%는 아니다(복합명사를 과하게 띄우는 경우도 있음).
- **수식**: 텍스트 추출·OCR 모두 수식 기호가 깨진다. 정확한 수식은 원본 PDF를 본다.
- **OCR**: 영문 슬라이드는 양호, 한국어 슬라이드(Intro)는 표·세로 글씨가 섞여 일부 깨짐. 그림 속 축 눈금 숫자가 본문에 섞여 들어온다.
- **OneNote 강의노트**: 손글씨·펜 필기는 텍스트로 나오지 않음. 교수님 말씀의 정확한 원문은 전체판 '부록 A'를 우선 참고.
- **받아쓰기**: Whisper 자동 전사라 용어 오인식이 많다. 시각(mm:ss) 기준으로 원본 녹음과 대조하는 용도.
- **전체판의 슬라이드 이미지**는 텍스트로 옮기지 못했다. 슬라이드 내용은 같은 위치의 '슬라이드 원문' 박스와 `slides/` 폴더(원본 슬라이드 PDF 변환)를 함께 본다.
