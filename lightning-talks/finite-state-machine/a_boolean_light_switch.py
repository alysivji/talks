class LightSwitch:
    def __init__(self):
        self.on = False

    def flip_switch_up(self):
        if not self.on:
            self.on = True

    def flip_switch_down(self):
        if self.on:
            self.on = False
