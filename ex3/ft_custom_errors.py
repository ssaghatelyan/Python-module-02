class GardenError(Exception):
    def __init__(self, message: str ="Unknown plant error") -> None:
        super().__init__(message)

class PlantError(GardenError):
	def __init__(self,  message: str ="Unknown plant error") -> None:
		super().__init__(message)

class WaterError(GardenError):
    def __init__(self,  message: str ="Unknown plant error") -> None:
        super().__init__(message)

def checkPlant() -> None:
		raise PlantError("The tomato plant is wilting!")

def checkWater() -> None:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        checkPlant()
    except PlantError as ex:
        print(f"Caught PlantError: {ex}")
    print("\nTesting WaterError...")
    try:
           checkWater()
    except WaterError as ex:
           print(f"Caught WaterError: {ex}")
    print("\nTesting catching all garden errors...")
    try:
           checkPlant()
    except GardenError as ex:
           print(f"Caught GardenError: {ex}")
    try:
           checkWater()
    except GardenError as ex:
        print(f"Caught GardenError: {ex}")
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
       test_custom_errors()