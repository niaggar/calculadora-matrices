from Program.ControlUser import UserControlMatrix
from Program.ControlData import insert_matrix

from time import sleep
import json
import os

from Program import validation_prompt_yesno

main_options = ['create_matrix', 'edit_matrix', 'do_operation', 'close']


if __name__ == '__main__':
    try:
        # controller = UserControlMatrix()
        # a = controller.create_new_matrix()
        #
        # insert_matrix(a)

        res = validation_prompt_yesno('yust try')

        print(res)

    except Exception as e:
        print('Something went wrong. Please try again. \n{}'.format(e))


