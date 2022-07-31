from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import prompt


class OptionCompleter(Completer):
    def __init__(self, options: list[str]):
        Completer.__init__(self)
        self.options = options

    def get_completions(self, document, complete_event):
        for opt in self.options:
            yield Completion(opt, start_position=-len(document.text))


class OptionValidation(Validator):
    def __init__(self, options: list[str]):
        Validator.__init__(self)
        self.options = options

    def validate(self, document):
        text = document.text
        if text not in self.options:
            raise ValidationError(message=f'The input is invalid. Valid input: {", ".join(map(str, self.options))}')


def validation_prompt_yesno(text: str) -> bool:
    opt_list = ['yes', 'no']
    res = prompt(f'{text}: ', completer=OptionCompleter(opt_list), validator=OptionValidation(opt_list))

    if res == opt_list[0]:
        return True
    if res == opt_list[1]:
        return False


def validation_prompt_okcancel(text: str) -> bool | None:
    return None
    pass
