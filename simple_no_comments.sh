#!/bin/bash

echo "One course Alta3 Research offers is..."

altacourses[0]="Python Essentials (5 days)"
altacourses[1]="Terraform Essentials (4 days)"
altacourses[2]="Kubernetes CKA Exam Prep"
altacourses[3]="Git and GitHub Training (2 days)"
altacourses[4]="Generative AI Building and Training LLM Models (4 days)"
altacourses[5]="SIP and VoIP Essentials (5 days)"


array_length=${#altacourses[@]} 
index=$(($RANDOM % $array_length))

echo ${altacourses[$index]}

