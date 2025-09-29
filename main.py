#DRILL 2    

from pyscript import display, document

def generate_message(e):
    # Get input values
    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    # Strings
    student_name = {name}   
    student_age = {age}      
    student_school = {school}
    display(f' Welcome, {name}!')
    display(f'{name} is currently {age} years old studying in {school}', target='output')
