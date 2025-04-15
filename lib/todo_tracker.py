class TodoList():
    def __init__(self):
        self.items = []
        
    def add(self, item):
        #Parameters:
        # item: string
        self.items.append(item)
        pass

    def view_items(self):
        # Returns:
        #  list of items
        return self.items
        pass

    def mark_complete(self):
        # Parameters:
        #  item: boolean 
        #       marked complete = True
        #       not marked complete = False
        pass