

2# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:26:25 2024

@author: OEM
""" 
# This is a code written for the purpose of extracting information from a
# Gaussian output and use that information to calculate the B-N bond 
# dissociation energy of amine boranes using Hess's law.

# The bond dissociation along the B-N bond is given as
# ANx-BH3 >>> ANx + BH3

# Function to extract 'Sum of electronic and thermal Enthalpies' from Gaussian output file

def extract_enthalpy(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'Sum of electronic and thermal Enthalpies' in line:
                # Extract the value after the "=" sign and convert it to float
                enthalpy = float(line.split('=')[1].strip())
                return enthalpy
    return None

# File paths for the Gaussian output files
MPBH3_file = 'MPBH3.out'
MP_file = 'MP.out'
BH3_file = 'BH3.out'

# Extracting enthalpy values from Gaussian output files
MPBH3_enthalpy = extract_enthalpy(MPBH3_file)
MP_enthalpy = extract_enthalpy(MP_file)
BH3_enthalpy = extract_enthalpy(BH3_file)

# Check if enthalpy values are successfully extracted
if MPBH3_enthalpy is not None and MP_enthalpy is not None and BH3_enthalpy is not None:
    # Calculate the B-N bond dissociation energy
    bond_dissociation_energy = round((((MP_enthalpy + BH3_enthalpy) - MPBH3_enthalpy)*2625.5),1)

    # Print the result
    print(f"B-N Bond Dissociation Energy: {bond_dissociation_energy} kJ/mol")
else:
    print("Error: Unable to extract enthalpy values from one or more file'')




