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

First open a **New Project** in **PyCharm**.

![](https://i.imgur.com/sBKaoad.png)

Then choose **Pure Python** and hit **Create**.

![](https://i.imgur.com/QvyQl4r.png)

Then go to **File** > **Settings** > **Project: ExampleName** > **Python Interpreter** > Click the **+** sign.

![](https://i.imgur.com/cS2grry.png)

Search for **djitellopy** and **Install Package**.

![](https://i.imgur.com/EbiS1MR.png)

After that type this on top to import the library.

```python
from djitellopy import tello
```



#### (Optional) Install Visual Studio Code.

If you do not have access to PyCharm, Visual Studio Code is also our recommended Editor.

1. Install [VS Code](https://code.visualstudio.com/).

2. Next, install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Marketplace. For additional details on installing extensions, see [Extension Marketplace](https://code.visualstudio.com/docs/editor/extension-marketplace). The Python extension is named **Python** and it's published by Microsoft.

   ![https://code.visualstudio.com/assets/docs/python/tutorial/python-extension-marketplace.png](https://code.visualstudio.com/assets/docs/python/tutorial/python-extension-marketplace.png)

   3. Install a Python interpreter[#](https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter).

   Along with the Python extension, you need to install a Python interpreter. Which interpreter you use is dependent on your specific needs, but some guidance is provided below.

   ### Windows[#](https://code.visualstudio.com/docs/python/python-tutorial#_windows).

   Install [Python from python.org](https://www.python.org/downloads/). You can typically use the **Download Python** button that appears first on the page to download the latest version.

   > **Note**: If you don't have admin access, an additional option for installing Python on Windows is to use the Microsoft Store. The Microsoft Store provides installs of [Python 3.7](https://www.microsoft.com/en-us/p/python-37/9nj46sx7x90p), [Python 3.8](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l), and [Python 3.9](https://www.microsoft.com/en-au/p/python-39/9p7qfqmjrfp7). Be aware that you might have compatibility issues with some packages using this method.

   For additional information about using Python on Windows, see [Using Python on Windows at Python.org](https://docs.python.org/3.9/using/windows.html)

   4. Verify the Python installation[#](https://code.visualstudio.com/docs/python/python-tutorial#_verify-the-python-installation)

      To verify that you've installed Python successfully on your machine, run one of the following commands (depending on your operating system):

      - Linux/macOS: open a Terminal Window and type the following command:

        ```
        python3 --version
        ```

      - Windows: open a command prompt and run the following command:

        ```
        py -3 --version
        ```

      If the installation was successful, the output window should show the version of Python that you installed.

   5. Create a Python file. Go to **File** > **New File**.

      ![](https://i.imgur.com/2Jh9whn.png)

   6. **Click** on **Select a language** and type **Python**.

   7. Use the Command Palette to run **Terminal: Create New Integrated Terminal** (Ctrl+Shift+`).

   8. **Type** this in the just opened terminal.

      ```python
      python -m ensurepip
      ```

      and then.

      ```python
      pip install djitellopy
      ```

   9. After that type on **top of the python file created** to import the library.

      ```python
      from djitellopy import tello
      ```

### Connect to DJI Tello drone

1. Turn on the drone with the button on the side. 

2. Turn on Wi-Fi on your PC.

3. Search for Wi-Fi name starts with **TELLO**.

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

###### **Tip: run a function (out side any parent function)**

```python
my_function()
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
