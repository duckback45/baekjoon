import re

def get_stt_filter(stt_list):
    try:
        whole_stt = "".join(stt_list)
        stt_span = re.search("안녕.*동해물과",whole_stt)
        if stt_span != None:
            start, end = stt_span.span()
            return get_stt_start_and_last_index(stt_list, start, end)
        return [0,0]
    except:
        return [0,0]


def get_stt_start_and_last_index(stt_list, start, end):
    result = [0,0]
    last_sst_index = 0
    for idx, stt in enumerate(stt_list):
        if stt:  # 문자열이 비어있지 않은 경우에만 처리
            last_sst_index = last_sst_index + (len(stt))
            if start >= last_sst_index:
                result[0] = idx
            elif end >= last_sst_index:
                result[1] = idx


    return result


print(get_stt_filter(["안녕하세요", "저는 백용용입니다", "키특키득","동해물과","백두산이 마르고 닳도록"]))



