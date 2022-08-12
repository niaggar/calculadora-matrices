from Program.Prompt import validation_prompt_yesno

from time import sleep
import json
import os


if __name__ == '__main__':
    try:
        res = validation_prompt_yesno('yust try')

        print(res)

    except Exception as e:
        print('Something went wrong. Please try again. \n{}'.format(e))


