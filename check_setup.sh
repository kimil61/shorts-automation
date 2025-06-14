#!/bin/bash
# 설정 확인 스크립트

echo "🔍 시스템 설정 확인"

# Python 버전 확인
echo "Python: $(python --version)"

# 패키지 설치 확인
echo "📦 핵심 패키지 확인:"
python -c "
import sys
packages = ['moviepy', 'requests', 'pandas', 'streamlit', 'openai']
for pkg in packages:
    try:
        __import__(pkg)
        print(f'✅ {pkg}')
    except ImportError:
        print(f'❌ {pkg} (설치 필요)')
"

# 환경 변수 확인
echo ""
echo "🔐 환경 변수 확인:"
if [ -f .env ]; then
    echo "✅ .env 파일 존재"
    grep -v "^#" .env | grep -v "^$" | wc -l | xargs echo "   설정된 변수 수:"
else
    echo "❌ .env 파일 없음"
    echo "   .env.example을 복사하여 .env 생성 필요"
fi

# 폴더 구조 확인
echo ""
echo "📁 폴더 구조 확인:"
required_dirs=("src" "output" "data" "models")
for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/"
    else
        echo "❌ $dir/ (생성 필요)"
    fi
done

# 테스트 실행
echo ""
echo "🧪 기본 테스트 실행:"
python main.py test
