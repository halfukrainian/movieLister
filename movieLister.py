import os

def list_films(folder_path, output_file):
    film_extensions = ('.mp4', '.mkv', '.avi', '.mov')
    folder_path = os.path.normpath(folder_path)  #
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Films directory structure: {folder_path}\n")
        f.write("=" * 50 + "\n")
        
        for root, _, files in os.walk(folder_path): #goign through all folders
            relative_path = os.path.relpath(root, folder_path) #get relative path
            relative_path = relative_path.replace(os.sep, '/')  
            if relative_path == ".":
                relative_path = "films"
            
            films = [file for file in files if file.endswith(film_extensions)]
            parent_folder = os.path.basename(root)  # Get the folder name
            
            # Ensure we only list the movie if the folder name matches the movie name
            filtered_films = []
            for file in films:
                movie_name, _ = os.path.splitext(file)
                if movie_name.lower() != parent_folder.lower():
                    filtered_films.append(file)
            
            if filtered_films:
                f.write(f"\n{relative_path}/\n")
                for file in filtered_films:
                    f.write(f"  ├── {file}\n")
    
    print(f"Film list saved to {output_file}")
    input("\nPress Enter to exit...")  # Prevents console from closing immediately

if __name__ == "__main__":
    import string
    available_drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
    print(f"Available drives: {', '.join(available_drives)}")
    
    films_folder = input("Enter the path to your films folder: ").strip()
    films_folder = os.path.normpath(films_folder)  # Normalize user input path
    print(f"Checking path: {films_folder}") 
    
    output_file = "film_list.txt"
    
    if os.path.exists(films_folder):
        list_films(films_folder, output_file)
    else:
        print("Invalid path! Please check and try again.")
        input("\nPress Enter to exit...")
