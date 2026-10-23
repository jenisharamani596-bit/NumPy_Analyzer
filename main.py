import numpy as np


class DataAnalytics:

    # Constructor
    def __init__(self):
        self.__array = None          

    # Class method
    @classmethod
    def from_list(cls, values):
        return np.array(values)

    # Static method
    @staticmethod
    def read_numbers(message, count):
        while True:
            try:
                values = [int(x) for x in input(message).split()]
                if len(values) == count:
                    return values
                print(f"Please enter exactly {count} elements.")
            except ValueError:
                print("Invalid input. Enter whole numbers only.")

    # Private method
    def __need_array(self):
        if self.__array is None:
            print("\nPlease create an array first (option 1).")
            return False
        return True

    # 1. Create array, indexing, slicing
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            shape = (int(input("\nEnter the number of elements: ")),)
        elif choice == 2:
            rows = int(input("\nEnter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            shape = (rows, cols)
        elif choice == 3:
            depth = int(input("\nEnter the number of blocks: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            shape = (depth, rows, cols)
        else:
            print("Invalid choice.")
            return

        total = int(np.prod(shape))
        values = self.read_numbers(
            f"Enter {total} elements for the array separated by space: ", total)
        self.__array = self.from_list(values).reshape(shape)

        print("\nArray created successfully:")
        print(self.__array)
        self.array_operations()

    def array_operations(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                idx = input("\nEnter index (comma separated, e.g. 1,2): ")
                try:
                    idx = tuple(int(i) for i in idx.split(","))
                    print("\nElement:", self.__array[idx])
                except (ValueError, IndexError):
                    print("Invalid index.")
            elif choice == 2:
                if self.__array.ndim == 1:
                    s, e = input("\nEnter the range (start:end): ").split(":")
                    print("\nSliced Array:")
                    print(self.__array[int(s):int(e)])
                else:
                    r1, r2 = input("\nEnter the row range (start:end): ").split(":")
                    c1, c2 = input("Enter the column range (start:end): ").split(":")
                    print("\nSliced Array:")
                    print(self.__array[..., int(r1):int(r2), int(c1):int(c2)])
            elif choice == 3:
                break
            else:
                print("Invalid choice.")

    # 2. Mathematical operations
    def math_operations(self):
        if not self.__need_array():
            return
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice: "))

        n = self.__array.size
        values = self.read_numbers(
            f"\nEnter the same-size array elements ({n} elements separated by space): ", n)
        second = self.from_list(values).reshape(self.__array.shape)

        print("\nOriginal Array:")
        print(self.__array)
        print("\nSecond Array:")
        print(second)

        if choice == 1:
            print("\nResult of Addition:")
            print(self.__array + second)
        elif choice == 2:
            print("\nResult of Subtraction:")
            print(self.__array - second)
        elif choice == 3:
            print("\nResult of Multiplication:")
            print(self.__array * second)
        elif choice == 4:
            print("\nResult of Division:")
            print(self.__array / second)
        else:
            print("Invalid choice.")

    # 3. Combine or split
    def combine_or_split(self):
        if not self.__need_array():
            return
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = self.__array.size
            values = self.read_numbers(
                f"\nEnter the elements of another array to combine ({n} elements separated by space): ", n)
            second = self.from_list(values).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(second)
            print("\nCombined Array:")
            print(np.concatenate((self.__array, second)))
        elif choice == 2:
            parts = int(input("\nEnter the number of parts to split into: "))
            if self.__array.shape[0] % parts != 0:
                print("Array cannot be split into equal parts.")
                return
            print("\nOriginal Array:")
            print(self.__array)
            for i, part in enumerate(np.split(self.__array, parts), start=1):
                print(f"\nPart {i}:")
                print(part)
        else:
            print("Invalid choice.")

    # 4. Search, sort, filter
    def search_sort_filter(self):
        if not self.__need_array():
            return
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(self.__array)

        if choice == 1:
            value = int(input("\nEnter the value to search: "))
            positions = np.argwhere(self.__array == value)
            if len(positions) == 0:
                print("Value not found.")
            else:
                for p in positions:
                    print("Value found at index:", tuple(int(i) for i in p))
        elif choice == 2:
            print("\nSorted Array:")
            print(np.sort(self.__array))
            print("(Sorting applied row-wise.)")
        elif choice == 3:
            value = int(input("\nEnter the value (show elements greater than it): "))
            print("\nFiltered Values:")
            print(self.__array[self.__array > value])
        else:
            print("Invalid choice.")

    # 5. Aggregates and statistics
    def aggregates_statistics(self):
        if not self.__need_array():
            return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = int(input("Enter your choice: "))

        print("\nOriginal Array:")
        print(self.__array)

        if choice == 1:
            print("\nSum of Array:", np.sum(self.__array))
        elif choice == 2:
            print("\nMean of Array:", np.mean(self.__array))
        elif choice == 3:
            print("\nMedian of Array:", np.median(self.__array))
        elif choice == 4:
            print("\nStandard Deviation of Array:", np.std(self.__array))
        elif choice == 5:
            print("\nVariance of Array:", np.var(self.__array))
        else:
            print("Invalid choice.")


def main():
    app = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    print("=" * 40)

    while True:
        print("Choose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            app.create_array()
        elif choice == 2:
            app.math_operations()
        elif choice == 3:
            app.combine_or_split()
        elif choice == 4:
            app.search_sort_filter()
        elif choice == 5:
            app.aggregates_statistics()
        elif choice == 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice.")
        print()


if __name__ == "__main__":
    main()