- [ ] Shell should work in interactive and non-interactive mode
  - [ ] `./console.py` and `echo "help" | ./console.py`
- [ ] Tests should also pass in non-interactive mode.
  - [ ] `echo "python3 -m unittest discover tests" | bash`

# Tasks

## Documentation

- [ ] README.md file
  - [ ] Description of the project
  - [ ] Description of the command interpreter
    - [ ] How to start it
    - [ ] How to use it
    - [ ] Examples
      - [ ] Code snippets
- [ ] AUTHORS file

## Tests

- [ ] Describe test cases for files, classes and functions.
- [ ] Write unit tests.
- [ ] Ensure tests run in non-interactive mode as well.

## Models

### BaseModel

- `models/base_model.py`
- [ ] Create the class BaseModel
  - [ ] Public instance attributes
    - [ ] `id`
    - [ ] `created_at`
    - [ ] `updated_at`
  - [ ] Public instance methods
    - [ ] `save(self)`
    - [ ] `to_dict(self)`
- [ ] Generate an instance of BaseModel from dictionary representation.
  - [ ] Implement `__init__(self, *args, **kwargs)`
- [ ] Update `models/base_model.py`: to link `BaseModel` to `FileStorage` using the `storage` variable
  - [ ] Import the variable `storage`
  - [ ] In the `save(self)` method:
    - [ ] Call `save(self)` method of `storage`
  - [ ] in `__init__(self, *args, **kwargs)`, if it's a new instance, call new(self) on storage

```python

def positional(*args)
  print(args[0])
  print(args[1])


def named(**kwargs)
  print(**kwargs["one"])
  print(**kwargs["two"])


positional("hello", "world")
named(one="hello", two="world")
named(two="world", one="hello")

my_dict = {
  two: "world"
  one: "hello",
}

def mixed(one, two, **kwargs)


mixed("hello", "world")

# *args
positional(*my_dict) == positional("hello", "world")

# **kwargs
positional(**my_dict) == positional(one="hello", two="world")
```

### FileStorage

- `models/engine/file_storage.py`
- [ ] Private class attributes
  - [ ] `__file_path`: string path to the JSON file.
  - [ ] `__objects`: dictionary that will store all objects by `<class name>.id`
- [ ] Public instance methods
  - [ ] `all(self)`: returns the dictionary `__objects`
  - [ ] `new(self, obj)`: sets in `__objects` the obj passed as parementer
  - [ ] `save(self)`: serializes `__objects` to the `__file_path`
  - [ ] `reload(self)`: deserialize JSON file to `__objects`
- [ ] Update `models/__init__.py` to create a unique `FileStorage` instance
  - [ ] import `file_storage.py`
  - [ ] create the varialbe `storage`, an instance of `FileStorage`
  - [ ] call `reload()` method on the variable.

## Console

- `console.py`
- Entry point
- [ ] Create basic command interpreter
  - [ ] uses the cmd module
  - [ ] implement `quit` and `EOF`
  - [ ] implement `help`
  - [ ] custom prompt `(hbnb)`
  - [ ] empty line + `ENTER` shouldn't execute anything
- [ ] v0.1
  - [ ] implement `create` create's new instance of `BaseModel`, saves it and prints the `id`
    - [ ] handle `create` errors.
  - [ ] implement `show`. Prints string repr of an instance based on the classname and id
    - [ ] handle `show` errors.
  - [ ] implement `destroy`. Deletes an instance base on the class name and `id`. Update JSON file.
  - [ ] implement `all`. Prints string repr of all instances based or not on the class name.
    - [ ] handle `all` errors.
  - [ ] implement `update`. Updates
