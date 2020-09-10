class TrafficLight:
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

    def __init__(self):
        self.state = self.RED

    def go(self):
        if self.state == self.RED:
            self.state = self.GREEN

    def slow_down(self):
        if self.state == self.GREEN:
            self.state = self.YELLOW

    def stop(self):
        if self.state == self.YELLOW:
            self.state = self.RED
