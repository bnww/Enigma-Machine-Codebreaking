class PlugLead:
    def __init__(self, mapping):
        if mapping.isupper() and len(mapping) == 2 and mapping[0] != mapping[1]:
            self.mapping = mapping
        else:
            raise ValueError("Input must be a string of 2 different uppercase letters.")

    def encode(self, char):
        if self.mapping[0] == char:
            return self.mapping[1]
        elif self.mapping[1] == char:
            return self.mapping[0]
        elif char.isupper() and len(char) == 1:
            return char
        else:
            raise ValueError("Input must be a single uppercase character.")


class Plugboard:
    def __init__(self):
        self.board = []
    
    def __str__(self):
        return f"Plugleads connected to the plugboard are: {self.board}"

    def is_full(self):
        return len(self.board) == 10
    
    def is_empty(self):
        return len(self.board) == 0
    
    def is_connected(self, char):
        for lead in self.board:
            if char in lead:
                return True
        return False
    
    def add(self, lead):
        if self.is_full():
            raise ValueError("Plugboard is full.")
        for char in lead.mapping:
            if self.is_connected(char):
                raise ValueError(f"{char} is already connected.")
        self.board.append(lead.mapping)
        
    def remove(self, lead):
        if self.is_empty():
            raise ValueError("Plugboard is empty.")
        elif lead.mapping in self.board:
            for i in range(self.board.index(lead.mapping), len(self.board) - 1):
                self.board[i] = self.board[i+1]
            self.board = self.board[:-1]
        else:
            raise ValueError("Those characters are not connected.")
        
    def encode(self, char):
        for lead in self.board:
            if char in lead:
                return PlugLead(lead).encode(char)
        if char.isupper() and len(char) == 1:
            # no connection is found
            return char
        else:
            raise ValueError("Input must be a single uppercase character.")
            

class rotor_from_name:
    def __init__(self, label):
        self._mappings = {"Beta": ["L","E","Y","J","V","C","N","I","X","W","P","B","Q","M","D","R","T","A","K","Z","G","F","U","H","O","S"],
                          "Gamma": ["F","S","O","K","A","N","U","E","R","H","M","B","T","I","Y","C","W","L","Q","P","Z","X","V","G","J","D"],
                          "I": ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"],
                          "II": ["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"],
                          "III": ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"],
                          "IV": ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B"],
                          "V": ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K"],
                          "A": ["E","J","M","Z","A","L","Y","X","V","B","W","F","C","R","Q","U","O","N","T","S","P","I","K","H","G","D"],
                          "B": ["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"],
                          "C": ["F","V","P","J","I","A","O","Y","E","D","R","Z","X","W","G","C","T","K","U","Q","S","B","N","M","H","L"]}
        
        if label in self._mappings.keys():
            self._rotor = self._mappings[label] # this references the list of mappings for the rotor in question
        else:
            raise ValueError("Invalid label.")
    
    def encode_right_to_left(self, character):
        if character.isupper() and len(character) == 1:
            return self._rotor[ord(character) - 65]
        else:
            raise ValueError("Input must be a single uppercase character.")
    
    def encode_left_to_right(self, character):
        if character.isupper() and len(character) == 1:
            return chr(self._rotor.index(character) + 65)
        else:
            raise ValueError("Input must be a single uppercase character.")
    

