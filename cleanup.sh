#!/bin/bash
# 정리 스크립트

echo "🧹 시스템 정리"

# 임시 파일 삭제
echo "🗑️ 임시 파일 삭제 중..."
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find . -name "*.tmp" -delete
find . -name "temp-*" -delete

# 로그 파일 정리 (30일 이상)
echo "📋 오래된 로그 파일 정리 중..."
find output/logs -name "*.log" -mtime +30 -delete 2>/dev/null

# 생성된 임시 영상 파일 정리
echo "🎬 임시 영상 파일 정리 중..."
find output -name "temp_*" -delete 2>/dev/null

# 모델 백업 파일 정리
echo "🤖 오래된 모델 백업 정리 중..."
find models -name "*.pkl.bak" -mtime +7 -delete 2>/dev/null

echo "✅ 정리 완료"
