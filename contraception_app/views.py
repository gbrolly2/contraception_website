from django.shortcuts import render
from .forms import QuestionnaireForm

#categories for results 

# iud 
# copper_iud 
# combined_oral_hormonal
# progesterone_only_hormonal 
# progesterone_only_oral_hormonal - nexplanon and depo-provera 
# sterilization 
# emergency 
# cervical_caps_and_diaphragms 
# fam 
# condoms  
# internal_condoms
# spermicide_or_vaginal_sponge
# pulling_out 
# abstinence 
# patch 
# ring 

NAME_MAPPING = {
    'iud': 'Hormonal IUD',
    'copper_iud': 'Copper IUD',
    'combined_oral_hormonal': 'Combined Hormonal Oral Contraception',
    'nexplanon': 'Nexplanon Contraceptive Implant',
    'depo-provera': 'Depo-Provera Contraceptive Injection',
    'progesterone_only_oral_hormonal': 'Progesterone Only Oral Contraception',
    'sterilization': 'Tubal Ligation (Sterilization)',
    'emergency': 'Emergency Contraception',
    'cervical_caps_and_diaphragms': 'Cervical Cap or Diaphragm',
    'fam': 'Family Planning',
    'condoms': 'Condoms',
    'internal_condoms': 'Internal Condoms',
    'spermicide_or_vaginal_sponge': 'Spermicide or Vaginal Sponge',
    'pulling_out': 'Pulling Out',
    'abstinence': 'Abstinence',
    'patch': 'Birth Control Patch',
    'ring': 'Vaginal Ring',
}

#logic for results
def calculate_total(question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20):

    #add a section if the user does not answer all the questions so they are prompted to complete them all
   # Define the list of questions
    questions = [
    question1, question2, question3, question4, question5, question6,
    question7, question8, question9, question10, question11, question12,
    question13, question14, question15, question16, question17, question18,
    question19, question20
]

