#!/bin/bash
# 대시보드 실행 스크립트

echo "📊 대시보드 실행"

# 가상환경 활성화
source venv/bin/activate

# Streamlit 실행
streamlit run dashboard.py --server.port 8501 --server.headless true
