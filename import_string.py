import string
import sys

# Danno Denis Dhaifullah
# 5025211027

class TuringMachine:
    def __init__(self, current_state, head_position, tape):
        self.current_state = current_state
        self.head_position = head_position
        self.tape = tape

    def getState(self):
        return self.current_state

    def getHead(self):
        return self.head_position
    
    def getTape(self):
        return self.tape

    # Table of rules
    def updateMachine(self, allowed_characters):
        # Initial State
        if self.current_state == 'q1':
            if self.tape[self.head_position] != 0:
                # Move to state pN. N = index of allowed_characters
                read_character = self.tape[self.head_position]
                character_index = allowed_characters.index(read_character)
                self.current_state = ''.join(['p', str(character_index)])
                # Write 0 to the current tape position
                self.tape[self.head_position] = 0
                # Move head to the right
                self.head_position += 1
            else:
                # Reach acceptance state qy
                self.current_state = 'qy'
                # Write 0
                self.tape[self.head_position] = 0
                # Move head to the right
                self.head_position += 1
    
        elif self.current_state.startswith('p'):
            if self.tape[self.head_position] != 0:
                # Stay in the same state
                self.current_state = self.current_state
                # WRITE (unchanged)
                self.tape[self.head_position] = self.tape[self.head_position]
                # Move head to the right
                self.head_position += 1
            else:
                # Move to state rN. N = index from state pN
                self.current_state = ''.join(['r', self.current_state[1:]])
                # Write 0 to the current tape position
                self.tape[self.head_position] = 0
                # Move head to the left
                self.head_position -= 1
                    
        elif self.current_state.startswith('r'):
            read_character = allowed_characters[int(self.current_state[1:])]
            if self.tape[self.head_position] != read_character and self.tape[self.head_position] != 0:
                # Move to state qn if characters do not match
                self.current_state = 'qn'
                # Leave the tape unchanged
                self.tape[self.head_position] = self.tape[self.head_position]
                # Move head to the left
                self.head_position -= 1
            else:
                # Move to state q2 if characters match
                self.current_state = 'q2'
                # Write 0 to the current tape position
                self.tape[self.head_position] = 0
                # Move head to the left
                self.head_position -= 1
                
        elif self.current_state == 'q2':
            if self.tape[self.head_position] != 0:
                # Stay in state q2
                self.current_state = 'q2'
                # WRITE (unchanged)
                self.tape[self.head_position] = self.tape[self.head_position]
                # Move head to the left
                self.head_position -= 1
            else:
                # Move back to state q1
                self.current_state = 'q1'
                # Write 0 to the current tape position
                self.tape[self.head_position] = 0
                # Move head to the right
                self.head_position += 1

def check_palindrome(initial_string):
    # Define Character Set
    allowed_characters = list(string.ascii_lowercase + string.digits)
    allowed_characters.append(' ') # to allow for spaces

    # Initial string
    print('Checking: ' + initial_string)
    print('- - -')
    initial_list = list(initial_string)

    # check for only used allowed characters
    for i in initial_list:
        if i not in allowed_characters:
            print('Error! Initial character >', i, '< not in allowed character list!')
            sys.exit()

    # Append list
    initial_list.append(0)

    # Set up the Turing machine
    initial_head_position = 0
    initial_state = 'q1' # initial state
    initial_tape = initial_list

    # Initiate the class
    turing_machine = TuringMachine(initial_state, initial_head_position, initial_tape)
    print(turing_machine.getState(), turing_machine.getHead(), turing_machine.getTape())

    # Run the machine
    counter = 0
    while turing_machine.getState() != 'qy' and turing_machine.getState() != 'qn' and counter < 1000:
        turing_machine.updateMachine(allowed_characters)
        print(turing_machine.getState(), turing_machine.getHead(), turing_machine.getTape())
        counter += 1
    print('- - -')

    # Output
    if turing_machine.getState() == 'qy':
        print(initial_string, 'is a palindrome!')
    else:
        print(initial_string, 'NOT a palindrome!')

test_cases = ['tenet', 'racecar', 'hello', 'w0rld', 'aa22aa', 'a010a', '1', 'ab0']

for test in test_cases:
    check_palindrome(test)