import os


def count_files(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count


folder_path = "your_folder_path"  # 将此处替换为您要统计的文件夹路径
print(count_files(folder_path))