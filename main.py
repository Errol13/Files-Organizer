from utils import organize_files, dry_run

def main():
    directory = input("Enter the directory to organize (e.g., /path/to/directory): ").strip()
    dry_run_choice = input("Perform a dry run? (y/n): ").strip().lower() == 'y'
    if dry_run_choice:
        print("Performing dry run...")
        dry_run(directory)
        proceed = input("Proceed with the file organization? (y/n)").strip().lower() == 'y'
        #If the user does not want to proceed, file organization will not be performed
        if not proceed:
            print("File organization cancelled.")
            return
        else:
            organize_files(directory)
    else:
        organize_files(directory)

if __name__ == "__main__":
    main()
