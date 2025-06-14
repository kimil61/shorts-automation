#!/bin/bash
# 개발용 실행 스크립트

echo "🚀 개발 모드 실행"

# 가상환경 활성화
source venv/bin/activate

# 환경 변수 확인
if [ ! -f .env ]; then
    echo "⚠️ .env 파일이 없습니다. 테스트 모드로 실행합니다."
    python main.py test
    exit 0
fi

# 메인 실행
python main.py run
