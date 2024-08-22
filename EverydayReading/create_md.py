import os
from datetime import datetime

def create_markdown_file_if_not_exists(path):
    # 获取当天日期并格式化为 yyyymmdd
    today = datetime.now().strftime("%Y%m%d")
    filename = f"{today}.md"

    # 确定完整文件路径
    file_path = os.path.join(path, filename)

    # 检查文件是否存在
    if os.path.exists(file_path):
        print(f"File already exists: {file_path}")
    else:
        # 创建文件并写入一些初始内容
        with open(file_path, 'w') as file:
            file.write(f"# {today}\n\n")
            file.write("> This markdown file created on " + today + ".\n")
        print(f"File created: {file_path}")

directory_path = "./reading"
create_markdown_file_if_not_exists(directory_path)
