def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "Hello" + 42 # type: ignore
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as ex:
            print(f"Caught ValueError: {ex}")
        except ZeroDivisionError as ex:
            print(f"Caught ZeroDivisionError: {ex}")
        except FileNotFoundError as ex:
            print(f"Caught FileNotFoundError: {ex}")
        except TypeError as ex:
            print(f"Caught TypeError: {ex}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
