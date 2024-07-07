> As you might be able to tell, the following README is written by ChatGPT with a bit of human curation. This was just a quick idea I had which I thought would be funny to very quickly hack together. It is by no means a serious project!

---

# 🐍 Pyrattle 🔥
> Code without boundaries -- or syntax, or structure, or consistency.

Pyrattle is a BRAND-NEW programming language POWERED by recent advances in AI 🤖.  This 🌟GROUND-BREAKING🌟 language is here to 💥SHATTER💥 the chains of conventional programming -- Pyrattle lets you write the sloppiest, most unstructured code you can imagine, without worrying about syntax or conventions, and it will 🪄AUTOMAGICALLY🪄 be turned into BORING and 🧽PRISTINE🧽 production-ready code. 

For example, have a look 👀 at `quicksort.pyr`:

```python
def quicksort(A):
  # not quite sure what to do here
  smaller = None # things smaller than a pivot
  larger = # not actually too sure
  middle = the pivot + the other bits

  return quicksort(smaller) + larger + quicksort(middle)

print(quicksort([10...0]))
```

As you can see, Pyrattle is a big superset of Python, and actually a superset of multiple other programming languages. Running this is easy, using the 😎COMMAND-LINE TOOL😎:

```sh
$ pyrattle quicksort.pyr
-- Code to run --
def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    smaller = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    larger = [x for x in A if x > pivot]

    return quicksort(smaller) + middle + quicksort(larger)

print(quicksort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


-- Continue? --
[yes]/no: yes


-- Output --
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Too safe for you? Tell it to automatically run the code without asking you first 😱😱😱

```
$ pyrattle quicksort.pyr --no-railings
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

For another example, consider this ✨outstanding reference implementation✨ of depth-first search:

```python
class Graph:
  # TODO

class Node:
  # TODO

def dfs(graph):
  for node in graph:
    node.f = infinity
    node.d = infinity
    node.color = "white"
    node.back = null

  time = 0

  for node in graph:
    if node.color == "white":
      dfs_visit(node)

def dfs_visit(graph):
  # something about updating time, color to grey then black and then
  # calling dfs visit on all the unexplored adjacent vertices

def print_backpointer_table(graph):
  # literally can't be bothered

graph = Graph()
dfs(graph)
print_backpointer_table(graph)
```

And, as if by 🪄magic🪄:

```sh
$ pyrattle dfs.pyr
-- Code to run --
class Graph:
  pass

class Node:
  def __init__(self):
    self.f = float('inf')
    self.d = float('inf')
    self.color = "white"
    self.back = None
    self.adjacent_nodes = []

def dfs(graph):
  def dfs_visit(node):
    nonlocal time
    node.color = "grey"
    time += 1
    node.d = time
    for adj_node in node.adjacent_nodes:
      if adj_node.color == "white":
        adj_node.back = node
        dfs_visit(adj_node)
    node.color = "black"
    time += 1
    node.f = time

  for node in graph:
    node.f = float('inf')
    node.d = float('inf')
    node.color = "white"
    node.back = None

  time = 0

  for node in graph:
    if node.color == "white":
      dfs_visit(node)

def print_backpointer_table(graph):
  for node in graph:
    print(f"Node {node}: {node.back}")

graph = [Node() for _ in range(5)]
graph[0].adjacent_nodes = [graph[1], graph[2]]
graph[1].adjacent_nodes = [graph[2]]
graph[2].adjacent_nodes = [graph[3]]
graph[3].adjacent_nodes = [graph[1]]
dfs(graph)
print_backpointer_table(graph)
```

