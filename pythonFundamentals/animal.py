class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        print "Decreased by 1" + self.health
        self.health -= 1
    
    def run(self):
        print "Decreased by 5" + self.health
        self.health -= 5

        print "Print to the terminal the animal's health"
       