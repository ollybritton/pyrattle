# 🐍 Pyrattle 🔥
> Code without boundaries -- or syntax, or structure, or consistency.

Pyrattle is a BRAND-NEW programming language POWERED by recent advances in AI 🤖.  This 🌟GROUND-BREAKING🌟 language is here to 💥SHATTER💥 the chains of conventional programming -- pyrattle lets you write the sloppiest, most unstructured Python code you can imagine, without worrying about syntax or conventions, and it will 🪄 AUTOMAGICALLY 🪄 be turned into BORING and PRISTINE 🧽 production-ready code. 

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

As you can see, Pyrattle is a big superset of Python. Running this is easy, using

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

For another example, consider this ✨ outstanding reference implementation ✨ of depth-first search:

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

And, as if by 🪄 magic 🪄:

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
| **PROS**                                                                                                                      | **CONS**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Programming is fun again!                                                                                                     | You might find yourself becoming so successful, drowning in wealth and fame, leaving behind the  simple joys of life you once cherished. Your family, feeling neglected  and replaced, might drift apart, their hearts heavy with longing. As  misunderstandings and resentments fester, cherished bonds begin to fray,  casting shadows on once-happy memories. One day, gazing upon your  mountain of riches, you could realize you have lost sight of what truly  matters. With tears in your eyes, you might vow to rebuild the bridges  you have burned and fight to reclaim the love and warmth of your family,  hoping it isn't too late. |
| 4k context length ensures your code remains concise                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Congrats! Your business is now powered by AI                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Limited liability -- how can you be fired if you didn't write the code?                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Your secret corporate data will be used to train the next generation of LLMs, making them even better suited for your usecase |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Literally a million others                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### More examples!
- [`examples/calculator.pyr`](examples/calculator.pyr)
- [`examples/dfs.pyr`](examples/dfs.pyr)
- [`examples/fizzbuzz.pyr`](examples/fizzbuzz.pyr)
- [`examples/mandlebrot.pyr`](examples/mandlebrot.pyr)
- [`examples/quicksort.pyr`](examples/quicksort.pyr)

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

If any of the above fails, try harder.

### Future work
- Bootstrapping this project
- Support for modules
- More AI
- Incorporate as a company? Seed round?
- Comprehensive research into AGI safety and ethics before we all die at the hand of a machine god

