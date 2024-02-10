from datetime import datetime, timedelta, timezone

# 한국 표준시 UTC+9:00을 나타내는 timedelta 객체 생성
kst_offset = timedelta(hours=9)

# UTC 시간을 구합니다.
utc_now = datetime.utcnow()

# UTC 시간에 한국 표준시를 더하여 한국 시간을 얻습니다.
kst_now = utc_now + kst_offset

# YYYY-MM-DD 형식으로 출력합니다.
formatted_date_kst = kst_now.strftime('%Y-%m-%d')
print(formatted_date_kst)
