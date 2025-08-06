import traceback

try:
    with open("diary.txt", "a") as file:
        prompt = "What happened today? "
        while True:
            try:
                line = input(prompt)
            except EOFError:
                raise Exception("Input ended unexpectedly (EOF)")

            file.write(line + "\n")

            if line.strip().lower() == "done for now":
                break
            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            f'File : {trace.filename} , Line : {trace.lineno}, Func.Name : {trace.name}, Message : {trace.line}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")