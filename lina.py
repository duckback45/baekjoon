from collections import defaultdict

# 주어진 guide 리스트
guide = [
    {'detail_code': 1, 'transscript': '안녕하세요', 'number': 1, 'start_time': "0800", 'end_time': "09000"},
    {'detail_code': 1, 'transscript': '홍길동입니다', 'number': 1, 'start_time': "0901", 'end_time': "10000"},
    {'detail_code': 2, 'transscript': '고객님', 'number': 1, 'start_time': "0901", 'end_time': "10000"},
    {'detail_code': 1, 'transscript': '지반번에', 'number': 1, 'start_time': "1100", 'end_time': "1200"}
]

# 결과를 저장할 딕셔너리
result = defaultdict(
    lambda: {'detail_code': None, 'transscript': '', 'start_time': None, 'end_time': None})

# guide 리스트를 순회하면서 그룹화 및 합산
for item in guide:
    key = (item['detail_code'], item['number'])

    # transscript을 합침
    result[key]['transscript'] += " " + item['transscript'] if result[key]['transscript']  else item['transscript']
    result[key]['detail_code'] = item['detail_code']

    # start_time의 최솟값 설정
    if result[key]['start_time'] is None or item['start_time'] < result[key]['start_time']:
        result[key]['start_time'] = item['start_time']

    # end_time의 최댓값 설정
    if result[key]['end_time'] is None or item['end_time'] > result[key]['end_time']:
        result[key]['end_time'] = item['end_time']

# 결과 출력
final_result = list(result.values())
print(final_result)