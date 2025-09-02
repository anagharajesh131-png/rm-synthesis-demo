# RM Synthesis on Synthetic Data

This repository contains the workflow I used for experimenting with **Rotation Measure (RM) synthesis** on synthetic polarized data.

## Repository Contents
- `make_synthetic_data.py` → Python script to generate synthetic data  
- `commands.txt` → text file with the exact CMD commands I used to  
  - generate synthetic data from the script  
  - run RM synthesis using RM-Tools  
- `do_RMsynth_1D.py` → script used for performing RM synthesis  
- Output plots (`.pdf`) → example figures generated from my run  

## Important Note
This repository is **not a replacement for RM-Tools**.  
It only contains the scripts and commands I personally used.  

If you want to **install RM-Tools** or learn more about its modules, please visit the official repository:  
👉 [CIRADA-Tools/RM-Tools on GitHub](https://github.com/CIRADA-Tools/RM-Tools)

## Acknowledgement
This work makes use of **RM-Tools**.  
Please cite RM-Tools as directed in their repository if you use it in research.

## How to Reproduce
1. Generate synthetic data:
   ```bash
   python make_synthetic_data.py
2.Run RM synthesis (with RM-Tools installed):   
python do_RMsynth_1D.py data/synthetic_data.txt -S



   The resulting plots will be saved in the outputs (two example PDFs are included in this repository).
