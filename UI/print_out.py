import colorful as cf


def input_yes_no(sentence):
    """Generic yes-no question and input catcher"""
    print(sentence)
    print(cf.white("Please " + cf.red('press "y" ', nested=True) + "if yes"))
    print(cf.white(
        "Otherwise, " + cf.green('press any key ',
                                 nested=True) + 'to continue'))

    answer = input(": ")
    return answer


sentence = {
    "erase": "Would you like to erase all the tables and fill them again ? ",
    "data": "",
}
