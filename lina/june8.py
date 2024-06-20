import re

def get_stt_filter(stt_list):
    try:
        whole_stt = "".join(stt_list)
        start, end = re.search("안녕.*동해물과",whole_stt).span()
        start1, end1 = re.search("백용용.*백두산",whole_stt).span()
        start2, end2 = re.search("키특키득.*닳도록",whole_stt).span()
        lists = []
        lists.append({"start":start,"end": end})
        lists.append({"start":start1, "end":end1})
        lists.append({"start":start2, "end":end2})
        result = []
        for l in lists:
            result.append(get_stt_start_and_last_index(stt_list, l["start"], l["end"]))

        print(result)
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



