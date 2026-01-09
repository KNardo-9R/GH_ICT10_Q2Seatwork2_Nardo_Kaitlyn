from pyscript import display, document

def getting_info(e): 

    # output
    document.querySelector('#studentsubjects').innerText = " "
    document.querySelector('#popup').innerText = " "

    # list 
    subject_list = ['Science', 'Math', 'Filipino', 'English', 'SS', 'PE']

    # tuple
    subject_units = (5,5,3,5,4,1)

    # subjects 
    Science = float(document.getElementById('ScienceG').value)
    Math = float(document.getElementById('MathG').value)
    Filipino = float(document.getElementById('FilG').value)
    English = float(document.getElementById('EngG').value)
    SS = float(document.getElementById('SSG').value)
    PE = float(document.getElementById('PEG').value)

    subject_values = [Science, Math, Filipino, English, SS, PE]

    # computation 

    Science_value = subject_values[0] * subject_units[0]
    Math_value = subject_values[1] * subject_units[1]
    Filipino_value = subject_values[2] * subject_units[2]
    English_value = subject_values[3] * subject_units[3]
    SS_value = subject_values[4] * subject_units[4]
    PE_value = subject_values[5] * subject_units[5]
 
    # sum of subjects 
    Sum = Science_value + Math_value + Filipino_value + English_value + SS_value + PE_value 

    # sum of units
    Unit_sum = subject_units[0] + subject_units[1] + subject_units[2] + subject_units[3] + subject_units[4] + subject_units[5]

    GWA =  Sum / Unit_sum

    Subjects = f"""

    {subject_list[0]}: {subject_values[0]:.2f}
    {subject_list[1]}: {subject_values[1]:.2f}
    {subject_list[2]}: {subject_values[2]:.2f}
    {subject_list[3]}: {subject_values[3]:.2f}
    {subject_list[4]}: {subject_values[4]:.2f}
    {subject_list[5]}: {subject_values[5]:.2f}

    """
    if GWA > 74: 
        display(f'PASSED', target='result')
    else: 
        display(f'FAILED', target='result')
        
    display(Subjects, target='studentsubjects')
    display(f'Your General Weighted Average is {GWA:.2f}',target='popup')

    

