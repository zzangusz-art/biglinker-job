# _config.py — job 서브도메인 전용 설정
# build.py 가 이 파일을 import해서 사용합니다.

SITE_VARS = {
    "FAMILY_ACTIVE_TRANSFER": "",
    "FAMILY_ACTIVE_GRADUATE": "",
    "FAMILY_ACTIVE_JOB":      "is-active",
    "FAMILY_ACTIVE_BIZ":      "",
    "BRAND_COPY": "기업면접·병원취업·임용 코칭 전문",
}

CATEGORY_TABS_ITEMS = [
    ("corporate-interview-coaching", "기업면접리드코칭"),
    ("hospital-job-coaching",        "병원리드코칭"),
]
