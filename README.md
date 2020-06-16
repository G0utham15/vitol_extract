# vitol_extract
Extract details from pdf certificate 

Run the code in the following sequence:

```
conda create -n venv python
conda activate venv

conda install -c conda-forge poppler
pip3 install -r requirements.txt

python3 main.py
Give the folder path as input after running last step
```

## Output 
We finally get 3 CSV Files
1. Check_again.csv - Contains Path to files which have to be verified again
2. Details.csv - Contains all the details like Reg. No, Name, Certificate ID, Marks, Grade
3. Duplicates.csv - Contains the duplicate certificate ID which needs to be verified again 