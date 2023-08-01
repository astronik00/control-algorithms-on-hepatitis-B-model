import os
from run_continuous import run as run_continuous
from run_discrete import run as run_discrete

def main():
    images_paths = ['images/adar/png', 'images/adar/svg', 'images/no_control/png', 'images/no_control/svg',
                    'images/adar+dadar/png', 'images/adar+dadar/svg']

    # default workdirs to load coefficients and save images
    coefficients_filepath, images_filepath = 'coefficients/coeffs1.txt', 'images/'

    flag = True

    print("Hello and welcome to hepatitis B modeling script for continuous case")

    # create required paths if not exist
    for path in images_paths:
        if not os.path.exists(path):
            os.makedirs(path)

    while flag:
        user_number = int(input('1 - change workdir\n2 - continuous\n3 - discrete\n0 - exit\n>>> '))

        if user_number == 1:
            user_number = int(input('\n1 - change coefficients dir\n2 - change images dir\n>>> '))

            if user_number == 1:
                new_coefficients_filepath = input("New coefficients filepath:\n>>> ")  # coefficients/coeffs1.txt
                if os.path.exists(new_coefficients_filepath):
                    coefficients_filepath = new_coefficients_filepath
                    a = [float(x) for x in open(coefficients_filepath).read().split("\n")]
                else:
                    print("IncorrectFilepath: file does not exist, dir was not changed\n")

            elif user_number == 2:
                new_images_filepath = input("new images filepath:\n>>> ")  # images/no_control/
                if os.path.exists(new_images_filepath):
                    images_filepath = new_images_filepath
                else:
                    print("IncorrectFilepath: file does not exist, dir was not changed\n")

        elif user_number == 2:
            run_continuous(images_filepath, coefficients_filepath)

        elif user_number == 3:
            run_discrete(images_filepath, coefficients_filepath)
        else:
            flag = False


if __name__ == "__main__":
    main()
