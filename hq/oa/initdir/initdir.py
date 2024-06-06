import os
import shutil

def copy_files_to_directories(source_dir, destination_root_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    # Base directory should already exist
    if not os.path.exists(destination_root_dir):
        print(f"Destination directory {destination_root_dir} does not exist.")
        return

    # Create 6 depth1 directories in the destination root directory
    for i in range(1, 7):
        depth1_dir = os.path.join(destination_root_dir, f"depth1_{i}")
        os.makedirs(depth1_dir, exist_ok=True)
        
        # Create 3 depth2 directories within each depth1 directory
        for j in range(1, 4):
            depth2_dir = os.path.join(depth1_dir, f"depth2_{j}")
            os.makedirs(depth2_dir, exist_ok=True)
            
            # Create 2 depth3 directories within each depth2 directory
            for k in range(1, 3):
                depth3_dir = os.path.join(depth2_dir, f"depth3_{k}")
                os.makedirs(depth3_dir, exist_ok=True)
                
                # Create 30 depth4 directories within each depth3 directory
                for l in range(1, 31):
                    depth4_dir = os.path.join(depth3_dir, f"depth4_{l}")
                    os.makedirs(depth4_dir, exist_ok=True)
                    
                    # Create 24 depth5 directories within each depth4 directory
                    for m in range(1, 25):
                        depth5_dir = os.path.join(depth4_dir, f"depth5_{m}")
                        os.makedirs(depth5_dir, exist_ok=True)
                        
                        # Get the first 60 files from the source directory
                        files = os.listdir(source_dir)[:60]
                        
                        if not files:
                            print("No more files to copy.")
                            return
                        
                        # Copy each file to the depth5 directory
                        for file_name in files:
                            source_file = os.path.join(source_dir, file_name)
                            destination_file = os.path.join(depth5_dir, file_name)
                            shutil.copy2(source_file, destination_file)
                            
                            # Remove the file from the source directory list to avoid copying the same file again
                            os.remove(source_file)
                        
                        print(f"Copied 60 files to {depth5_dir}")

# Set the source and destination directories
source_dir = r"C:\test"
destination_root_dir = r"\\172.16.20.204\testimagedata"

# Call the function to copy files
copy_files_to_directories(source_dir, destination_root_dir)
