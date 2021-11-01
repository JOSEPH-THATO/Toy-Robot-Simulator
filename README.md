## Introduction

● The application is a simulation of a toy robot moving on a square tabletop, of
dimensions 5 units x 5 units.
● There are no other obstructions on the table surface.
● The robot is free to roam around the surface of the table, but must be prevented from
falling to destruction. Any movement that would result in the robot falling from the
table must be prevented, however further valid movement commands must still be
allowed.


## Project Structure
The project is as the following structure:

```bash
Toy-Robot-Simulator
├── tests
├── toy_robot_sim
│   ├── app
|   |   ├── constroller
|   │   ├── constants.py
|   |
│   ├── cli
|       ├── cli.py

```

## Setting up and Running the project

### export PYTHONPATH=/Users/joes/Desktop/Toy-Robot-Simulator
or
### edit sys.path.append("/Users/joes/Desktop/Toy-Robot-Simulator") to your project path

### Installing pre-requisites
The project uses pip-tool to manage dependencies and it also utilize a Makefile that can be found at the root of the project.

#### Update requirements.txt
```bash
make up
```

#### Update dependencies in virtual environment/The system Python
```bash
make deps
```

#### To run the project
```bash
make run
```