class Rotors:
    def __init__(self):
        self._reflector_maps={"A": ["E","J","M","Z","A","L","Y","X","V","B","W","F","C","R","Q","U","O","N","T","S","P","I","K","H","G","D"],
                              "B": ["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"],
                              "C": ["F","V","P","J","I","A","O","Y","E","D","R","Z","X","W","G","C","T","K","U","Q","S","B","N","M","H","L"]
                              }
        
        self._rotor_maps = {"Beta": ["L","E","Y","J","V","C","N","I","X","W","P","B","Q",
                                     "M","D","R","T","A","K","Z","G","F","U","H","O","S"],
                            "Gamma": ["F","S","O","K","A","N","U","E","R","H","M","B","T","I",
                                      "Y","C","W","L","Q","P","Z","X","V","G","J","D"],
                            "I": ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W",
                                  "Y","H","X","U","S","P","A","I","B","R","C","J"],
                            "II": ["A","J","D","K","S","I","R","U","X","B","L","H","W","T",
                                   "M","C","Q","G","Z","N","P","Y","F","V","O","E"],
                            "III": ["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y",
                                    "E","I","W","G","A","K","M","U","S","Q","O"],
                            "IV": ["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X",
                                   "L","N","F","T","G","K","D","C","M","W","B"],
                            "V": ["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L",
                                  "X","A","W","M","J","Q","O","F","E","C","K"]}
    
    def __str__(self):
        return f"Reflector: {self._reflector}, Rotors: {self._rotors}, Ring settings: {self._rings}, Initial positions: {self._positions}, Notches: {self._notches}"
    
    def new_reflector(self, name, mapping):
        self._reflector_maps[name] = mapping
        
    def new_rotor(self, name, mapping):
        self._rotor_maps[name] = mapping
        
    def swap_reflector_wiring(self, reflector, *pairs_list): # changes the reflector mapping so that the new pairs are wired together - this is used for codebreaker # 5
        import copy
        mapping = self._reflector_maps[reflector]
        new_mapping = copy.copy(mapping)
        for pair in pairs_list:
            wire_1 = pair[0]
            wire_2 = pair[1]
            new_mapping[mapping.index(wire_1[0])] = wire_2[1]
            new_mapping[mapping.index(wire_2[1])] = wire_1[0]
            new_mapping[mapping.index(wire_1[1])] = wire_2[0]
            new_mapping[mapping.index(wire_2[0])] = wire_1[1]
        self.new_reflector(reflector + "_modified", new_mapping)
        
    def set_ref_rotors(self, reflector, *rotors):
        if reflector in self._reflector_maps.keys() and all(rotor in self._rotor_maps.keys() for rotor in rotors):
            self._rotors = rotors
            self._reflector = reflector
            
            def char_to_int(collection):
                result = []
                for char in collection:
                    result.append(ord(char) - 65)
                return result
            
            # Defining the mappings for the 3 or 4 rotors and reflector as integer lists (0-25 instead of A-Z):
            if len(self._rotors) == 4:
                self._r4_map = char_to_int(self._rotor_maps[self._rotors[-4]])
            
            self._reflector_map = char_to_int(self._reflector_maps[reflector])    
            self._r3_map = char_to_int(self._rotor_maps[self._rotors[-3]])
            self._r2_map = char_to_int(self._rotor_maps[self._rotors[-2]])
            self._r1_map = char_to_int(self._rotor_maps[self._rotors[-1]])
        else:
            raise ValueError("Invalid rotor(s) / reflector.")

    def ring_settings(self, *rings): 
        if len(rings) == len(self._rotors) and all(1 <= ring <= 26 for ring in rings):
            self._rings = rings
            self._rings_offset = []
            for ring in self._rings:
                self._rings_offset.append((ring-1) * -1)
                
        else: raise ValueError("There must be a valid ring setting (1-26) for each rotor.")
    
    def initial_positions(self, *positions):
        if len(positions) == len(self._rotors) and all(position.isupper() for position in positions):
            self._positions = positions
            self._position_offset = []
            for position in self._positions:
                self._position_offset.append(ord(position) - 65) 
            
            # Defining notches:
            self._notches = {"I":"Q", "II":"E", "III":"V", "IV":"J", "V":"Z"}
            self._int_notches = {} # converting notches to integers to use in enigma rotor rotation
            for rotor, notch in self._notches.items():
                self._int_notches[rotor] = ord(notch) - 65
        else:
            raise ValueError("There must be a valid position (A-Z) for each rotor.")
            
            
