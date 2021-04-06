class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue=[]
    def add_to_queue(self, person):
        if self.name == person.destination or person.destination==0:
            self.queue.append(person)

    def queue_length(self):
        return len(self.queue)
    
    def clear(self):
        self.queue = []
    