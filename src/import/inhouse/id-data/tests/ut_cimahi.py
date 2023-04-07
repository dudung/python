import id_data.jawabarat.cimahi.cimahiselatan as cims
import id_data.jawabarat.cimahi.cimahitengah as cimt
import id_data.jawabarat.cimahi.cimahiutara as cimu

print("Cimahi Selatan population in 2021")
print(cims.population['2021'])
print()

print("Cimahi Tengah population in 2021")
print(cimt.population['2021'])
print()

print("Cimahi Utara population in 2021")
print(cimu.population['2021'])
print()

print("Cimahi Selatan PDRB ADHK sector A in 2016")
print(cims.pdrb_adhk['A']['2016'])
print()

print("Cimahi Selatan PDRB ADHK sector C in 2016")
print(cims.pdrb_adhk['C']['2016'])
print()

print("Cimahi Selatan PDRB ADHK sector C in 2017")
print(cims.pdrb_adhk['C']['2017'])
print()


"""
$ python -m tests.ut_cimahi
Cimahi Selatan population in 2021
240990000

Cimahi Tengah population in 2021
161758000

Cimahi Utara population in 2021
165652000

Cimahi Selatan PDRB ADHK sector A in 2016
32366200000.0

Cimahi Selatan PDRB ADHK sector C in 2016
8626902500.0

Cimahi Selatan PDRB ADHK sector C in 2017
8983519100.0

"""
