from fastapi import FastAPI

app = FastAPI()
@app.get("/")                         # If you define the same URL twice,
#                                        FastAPI will always run the first one and
#                                       completely ignore the second one.
def read_root():                            
    return {"message": "Hello SAIF!"}



@app.get("/")
def read_root():
    return {"message" : "Hello World!"}




@app.get("/")
def user():
    return {"message": "I am User"}

#Question : Is It necessary fast APi can return only the dictionary????
# Answer : NO 
#You can return:
# Dictionary
# list 
# string 
# integer 
# pydandic model (most professional one )

# But dictionary is most common because:

# JSON (what APIs return) is basically a dictionary
# Frontend/apps expect structured key-value data
# It's readable and easy to work with

# The rule is simple:

# Whatever you return, FastAPI automatically converts it to JSON and sends it as the response.

# So return whatever makes sense for your use case — dict, list, string, model, anything!

@app.get("/myEx")
def myEXname():
    return "She..."


# Question
'''here i return the string , it is actually not in the format of dict 
then why you said its a rule 
Whatever you return, FastAPI automatically converts it to JSON and sends it as the response.
So return whatever makes sense for your use case — dict, list, string, model, anything! '''

# Answer
'''
You are absolutely right to question that! And the answer is — it IS converting it to JSON!
The thing is:
A JSON string looks exactly like this:
json"She..."
JSON is not just dictionaries. JSON supports multiple types:
PythonJSON"She...""She..."4242Truetrue["a", "b"]["a", "b"]{"key": "val"}{"key": "val"}

So FastAPI DID convert it to JSON:
python@app.get("/myEx")
def my_ex():
    return "She..."   # Python string
👇 FastAPI converted it to:
json"She..."              # Valid JSON string

The confusion is:
Most people think JSON = dictionary only, but that's wrong.

JSON stands for JavaScript Object Notation — and it supports strings, numbers, lists, booleans,
    and objects (dicts).

So my statement was correct — FastAPI always converts to JSON, 
even when you return a plain string. You saw the proof yourself in the browser! ✅
  '''
