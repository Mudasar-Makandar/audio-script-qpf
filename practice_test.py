from fingerprint import ReferenceFingerprint, QueryFingerprint
from db import *

'''
db = QfpDB()
fp_r = ReferenceFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/CLOVER-2000.WAV")
fp_r.create()
db.store(fp_r, "CLOVER2")

fp_r = ReferenceFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/Japanese Slot Machine (XSL).ogg")
fp_r.create()
db.store(fp_r, "SLOT-MACHINE")

fp_r = ReferenceFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/PACTOR-III_14.WAV")
fp_r.create()
db.store(fp_r, "PACTOR")

fp_r = ReferenceFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/STANAG 4285_p10.mp3")
fp_r.create()
db.store(fp_r, "STANAG")

fp_r = ReferenceFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/Volmet_HKG.wav")
fp_r.create()
db.store(fp_r, "VOLMET")
'''
db_file = sqlite3.connect("qfp.db")
ce = db_file.cursor()
ce.execute("""SELECT * FROM Records;""")
print(ce.fetchall())

fp_q = QueryFingerprint("/home/mudassar/Mudassar/work/Freelance/qpf/audio_files/Volmet_HKG.wav")
fp_q.create1()
db = QfpDB(db_path="qfp.db")
db.query(fp_q)
print(fp_q.matches)
