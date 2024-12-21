
import os
import shutil
import sys
FILE_CATEGORIES = {
    'docs': ['.doc', '.docx', '.txt', '.rtf'],
    'pdf': ['.pdf'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'audio': ['.mp3', '.wav', '.aac', '.flac'],
    'spreadsheets': ['.xls', '.xlsx', '.csv'],
    'presentations': ['.ppt', '.pptx'],
    'archives': ['.zip', '.tar', '.tar.gz', '.rar', '.7z'],
}

def create_category_directory(category):
    category_dir = os.path.join(source_dir, category)
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    return category_dir
def move_file(file, category_dir):
    destination = os.path.join(category_dir, os.path.basename(file))
    shutil.move(file, destination)
    print(f"Moved: {file} -> {destination}")
def sort_files():
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isdir(file_path):
            continue
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_dir = create_category_directory(category)
                move_file(file_path, category_dir)
                moved = True
                break
        if not moved:
            others_dir = create_category_directory('others')
            move_file(file_path, others_dir)

def get_arguments():
    if len(sys.argv) < 2:
        print("Error: No source directory provided.")
        sys.exit(1)
    return sys.argv[1]
    
def main():
    global source_dir
    source_dir = args.source_dir
    if not os.path.isdir(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        return
    sort_files()
    print("Files have been sorted.")

if __name__ == '__main__':
    main()
