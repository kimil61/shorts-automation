#!/usr/bin/env python3
"""
🎬 Python 쇼츠 자동화 시스템 - 메인 실행 파일
"""

import asyncio
import schedule
import time
import sys
import os
from datetime import datetime
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.automation_master import ShortsAutomationMaster
from src.utils import setup_logging, load_config

def main():
    """메인 실행 함수"""
    print("🎬 Python 쇼츠 자동화 시스템 v2.0")
    print("=" * 50)
    
    # 로깅 설정
    logger = setup_logging()
    
    # 설정 로드
    config = load_config()
    
    # 자동화 마스터 초기화
    automation = ShortsAutomationMaster(config)
    
    try:
        if len(sys.argv) > 1:
            command = sys.argv[1].lower()
            
            if command == "run":
                # 즉시 실행
                print("⚡ 즉시 실행 모드")
                asyncio.run(automation.run_daily_automation())
                
            elif command == "schedule":
                # 스케줄러 모드
                print("⏰ 스케줄러 모드")
                setup_scheduler(automation)
                
            elif command == "dashboard":
                # 대시보드 실행
                print("📊 대시보드 모드")
                os.system("streamlit run dashboard.py")
                
            elif command == "test":
                # 테스트 모드
                print("🧪 테스트 모드")
                asyncio.run(automation.run_test_mode())
                
            else:
                print_usage()
        else:
            # 기본값: 스케줄러 모드
            print("⏰ 기본 스케줄러 모드")
            setup_scheduler(automation)
            
    except KeyboardInterrupt:
        print("\n👋 사용자가 중단했습니다.")
    except Exception as e:
        logger.error(f"시스템 오류: {e}")
        print(f"❌ 오류 발생: {e}")
        sys.exit(1)

def setup_scheduler(automation):
    """스케줄러 설정 및 실행"""
    
    # 매일 08:00에 자동화 실행
    schedule.every().day.at("08:00").do(
        lambda: asyncio.run(automation.run_daily_automation())
    )
    
    # 주간 모델 재훈련 (일요일 02:00)
    schedule.every().sunday.at("02:00").do(
        lambda: asyncio.run(automation.retrain_models())
    )
    
    print("📅 스케줄 등록 완료:")
    print("   - 일일 자동화: 매일 08:00")
    print("   - 모델 재훈련: 매주 일요일 02:00")
    print("   - 종료: Ctrl+C")
    print("\n⏳ 스케줄 대기 중...")
    
    # 스케줄 실행 루프
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1분마다 체크

def print_usage():
    """사용법 출력"""
    print("📖 사용법:")
    print("  python main.py run       - 즉시 실행")
    print("  python main.py schedule  - 스케줄러 모드")
    print("  python main.py dashboard - 대시보드 실행")
    print("  python main.py test      - 테스트 모드")

if __name__ == "__main__":
    main()
