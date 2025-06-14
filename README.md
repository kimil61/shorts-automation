# 🎬 Python 쇼츠 자동화 시스템 v2.0

> 완전 Python 기반 YouTube 쇼츠 자동 생성 및 업로드 시스템

## ✨ 주요 기능

- 🔍 **자동 키워드 수집**: 트렌드 분석 기반 키워드 발굴
- 🤖 **AI 스크립트 생성**: GPT 기반 매력적인 스크립트 자동 작성
- 🎬 **자동 영상 렌더링**: MoviePy 기반 고품질 쇼츠 영상 생성
- 📤 **자동 업로드**: 시간대별 예약 업로드
- 📊 **성과 분석**: ML 기반 성과 예측 및 최적화
- 🎯 **수익 연동**: 쿠팡 파트너스 자동 연결

## 🚀 빠른 시작

### 1. 자동 설치 (권장)
```bash
# 설치 스크립트 다운로드 및 실행
curl -O https://raw.githubusercontent.com/your-repo/deploy.sh
bash deploy.sh
```

### 2. 수동 설치
```bash
# 저장소 클론
git clone https://github.com/your-repo/shorts-automation.git
cd shorts-automation

# 가상환경 생성
python3 -m venv venv
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 환경 설정
cp .env.example .env
# .env 파일에 API 키 입력

# 테스트 실행
python main.py test
```

## 📋 필수 API 키

1. **OpenAI API** - GPT 스크립트 생성
   - 발급: https://platform.openai.com/api-keys
   - 월 사용료: ~$10-30

2. **YouTube Data API** - 영상 업로드
   - 발급: https://console.developers.google.com
   - 무료 (할당량 제한 있음)

3. **쿠팡 파트너스 API** - 수익 연동
   - 발급: https://partners.coupang.com
   - 무료 (승인 필요)

4. **TTS API** (선택사항)
   - TypeCast: https://typecast.ai
   - ElevenLabs: https://elevenlabs.io

## 🎯 실행 방법

### 즉시 실행
```bash
# 개발 모드
./run_dev.sh

# 또는
python main.py run
```

### 스케줄러 모드
```bash
# 운영 모드 (백그라운드)
./run_production.sh

# 또는
python main.py schedule
```

### 대시보드
```bash
# 모니터링 대시보드
./run_dashboard.sh

# 또는
streamlit run dashboard.py
```

## 📊 성과 모니터링

- **대시보드**: http://localhost:8501
- **로그 확인**: `tail -f output/logs/automation.log`
- **일일 리포트**: `reports/` 폴더 확인

## 🔧 유지보수

### 시스템 점검
```bash
./check_setup.sh
```

### 업데이트
```bash
./update.sh
```

### 정리
```bash
./cleanup.sh
```

### 백업
```bash
./backup.sh
```

## 📁 프로젝트 구조

```
shorts_automation/
├── main.py              # 메인 실행 파일
├── dashboard.py         # 모니터링 대시보드
├── config.json          # 시스템 설정
├── .env                 # API 키 (생성 필요)
├── requirements.txt     # 패키지 의존성
├── 
├── src/                 # 소스코드
│   ├── automation_master.py
│   ├── utils.py
│   └── ...
├── 
├── assets/              # 리소스
│   ├── fonts/          # 한글 폰트
│   ├── templates/      # 영상 템플릿
│   └── sounds/         # 효과음
├── 
├── output/              # 출력 결과
│   ├── videos/         # 렌더링된 영상
│   ├── audio/          # TTS 음성
│   ├── thumbnails/     # 썸네일
│   └── logs/           # 로그 파일
├── 
├── data/                # 데이터
├── models/              # ML 모델
├── reports/             # 성과 리포트
└── *.sh                # 유틸리티 스크립트
```

## ⚙️ 설정 조정

### config.json 주요 설정
- `daily_video_count`: 일일 영상 생성 수 (기본: 3개)
- `upload_times`: 업로드 시간 (기본: 17:00, 19:30, 21:00)
- `min_validation_score`: 키워드 검증 최소 점수 (기본: 70점)

### .env 환경 변수
- 모든 API 키는 `.env` 파일에 보관
- `.env.example` 참고하여 작성
- 절대 Git에 커밋하지 마세요!

## 🐛 문제 해결

### 일반적인 문제

1. **패키지 설치 오류**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

2. **폰트 렌더링 오류**
   ```bash
   # 폰트 파일 확인
   ls -la assets/fonts/
   
   # 폰트 재다운로드
   rm -rf assets/fonts/*.ttf
   python -c "from setup import download_fonts; download_fonts()"
   ```

3. **메모리 부족**
   - config.json에서 `video.resolution` 낮추기
   - `MAX_WORKERS` 환경변수 줄이기

4. **API 할당량 초과**
   - 각 API 사용량 확인
   - config.json에서 `daily_video_count` 줄이기

### 로그 확인
```bash
# 실시간 로그 확인
tail -f output/logs/automation_$(date +%Y%m%d).log

# 에러 로그만 확인
grep ERROR output/logs/*.log
```

## 📈 성능 최적화

1. **렌더링 속도 향상**
   - SSD 사용 권장
   - RAM 4GB+ 권장
   - 멀티코어 CPU 활용

2. **API 비용 절약**
   - OpenAI 모델을 gpt-3.5-turbo 사용
   - 캐싱 활용으로 중복 요청 방지

3. **안정성 향상**
   - 정기적인 백업 실행
   - 에러 알림 설정
   - 자동 재시작 기능 활용

## 🤝 기여하기

1. Fork 프로젝트
2. Feature 브랜치 생성
3. 변경사항 커밋
4. Pull Request 제출

## 📜 라이선스

MIT License - 자유롭게 사용 가능

## 🙋‍♂️ 지원

- **GitHub Issues**: 버그 리포트 및 기능 요청
- **Discussions**: 사용법 질문 및 아이디어 공유
- **Wiki**: 상세한 설정 가이드

---

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!
