# 계획 문서 — 「보건학을 위한 기계학습」 학습자료 공개 저장소

작성 2026-10-24 · 최종 갱신 2026-10-25 · 담당 Jae-Yul Woo · 저장소 <https://github.com/dkdlqoddi/study-arrangement> (PUBLIC)

> 한 줄 요약: 8차시까지의 수업 자료를 Markdown으로 변환해, **요약본과 모아보기만** 공개하고, ChatGPT에는 **URL 하나(`llms.txt`)**만 주면 알맞은 문서를 찾아 답하도록 만든다.

## 0. 진행 상황 트래커

| 단계 | 내용 | 상태 | 완료일 | 비고 |
|---|---|---|---|---|
| P1 | 원본 전수 조사 → 변환 파이프라인 작성 → 1~8차시 변환(223개 문서) | ✅ 완료 | 2026-10-24 | OCR 약 170쪽, 띄어쓰기 복원, 12,000 tokens 분할 |
| P2 | 공개 범위 결정·분리: 요약본 + 모아보기만 `docs/`, 나머지는 `private/`(git 제외) · 사람 이름 치환 | ✅ 완료 | 2026-10-24 | `PUBLIC_CATEGORIES`, `private/redact.json` |
| P3 | 첫 커밋·푸시, raw URL 확인 | ✅ 완료 | 2026-10-24 | `e647d76`, `ac46e7f` |
| P4 | **단일 URL 허브 재구축**: `llms.txt`를 "질문 유형별 안내 + 모아보기 목록 + 차시별 절(§) 색인 + raw URL"로 재설계, README 사용법 개정 | ✅ 완료 | 2026-10-25 | 허브 8.1K tokens(한도 10K) |
| P5 | **2차시 요약본 작성·공개**: 전체판(비공개)에서 요약본 Markdown 작성(42,511자, 7절) → 변환(3파트) → 모아보기·허브·TOPICS 반영 | ✅ 완료 | 2026-10-25 | 공개 문서 44→48개 |
| P6 | ChatGPT 실사용 검증(허브 URL + 질문) | ⏳ 대기 | — | 사용자 테스트 필요(6.3) |
| P7 | 9차시 이후 주차 추가 | ⏳ 대기 | — | 수업 진행에 따라, 절차 6.4 |
| P8 | 품질 개선(선택) | ⏳ 대기 | — | 6.5 우선순위 순 |

범례: ✅ 완료 · 🔄 진행 · ⏳ 대기 · ❌ 보류/취소

## 1. 목표와 공개 범위

- 한 학기(현재 1~8차시, 2026-09-02 ~ 2026-10-21) 동안 배운 내용을 **ChatGPT가 URL로 바로 읽는 Markdown**으로 정리한다.
- **사용 방식(2026-10-25 재설계)**: 사용자는 ChatGPT에 `llms.txt`의 raw URL 하나와 질문만 보낸다. 허브 파일이 질문 유형별 안내와 차시별 절 색인을 제공하므로 ChatGPT가 스스로 알맞은 문서를 열어 답한다. 문서별 URL을 외우거나 찾을 필요가 없다.
- **공개 범위(2026-10-24 결정)**: GitHub에는 각 차시 「시험대비 학습자료 요약본」과 학기 「모아보기」만 올린다. 전체판·강의노트·슬라이드·녹음 받아쓰기·논문읽기과제(Efron 발표·요약, 동료 Shmueli 발표자료)·R 코드·공통 자료는 로컬 `private/`(git 제외)에만 둔다. 교재·논문 원문은 링크만. 변환물 전체에서 사람 이름은 `[발표자]`, `[발표 학생]`으로 치환한다.
- 원본(PDF·PPTX·녹음·칠판 사진, 1.5 GB)은 `machine_learning_for_health_science/`에만 두고 `.gitignore`로 제외한다.

## 2. 현황 스냅샷 (2026-10-25)

