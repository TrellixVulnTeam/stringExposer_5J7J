# stringExposer

## About
This is to look through malware sting dumps to ID anything interesting. Windows API calls are mapped. With the discovered API calls, you can goto malapi.io and map them. 

It will then extract any potential IoC's from the list of strings that can be used for further pivoting. These will be saved as a dataframe. 

## Usage
Save the floss output into the main directory of this project and call it strings.txt. 

Then execute using python3 stringExposer.py

Check the iocList.csv for complete output of IoCs. 



