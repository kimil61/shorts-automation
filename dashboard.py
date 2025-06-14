#!/usr/bin/env python3
"""
📊 쇼츠 자동화 시스템 대시보드
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import os
import json

st.set_page_config(
    page_title="쇼츠 자동화 대시보드",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 쇼츠 자동화 시스템 대시보드")

# 사이드바
with st.sidebar:
    st.header("🎛️ 제어 패널")
    
    if st.button("▶️ 즉시 실행", type="primary"):
        st.info("자동화 실행 중... (실제 구현 필요)")
    
    if st.button("🔄 모델 재훈련"):
        st.info("모델 재훈련 중... (실제 구현 필요)")

# 메인 대시보드
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 총 조회수", "47,238", "2,341")

with col2:
    st.metric("💰 예상 수익", "₩73,420", "₩8,210")

with col3:
    st.metric("🎯 쿠팡 클릭", "189", "23")

with col4:
    st.metric("🤖 자동화율", "87%", "3%")

# 차트 섹션
st.subheader("📈 성과 추이")

# 더미 데이터
data = pd.DataFrame({
    'date': pd.date_range('2024-12-01', periods=14),
    'views': [1000, 1200, 800, 1500, 2000, 1800, 2200, 
             2500, 2100, 2800, 3000, 2700, 3200, 3500],
    'revenue': [50, 60, 40, 75, 100, 90, 110,
               125, 105, 140, 150, 135, 160, 175]
})

fig = px.line(data, x='date', y=['views', 'revenue'], 
              title="일별 조회수 및 수익 추이")
st.plotly_chart(fig, use_container_width=True)

# 시스템 상태
st.subheader("🤖 시스템 상태")

status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    st.success("**🔍 키워드 수집**\n✅ 정상 동작")

with status_col2:
    st.success("**🎬 영상 렌더링**\n✅ 정상 동작")

with status_col3:
    st.success("**📤 업로드**\n✅ 정상 동작")

st.info("💡 실제 구현은 main.py와 연동하여 동작합니다.")
