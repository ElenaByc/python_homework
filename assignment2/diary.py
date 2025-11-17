import os
import traceback


try:
    diary_path = os.path.join(os.path.dirname(__file__), "diary.txt")
    with open(diary_path, "a") as diary_file:
        # The first prompt should say, "What happened today?"
        prompt = "What happened today?\n"
        while True:
            user_input = input(prompt)
            diary_file.write(user_input + "\n")
            # When the special line "done for now" is received, write that to diary.txt. 
            # Then close the file and exit the program
            if user_input.strip().lower() == "done for now":
                break
            # All subsequent prompts should say "What else?"  
            prompt = "What else?\n"
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []
    for trace in trace_back:
        stack_trace.append(
            f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
        )
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
