import asyncio


import dis

def example_function(a, b):
    return a + b

async def example_function_async(a, b):
    return a + b

# Disassemble the function
#dis.dis(example_function)
print("----")
dis.dis(example_function_async)

asyncio.run(example_function_async(1,2), debug=True)
