import csv
import os
import random

questions = {
    "Physics": [
        ("Mechanics","According to Newton's second law, force is equal to:","Mass × Acceleration","Mass × Velocity","Weight","Momentum","A"),
        ("Mechanics","The SI unit of force is:","Newton","Joule","Pascal","Watt","A"),
        ("Current Electricity","Ohm's law states that current is directly proportional to:","Resistance","Voltage","Power","Charge","B"),
        ("Current Electricity","Unit of resistance is:","Volt","Ampere","Ohm","Henry","C"),
        ("Thermodynamics","Heat naturally flows from:","Cold body to hot body","Hot body to cold body","Higher pressure to lower pressure","Vacuum to matter","B"),
        ("Optics","The unit of power of a lens is:","Dioptre","Newton","Lux","Candela","A"),
        ("Modern Physics","Electron was discovered by:","Rutherford","Bohr","J.J. Thomson","Chadwick","C"),
        ("Waves","Speed of sound is maximum in:","Air","Water","Steel","Vacuum","C"),
        ("Gravitation","Acceleration due to gravity on Earth is approximately:","8.9 m/s²","9.8 m/s²","10.8 m/s²","11.8 m/s²","B"),
        ("Kinematics","Velocity is defined as:","Distance per unit time","Displacement per unit time","Acceleration per unit time","Force per unit mass","B")
    ],

    "Chemistry":[
        ("Atomic Structure","Atomic number represents:","Neutrons","Electrons+Neutrons","Protons","Mass number","C"),
        ("Chemical Bonding","Ionic bond is formed by:","Sharing electrons","Transfer of electrons","Sharing protons","Transfer of neutrons","B"),
        ("Periodic Table","Fluorine belongs to group:","16","17","18","1","B"),
        ("Organic Chemistry","Methane has molecular formula:","CH2","CH4","C2H6","CH3OH","B"),
        ("Solutions","pH of neutral water is:","5","6","7","8","C"),
        ("Redox","Oxidation is:","Gain of electrons","Loss of electrons","Gain of neutrons","Loss of protons","B"),
        ("Thermochemistry","SI unit of energy is:","Newton","Pascal","Joule","Watt","C"),
        ("States of Matter","Ideal gas equation is:","PV=nRT","P=nRT","V=nRT","PV=RT","A"),
        ("Electrochemistry","Cathode is the electrode where:","Oxidation occurs","Reduction occurs","Melting occurs","Combustion occurs","B"),
        ("Biomolecules","Glucose is a:","Protein","Carbohydrate","Lipid","Vitamin","B")
    ],

    "Botany":[
        ("Cell","Powerhouse of cell is:","Nucleus","Ribosome","Mitochondria","Golgi body","C"),
        ("Plant Physiology","Photosynthesis occurs in:","Mitochondria","Chloroplast","Nucleus","Ribosome","B"),
        ("Plant Kingdom","Bryophytes are called:","Amphibians of plant kingdom","Flowering plants","Seed plants","Gymnosperms","A"),
        ("Morphology","Stomata help in:","Photosynthesis only","Gas exchange","Reproduction","Seed formation","B"),
        ("Genetics","DNA stands for:","Deoxyribonucleic Acid","Ribonucleic Acid","Dynamic Nuclear Acid","None","A"),
        ("Ecology","Green plants are:","Consumers","Producers","Decomposers","Parasites","B"),
        ("Reproduction","Double fertilization occurs in:","Gymnosperms","Angiosperms","Algae","Bryophytes","B"),
        ("Anatomy","Xylem transports:","Food","Water","Hormones","Oxygen","B"),
        ("Anatomy","Phloem transports:","Water","Minerals","Food","Nitrogen","C"),
        ("Biotechnology","PCR is used for:","Protein synthesis","DNA amplification","Photosynthesis","Respiration","B")
    ],

    "Zoology":[
        ("Human Physiology","Largest organ in human body is:","Brain","Liver","Skin","Heart","C"),
        ("Digestion","Enzyme present in saliva is:","Pepsin","Trypsin","Amylase","Lipase","C"),
        ("Respiration","Gas exchanged in lungs is:","Nitrogen","Carbon dioxide and Oxygen","Helium","Hydrogen","B"),
        ("Circulation","Normal human heart has:","2 chambers","3 chambers","4 chambers","5 chambers","C"),
        ("Genetics","Father of Genetics is:","Darwin","Mendel","Watson","Morgan","B"),
        ("Evolution","Theory of natural selection was proposed by:","Mendel","Darwin","Lamarck","Morgan","B"),
        ("Animal Kingdom","Earthworm belongs to phylum:","Arthropoda","Annelida","Chordata","Mollusca","B"),
        ("Biomolecules","Basic unit of protein is:","Fatty acid","Amino acid","Glucose","Nucleotide","B"),
        ("Human Health","Insulin is secreted by:","Liver","Pancreas","Kidney","Heart","B"),
        ("Neural Control","Functional unit of nervous system is:","Neuron","Nephron","Alveolus","Osteon","A")
    ]
}

rows=[]
qid=1

for subject,data in questions.items():
    for chapter,question,a,b,c,d,ans in data:
        rows.append({
            "QuestionID":f"Q{qid:04d}",
            "Subject":subject,
            "Chapter":chapter,
            "Difficulty":random.choice(["Easy","Medium","Hard"]),
            "Question":question,
            "OptionA":a,
            "OptionB":b,
            "OptionC":c,
            "OptionD":d,
            "CorrectAnswer":ans
        })
        qid+=1

os.makedirs("data",exist_ok=True)

with open("data/questions.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=[
        "QuestionID","Subject","Chapter","Difficulty",
        "Question","OptionA","OptionB","OptionC","OptionD","CorrectAnswer"
    ])
    writer.writeheader()
    writer.writerows(rows)

print("✅ data/questions.csv generated successfully!")