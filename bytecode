import dis

bytecode = []

i=0
while i < len(bytecode):
    op = dis.opname[bytecode[i]]
    if op == 'LOAD_CONST':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'STORE_FAST':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'LOAD_GLOBAL':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'LOAD_FAST':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'JUMP_ABSOLUTE':
        print i, op, int(bytecode[i+1])
        i+=2
    elif op == 'BUILD_LIST':
        print i, op
        i+=2
    elif op == 'SETUP_LOOP':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'CALL_FUNCTION':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'FOR_ITER':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'COMPARE_OP':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'POP_JUMP_IF_FALSE':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'JUMP_FORWARD':
        print i, op, bytecode[i+1]
        i+=2
    elif op == 'STOP_CODE':
        pass
    else:
        print i, op
    i+=1
