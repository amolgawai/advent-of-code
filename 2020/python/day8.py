"""Day 8 solution"""
import sys


def does_prog_terminate(prog_instr_lst):
    """Checks weather the programme terminates given the instructions"""
    accumulator = 0
    instr_crnt = 0
    instr_prev = []
    instr_len = len(prog_instr_lst)
    prog_complete = False
    while True:
        if instr_crnt in instr_prev:
            break
        instr_prev.append(instr_crnt)
        if instr_crnt > instr_len - 1:
            prog_complete = True
            break
        cmd, value = prog_instr_lst[instr_crnt].split()
        value = int(value)
        if cmd == 'nop':
            instr_crnt += 1
        elif cmd == 'acc':
            accumulator += value
            instr_crnt += 1
        elif cmd == 'jmp':
            instr_crnt += value
        else:
            print("Invalid instructions")
            break
    if prog_complete:
        print(f"Accu = {accumulator}")
    return prog_complete


def replace_and_run_prog(orig_lst, replace_tpl_lst, str_to_replace, repls_str):
    """ Replaces the instruction and runs the programme"""

    for nop_instr in replace_tpl_lst:
        new_lst = orig_lst.copy()
        new_lst[nop_instr[0]] = nop_instr[1].replace(str_to_replace, repls_str)
        if does_prog_terminate(new_lst):
            return True
    return False


def main(input_f_name):
    """The main function"""
    with open(input_f_name) as input_f:
        instructions = input_f.readlines()
    print(does_prog_terminate(instructions))
    no_zero_nops = []
    jmps = []
    for indx, instr in enumerate(instructions):
        cmd, value = instr.split()
        if cmd == 'nop' and int(value) !=0:
            no_zero_nops.append((indx, instr))
        elif cmd == 'jmp':
            jmps.append((indx, instr))

    if replace_and_run_prog(instructions, no_zero_nops, 'nop', 'jmp'):
        print("Found Solution by changing nop")
    elif replace_and_run_prog(instructions, jmps, 'jmp', 'nop'):
        print("Found Solution by changing jmp")
    else:
        print("No slution found")


if __name__ == '__main__':
    main(sys.argv[1])
