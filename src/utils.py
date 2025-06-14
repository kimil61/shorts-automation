"""
🛠️ 유틸리티 함수들
"""

import logging
import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

def setup_logging():
    """로깅 설정"""
    
    # 로그 디렉토리 생성
    log_dir = Path("output/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # 로그 파일명 (날짜별)
    log_file = log_dir / f"automation_{datetime.now().strftime('%Y%m%d')}.log"
    
    # 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def load_config():
    """설정 파일 로드"""
    
    # 환경 변수 로드
    load_dotenv()
    
    # config.json 로드
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    return config

def ensure_directories():
    """필수 디렉토리 생성"""
    
    dirs = [
        'output/videos', 'output/audio', 'output/thumbnails',
        'output/logs', 'data/keywords', 'data/scripts',
        'models', 'reports'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

def get_api_key(service_name):
    """API 키 안전하게 가져오기"""
    
    key = os.getenv(f"{service_name.upper()}_API_KEY")
    
    if not key:
        raise ValueError(f"{service_name} API 키가 설정되지 않았습니다.")
    
    return key
