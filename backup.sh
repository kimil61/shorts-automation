#!/bin/bash
# 백업 스크립트

echo "💾 데이터 백업"

BACKUP_DIR="backups/backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# 설정 파일 백업
echo "⚙️ 설정 파일 백업 중..."
cp .env "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ .env 파일 없음"
cp config.json "$BACKUP_DIR/"

# 데이터 백업
echo "📊 데이터 백업 중..."
cp -r data/ "$BACKUP_DIR/"
cp -r models/ "$BACKUP_DIR/"

# 최근 리포트 백업
echo "📋 리포트 백업 중..."
cp -r reports/ "$BACKUP_DIR/"

# 압축
echo "🗜️ 압축 중..."
tar -czf "${BACKUP_DIR}.tar.gz" "$BACKUP_DIR"
rm -rf "$BACKUP_DIR"

echo "✅ 백업 완료: ${BACKUP_DIR}.tar.gz"
