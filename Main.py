'''
Karvonen-Formel und Edwards-Belastungszonen-Kalkulator
(c) Kurt Höblinger aka NitricWare

v0.1
'''

import math

print("Karvonen 1.0")
print("(c) Kurt Höblinger aka NitricWare")
print()

age = 0
hfmin = 0

while (age == 0):
    try:
        age = int(input("Alter in Jahre: "))
    except ValueError:
        print ("Kein valides Alter...")

while (hfmin == 0):
    try:
        hfmin = int(input("Ruhepuls: "))
    except ValueError:
        print ("Kein valider Ruhepuls...")

hfmax = 220 - age

hftrain_int = math.ceil(((hfmax - hfmin) * 0.8) + hfmin)
hftrain_ext = math.ceil(((hfmax - hfmin) * 0.6) + hfmin)
hftrain_nor = math.ceil(((hfmax - hfmin) * 0.5) + hfmin)

edw_a_low = math.ceil(hfmin + (hfmax - hfmin) * 0.5)
edw_a_high = math.ceil(hfmin + (hfmax - hfmin) * 0.6)

edw_b_high = math.ceil(hfmin + (hfmax - hfmin) * 0.7)

edw_c_high = math.ceil(hfmin + (hfmax - hfmin) * 0.8)

edw_d_high = math.ceil(hfmin + (hfmax - hfmin) * 0.9)

edw_e = math.ceil(hfmin + (hfmax - hfmin))

print()
print("HF(max) ist: " + str(hfmax))
print()
print("Trainingsfrequenz (intensives Ausdauertraining) ist: " + str(hftrain_int) + "bpm")
print("Trainingsfrequenz (extensives Ausdauertraining) ist: " + str(hftrain_ext) + "bpm")
print("Trainingsfrequenz (untrainierter Mensch) ist: " + str(hftrain_nor) + "bpm")
print()
print("Ihre Belastungszonen nach Edwards:")
print()
print("Gesundheitzone: " + str(edw_a_low) + "bpm - " + str(edw_a_high) + "bpm")
print("Fettstoffwechselzone: " + str(edw_a_high) + "bpm - " + str(edw_b_high) + "bpm")
print("Aerobe Zone: " + str(edw_b_high) + "bpm - " + str(edw_c_high) + "bpm")
print("Anaerobe Zone: " + str(edw_c_high) + "bpm - " + str(edw_d_high) + "bpm")
print("Wettkampfspezifische Ausdauerzone: " + str(edw_d_high) + "bpm - " + str(edw_e) + "bpm")
