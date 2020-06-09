from PyInquirer import style_from_dict, prompt, Token, Separator


class PyInquirerHandler(object):
    def _get_style(self):
        style = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })

        return style

    def get_answer(self, questions):
        answers = prompt(questions, style=self._get_style())
        return answers
