def what_to_do(instr: str):
    says = 'Simon says'
    if instr.startswith(says):
        return "I " + instr.replace(says + ' ', '')
    if instr.endswith(says):
        return "I " + instr.replace(' ' + says, '')
    return "I won't do it!"
# print(what_to_do(input()))
