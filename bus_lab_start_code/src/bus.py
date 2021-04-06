class Bus:
    def __init__(self, route_number,destination):
        self.route_number=route_number
        self.destination=destination
        self.pessenger= []

    def drive(self):
        return "Brum brum"
    def passenger_count(self):
        return len (self.pessenger)
    def pick_up(self, person):
        self.pessenger.append(person)
    def drop_off(self, person):
        self.pessenger.remove(person)
    def empty(self):
        self.pessenger= []
    
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        bus_stop.queue.clear()