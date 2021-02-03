mkdir /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/test_found

python test.py

rm /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/test_found/._*

python highlight.py

cp results_proc.py /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/png_files/
rm /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/._*
python /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/png_files/results_proc.py
rm /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/png_files/results_proc.py

rm -fr /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/test_found
#rm -fr /Volumes/MY_PASSPORT/JRF/cancer_genome/cancer/csv_files
