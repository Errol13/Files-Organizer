from utils import organize_files

def main():
    directory = input("Enter the directory to organize: ").strip()
    organize_files(directory)

if __name__ == "__main__":
    main()
