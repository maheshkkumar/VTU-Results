#!/usr/bin/python   
# -*- coding: utf-8 -*-
#######################################  
# Created by Mahesh Kumar K           #
# Python Script to fetch VTU Results  #
#######################################

import requests
from lxml import html

base_url = 'http://results.vtu.ac.in/vitavi.php?rid='

def rolno():
    usn = raw_input('Enter your usn: ')
    if len(usn) == 10:
        complete_url = base_url+usn+'&submit=SUBMIT'
        response = requests.get(complete_url)
        text = html.fromstring(response.text)
        print_marks(text)    
    else :
        print "Invalid USN"

def print_marks(html_data):
    subjects = html_data.xpath('//i/text()')
    marks = html_data.xpath('//td[@width=60][@align="center"]/text()')
    student_details = html_data.xpath('//b/text()')
    t_marks = html_data.xpath('//td/text()')
    total_marks = int(t_marks[61])
    student_name = student_details[0]
    semester = int(student_details[2])
    result = student_details[3].encode('ascii','ignore')
    print "Name : "+student_name
    print "Semester: ",semester
    print "Marks format is : Subject Name / Internal / External / Total"
    if subjects:
        internal = marks[5::3]
        external = marks[4::3]
        total = marks[6::3]        
        for i,j,k,l in zip(subjects, internal, external, total):
            print i,j,k,l
        print "Total Marks = ",total_marks
        if semester == 8:
            print "Average = ",round(float(total_marks * 100)/750, 2)
        elif semester == 1 or semester == 2:
            print "Average = ",round(float(total_marks * 100)/775, 2)
        else:
            print "Average = ",round(float(total_marks * 100)/900, 2)
        print "Result = "+result[8:]    
    else:
        print "Enter a Valid USN"
    
if __name__ == '__main__':
    rolno()
    
    
