# python-samples

# Bytecode analysis

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

* [Demystifying Python Bytecode: A Guide to Understanding and Analyzing Code Execution](https://medium.com/@noransaber685/demystifying-python-bytecode-a-guide-to-understanding-and-analyzing-code-execution-6a163cb83bd1)


## Installing Python 3.13

If you have Docker, you can quickly spin up a Python 3.13 shell to play around with the examples in this article like so:

```
$ docker run -it --rm python:3.13
```

Not using Docker? We recommend installing Python 3.13 with [pyenv](https://github.com/pyenv/pyenv):

```
$ pyenv install 3.13.0
```

## Installing Pyenv

Follow the instuctions on the [link](https://github.com/pyenv/pyenv)

##### to add to ~/.zprofile:

```she
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zprofile
```

### mypy 

`mypy` is a static type checker for Python. Its primary purpose is to ensure that Python code adheres to type annotations, helping developers catch type-related errors before runtime. Here's a breakdown of `mypy`'s usage and benefits:

#### 1. **Type Checking**

* `mypy` analyzes type hints in your Python code without actually running the code.
* It catches type inconsistencies, like trying to assign a string to a variable that’s annotated as an integer, providing errors or warnings about these issues.

#### 2. **Error Prevention**

* By enforcing type consistency, `mypy` helps identify potential bugs that could otherwise lead to runtime errors.
* For example, if a function expects an argument of type `List[int]` and you pass `List[str]`, `mypy` will catch the mismatch.

#### 3. **Improving Code Readability and Documentation**

* Type annotations make code easier to understand for both developers and tools by documenting what types of data are expected.
* `mypy` enforces these annotations, helping you maintain consistent and well-documented code.

#### How to Use `mypy`

1. **Install** : You can install `mypy` using pip:

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install mypy
   </code></div></div></pre>

1. **Run** : Run `mypy` on your Python files:

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">mypy my_script.py</code></div></div></pre>


The `-m` parameter in Python allows you to run a module as a script directly from the command line, rather than running a file. Here’s a breakdown of what it does, why it's useful, and examples of when you might use it:

#### 1. **Usage of `-m`**

* When you use `python -m <module_name>`, Python will locate and run the specified module as a script.
* This works by searching for the module in the Python environment’s path (using `sys.path`) and running the module's `__main__` block if it exists.

#### 2. **Why We Need `-m`**

* **Module-based Execution** : It enables you to run standard library modules and custom modules in your Python environment without specifying the full path.
* **Path Management** : `-m` lets Python know to look for the module in the package path rather than treating the name as a script path. This avoids issues with `PYTHONPATH` and is particularly useful for packages with submodules.
* **Testing and Running Tools** : Many tools and libraries provide `-m` functionality to easily run specific tasks, like unit tests or installing packages.

#### **Running Python Standard Library Modules**

* `python -m http.server`: Starts a simple HTTP server.
* `python -m venv myenv`: Creates a virtual environment in the `myenv` directory.
* `python -m unittest`: Runs the Python unit test framework.

#### b. **Running Third-party Modules**

* `python -m pip install <package>`: Runs the `pip` package manager.
* `python -m mymodule.submodule`: Useful when you want to run a specific module or script within a package or a virtual environment.

#### c. **Running Your Own Packages and Scripts**

* If you have a package structure like this:

  <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">css</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-css">mypackage/
  ├── __init__.py
  └── main.py
  </code></div></div></pre>

  You can run `main.py` with `python -m mypackage.main` instead of specifying the path directly.
