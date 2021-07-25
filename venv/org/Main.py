import os

# zip.

root_directory = r'C:\Users\Matze\Downloads'
extensions = ["NONE", "7z", "dll", "docx", "exe", "gz", "htm", "ics", "ini", "iso", "jar", "jpg", "msi", "pdf", "png", "py",
               "rar", "tif", "ttf", "txt", "xcf", "xlsx", "zip"]


def make_directories(extensionss):
    folders = []
    folders.append("_FOLDERS")
    folders.extend(extensionss)
    for folder in folders:
        new_directory = os.path.join(root_directory, folder)
        if (not os.path.isdir(new_directory)):
            os.mkdir(new_directory)
    return folders


def get_folder_names():
    global extensions
    directories = []
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if root == root_directory:
                extensions.append(os.path.splitext(file)[1].lower())
        for dir in dirs:
            if root == root_directory:
                directories.append(os.path.join(root,dir))
    extensions = set(extensions)
    extensions = [ext.replace(".", " ") for ext in extensions if ext]
    folders = make_directories(extensions)
    directories = [dir for dir in directories if dir not in folders]

    return extensions, directories


def move_files():
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if root == root_directory:
                print(file)
                if file == "Sort Downloads.py":
                    continue
                path_file = os.path.join(root, file)
                extension = os.path.splitext(path_file)[1].lower().replace(".", "")
                extension = "NONE" if extension == "" else extension
                new_path = os.path.join(root, extension, file)
                os.rename(path_file, new_path)


def move_folders(extensions, directories):
    print(extensions)
    for dir in directories:
        path_split = os.path.split(dir)
        if path_split[1] not in extensions and path_split[1] != "_FOLDERS":
            new_path = os.path.join(path_split[0], "_FOLDERS", path_split[1])
            os.rename(dir, new_path)


if __name__ == "__main__":
    extensions, directories = get_folder_names()
    move_files()
    move_folders(extensions, directories)
