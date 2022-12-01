# **Kolpy**

A package to compute upper bounds of kolmogorov complexity of a python code script.

<p align="center">
  <img src="assets/kolmogorov-complexity-joke.png" alt="General illustration of the Kolpy" width="35%"/>
</p>

# Why Kolpy ?

In order to evaluate upper bounds of the Kolmogorov complexity of some task, we need a tool to evaluate the upper bound of a python program that succeeds at the said task.

This package exists as the tool to fulfill that need.

## Objective of the project

This project will be completed when we will be able to parse any single python file and evaluate an upper bound of its kolmogorov complexity using both the true lenght of the file and the lenght of the bitecode compiled code of the python file.

# Table of Contents

-   [**Installation**](#installation)
-   [**Usage**](#usage)

# Installation

Make sure you have Python installed:

**1. (Optional) Create a virtual environment:**

```bash
python -m venv .env
```

**2. Install the package with pip in your terminal:**

```bash
pip install git+https://github.com/IRLL/Kolpy.git
```

# Usage

**Run the project with the following command:**

```bash
kolpy --help
```

or:

```bash
python -m kolpy --help
```
