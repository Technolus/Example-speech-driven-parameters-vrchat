# WARNING!
the application is still work-in-progress, please don't expect it to function as intended just yet.
# speech-driven-parameters
a very simple vrchat parameter driver that uses speech to drive parameters, currently only supports `boolean` as data type, that's all you get.

how to use:
1. download and install python from [here](https://www.python.org/downloads/)
2. install the modules mentioned in the requirements.txt file by running the following command in CMD where the requirements.txt file is found.
```
py -m pip install -r requirements.txt
```
3. run the script `main.py` using your favorite python interpreter.
4. press the "F" key each time you want to be heard by the application. say: `disable` or `enable` followed by your parameter's name, once the speech has been properly processed. it'll turn into a `command` and be sent to vrchat's avatar parameters osc endpoint to perform your request.
