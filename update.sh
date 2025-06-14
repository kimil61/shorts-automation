#!/bin/bash
# 시스템 업데이트 스크립트

echo "🔄 시스템 업데이트"

# 가상환경 활성화
source venv/bin/activate

# 패키지 업데이트
echo "📦 패키지 업데이트 중..."
pip install --upgrade pip
pip install -r requirements.txt --upgrade

# 모델 재훈련
echo "🤖 모델 업데이트 중..."
python -c "
import asyncio
from src.automation_master import ShortsAutomationMaster
from src.utils import load_config

config = load_config()
automation = ShortsAutomationMaster(config)
asyncio.run(automation.retrain_models())
"

echo "✅ 업데이트 완료"
