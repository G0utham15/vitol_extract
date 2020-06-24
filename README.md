# vitol_extract
[![CodeFactor](https://www.codefactor.io/repository/github/g0utham15/vitol_extract/badge)](https://www.codefactor.io/repository/github/g0utham15/vitol_extract)

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
* Check_again.csv - Contains Path to files which needs manual verification
* Details.csv - Contains all the details like Reg. No, Name, Certificate ID, Marks, Grade
* Duplicates.csv - Contains the duplicate certificate ID which needs verification