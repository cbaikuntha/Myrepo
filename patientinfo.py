patient_dict={}

@post('/ZeOmega/<idn>')
def AddPatient(idn):
    idn=request.POST['idn']
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']
    Details=','.join([name,email,address,phone])
    patient_dict.update({idn:Details})
    return 	patient_dict
	

		
@put('/ZeOmega/<idn>')
def Update(idn):
	if idn in patient_dict.keys():
	    idn=request.POST['idn']
	    name=request.POST['name']
	    email=request.POST['email']
	    address=request.POST['address']
	    phone=request.POST['phone']
	    Details=','.join([name,email,address,phone])
	    patient_dict.update({idn:Details})
	    return 	patient_dict
	    
	
@delete('/ZeOmega/<idn>')
def rmv_patient(idn):
	if idn in patient_dict.keys():
		del(patient_dict[idn])
		return patient_dict
	else:
		return 'no record found'
		
@get('/ZeOmega/<idn>')
def PatientInfo(idn):
	return template('<b> {{patient_dict[idn]}}',patient_dict=patient_dict,idn=idn)
	
run(host='localhost',port=8080)
