def main():
    print("ET0735 (DevOps for AIoT) -Lab2 - intro to python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("Enter some numbers separated by commas (eg 5, 67,32)")

def get_user_input():
    x = input()
    num_list = x.split(",")
    float_list = list(map(float, num_list))
    print("float list" + str(float_list))
    return float_list
def calc_average():
    print("calc_average")

if __name__ == "__main__":
    main()
