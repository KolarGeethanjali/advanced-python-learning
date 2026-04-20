#current working dicrectory is the folder name where python is operating

import os
from statistics import mode

# cwd = os.getcwd()
# print(cwd)

#change the current working directory
#os.chdir('path of the folder')

#create a new directory #this method rises an error FIleExistsError if the directory already exists

# os.mkdir('name of the folder')
# os.mkdir(path,mode) #mode is the permission of the folder in octal number this is another method to create a new directory

# os.makedirs('path of the folder') #this method creates all the intermediate folders if they do not exist

# listing out the files and directories with pyhton

#os.listdir("python") #this method lists out all the files and directories in the given path if no path is given it lists out the files and directories in the current working directory

# files = os.listdir("C:/Users/kolar/Advanced_python/python")
# print(files)

# new_dir = os.mkdir("C:/Users/kolar/Advanced_python/python/new_folder")
# print(new_dir)

# os = print(os.name) #this method gives the name of the operating system dependent module imported. The following names have currently been registered: 'posix', 'nt', 'os2', 'ce', 'java', and 'riscos'. It is always 'posix' on Unix-like systems and 'nt' on Windows.
# print(os)

#os.remove("C:/Users/kolar/Advanced_python/python/new_folder") #this method removes the file path given as an argument

#os.rmdir("C:/Users/kolar/Advanced_python/python/new_folder") #this method removes the directory path given as an argument. The directory must be empty, otherwise an OSError is raised. To remove a non-empty directory, use shutil.rmtree().   

info = os.stat("C:/Users/kolar/Advanced_python/python/3_pydantic") #this method performs a stat system call on the given path. It returns an object containing several attributes that describe the file or directory at the given path, such as its size, permissions, and timestamps.
print(info)
