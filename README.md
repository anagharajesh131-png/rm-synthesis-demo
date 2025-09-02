RM-Synthesis Workflow with Test Data

This repository documents the steps I followed to generate synthetic polarization data and process it with RM-Tools using RM-Synthesis and RM-CLEAN.

It is intended as a personal reference for learning and reproducing the workflow.

1. Workflow Overview

Generate test data using the provided catalogue.csv.

Run RM-Synthesis on each synthetic source.

Apply RM-CLEAN to refine the Faraday spectra.

Outputs include ASCII data files, plots, and cleaned spectra for each source.

2. Repository Contents

rmsynthesis_pipeline.py → Python script that runs the full pipeline automatically (test data generation + RM-Synthesis + RM-CLEAN).

Example CMD commands → For users who prefer running the steps manually.

This README.md → Instructions and documentation.

3. Requirements

Python 3

RM-Tools installed (official package)

catalogue.csv (example source catalogue, provided in cats/)

4. Option 1: Run Step by Step (CMD)

# Generate 8 test sources:

python mk_test_ascii_data.py cats\catalogue.csv -c 1024 -n 0.01


# Run RM-Synthesis and RM-CLEAN for all 8 sources:

python do_RMsynth_1D.py data\Source1.dat
python do_RMclean_1D.py data\Source1.dat

python do_RMsynth_1D.py data\Source2.dat
python do_RMclean_1D.py data\Source2.dat

...
python do_RMsynth_1D.py data\Source8.dat
python do_RMclean_1D.py data\Source8.dat

5. Option 2: Run Entire Workflow with Python

# Instead of typing commands one by one, you can run everything at once:

python rmsynthesis_pipeline.py


This script will:

Create the test dataset in data/

Run RM-Synthesis + RM-CLEAN for all 8 sources

Save the outputs automatically

⚠️ Important Note

This repository is not a replacement for RM-Tools.
It only contains the scripts and commands I personally used.

If you want to install RM-Tools or learn more about its modules, please visit the official repository:
👉 https://github.com/CIRADA-Tools/RM-Tools/wiki/RMsynth1D

🙏 Acknowledgement

This work makes use of RM-Tools.
If you use RM-Tools in your research, please cite it as directed in their official repository.
