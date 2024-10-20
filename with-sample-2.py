method = 2
print(f"method = {method}")
if method == 1:
    # 1) without using with statement
    file = open('./samplefile.txt', 'w')
    file.write('hello world ! method='+str(method))
    file.close()
elif method == 2:
    # 2) without using with statement
    file = open('./samplefile.txt', 'w')
    try:
        file.write('hello world ! method='+str(method))
    finally:
        file.close()   
elif method == 3:
    # using with statement
    with open('./samplefile.txt', 'w') as file:
        file.write('hello world ! method='+str(method))
else:
    print("Please select 1-2-3 method")