#!/bin/bash
# 운영용 실행 스크립트

echo "🏭 운영 모드 실행"

# 가상환경 활성화
source venv/bin/activate

# 환경 변수 확인
if [ ! -f .env ]; then
    echo "❌ .env 파일이 필수입니다."
    exit 1
fi

# 백그라운드 실행
nohup python main.py schedule > output/logs/production.log 2>&1 &

echo "✅ 백그라운드에서 실행 중"
echo "📋 로그: tail -f output/logs/production.log"
echo "🛑 중지: pkill -f 'python main.py'"
