import os
from datetime import datetime

today = datetime.now().strftime('%Y%m%d')

folder_path = os.path.join(os.getcwd(), today)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Dir '{folder_path}' created.")
else:
    print(f"Dir '{folder_path}' existed.")

md_file_path = os.path.join(folder_path, f"README.md")

if not os.path.isfile(md_file_path):
    with open(md_file_path, 'w') as md_file:
        md_file.write('# ' + today + '\n\n')
        md_file.write("> This markdown file created on " + today + ".\n")
    print(f"Markdown '{md_file_path}' created.")
else:
    print(f"Markdown '{md_file_path}' existed.")
