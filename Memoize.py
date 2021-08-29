class Memoize:
    def __init__(self, function):
        self.function = function
        self.ListOfHashes = {}

    def __call__(self, *args):
        grid = args[0].grid

        grid.flags.writeable = False
        gridHash = hash(grid.tobytes())
        grid.flags.writeable = True

        #print(gridHash)

        if not (gridHash in self.ListOfHashes):
            
            self.ListOfHashes[gridHash] = self.function(*args)
        #else:
        #    print("Evaluation function skipped let's go")
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.ListOfHashes[gridHash]