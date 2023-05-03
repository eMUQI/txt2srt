import os
import re

def to_srt(file_path):
    # 读取指定txt文件中的文本
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 将文本分成多个句子
    sentences = re.split(r'[。！~？]', text)

    # 去除空句子
    sentences = [s.strip() for s in sentences if s.strip()]

    # 计算每个句子的持续时间
    end_time = 0
    srt = ''
    for i, sentence in enumerate(sentences):
        start_time = end_time + 2
        start_time_str = "{:02d}:{:02d}:{:02d},{}".format(int(start_time // 3600), int((start_time % 3600) // 60), int(start_time % 60), "000")
        duration = len(sentence) * 0.25
        end_time = start_time + duration
        end_time_str = "{:02d}:{:02d}:{:02d},{}".format(int(end_time // 3600), int((end_time % 3600) // 60), int(end_time % 60), "000")
        srt += "{}\n{} --> {}\n{}\n\n".format(i+1, start_time_str, end_time_str, sentence)

    # 保存srt文件
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(f"{file_name}.srt", 'w', encoding='utf-8') as f:
        f.write(srt)

# 获取当前目录下所有txt文件
txt_files = [f for f in os.listdir() if f.endswith('.txt')]

# 遍历每个txt文件并生成srt文件
for txt_file in txt_files:
    to_srt(txt_file)