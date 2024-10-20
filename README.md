# python-samples

Hello.py

The disassembled code will be displayed with line numbers. Each line represents a bytecode instruction and tells the interpreter what to do. For example, in the given disassembled code:

`def myfunc():    print("ahmet")`

Bytecode

`  4           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('ahmet')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
`

| Mnemonics     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        | Source Code |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| LOAD_GLOBAL   | Loads the global named co_names[/namei/] onto the sta                                                                                                                                                                                                                                                                                                                                                                                              |             |
| CALL_FUNCTION | Calls a function. The low byte of /argc/ indicates the number of positional parameters, the high byte the number of keyword parameters. On the stack, the opcode finds the keyword parameters first. For each keyword argument, the value is on top of the key. Below the keyword parameters, the positional parameters are on the stack, with the right-most parameter on top. Below the parameters, the function object to call is on the stack. |             |
| POP_TOP       | Removes the top-of-stack (TOS) item                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| LOAD_COST     | Pushes "co_consts[/consti/]" onto the stac                                                                                                                                                                                                                                                                                                                                                                                                         |             |

For all opcodes [link](https://unpyc.sourceforge.net/Opcodes.html)
