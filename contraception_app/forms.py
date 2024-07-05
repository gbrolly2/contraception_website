# forms.py
from django import forms

class QuestionnaireForm(forms.Form):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
        #choices for 12-16
    YES_NO_PREFER_NOT_TO_ANSWER_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('prefer_not_to_answer', 'Prefer not to answer')
    ]

    # Choices for question 17 
    YES_NO_NO_PREFERENCE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('no_preference', 'No Preference')
    ]
    
    QUESTION4_CHOICES = [
        ('a', '35 years or older and smoke'),
        ('b', 'High blood pressure'),
        ('c', 'Blood clotting in your legs, lungs, brain or anywhere else'),
        ('d', 'Inherited clotting disorder of any kind'),
        ('e', 'Lupus with positive or unknown antibodies'),
        ('f', 'Valvular heart disease'),
        ('g', 'Active breast cancer, or uterine or endometrial cancer'),
        ('h', 'Migraine with aura'),
        ('i', 'Liver disease'),
        ('j', 'None of the above'),
    ]

    QUESTION20_CHOICES = [
        ('a', 'Effective, dependable birth control'),
        ('b', 'Easy to hide (from parents, roommates, friends, caregivers, etc.)'),
        ('c', 'Ready in the heat of the moment'),
        ('d', 'Long-standing'),
        ('e', 'Low maintenance'),
        ('f', 'Want hormone therapy to reduce symptoms of heavy painful periods'),
        ('g', 'Accessible without a clinical appointment or coming to the doctor\'s office.'),
        ('h', 'None of the above'),
    ]

    question1 = forms.ChoiceField(label='1. Have you given birth in the last 6 weeks?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question2 = forms.ChoiceField(label='2. Are you currently breastfeeding?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question3 = forms.ChoiceField(label='3. Have you given birth in the past 6 months?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question4 = forms.MultipleChoiceField(label='4. Do you have any of the following history? (Select multiple if applicable)', choices=QUESTION4_CHOICES, widget=forms.CheckboxSelectMultiple)
    question5 = forms.ChoiceField(label='5. History of seizure disorder?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question6 = forms.ChoiceField(label='6. Do you take either of the following Carbamazepine/Phenytoin?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question7 = forms.ChoiceField(label='7. History of irritable bowel disease, Crohn\'s disease or Ulcerative colitis?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question8 = forms.ChoiceField(label='8. History of diabetes?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question9 = forms.ChoiceField(label='9. Do you have a copper allergy?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question10 = forms.ChoiceField(label='10. Do you have an allergy to silicone?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question11 = forms.ChoiceField(label='11. Have you ever been diagnosed with an anatomical abnormality of the uterus?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question12 = forms.ChoiceField(label='12. Have you ever been diagnosed with a pelvic infection (PID)?', choices=YES_NO_PREFER_NOT_TO_ANSWER_CHOICES, widget=forms.RadioSelect)
    question13 = forms.ChoiceField(label='13. Do you have a current sexually transmitted infection (STI)?', choices=YES_NO_PREFER_NOT_TO_ANSWER_CHOICES, widget=forms.RadioSelect)
    question14 = forms.ChoiceField(label='14. Have you ever been diagnosed with cervical cancer?', choices=YES_NO_PREFER_NOT_TO_ANSWER_CHOICES, widget=forms.RadioSelect)
    question15 = forms.ChoiceField(label='15. Do you have a history of HIV/AIDs?', choices=YES_NO_PREFER_NOT_TO_ANSWER_CHOICES, widget=forms.RadioSelect)
    question16 = forms.ChoiceField(label='16. Are you on hormone replacement therapy for gender-affirming care?', choices=YES_NO_PREFER_NOT_TO_ANSWER_CHOICES, widget=forms.RadioSelect)
    question17 = forms.ChoiceField(label='17. Do you prefer hormonal birth control methods?', choices=YES_NO_NO_PREFERENCE_CHOICES, widget=forms.RadioSelect)
    question18 = forms.ChoiceField(label='18. Do you have any interest in getting your tubes tied?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question19 = forms.ChoiceField(label='19. Are you consistent with taking daily pills?', choices=YES_NO_CHOICES, widget=forms.RadioSelect)
    question20 = forms.MultipleChoiceField(label='20. Check off what is most important to you (choose as many as you want)', choices=QUESTION20_CHOICES, widget=forms.CheckboxSelectMultiple)
