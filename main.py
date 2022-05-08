from venv import create
from Program.ControlUser import UserControlMatrix
from Program.ControlData import insert_matrix
from time import sleep

import enquiries
import json
import os


# options = ['thing 1', 'thing 2', 'thing 3']
# choice = enquiries.choose('Choose one of these options: ', options)

# if enquiries.confirm('Do you want to write something?'):
#     text = enquiries.freetext('Write something interesting: ')
#     print(text)



main_options = ['create_matrix', 'edit_matrix', 'do_operation', 'close']


if __name__ == '__main__':
    try:
        controller = UserControlMatrix()
        a = controller.create_new_matrix()

        insert_matrix(a)

        # actions_control =  {
        #     'create_matrix': controller.create_new_matrix,
        #     'edit_matrix': controller.edit_matrix,
        # }

        # while True:
        #     choice = enquiries.choose('Choose one of these options: ', main_options)
        #     if choice == 'close':
        #         break
        #     else:
        #         actions_control.get(choice)()
    
    except Exception as e:
        print('Something went wrong. Please try again. \n{}'.format(e))

