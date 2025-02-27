# Console-Application-for-Managing-a-Collection-of-Objects
Implement a console application that manages a collection of objects interactively. The collection should store instances of the Flat class, with the given description and requirements.

## Overview

This console application allows users to manage a collection of `Flat` objects interactively. The application supports various commands for adding, updating, removing, and displaying elements in the collection. Data is stored in JSON format and can be loaded from a file specified via command-line arguments.

## Features

- Interactive command-line interface for managing a collection of `Flat` objects.
- Automatic population of the collection from a specified JSON file on startup.
- Support for various commands to manipulate and display the collection.
- Error handling for incorrect user input and file access issues.
- Documentation for all classes using Python docstrings.

## Requirements

1. The class managing the collection must implement default sorting.
2. All class field requirements must be fulfilled as specified.
3. Use `collections.deque` for storage.
4. The application should read data from a JSON file specified as a command-line argument.
5. Data should be stored in JSON format.
6. Use Python's built-in file handling for reading and writing data.
7. All classes must be documented with docstrings.
8. The application must handle incorrect data gracefully.

## Commands

The application supports the following commands:

- `help`: Display help information about available commands.
- `info`: Output information about the collection (type, initialization date, number of elements, etc.).
- `show`: Output all elements of the collection in string representation.
- `add {element}`: Add a new element to the collection.
- `update id {element}`: Update the value of the collection element with the specified id.
- `remove_by_id id`: Remove an element from the collection by its id.
- `clear`: Clear the collection.
- `save`: Save the collection to a file.
- `execute_script file_name`: Read and execute a script from the specified file.
- `exit`: Exit the program (without saving to a file).
- `remove_head`: Output the first element of the collection and remove it.
- `add_if_min {element}`: Add a new element to the collection if its value is less than the smallest element in the collection.
- `history`: Output the last 9 commands (without their arguments).
- `count_less_than_number_of_rooms numberOfRooms`: Output the number of elements whose `numberOfRooms` field is less than the specified value.
- `filter_contains_name name`: Output elements whose `name` field contains the specified substring.
- `filter_less_than_central_heating centralHeating`: Output elements whose `centralHeating` field is less than the specified value.

## Input Format

- All command arguments that are standard data types should be entered on the same line as the command name.
- Composite data types should be entered one field per line, with prompts indicating the field name.
- For enum fields, the user should enter one of the constants, with the list displayed beforehand.
- In case of incorrect input, an error message will be shown, and the user will be prompted to re-enter the field.
- To input null values, use an empty string.
- Fields marked as "This field value should be generated automatically" should not be manually entered by the user.

## Class Descriptions

### Flat

```python
class Flat:
    def __init__(self, id, name, coordinates, area, number_of_rooms, floor, central_heating, transport, house=None):
        # Must be greater than 0, unique, and generated automatically
        # Cannot be null or empty
        # Cannot be null
        # Cannot be null, generated automatically
        # Must be greater than 0
        # Must be greater than 0
        # Must be greater than 0
        # Cannot be null
        # Cannot be null
```
### Coordinates
```python
class Coordinates:
    def __init__(self, x, y):
        # Must be greater than -61, cannot be null
        # Cannot be null
```
### House
```python
class House:
    def __init__(self, name=None, year=None, number_of_floors=None, number_of_flats_on_floor=None, number_of_lifts=None):
        # Can be null
        # Maximum value: 639, must be greater than 0
        # Must be greater than 0
        # Must be greater than 0
        # Must be greater than 0
```
### Transport Enum
```python
class Transport(Enum):
    FEW = "Few"
    NONE = "None"
    LITTLE = "Little"
    ENOUGH = "Enough"
```
## Getting Started
Clone the repository or download the source code.

Ensure you have Python installed on your machine.

Prepare a JSON file with the required data format.

Run the application from the command line with the filename as a command-line argument:
```
python your_application.py your_data_file.json
```
Follow the on-screen prompts to interact with the application.

## Acknowledgments
Inspired by ITMO University, Software Eng faculty, Java programming course, task 5, variant 4556 : collection management.