# Check if any question is not answered
    unanswered_questions = [
    f'Question {i+1}' for i, q in enumerate(questions) if q == ''
]

    if unanswered_questions:
        prompt = 'Please complete the following questions:'
        print(f"{prompt}, {unanswered_questions}")

        
    #dictionary for the results

    results = {
        'iud': 0,
        'copper_iud': 0,
        'combined_oral_hormonal': 0,
        'nexplanon': 0,
        'depo-provera': 0,
        'progesterone_only_oral_hormonal': 0,
        'sterilization': 0,
        'emergency': 0,
        'cervical_caps_and_diaphragms': 0,
        'fam': 0,
        'condoms': 0,
        'internal_condoms': 0,
        'spermicide_or_vaginal_sponge': 0,
        'pulling_out': 0,
        'abstinence': 0,
        'patch': 0,
        'ring': 0
    }

    conditions = [
        (question1, ['combined_oral_hormonal', 'patch', 'ring']),
        (question2, ['combined_oral_hormonal', 'patch', 'ring']),
        (question3, ['fam']),
       # (question4 != 'j', ['combined_oral_hormonal', 'patch', 'ring']),
        (question5, ['combined_oral_hormonal', 'patch', 'ring']),
        (question6, ['combined_oral_hormonal', 'patch', 'ring']),
        (question7, ['combined_oral_hormonal', 'patch', 'ring']),
        (question8, ['combined_oral_hormonal', 'patch', 'ring']),
        (question9, ['copper_iud']),
        (question10, ['cervical_caps_and_diaphragms']),
        (question11, ['iud', 'copper_iud']),
        (question12, ['copper_iud']),
        (question13, ['copper_iud']),
        (question14, ['cervical_caps_and_diaphragms']),
        (question15, ['cervical_caps_and_diaphragms']),
        (question16, ['fam']),
        
    ]
    
    if question17 == 'yes':
        results['combined_oral_hormonal'] += 10
        results['patch'] += 10
        results['ring'] += 10
        results['nexplanon'] += 10
        results['depo-provera'] += 10
        results['progesterone_only_oral_hormonal'] += 10
        results['iud'] += 10

    if question18 == 'yes':
        results['sterilization'] += 25
    else:
        results['sterilization'] = -1
    
    if 'a' in question20:
        results['iud'] += 1
        results['copper_iud'] += 1
        results['nexplanon'] += 1
       # results['sterilization'] += 1
        results['abstinence'] += 1

    if 'b' in question20:
        results['iud'] += 1
        results['copper_iud'] += 1
      #  results['sterilization'] += 1
        results['nexplanon'] += 1
        results['depo-provera'] += 1
        

    if 'c' in question20:
        results['iud'] += 1
        results['copper_iud'] += 1
        results['nexplanon'] += 1
        results['depo-provera'] += 1
        results['patch'] += 1
        results['condoms'] += 1
        results['internal_condoms'] += 1
      #  results['sterilization'] += 1
        results['ring'] += 1

    if 'd' in question20:
        results['iud'] += 1
        results['copper_iud'] += 1
        results['nexplanon'] += 1
    #    results['sterilization'] += 1

    if 'e' in question20:
        results['iud'] += 1
        results['copper_iud'] += 1
        results['nexplanon'] += 1
        results['depo-provera'] += 1
    #    results['sterilization'] += 1

    if 'f' in question20:
        results['iud'] += 1
        results['progesterone_only_oral_hormonal'] += 1
        results['nexplanon'] += 1
        results['depo-provera'] += 1

    if 'g' in question20:
        results['emergency'] += 1
        results['pulling_out'] += 1
        results['fam'] += 1
        results['condoms'] += 1
        results['internal_condoms'] += 1
        results['spermicide_or_vaginal_sponge'] += 1
    
    if 'h' in question20:
        #do nothing
        pass


    
    for condition, options in conditions:
        if condition == 'yes':
            for option in options:
                results[option] = -1

    if any(letter in question4 for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']):
        results['combined_oral_hormonal'] = -1
        results['patch'] = -1
        results['ring'] = -1
        
    if question19 == 'no':
        results['combined_oral_hormonal'] = -1
        results['progesterone_only_oral_hormonal'] = -1
    

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # sorted_results = [(method, score) for method, score in sorted_results if score != -1]
    sorted_results = [NAME_MAPPING[method] for method, score in sorted_results if score != -1]

    return sorted_results


#view for the questionnaire return the sorted_results dictionary
def questionnaire(request):

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            sorted_results = calculate_total(
                cleaned_data['question1'],
                cleaned_data['question2'],
                cleaned_data['question3'],
                cleaned_data['question4'],
                cleaned_data['question5'],
                cleaned_data['question6'],
                cleaned_data['question7'],
                cleaned_data['question8'],
                cleaned_data['question9'],
                cleaned_data['question10'],
                cleaned_data['question11'],
                cleaned_data['question12'],
                cleaned_data['question13'],
                cleaned_data['question14'],
                cleaned_data['question15'],
                cleaned_data['question16'],
                cleaned_data['question17'],
                cleaned_data['question18'],
                cleaned_data['question19'],
                cleaned_data['question20']
                
            )

            return render(request, 'results.html', {'form': form, 'sorted_results': sorted_results})
    else:
        form = QuestionnaireForm()

    return render(request, 'questionnaire.html', {'form': form})

#view for the results page printint out the sorted_results dictionary from the questionnaire view after the submit button is clicked 
def results(request):
    
        sorted_results = calculate_total(
            request.POST.get('question1'),
            request.POST.get('question2'),
            request.POST.get('question3'),
            request.POST.get('question4'),
            request.POST.get('question5'),
            request.POST.get('question6'),
            request.POST.get('question7'),
            request.POST.get('question8'),
            request.POST.get('question9'),
            request.POST.get('question10'),
            request.POST.get('question11'),
            request.POST.get('question12'),
            request.POST.get('question13'),
            request.POST.get('question14'),
            request.POST.get('question15'),
            request.POST.get('question16'),
            request.POST.get('question17'),
            request.POST.get('question18'),
            request.POST.get('question19'),
            request.POST.get('question20')
            
        )
    
        return render(request, 'results.html', {'sorted_results': sorted_results})

