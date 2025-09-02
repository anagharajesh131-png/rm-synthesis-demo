"""
rmsynthesis_pipeline.py

This script demonstrates how to:
1. Generate test data using the catalogue file
2. Perform RM-synthesis
3. Apply RM-CLEAN
for all 8 synthetic sources created from mk_test_ascii_data.py.

Requirements:
- RM-Tools installed
- Catalogue file: cats/catalogue.csv
"""

import os
import subprocess

# ------------------------------
# Step 1: Generate synthetic test data
# ------------------------------
print(">>> Generating synthetic test data...")

subprocess.run([
    "python", "mk_test_ascii_data.py",
    "cats/catalogue.csv",
    "-c", "1024",
    "-n", "0.01"
])

print(">>> Test data created in 'data/' folder.")

# ------------------------------
# Step 2: Run RM-synthesis + RM-CLEAN for all 8 sources
# ------------------------------
print(">>> Running RM-synthesis and RM-CLEAN...")

for i in range(1, 9):
    source_file = f"data/Source{i}.dat"

    print(f"\n--- Processing {source_file} ---")

    # RM-synthesis
    subprocess.run([
        "python", "do_RMsynth_1D.py",
        source_file,
        "-S"
    ])

    # RM-CLEAN
    subprocess.run([
        "python", "do_RMCLEAN_1D.py",
        source_file,
        "-p"
    ])

print("\n>>> All sources processed successfully!")
print("Check the output plots and cleaned Faraday spectra in your working directory.")

