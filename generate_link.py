import os

# 定义GitHub仓库的基本URL
base_url = "https://ghproxy.wjsphy.top/https://raw.githubusercontent.com/StephenQSstarThomas/Lecture-Notes/main/"

# 定义要遍历的根目录
root_dir = "./"

# 定义输出文件
output_file = "toc.md"

# 打开输出文件
with open(output_file, "w", encoding="utf-8") as f:
    # 遍历目录中的所有文件和子目录
    for root, dirs, files in os.walk(root_dir):
        # 获取一级文件夹名称
        first_level_folder = root.replace(root_dir, "").split(os.sep)[0]
        # 略过.git文件夹
        if ".git" in root:
            continue
        if first_level_folder:
            # 写入一级文件夹标题
            f.write(f"\n## {first_level_folder}\n")
        for file in files:
            if file.endswith(".pdf"):
                # 构建文件的相对路径
                relative_path = os.path.join(root, file).replace(root_dir, "").lstrip("/")
                # 构建完整的URL
                full_url = base_url + relative_path.replace(" ", "%20")
                # 写入toc.md文件
                f.write(f"[{file}]({full_url})\n")

print(f"所有PDF文件的链接已写入 {output_file}")