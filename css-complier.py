import os
import time
Files = os.listdir() ## Gets all files in directory
print("Enter output Name (without extension)") 
Final = open(input() + ".css", "w") ## Asks for output file name

for FileName in Files: ## Loops files
    if (".css" in FileName): ## Checks if .css
        f = open(FileName, "r") ## Opens file
        file_lines = f.read() ## Reads file
        Final.write(file_lines) ## Writes data into output file
        f.close() ## Close read file
        
Final.close() ## Close output file
print("Completed") ## Prompt
time.sleep(2) ## Delay