| 항목 | 값 |
|---|---|
| 원본 | 8개 주차 폴더 + 공통 5개 파일, 267개 파일, 1.5 GB |
| 변환 결과 | Markdown 227개(주차 문서 204 + 모아보기 21 + 공통 2), 약 188만 tokens, 가장 큰 파일 11,826 tokens |
| 공개(`docs/`) | 요약본(8차시, 27파트) + 모아보기(21파트) = 48개 문서 + 목차 파일 + 주차 README 8 + manifest. 2차시 요약본은 전체판에서 작성한 Markdown 원본(3파트) |
| 비공개(`private/`) | 전체판 100파트, 강의노트 11파트, 슬라이드 18, 받아쓰기 38파트, 논문과제 8파트, R 코드 2, 공통 2 + 목차·README·INDEX·manifest·redact.json |
| 허브 | `llms.txt` 8,129 tokens(한도 10,000). 모아보기 21파트(차시 범위 표기) + 요약본 파트 27개의 절 제목 색인 |
| GitHub | PUBLIC. 2026-10-24 `e647d76`(공개 74개) · `ac46e7f`(계획) · 2026-10-25 `fd35c16`(허브 재구축 + 2차시 요약본, 공개 문서 48개). raw llms.txt HTTP 200 확인 |
| 로컬 환경 | WSL2 Ubuntu 22.04, Python 3.10, sudo 없음(pip --user) |

## 3. 저장소 구조

```
.
├── llms.txt             ★ ChatGPT용 단일 진입 허브(자동 생성): 사용 규칙, 질문 유형별 안내, 모아보기 목록, 차시별 절(§) 색인 + raw URL
├── README.md            사람용 시작점: 빠른 탐색 방법 표, 주차 요약, ChatGPT 사용법(허브 템플릿), 공개 범위
├── INDEX.md             공개 문서 인덱스 (자동 생성, GitHub 상대 링크)
├── TOPICS.md            주제·키워드 → 문서 매핑 (비공개 자료는 '(비공개)'로 표시)
├── PLAN.md              이 문서 (트래커·완료/할 일)
├── .gitignore           원본 디렉토리, 원본 파일 형식, private/ 제외
├── tools/
│   ├── convert_sources.py   원본 → 변환 + 공개/비공개 분리 + 허브·인덱스 생성 파이프라인
│   ├── pdfmd.py             PDF → Markdown (제목 복원·표·OCR·띄어쓰기 복원)
│   ├── check_links.py       깨진 링크·비공개 경로 누출·토큰 한도·manifest 누락 점검
│   └── requirements.txt
├── docs/                ← 공개 (GitHub)
│   ├── compiled/            모아보기 6종(용어집·예상문제·강조 포인트·체크리스트·요약표·강의 개요) + 목차 파일
│   ├── weekNN_YYYYMMDD/
│   │   ├── README.md                 주차 인덱스 (키워드, 공개 문서 표, 비공개 자료 건수)
│   │   ├── study_guide_summary.md    여러 부일 때 목차(각 부의 절 제목 + raw URL)
│   │   └── study_guide_summary_partNN.md   N차시 시험대비 학습자료(요약본)
│   └── manifest.json        공개 문서 목록
├── private/             ← 비공개, git 제외
│   ├── INDEX.md, manifest.json       전체(공개+비공개) 인덱스·목록
│   ├── redact.json                   실명 치환 목록 [["이름","[발표자]"],…] (다른 PC에서는 먼저 만들 것)
│   └── docs/common/, docs/weekNN_YYYYMMDD/{README.md, week_manifest.json, study_guide_full/, lecture_notes*.md, slides/, transcripts/, code/, paper_assignment/}
└── machine_learning_for_health_science/   원본 — git 제외 (2차시 요약본 Markdown 원본도 이 폴더의 20260909/에 둠)
```

## 4. 단일 URL 허브(`llms.txt`) 설계

