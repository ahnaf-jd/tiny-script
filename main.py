from cpu import CPU
with open("program.txt", "r") as file:
    lines = file.readlines()

cpu = CPU()
lines = [line.strip() for line in lines]
words = [line.split() for line in lines]
for instruction in words:
    operation = instruction[0]

    if len(instruction) > 1:
        argument = instruction[1]

        if operation == "LOAD":
            cpu.load(int(argument))
            print(cpu.accumulator)   
        elif operation == "ADD":
            cpu.add(int(argument))
            print(cpu.accumulator)
        elif operation == "MUL":
            cpu.mul(int(argument))
            print(cpu.accumulator)
        elif operation == "DIV":
            cpu.div(int(argument))
            print(cpu.accumulator)    
    else:
        cpu.print_acc()            