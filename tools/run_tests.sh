#!/usr/bin/env bash
# ROS 환경의 pytest 플러그인 충돌을 피해 단위 테스트 실행
cd "$(dirname "$0")/.." && PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest tools/tests -q "$@"
