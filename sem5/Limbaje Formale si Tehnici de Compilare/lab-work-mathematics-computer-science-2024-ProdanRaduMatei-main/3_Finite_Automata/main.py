"""
This program reads and displays the elements of a finite automaton (FA) from a file.

Expected Input Format (FA.in):
FA_file       ::= states "\n" alphabet "\n" transitions* initial_state "\n" final_states
states        ::= state (" " state)*
alphabet      ::= symbol (" " symbol)*
transitions   ::= state " " symbol " " state "\n"
initial_state ::= state
final_states  ::= state (" " state)*
state         ::= any string without whitespace
symbol        ::= any single non-whitespace character

The program will display:
- Set of states
- Alphabet
- Transitions
- Initial state
- Final states
"""
class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.final_states = set()
        self.initial_state = None

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Parsing states
            self.states = set(lines[0].strip().split())

            # Parsing alphabet
            self.alphabet = set(lines[1].strip().split())

            # Parsing transitions
            for transition in lines[2:-2]:
                start_state, symbol, end_state = transition.strip().split()
                if (start_state, symbol) not in self.transitions:
                    self.transitions[(start_state, symbol)] = set()
                self.transitions[(start_state, symbol)].add(end_state)

            # Parsing initial state
            self.initial_state = lines[-2].strip()

            # Parsing final states
            self.final_states = set(lines[-1].strip().split())

    def display(self):
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transitions:")
        for (start, symbol), end_states in self.transitions.items():
            print(f"  {start} --{symbol}--> {', '.join(end_states)}")
        print("Initial State:", self.initial_state)
        print("Final States:", self.final_states)

# Example usage
fa = FiniteAutomaton()
fa.load_from_file('/Volumes/Samsung/AN3/sem5/Limbaje formale de compilare/lab-work-mathematics-computer-science-2024-ProdanRaduMatei-main/3_Finite_Automata/FA.in')
fa.display()