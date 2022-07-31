from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt


class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except:
            raise ValidationError(message='This input contains non-numeric characters')


class TextValidator(Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise ValidationError(message='This input contains non-numeric characters')


def get_prompt_number(text: str) -> float:
    """
    Ask the user a number (float) and validate that impute is a real number.
    """
    res = prompt(text, validator=NumberValidator())
    num = float(res)

    return num


def get_prompt_text(text: str) -> str:
    """
    Ask the user a text and validate that impute exist.
    """
    return prompt(text, validator=TextValidator())
