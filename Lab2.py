import input_functions
import output_functions

def main()->int:
    user_name: str = input_functions.get_name()
    output_functions.put_greeting(user_name)
    return 1

if __name__ == "__main__":
    main()