| 구성 | 내용 | 목적 |
|---|---|---|
| 0. AI 어시스턴트 사용 규칙 | 문서 고르기 → raw URL 열어 끝까지 읽기 → 출처 표기 → 없는 내용은 "자료에 없음" · 출처 라벨([노트]/[녹음]/[교재]/[추가]) 설명 · 영어 요약 한 줄 | ChatGPT가 허브를 "안내서"로 인식하고 따라가게 |
| 1. 질문 유형별 안내 | 용어 → 용어집, 문제 연습 → 예상문제, 교수님 강조 → key_points, 비교·복습 → 요약표, 학기 흐름 → 강의 개요, 상세 설명 → 차시 색인 | 첫 번째 열 문서를 빨리 고르게 |
| 2. 모아보기 목록 | 6종 × 파트별 raw URL, 각 파트에 들어 있는 차시 범위(예: `(2/2) 6·7·8차시 →`) | 학기 전체 질문을 1~2개 파일로 해결 |
| 3. 차시별 요약본 색인 | 차시 제목·키워드 + 파트별 raw URL + 그 파트에 든 절 제목(§) 목록(참조 괄호 제거) | 개념 질문을 정확한 파트로 연결 |
| 4. 사람용 목록 | GitHub, INDEX, TOPICS, README URL | 사람이 허브에서 되돌아가기 |

- 크기 제한: 허브 자체가 한 번에 읽히도록 **10,000 tokens** 이하. 넘으면 절 제목 길이를 70→56→44→34→26자로 줄여 재생성(`write_llms_txt`).
- 모든 링크는 절대 raw URL(`https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/…`). 상대 링크는 ChatGPT가 따라가지 못한다.
- 재생성: `python3 tools/convert_sources.py --index-only` (문서 변환 없이 허브·인덱스·모아보기만 다시 만듦).
- 사용 템플릿(README에도 있음): "다음 URL의 안내 문서를 읽고, 그 안의 규칙대로 질문에 맞는 자료를 찾아 읽은 뒤 답해줘. 답 끝에 출처(차시·절)를 밝혀줘. URL: …/llms.txt 질문: …"

## 5. 작업 로그

- 2026-10-24 · 원본 267개 파일 조사(형식·중복·텍스트 추출 가능 여부). 다른 과목 노트 1개 제외, 누적 노트북은 8차시 부분만, 중복 슬라이드는 첫 등장 주차에서만 변환.
- 2026-10-24 · 변환 파이프라인(`tools/`): PDF 제목 복원·표·OCR(RapidOCR 한국어 모델)·띄어쓰기 복원(kiwipiepy), PPTX/DOCX/HTML/받아쓰기 변환, 12,000 tokens 분할, 목차 파일, 이메일·전화번호 제거.
- 2026-10-24 · 1~8차시 전체 변환(223개 문서), 모아보기 6종 생성, INDEX/TOPICS/README/llms.txt 작성.
- 2026-10-24 · 사용자 결정에 따라 공개 범위를 요약본+모아보기로 축소. 비공개 문서를 `private/`로 분리, 공개 문서→비공개 링크 0건 확인, 이름 치환(파일명·본문·manifest·소스), 치환 목록은 `private/redact.json`으로.
- 2026-10-24 · 첫 커밋 `e647d76` 푸시, raw URL HTTP 200 확인. 계획 갱신 `ac46e7f`.
- 2026-10-25 · 허브 재설계: `llms.txt`를 질문 유형별 안내 + 모아보기 + 차시별 절 색인 구조로 재생성(7.7K tokens). README 사용법을 "URL 하나 + 질문"으로 개정. 파이프라인에 Markdown 요약본 원본(`summary_md`) 지원 추가.
- 2026-10-25 · 2차시 요약본 작성 완료(전체판 6파트 기반, 7절 42,511자; 발표자·시험 언급 등 전체판에 없는 항목은 '기록 없음'으로 명시) → `summary_md`로 변환(3파트) → 모아보기 6종·허브·TOPICS·README 반영. 공개 문서 48개.
- 2026-10-25 · 버그 수정: 재치환 단계가 `private/redact.json`까지 치환해 목록을 망가뜨리던 문제(해당 파일 제외) — 비공개 2차시 문서에 잠깐 남았던 이름 재치환 완료.

