from builtins import object
import os
import fsutils.file

class SubFileSystem(object):
    def __init__(self, rootdir):
        self.rootdir = rootdir
        self.cwd = rootdir
        self.level = 0
        self.dir_stack = []
        self.dir_stack.append(rootdir)

    def depth(self):
        return self.level

    def cd(self, dir):
        if dir == "..":
            self.cdup()
            return
        
        self.dir_stack.append(self.cwd)
        self.level += 1
        self.cwd += "/" + dir
        print("pushed:", self.cwd)

    def up(self):
        if self.level == 0:
            return;

        self.level -= 1
        self.cwd = self.dir_stack.pop()
        print("popped:", self.cwd)

    def list(self):
        self.files = []

        # Get the list of files in the current working directory
        it = os.scandir(self.cwd)

        # Loop through the files, collecting some information in each
        for entry in it:

            # Start with the name
            name = entry.name
            displayname = name

            # Do some filtering. (To-do: create a filter class do do this)
            if name.startswith("."):
                continue

            if entry.is_dir():
                type = 'd'
            elif entry.is_file():
                type = 'f'
            elif entry.is_symlink():
                type = 'l'
            else:
                type = 'u'

            # Do some more filtering. (To-do: filter class)
            if type == 'l':
                continue

            # If the file is a directory, append a slash to the
            # display name this is how we visually distinguish
            # directories and folders from regular files.

            if type == 'd':
                displayname += "/"

            # Call stat to get information that includes the file size
            statinfo = entry.stat()
            size = statinfo.st_size

            # Create a tuple and append it to the list of files
#            file_tuple = (name, size)
            the_file = fsutils.file.File(name, displayname, size, type)
            self.files.append(the_file)

        # Lastly, return the list of file tuples
        self.files = sorted(self.files)
        return self.files