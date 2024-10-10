# Ohm's Law Calculator

# V = IR
def find_voltage(current, resistance):
    return current * resistance

def find_current(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance

def find_resistance(voltage, current):
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current

def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\n Invalid input. Please enter a numeric value.")

def main():
    history = []

    while True:
        print("\n Choose :- ")
        print("\n 1) Find Voltage")
        print("\n 2) Find Current")
        print("\n 3) Find Resistance")
        print("\n 4) View History")
        print("\n 5) Exit")

        choice = get_input("\n Enter your choice please: ")

        if choice == 1:
            cur = get_input("\n Enter Current: ")
            res = get_input("\n Enter Resistance: ")
            volt = find_voltage(cur, res)
            result = f"\n Voltage: {volt} V"
            print(result)
            history.append(result)

        elif choice == 2:
            volt = get_input("\n Enter Voltage: ")
            res = get_input("\n Enter Resistance: ")
            try:
                cur = find_current(volt, res)
                result = f"\n Current: {cur} A"
                print(result)
                history.append(result)
            except ValueError as e:
                print(f"\n Error: {e}")

        elif choice == 3:
            volt = get_input("\n Enter Voltage: ")
            cur = get_input("\n Enter Current: ")
            try:
                res = find_resistance(volt, cur)
                result = f"\n Resistance: {res} Ω"
                print(result)
                history.append(result)
            except ValueError as e:
                print(f"\n Error: {e}")

        elif choice == 4:
            if history:
                print("\n History of Calculations:")
                for item in history:
                    print(item)
            else:
                print("\n No calculations yet.")

        elif choice == 5:
            print("\n Exit!")
            break

        else:
            print("\n Invalid choice...Please select a valid option.")

if __name__ == "__main__":
    main()