from rotors import Rotors
class Machine():
    def __init__(self):
        self.rotor = Rotors()
        self.reference = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.plugboard = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def swap(self, letter):
        return(self.plugboard[self.reference.index(letter)])

    def addPlugboardConnecion(self, firstLetter, secondLetter):
        #FIXME: make sure there arent doubling plugboard connectons
        # and give a warning when changing an existing plugboard connection
        self.plugboard[self.reference.index(firstLetter)] = secondLetter
        self.plugboard[self.reference.index(secondLetter)] = firstLetter
    
    def returnOutput(self, letter):
        return self.swap(self.rotor.output(self.swap(letter)))
        

if __name__ == "__main__":
    machine = Machine()
    machine.addPlugboardConnecion("A", "B")
    print(machine.swap("A"))
    print(machine.swap("B"))
    print(machine.plugboard)
