# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 05:28:31 2023

APP for calculation of amount of product to be added in water using automatic water dosage system - broilers (DOSATRON)

The daily volume of water were calculated based on:
https://www.thepoultrysite.com/articles/broiler-water-consumption
According to Dr Susan Watkins and Dr G.T. Tabler of the University of Arkansas. They have monitored water intake daily over 12 consecutive flocks, reporting their results in the University's Avian

@author: BRGUBO
"""

import PySimpleGUI as psg
from pandas.io import clipboard

app_version = '1.0'
app_title = f'Easy WS Dosage FIT for Broilers - v:{app_version}'  
vol_of_treated_water = .5 # percentual of the total volume of water that will be treated with product - .4 to .7 is frequently used


water_consump_dict = { '1': 0.01,
                       '2': 0.02025,
                       '3': 0.0291,
                       '4': 0.04156,
                       '5': 0.04860,
                       '6': 0.05314,
                       '7': 0.06041,
                       '8': 0.066963,
                       '9': 0.073853,
                       '10': 0.04860,
                       '11': 0.085323,
                       '12': 0.10534796,
                       '13': 0.11428152,
                       '14': 0.12408574,
                       '15': 0.13165656,
                       '16': 0.13517699,
                       '17': 0.147403865,
                       '18': 0.156564558,
                       '19': 0.163037609,
                       '20': 0.166860873,
                       '21': 0.174848088,
                       '22': 0.178784914,
                       '23': 0.187869898,
                       '24': 0.201686645,
                       '25': 0.205699179,
                       '26': 0.206607678,
                       '27': 0.2178882,
                       '28': 0.226973184,
                       '29': 0.238783663,
                       '30': 0.238783663,
                       '31': 0.2485,
                       '32': 0.2585056,
                       '33': 0.26535724,
                       '34': 0.2658114,
                       '35': 0.2747,
                       '36': 0.2671,
                       '37': 0.2814,
                       '38': 0.2921,
                       '39': 0.2975,
                       '40': 0.2987,
                       '41': 0.30597,
                       '42': 0.3116,
                       '43': 0.307299,
                       '44': 0.30355,
                       '45': 0.307299,
                       
                       }

#print(water_consump_dict['1'])

input_size_lbl = (30,1)
font_size_title=12
slider_secund_size=(20,15)
font_recommend = ("Arial", 16, 'bold')
font_title= ("Helvetica", 16, 'bold')
psg.theme('DarkBlue3')
font_out = "Arial", 16, 'bold'
input_size=(15,2)



psg.set_options(font='calibri 16', button_element_size=(2,1))
menu_def = [['Setup', ['% of treated water','Exit']]]
layout = [  
            [psg.Menu(menu_def)],
            [psg.Text('Calculator for Automatic Dosage Systems - Broilers', text_color= 'black', font=font_title, size=input_size_lbl, justification='center', expand_x=True)],
            [psg.Text("_" * 60)],
            [psg.Text('Number of Birds', size=input_size_lbl, justification='center', expand_x=True)],
            [psg.Slider(range=(1000,50000), resolution=1000, size=slider_secund_size, expand_x=True, default_value=10, enable_events=True ,orientation='h', key='-N_BIRDS-')],
            [psg.Text('AGE', size=input_size_lbl, justification='center', expand_x=True)],
            [psg.Slider(range=(1,45), resolution=1, size=slider_secund_size, expand_x=True, default_value=7, enable_events=True ,orientation='h', key='-AGE-')],
            [psg.Text('Dosage / 1000 birds (g)', size=input_size_lbl, justification='center', expand_x=True)],
            [psg.Slider(range=(5,15), size=slider_secund_size, resolution=5, expand_x=True, default_value=10, enable_events=True ,orientation='h', key='-DOSAGE-')],
            [psg.Text('Mixing rate (%)', size=input_size_lbl, justification='center', expand_x=True)],
            [psg.Slider(range=(.5,5), size=slider_secund_size, resolution=.1, expand_x=True, default_value=1.5, enable_events=True ,orientation='h', key='-MIX_RATE-')],
            [psg.Text("_" * 60)],
            [psg.Text(" " * 28), psg.Text('       Dosage Recomendation', font=font_recommend, size=input_size_lbl, justification='left',expand_x=True )],
            [psg.Text("_" * 60)],
            [psg.Text('Total Water / day (liters) :', font=font_out, size=input_size_lbl, justification='left'),
             psg.Input('', key='-OUTPUT_WATER_DAY-', font=font_out, justification='left', expand_x=False, readonly=True, size=input_size)],
            [psg.Text('Total Water treated / day (liters) :', font=font_out,size=input_size_lbl, justification='left'),
             psg.Input('', key='-OUTPUT_WATER_TREATED-', font=font_out, justification='left', expand_x=False, readonly=True, size=input_size),
             psg.Text('', key='-WATER_BE_TREAT', font=font_out,size=input_size_lbl, justification='left', enable_events=True)],
            [psg.Text('Product to be added (grams):', font=font_out, size=input_size_lbl, justification='left'),
             psg.Input('', key='-OUTPUT_PROD-', font=font_out, justification='left', expand_x=False, readonly=True, size=input_size, text_color= 'blue')],
            [psg.Text('Vol. mother soluction (liters):', key='-VOL_WATER-', font=font_out,size=input_size_lbl, justification='left', enable_events=True),
             psg.Input('', key='-OUTPUT_WATER-', font=font_out, justification='left', expand_x=False, readonly=True, size=input_size, text_color= 'blue')],
            [psg.Text("_" * 60)],
            [psg.Button("Exit", key='-EXIT-', font=("Helvetica", 12, 'bold'), enable_events=True,  size=(5, 0), button_color='#7d92a5'),
             psg.Button("Copy to Clipboard", font=("Helvetica", 12, 'bold'), key='-COPY-',  enable_events=True, size=(25, 0), button_color='#7d92a5')],
            
            [psg.Text("Water consumption estimated based on Dr Susan Watkins and G.Tabler, (2009)\nhttps://www.thepoultrysite.com/articles/broiler-water-consumption ", font=('Arial', 9))],
 
            ]
   

window = psg.Window(f'{app_title}', layout,size=(550, 800), finalize=True)
#window = psg.Window(f'{app_title}', layout, finalize=False)

while True:
        
        event, values = window.read()
        
        if event == psg.WIN_CLOSED or event=='-EXIT-' or event=='Exit':
            break
        
        if event == '% of treated water':
           perc_treated_water = psg.popup_get_text('Input value from 20% to 80%', title='Percentage of Total Water to be Treated (%)')
           if int(perc_treated_water) <20 or int(perc_treated_water) >80:
               psg.popup_error('ERROR - Only values between 20% and 80% is accepted!')
               perc_treated_water = str(vol_of_treated_water*100)
               window['-WATER_BE_TREAT'].update(str(round(vol_of_treated_water*100,1)) + ' %')
           
            
           vol_of_treated_water = float(perc_treated_water)/100
           
        window['-WATER_BE_TREAT'].update(str(round(vol_of_treated_water*100,1)) + ' %')                       
        
        n_birds = int(values['-N_BIRDS-'])
        bird_age = int(values['-AGE-'])
        vol_water_bird_d = water_consump_dict[str(bird_age)]
        dosage_product = int(values['-DOSAGE-'])
        mix_rate = float(values['-MIX_RATE-'])
        tot_water_vol = n_birds * vol_water_bird_d
        tot_water_treatyed_day = tot_water_vol * vol_of_treated_water
        tot_product = n_birds/1000 * dosage_product
        tot_mother_sol = tot_water_treatyed_day * mix_rate/100
        window['-OUTPUT_WATER_DAY-'].update(round(tot_water_vol,1))
        window['-OUTPUT_WATER_TREATED-'].update(round(tot_water_treatyed_day,1))
        window['-OUTPUT_PROD-'].update(round(tot_product,1))
        window['-OUTPUT_WATER-'].update(round(tot_mother_sol,1))
        
        
        
        if event == '-COPY-':
            prod = round(tot_product,1)
            solution = round(tot_mother_sol,1)
            text= f'\n*** {app_title} ***\nNumber of birds to be treated: {n_birds}\nAge (days): {bird_age}\nAmount of product (grams): {prod}\nMixing rate (%): {mix_rate}\nVolume of Mother Solution (Liters): {solution}\n\n\n'
            
            clipboard.copy(text)
            psg.popup_auto_close('Recommendation copied to clipboard', non_blocking=True)
            
            '''
            # send email
            import win32com.client
            ol=win32com.client.Dispatch("outlook.application")
            olmailitem=0x0 #size of the new email
            newmail=ol.CreateItem(olmailitem)
            newmail.Subject= 'Dosage Recomendation for Drink Solutions - Broilers'
            #newmail.To= 'brgubo@chr-hansen.com'
            newmail.To= email_inputed_by_user
            newmail.CC=''
            newmail.Body= f'\nNumber of Birds to be treated: {n_birds}\nAge (days): {bird_age}\nDosage of Product (gramas): {dosage_product}\nMixing rate (%): {mix_rate}\nTotal Mother Solution (Liters): {round(tot_mother_sol,0)}\n\n\n'
            '''
        
            
        
        
window.close()

