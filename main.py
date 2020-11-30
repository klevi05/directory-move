import shutil


def move_directory(src, destination):
    shutil.move(src, destination)


print('Ky program meret me transferimin e folderva nga nje dir ne nje tjeter')
print('Path duhet te jete me dy \\ jo me nje qe te punoj si dhe dir duhet te jen aktive')
source = input("Jep path e folderit qe deshiron te transferosh: ")
destination = input("Jep path e folderit prites: ")

move_directory(source, destination)
