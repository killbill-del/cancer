# Converting cancer mutation information to image

## Introduction:
- Lines about the importance of the project


*There are multiple steps involved in the process*

## Steps:
### Step 0:
 - Unzip the folder in the work directory
 - cd cancer

### Step 1:
#### System requirements:
1. Python 3.5 or higher
2. Pandas
3. PIL
4. Numpy
 - To install all the packages either use environment.yml or install them separately
  - Change the location on line 11 of environment.yml before use
  - Run: conda env create -f environment.yml

### Step 2:
 - After satisfying all the system requirements, change paths in all the sh, py files in your working directory.
   - open data_image_gen.py, test.py, sc.sh, result_proc.py, result_proc.sh, highlight.py
   - change all the work directory locations
   - **do not remove test_file folder from the workdirectory after unzip** 
 - To generate dataset image
   - **sh sc.sh**
    - It will generate individual csv (within csv_files) and png (within png_files) files for each chromosome and a combined dataset image in your working directory.
 - To generate result image with highlighted query
   - **sh result_proc.sh**
    - it will generate a final_result image in png_files folder within your working directory.

##### Note: Keep all the scripts in your working folder.