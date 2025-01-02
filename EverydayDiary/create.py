import os
from datetime import datetime

def create_diary_if_not_exists(path):
    today = datetime.now().strftime("%Y%m%d")
    filename = f"{today}.md"

    file_path = os.path.join(path, filename)

    if os.path.exists(file_path):
        print(f"File already exists: {file_path}")
    else:
        with open(file_path, 'w') as file:
            file.write(f"# {today}\n\n")
            file.write("> This diary created on " + today + ".\n")
        print(f"File created: {file_path}")

directory_path = "./"
create_diary_if_not_exists(directory_path)