## 6. 해야 할 작업

### 6.1 공개 전 확인 (결정 반영 상태)

- [x] 공개 범위 결정 — 요약본 + 모아보기만 공개.
- [x] 동료 학생 자료 — 비공개로 이동, 실명은 `[발표 학생]`으로 치환.
- [x] Efron 발표 내용 — 발표자 이름을 `[발표자]`로 치환(비공개 폴더에 보관).
- [x] 교재·논문 원문 — 변환하지 않음. README에 공식 링크만.
- [x] 소스 코드에도 실명이 남지 않도록 치환 목록을 `private/redact.json`으로 이동, 원본 파일명은 글롭 패턴.
- [ ] 공개 문서를 한 번 훑어 교수님 사담·수강생 언급이 공개해도 괜찮은지 확인(`rg -n "농담|여담|학생" docs/`). 부담되면 `PUBLIC_CATEGORIES`에서 `study_guide_summary`를 빼고 모아보기만 공개.

### 6.2 P4·P5 마무리와 GitHub 반영

- [x] 2차시 요약본 Markdown 검수(7절 구조, 이름 없음, 42,511자) → `--only week02` 변환 → `--index-only` → `check_links.py` 통과(깨진 링크 0, 누출 0, 초과 0).
- [x] TOPICS.md의 2차시 행 7개를 새 요약본 §2.1~2.7 링크로 교체.
- [x] 커밋 `fd35c16` 푸시(2026-10-25). raw `llms.txt` HTTP 200, 8,129 tokens 확인.
  ```bash
  python3 tools/check_links.py && git add -A docs tools .gitignore README.md INDEX.md TOPICS.md PLAN.md llms.txt
  git commit -m "Rebuild llms.txt as single-URL hub; add week 2 summary" && git push origin main
  ```

### 6.3 ChatGPT 실사용 검증 (사용자)

- [ ] 허브 템플릿으로 세 가지 질문을 던져 본다: 용어 질문("c-통계량이 뭐야"), 개념 유도("LOOCV 지름길 공식 설명"), 시험 연습("7차시 서술형 문제 출제·채점"). 각각 ChatGPT가 어떤 URL을 열었는지, 출처를 밝혔는지 확인.
- [ ] ChatGPT가 허브를 끝까지 읽지 못하거나 링크를 따라가지 않으면: (a) 템플릿에 "먼저 llms.txt 전체를 읽어"를 추가, (b) `HUB_BUDGET_TOKENS`를 8,000으로 낮춰 재생성, (c) 그래도 안 되면 모아보기 파트 URL을 직접 지정(README 방법 2).
- [ ] 긴 파트가 잘리면 `--max-tokens 8000`으로 재생성.

### 6.4 다음 주차(9차시~) 추가 절차

1. 원본 폴더 `machine_learning_for_health_science/YYYYMMDD/`에 자료를 넣는다(학습자료 PDF, 강의노트 PDF, 슬라이드 PDF, 받아쓰기 txt). 새 사람 이름이 있으면 `private/redact.json`에 추가한다(다른 PC에서는 이 파일을 먼저 만든다).
2. `tools/convert_sources.py`의 `WEEKS`에 항목을 추가한다(n, folder, date, slug, title, topics, summary_pdf 또는 summary_md, full_pdf, notes, slides, reuse, skip). 다른 주차에 이미 있는 슬라이드는 `reuse`에 적는다. 실명이 든 원본 파일명은 글롭(`*`)으로 적는다.
3. `python3 tools/convert_sources.py --only week09` → 요약본은 `docs/`, 나머지는 `private/`로 자동 분리되고 허브·인덱스·모아보기가 갱신된다. 이어서 `python3 tools/check_links.py`.
4. `TOPICS.md`에 새 키워드 행을 추가하고, 6.1을 점검한 뒤 커밋·푸시한다.

