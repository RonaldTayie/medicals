# doctortypes =["Allergy and immunology","Anesthesiology","Dermatology","Diagnostic radiology","Emergency medicine","Family medicine","Internal medicine","Medical genetics","Neurology","Nuclear medicine","Obstetrics and gynecology","Ophthalmology","Pathology","Pediatrics","Physical medicine and rehabilitation","Preventive medicine","Psychiatry","Radiation oncology","Surgery","Urology"]


<!-- HOLD -->

@api_view(['GET'])
def search_doctor(request):

    all_doctors = Doctor.objects
    doctors = []
    for k,vals in request.GET.lists():
        for v in vals:
            print('%s:%s'%(k,v))
        model = all_doctors.filter(**{k: v})
        doctors.append(model)
    # first get all user in the doctor user group
    
    return Response(doctors)