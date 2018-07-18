#Substitution ciphers for the rotors are from here (I II, III):
#https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_offset
import time

class Rotors():
    def __init__(self):
        #TODO: Add reflection board
        #self.dict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
        self.dict = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.rotors = [
            #[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, X, Y, Z]
            ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"],
            ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"],
            ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"],
            ]
        self.startingPos = ["E", "A", "B"]
        self.reflector = ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T", "S", "P", "I", "K", "H", "G", "D"]

    def rotate(self):
        #Move first item to the back, 'rotating the rotor'. If the first rotor has completed a rotation, the next rotor rotates
        #TODO: Optimize for less hardcoded rotating

        self.rotors[0].append(self.rotors[0].pop(0))
        if self.rotors[0][0] == self.startingPos[0]:
            self.rotors[1].append(self.rotors[1].pop(0))
            if self.rotors[1][0] == self.startingPos[1]:
                self.rotors[2].append(self.rotors[2].pop(0))

    def output(self, inputLetter):
        #Uses the ciphers to encode a letter, then calls self.rotate()
        inputstr = inputLetter
        for x in self.rotors:
            inputstr = x[self.dict.index(inputstr)]
        inputstr = self.reflector[self.dict.index(inputstr)]
        for x in self.rotors[::-1]:
             inputstr = self.dict[x.index(inputstr)]
        self.rotate()
        return(inputstr)

    def configure(self, rotorSettings):
        #Rotates the rotors to the rotorSettings
        #TODO: Make sure rotorSettings are the same length as rotors
        for x, y in enumerate(self.rotors):
            self.rotors[x] = y[y.index(rotorSettings[x]):] + y[:y.index(rotorSettings[x])]

if __name__ == "__main__":
    rotor = Rotors()
    print(rotor.output("O"))
    print(rotor.output("A"))