class TrafficLight:
    def __init__(self):
        self.is_red = True
        self.is_yellow = False

    def go(self):
        if self.is_red and not self.is_yellow:
            self.is_red = False
            self.is_yellow = False

    def slow_down(self):
        if not self.is_red and not self.is_yellow:
            self.is_red = False
            self.is_yellow = True

    def stop(self):
        if not self.is_red and self.is_yellow:
            self.is_red = True
            self.is_yellow = False
