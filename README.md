# Drone Learning Environment Manual

## Introduction

Welcome to the Python learning environment with Dji Tello drone! 
The Drone Learning Environment is a simple easy to get going yet complex introduction to Python programming.

Based on the DJITelloPy library, it provides the following features:

- Implementation of all Tello commands
- Easily retrieve a video stream
- Receive and parse state packets
- Control a swarm of drones
- Support for python >= 3.6

This manual will guide you through the basics of programming in Python and lead you throughout the challenges.

## Getting Started

This section walks you through the basic of Drone Learning Environment and Python, helping you to create your first challenge.

### Setting up your development environment for Windows

This section provides a step-by-step guide for setting up your development environment for Windows.

#### Install PyCharm

Before you can start coding you will need an integrated development environment (**IDE**) and we recommend PyCharm for the upcoming challenges.

https://www.jetbrains.com/pycharm/download/#section=windows

#### Install DJITelloPy library

First open a **New Project** in PyCharm.

![](https://i.imgur.com/sBKaoad.png)

Then choose **Pure Python** and hit **Create**

![](https://i.imgur.com/QvyQl4r.png)

Then go to **File** > **Settings** > **Project: ExampleName** > **Python Interpreter** > Click the **+** sign.

![](https://i.imgur.com/cS2grry.png)

Search for **djitellopy** and **Install Package**.

![](https://i.imgur.com/EbiS1MR.png)

After that type on top **from djitellopy import tello** to import the library.

### Connect to DJI Tello drone

1. Turn on the drone with the button on the side. 

2. Turn on wifi on your PC.

3. Search for wifi name starts with **TELLO**.

4. Type these inside your file to connect to the drone and receives its battery from PyCharm.

   ```python
   me = tello.Tello()
   
   me.connect()
   
   print(me.get_battery())
   ```

   

You can start coding with the drone!

## Challenges

### #Challenge 1

**Description**: Make the drone take off, move forward and land.

### **#Challenge 2**

**Description:** Make the drone take off, rotate and land.

### #Challenge 3

**Description:** Make the drone take off, flip and land.

### #Challenge 4

**Description:** Make the drone fly in a rectangle pattern.

### #Challenge 5

**Description:** Make the drone take off, do 8D flips and land.

### #Challenge 6

**Description:** Make the drone fly in circle pattern.

### #Challenge 7

**Description:** Make the drone fly in a curve motion.

### #Challenge 8

**Description:** Make the drone take off, flip and land.

## Misc. and hints

Come to this section to further learn basics in Python and how to use the library.

### **Python**

**Python Functions**

```python
def my_function():
  print("Hello from a function")
```

**Python Syntax**

```python
if 5 > 2:
  print("Five is greater than two!")
```

**Python Comments**

```python
#This is a comment
print("Hello, World!")
```

**Python Variables**

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

**Python Numbers**

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

**Python If...Else**

```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

**Python While Loops**

```python
i = 1
while i < 6:
  print(i)
  i += 1
```

**Python For Loops**

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

### DJITelloPy Library

To view the whole library and all of its functions by **CTRL + Left Mouse Click** on one of the functions.

```python
def challenge1():
    me = tello.Tello()

    me.connect()

    print(me.get_battery())
```

For this example you can can **CTRL + Left Mouse Click** on `Tello()`, `connect()` or `get_battery()` and similarly for all functions you might use.

# MORE WILL BE UPDATED

