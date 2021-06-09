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

