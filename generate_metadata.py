import os
import glob

def generate_metadata():
    # 设置目录路径
    text_dir = "dataset/text"
    
    # 获取所有文本文件并排序
    text_files = glob.glob(os.path.join(text_dir, "*.txt"))
    text_files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
    
    # 创建metadata.csv
    with open("dataset/metadata.csv", "w", encoding="utf-8") as f:
        for text_file in text_files:
            # 获取文件名（不带扩展名）
            file_id = os.path.basename(text_file).split('.')[0]
            
            # 读取文本内容
            with open(text_file, "r", encoding="utf-8") as tf:
                text_content = tf.read().strip()
            
            # 写入metadata.csv，格式：id|text
            f.write(f"output_{file_id}|{text_content}\n")

if __name__ == "__main__":
    generate_metadata()
    print("metadata.csv has been generated successfully!") 