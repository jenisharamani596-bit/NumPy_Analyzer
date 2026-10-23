# 🔢 NumPy Analyzer -- Python Project

**Author:** Jenisha Ramani

**Project Name:** NumPy Analyzer

------------------------------------------------------------------------

## 📌 Project Overview

NumPy Analyzer is a Python-based console application developed using the
NumPy library. It provides multiple numerical and statistical operations
through a menu-driven program.

The project allows users to create 1D, 2D, and 3D NumPy arrays and
perform mathematical operations, array manipulation, searching, sorting,
filtering, and statistical calculations.

It demonstrates the practical implementation of NumPy and
Object-Oriented Programming (OOP) concepts in Python.

## 🛠️ Technology Used

-   Python
-   NumPy
-   Visual Studio Code
-   GitHub

## ✨ Features

### 1. Create a NumPy Array

-   Create 1D, 2D, and 3D arrays.
-   Perform indexing and slicing.
-   Take array elements from the user.

### 2. Mathematical Operations

-   Addition
-   Subtraction
-   Multiplication
-   Division

### 3. Combine or Split Arrays

-   Combine two arrays.
-   Split an array into multiple parts.

### 4. Search, Sort, or Filter Arrays

-   Search a specific value.
-   Sort array elements.
-   Filter values based on conditions.

### 5. Aggregates and Statistics

-   Sum
-   Mean
-   Median
-   Standard Deviation
-   Variance

## 📂 Project Structure

``` text
NumPy Analyzer/
│
├── main.py
└── README.md
```

## ▶️ How to Run the Project

### Step 1: Install NumPy

``` bash
pip install numpy
```

### Step 2: Run the Python File

``` bash
python main.py
```

## 💻 Sample Output

``` 
Welcome to the NumPy Analyzer!
========================================
Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 1

Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array
Enter your choice: 2

Enter the number of rows: 2
Enter the number of columns: 3
Enter 6 elements for the array separated by space: 10 20 30 40 50 60

Array created successfully:
[[10 20 30]
 [40 50 60]]

Choose an operation:
1. Indexing
2. Slicing
3. Go Back
Enter your choice: 2

Enter the row range (start:end): 0:2
Enter the column range (start:end): 1:3

Sliced Array:
[[20 30]
 [50 60]]

Choose an operation:
1. Indexing
2. Slicing
3. Go Back
Enter your choice: 3

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 2

Choose a mathematical operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter your choice: 1

Enter the same-size array elements (6 elements separated by space): 5 5 5 5 5 5

Original Array:
[[10 20 30]
 [40 50 60]]

Second Array:
[[5 5 5]
 [5 5 5]]

Result of Addition:
[[15 25 35]
 [45 55 65]]

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 3

Choose an option:
1. Combine Arrays
2. Split Array
Enter your choice: 1

Enter the elements of another array to combine (6 elements separated by space): 1 2 3 4 5 6

Original Array:
[[10 20 30]
 [40 50 60]]

Second Array:
[[1 2 3]
 [4 5 6]]

Combined Array:
[[10 20 30]
 [40 50 60]
 [ 1  2  3]
 [ 4  5  6]]

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 4

Choose an option:
1. Search a value
2. Sort the array
3. Filter values
Enter your choice: 2

Original Array:
[[10 20 30]
 [40 50 60]]

Sorted Array:
[[10 20 30]
 [40 50 60]]

(Sorting applied row-wise.)

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 5

Choose an aggregate/statistical operation:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
Enter your choice: 3

Original Array:
[[10 20 30]
 [40 50 60]]

Median of Array: 35.0

Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
Enter your choice: 6

Thank you for using the NumPy Analyzer! Goodbye!
```

## 📚 Learning Outcomes

Through this project, I learned:

-   Creating and manipulating NumPy arrays.
-   Performing mathematical operations on arrays.
-   Understanding array indexing and slicing.
-   Combining and splitting arrays.
-   Searching, sorting, and filtering array elements.
-   Calculating statistical values using NumPy.
-   Implementing menu-driven applications in Python.
-   Applying Object-Oriented Programming concepts.