(in this example, the AI realises that a `Graph` class isn't even required at all! Who knew?!)

## Why Pyrattle?!
| **PROS**                                                                                                                                                                        | **CONS**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Programming is fun again!                                                                                                                                                       | You might find yourself becoming so successful, drowning in wealth and fame, leaving behind the  simple joys of life you once cherished. Your family, feeling neglected  and replaced, might drift apart, their hearts heavy with longing. As  misunderstandings and resentments fester, cherished bonds begin to fray,  casting shadows on once-happy memories. One day, gazing upon your  mountain of riches, you could realize you have lost sight of what truly  matters. With tears in your eyes, you might vow to rebuild the bridges  you have burned and fight to reclaim the love and warmth of your family,  hoping it isn't too late. |
| 4k context length ensures your code remains concise                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Congrats! Your business is now powered by AI                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Limited liability -- how can you be fired if you didn't write the code?                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Your secret corporate data will be used to train the next generation of LLMs, making them even better suited for your usecase                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| A comprehensive standard library, consisting of the Python standard library but also of many functions and implementations from open source projects with restrictive licenses! |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Literally a million others                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### How it works
🚀Pyrattle🚀 unleashes 💫ADVANCED ALGORITHMS💫 (if statements) and 🤖AI POWER🤖 (sending off the code to the OpenAI chat API) to ⚡PRE-PROCESS⚡ your files, transforming them into 🐍REGULAR PYTHON🐍 code with 🔥LIGHTNING SPEED🔥 (~20 seconds for basic programs)!!! This tool then 💨RUNS💨 the processed Python, allowing you to 🌟BEHOLD🌟 the 🏆AMAZING RESULTS🏆 right before your very 👀EYES👀!!11!

### More examples!
All valid code!

##### [`examples/fizzbuzz.pyr`](examples/fizzbuzz.pyr)
Pyrattle can even help you out in your next JOB INTERVIEW!

```python
for i in range(51):
  # oh no what do i do oh no oh no they're going to figure out I don't know how to program
  # TODO: implement the full fizzbuzz program
```

##### [`examples/mandlebrot.pyr`](examples/mandlebrot.pyr)
Find math hard? Focus on the fun parts of the implementation with ❤️Pyrattle❤️.

```python
def draw_mandlebrot_ascii():
  # i wish i understood math
  # TODO: implement drawing the mandlebrot set with ascii
```

##### [`examples/calculator.pyr`](examples/calculator.pyr)
Pyrattle even lets you program using 💫ADVANCED ALGORITHMS💫 usually only reserved for 😎ELITE PROGRAMMERS😎.

```python
def shunting_yard(expression):
  # TODO

def calculate(expression):
  # hmmm
  rpn = shunting_yard(expression)

  state = []
  for thingy in rpn:
    if type(thingy) == int:
      state.append(thingy)
    elif thingy == "+":
      a, b = state.pop(), state.pop()
      state.append(a + b)
    elif # ... and so on for the rest of the arithmetic operations

output = calculate("(5 + 7) * 3 + 12")
print(output)
```

##### [`examples/therapy.pyr`](examples/therapy.pyr)
```python
# i just don't want to do programming anymore
# i've lost the last of the spark I had when I was younger
# now it's just not fun anymore
```

Output:

```
error: Well, that's unfortunate but taking a break is always a good idea. Maybe you'll find your spark again in the future.
```

When was the last time a programming language gave you LIFE ADVICE?!?

### Installing
```sh
$ git clone https://github.com/ollybritton/pyrattle
$ cd pyrattle
$ pip3 install openai click
$ python3 setup.py install
```

Then you just [need an OpenAI API key](https://platform.openai.com/account/api-keys). You should now be able to run Pyrattle files with 

```sh
$ export OPENAI_API_KEY=...
$ pyrattle FILENAME
```

Don't worry about making sure the filename ends in `.pyr`. This project will try and run any file, including binaries! For more options, see

```sh
$ pyrattle --help
```

If any of the above fails, try harder!!

### Future work
- Bootstrapping this project
- Support for modules
- More AI (??)
- Incorporate as a company? Seed round?
- Comprehensive research into AGI safety and ethics before we all die at the hand of a machine god

