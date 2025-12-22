import os
import re

def rename_markdown_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            match = re.match(r'(\d{3})-(.+)', filename)
            if match:
                num, rest = match.groups()
                # 去掉第一个零（如果有）
                if num[0] == '0':
                    new_num = num[1:]
                    new_filename = f"{new_num}-{rest}"
                    old_path = os.path.join(folder_path, filename)
                    new_path = os.path.join(folder_path, new_filename)
                    print(f"Renaming: {filename} -> {new_filename}")
                    os.rename(old_path, new_path)

if __name__ == "__main__":
    folder = input("请输入目标文件夹路径：")
    rename_markdown_files(folder)
