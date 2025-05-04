"""
Program: age_riddle_solver
--------------------------
This program calculates the ages of Anton, Beth, Chen,
Drew, and Ethan based on the relationships described
in the problem statement.
"""

def main():
    YEARS_OLD = " years old."

    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    print("\nAnton is " + str(anton) + YEARS_OLD)
    print("Beth is " + str(beth) + YEARS_OLD)
    print("Chen is " + str(chen) + YEARS_OLD)
    print("Drew is " + str(drew) + YEARS_OLD)
    print("Ethan is " + str(ethan) + YEARS_OLD)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

