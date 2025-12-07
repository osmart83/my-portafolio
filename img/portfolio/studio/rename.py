import os

def rename_jpg_files(folder_path):
    # Get all .JPG/.jpg files in the folder
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
    
    # Sort files alphabetically so renaming is consistent
    files.sort()
    
    # Rename files one by one
    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        new_name = f"{index}.jpg"
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    # Use the folder where the script is located
    folder = os.path.dirname(os.path.abspath(__file__))
    rename_jpg_files(folder)

