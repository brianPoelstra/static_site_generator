import shutil
import os

class Copy_To_File():
    def __init__(self, path, destination):
        
        self.path = path
        self.destination = destination

    def move_files(self):
        
        if os.path.exists(self.destination) == True:
            shutil.rmtree(self.destination)
        
        shutil.copytree(self.path, self.destination)
