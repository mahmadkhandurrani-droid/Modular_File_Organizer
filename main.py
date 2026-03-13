from setup_files import setup_files
from categories import define_categories
from organize_files import organize_files

if __name__ == "__main__":
    base_folder = "storage/emulated/0/file_organizer"
    setup_files(base_folder)
    categories = define_categories()
    organize_files(base_folder, categories)
