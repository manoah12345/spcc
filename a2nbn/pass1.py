class Assembler:
    def __init__(self):
        self.symbol_table = {}  # Stores label addresses
        self.intermediate_code = []  # Stores intermediate representation
        self.opcode_table = {
            "START": "(AD,01)", "END": "(AD,02)", "DS": "(DL,01)",
            "READ": "(IS,09)", "PRINT": "(IS,10)", "MOVER": "(IS,04)",
            "MOVEM": "(IS,05)", "ADD": "(IS,01)"
        }
        self.register_table = {
            "AREG": "(RG,01)", "BREG": "(RG,02)", "CREG": "(RG,03)"
        }
        self.location_counter = 0  # Memory location tracking

    def pass1(self, code):
        for line in code:
            tokens = line.split()

            if tokens[0] == "START":
                self.location_counter = int(tokens[1])
                self.intermediate_code.append(f"{self.opcode_table[tokens[0]]} (C,{tokens[1]})")
                continue

            if tokens[0] == "END":
                self.intermediate_code.append(f"{self.opcode_table[tokens[0]]} -")
                break

            if tokens[0] not in self.opcode_table:
                self.symbol_table[tokens[0]] = self.location_counter
                if tokens[1] == "DS":
                    self.intermediate_code.append(
                        f"(S,{len(self.symbol_table) - 1}) {self.opcode_table[tokens[1]]} (C,{tokens[2]})"
                    )
                    self.location_counter += int(tokens[2])
                    continue

            opcode = self.opcode_table.get(tokens[0], "")
            operands = []

            for operand in tokens[1:]:
                operand = operand.replace(",", "")
                if operand in self.register_table:
                    operands.append(self.register_table[operand])
                elif operand in self.symbol_table:
                    symbol_index = list(self.symbol_table.keys()).index(operand)
                    operands.append(f"(S,{symbol_index})")
                else:
                    operands.append(operand)

            self.intermediate_code.append(f"{opcode} {' '.join(operands)}")
            self.location_counter += 1

    def display_pass1(self):
        print("Pass 1 - Intermediate Code:")
        for instr in self.intermediate_code:
            print(instr)

        print("\nSymbol Table:")
        for index, (symbol, address) in enumerate(self.symbol_table.items()):
            print(f"(S,{index}) {symbol}: {address}")

    def pass2(self):
        print("\nPass 2 - Machine Code:")
        for instr in self.intermediate_code:
            parts = instr.split()

            # Declarative statements should print "-"
            if parts[0] in ["(AD,01)", "(AD,02)"] or "(DL,01)" in instr:
                print("-")
                continue

            opcode = parts[0].replace("(IS,", "").replace(")", "")  # Extract numerical opcode
            reg = "00"  # Default register value
            address = "00"  # Default address value

            for operand in parts[1:]:
                if operand.startswith("(RG,"):  # Register
                    reg = operand.replace("(RG,", "").replace(")", "")
                elif operand.startswith("(S,"):  # Symbol (address)
                    symbol_index = int(operand.replace("(S,", "").replace(")", ""))
                    address = str(list(self.symbol_table.values())[symbol_index])
                elif operand.startswith("(C,"):  # Constant
                    address = operand.replace("(C,", "").replace(")", "")

            print(f"{opcode} {reg} {address}")  # Ensures format: OPCODE REGISTER ADDRESS


if __name__ == "__main__":
    code = [
        "START 501", "A DS 1", "B DS 1", "C DS 1", "READ A", "READ B",
        "MOVER AREG, A", "ADD AREG, B", "MOVEM AREG, C", "PRINT C", "END"
    ]

    assembler = Assembler()
    assembler.pass1(code)
    assembler.display_pass1()
    assembler.pass2()
