from random import *


shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


    
def generate_quiz():
    text = choice(["RED","BLUE","YELLOW","GREEN"])
    color = choice(["#3F51B5","#C62828","#FFD600","#4CAF50"])
    quiz_type = randint(0,1)
    print(quiz_type)

    
    return [
                text,
                color,
                quiz_type,
            ]

def mouse_press(x, y, text, color, quiz_type):
    
    if text == "RED":
        if quiz_type == 0:
            if  140<x<240:
                if 60<y<160:
                    return True
            else:
                return False
        if quiz_type == 1:
            if color == "#FFD600":
                if 20<x<120:
                    if 180<y<280:
                        return True
                else:
                    return False
            if color == "#C62828":
                if 140<x<240:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#3F51B5":
                if 20<x<120:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#4CAF50":
                if 140<x<240:
                    if 180<y<280:
                        return True
                else:
                    return False
                

    if text == "BLUE":
        if quiz_type == 0:
            if 20<x<120:
                if 60<y<160:
                    return True
            else:
                return False
        if quiz_type == 1:
            if color == "#FFD600":
                if 20<x<120:
                    if 180<y<280:
                        return True
                else:
                    return False
            if color == "#C62828":
                if 140<x<240:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#3F51B5":
                if 20<x<120:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#4CAF50":
                if 140<x<240:
                    if 180<y<280:
                        return True
                else:
                    return False
    if text == "YELLOW":
        if quiz_type == 0:
            if 20<x<120:
                if 180<y<280:
                    return True
            else:
                return False
        if quiz_type == 1:
            if color == "#FFD600":
                if 20<x<120:
                    if 180<y<280:
                        return True
                else:
                    return False
            if color == "#C62828":
                if 140<x<240:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#3F51B5":
                if 20<x<120:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#4CAF50":
                if 140<x<240:
                    if 180<y<280:
                        return True
                else:
                    return False

                  
    if text == "GREEN":
        if quiz_type == 0:
            if 140<x<240:
                if 180<y<280:
                    return True
            else:
                return False
        if quiz_type == 1:
            if color == "#FFD600":
                if 20<x<120:
                    if 180<y<280:
                        return True
                else:
                    return False
            if color == "#C62828":
                if 140<x<240:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#3F51B5":
                if 20<x<120:
                    if 60<y<160:
                        return True
                else:
                    return False
            if color == "#4CAF50":
                if 140<x<240:
                    if 180<y<280:
                        return True
                else:
                    return False

            
       





           
        
    
    
