#copy dataset into current directory
cp ../all_6327.csv .
#grep chromosomes from dataset file and make separate file for each chromosome
grep -w "1" all_6327.csv > 1.csv
grep -w "2" all_6327.csv > 2.csv
grep -w "3" all_6327.csv > 3.csv
grep -w "6" all_6327.csv > 6.csv
grep -w "7" all_6327.csv > 7.csv
grep -w "8" all_6327.csv > 8.csv
grep -w "9" all_6327.csv > 9.csv
grep -w "10" all_6327.csv > 10.csv
grep -w "11" all_6327.csv > 11.csv
grep -w "12" all_6327.csv > 12.csv
grep -w "13" all_6327.csv > 13.csv
grep -w "15" all_6327.csv > 15.csv
grep -w "16" all_6327.csv > 16.csv
grep -w "17" all_6327.csv > 17.csv
grep -w "19" all_6327.csv > 19.csv
grep -w "22" all_6327.csv > 22.csv
grep -w "23" all_6327.csv > 23.csv 

sh cat.sh

# remove dataset file from the workdirectory
rm all_6327.csv
#run the image conversion script
python data_image_gen.py
#make csv directory for chromosome files and move them
mkdir csv_files
mv *.csv csv_files
#make png directory for images and move all images in the folder
mkdir png_files
mv *.png png_files