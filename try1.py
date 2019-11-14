import os
from func import deal_speaker

path = 'D:\\语音识别\\TIMIT\\TEST'
if __name__ == '__main__':
    count_dict = dict()
    for x in os.listdir(path):
        print(x)
        print(count_dict)
        if os.path.isdir(path + '\\' + x):
            s_path = path + '\\' + x
            print(s_path)
            for y in os.listdir(s_path):
                if os.path.isdir(s_path + '\\' + y):
                    gs_path = s_path + '\\' + y
                    gs_path = gs_path.replace("/", "\\")
                    deal_speaker(gs_path, count_dict)
                    print(gs_path)