### 6.5 품질 개선 (선택, 우선순위 순)

- [ ] 허브 색인에 모아보기 문서의 차시별 절 제목까지 넣기(현재는 차시 번호만) — 허브 토큰 예산(10K) 안에서 가능한지 확인.
- [ ] TOPICS.md를 허브처럼 절대 raw URL 버전으로도 제공(ChatGPT가 키워드 표를 직접 쓰게).
- [ ] 칠판 사진 117장: 썸네일 + 촬영 시각 또는 설명문 생성(비공개).
- [ ] 받아쓰기 교정본(비공개), 수식 LaTeX 정리(`formulas.md`).
- [ ] 변환 스크립트 단위 테스트(표 필터·분할·허브 예산).

## 7. 변환 규칙

| 규칙 | 내용 | 이유 |
|---|---|---|
| 파일 크기 | 파일당 ≤ 12,000 tokens(o200k_base). 허브는 ≤ 10,000 | ChatGPT 웹이 긴 페이지를 앞부분만 읽는 경우 대비 |
| 분할 지점 | `##` → `###` → `####` 제목 경계 우선, 그래도 크면 문단 경계. `_partNN.md` + 목차 파일 | 절이 중간에 끊기지 않게, 안정된 링크 |
| 경로·파일명 | ASCII 소문자 slug (`week03_20260916/study_guide_summary_part01.md`) | raw URL에 한글 인코딩이 들어가지 않게 |
| 공개 범위 | `PUBLIC_CATEGORIES = {study_guide_summary, compiled}`만 `docs/`, 나머지는 `private/docs/`(동일 구조). 공개 문서는 비공개 경로를 링크하지 않음(`check_links.py` 검사) | 저작권·개인정보 |
| 이름 치환 | `private/redact.json` 목록을 본문·파일명·manifest에 적용, 띄어쓰기로 갈라진 이름도 정규식으로 잡음. 공개 소스에는 이름을 적지 않음 | 공개 저장소에 실명이 남지 않도록 |
| 2차시 요약본 | 전체판에서 작성한 Markdown을 원본 폴더에 두고 `summary_md`로 지정 → 제목 단계를 한 단계 내려(##/###/####) 다른 차시와 같은 구조로 변환 | 모아보기 절 추출·허브 색인이 같은 규칙으로 동작 |
| 중복 처리 | md5가 같은 원본은 처음 등장한 주차에서만 변환 | 저장소 크기·검색 중복 방지 |
| 제외 | 녹음, 칠판 사진, 교재·논문 원문 PDF, `.fablize/`, pptx 초안·템플릿, 다른 과목 노트 | 용량·저작권·중복 |

## 8. 알려진 한계

- 한글 띄어쓰기: PDF 줄 끝에서 사라진 공백을 kiwipiepy로 복원하지만 100%는 아니다(복합명사를 과하게 띄우거나, 깨진 문장은 그대로).
- 수식: 텍스트 추출·OCR 모두 수식 기호가 깨진다. 정확한 수식은 원본 PDF.
- 요약본은 AI 2차 자료다. 교수님 발언은 [노트]/[녹음] 라벨로 구분되지만, 받아쓰기 오류가 요약에 섞일 수 있다.
- ChatGPT 브라우징은 비결정적이다. 허브를 따라가지 않는 경우가 있으면 6.3의 대안을 쓴다.
- 비공개 자료(전체판·받아쓰기)는 URL로 쓸 수 없다. 필요하면 ChatGPT Projects에 파일로 올린다.

## 9. 변경 이력

| 날짜 | 변경 |
|---|---|
| 2026-10-24 | 최초 작성. 변환·인덱스·gitignore 완료 |
| 2026-10-24 | 공개 범위를 요약본+모아보기로 축소, private/ 분리, 이름 치환, 첫 푸시 |
| 2026-10-25 | 트래커 도입. 단일 URL 허브 재설계(P4), 2차시 요약본 작성·공개(P5) 완료 — 커밋 `fd35c16` |