class Enigma:
    def __init__(self, rotors, plugboard = Plugboard()):
        self.rotors = rotors
        self.plugboard = plugboard
    
    def __str__(self):
        return f"{self.rotors}\n{self.plugboard}"
    
    def encode(self, message):
        encrypted = ""
        
        if message.isupper():
            for char in message:
                # Rotation
                if self.rotors._rotors[-2] in self.rotors._int_notches.keys():
                    # 2nd rotor has notch
                    if self.rotors._position_offset[-2] == self.rotors._int_notches[self.rotors._rotors[-2]]:
                        # 2nd rotor is on notch position, so move 2nd and 3rd rotor positions forward
                        self.rotors._position_offset[-3] = (self.rotors._position_offset[-3] + 1) % 26
                        self.rotors._position_offset[-2] = (self.rotors._position_offset[-2] + 1) % 26
                
                    elif self.rotors._rotors[-1] in self.rotors._int_notches.keys():
                        # 2nd rotor not in notch position, 1st rotor has notch
                        if self.rotors._position_offset[-1] == self.rotors._int_notches[self.rotors._rotors[-1]]:
                            # 1st rotor is on notch position
                            self.rotors._position_offset[-2] = (self.rotors._position_offset[-2] + 1) % 26
                
                elif self.rotors._rotors[-1] in self.rotors._int_notches.keys():
                    # only the 1st rotor has notch
                    if self.rotors._position_offset[-1] == self.rotors._int_notches[self.rotors._rotors[-1]]:
                        # 1st rotor is on notch position
                        self.rotors._position_offset[-2] = (self.rotors._position_offset[-2] + 1) % 26
                
                # 1st rotor always moves:       
                self.rotors._position_offset[-1] = (self.rotors._position_offset[-1] + 1) % 26
                
                
                offset = [] # Overall integer offset as a sum of the positive rotor position offset and negative ring setting offset.
                for (i, j) in zip(self.rotors._rings_offset, self.rotors._position_offset):
                    offset.append((i + j) % 26)
                
                # Encoding:
                # The signal is encoded in the plugboard, then this is converted to an integer (0-25 corresponding to A-Z).
                # The signal will pass through the machine as an integer until the final plugboard encoding.
                plugboard_1st = ord(self.plugboard.encode(char)) - 65
                
                # Passing through rotors right to left:
                r1_1st = (self.rotors._r1_map[(plugboard_1st + offset[-1]) % 26] - offset[-1]) % 26
                r2_1st = (self.rotors._r2_map[(r1_1st + offset[-2]) % 26] - offset[-2]) % 26
                r3_1st = (self.rotors._r3_map[(r2_1st  + offset[-3]) % 26] - offset[-3]) % 26
                
                
                if len(self.rotors._rotors) == 3:
                    reflect = self.rotors._reflector_map[r3_1st]
                    # Left to right:
                    r3_2nd = (self.rotors._r3_map.index((reflect + offset[-3]) % 26) - offset[-3]) % 26
                    
                    
                else:
                    r4_1st = (self.rotors._r4_map[(r3_1st + offset[-4]) % 26] - offset[-4]) % 26
                    reflect = self.rotors._reflector_map[r4_1st]
                    
                    # Left to right:
                    r4_2nd = (self.rotors._r4_map.index((reflect + offset[-4]) % 26) - offset[-4]) % 26
                    r3_2nd = (self.rotors._r3_map.index((r4_2nd + offset[-3]) % 26) - offset[-3]) % 26
                r2_2nd = (self.rotors._r2_map.index((r3_2nd + offset[-2]) % 26) - offset[-2]) % 26
                r1_2nd = (self.rotors._r1_map.index((r2_2nd + offset[-1]) % 26) - offset[-1]) % 26
                
                
                # After the signal has passed through the rotors twice, it is converted back to a letter and encoded in the plugboard.
                plugboard_2nd = self.plugboard.encode(chr(r1_2nd + 65))
                encrypted += plugboard_2nd
               
            return encrypted
        else:
            raise ValueError("Input must be an uppercase string.")
    