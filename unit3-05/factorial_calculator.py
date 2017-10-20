import ui

def calculate_button_touch_up_inside(sender):
    input = int(view['input_textfield'].text)
    
    counter = 1
    answer = 1
    
    while (input >= counter):
        answer = answer * counter
        counter = counter + 1
        view['answer_label'].text = 'The factorial is: ' + str(answer)

view = ui.load_view()
view.present('sheet')
