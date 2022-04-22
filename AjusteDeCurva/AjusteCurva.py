from multiprocessing.connection import wait
import matplotlib.pyplot as plt;
import subprocess
import time

x = [];
y = [];
xa = [];
ya = [];
r2 = 0;

cSharpPath = "C:\\Users\\wesle\\Documents\\Programming\\CSharp\\MatlabCodes";
command = "dotnet run"
# execute the command
process = subprocess.Popen(command, cwd=cSharpPath, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

time.sleep(3)

# each line of the file is an array separated by a space, read the file and store the data in the arrays
with open('Ajuste.txt', 'r') as file:
     filedata = file.readlines()
     x = filedata[0].split()
     y = filedata[1].split()
     xa = filedata[2].split()
     ya = filedata[3].split()
     r2 = filedata[4].split()

# change type of the data to float
x = [float(i) for i in x] 
y = [float(i) for i in y]
xa = [float(i) for i in xa]
ya = [float(i) for i in ya]
#remove ' from r2
r2 = r2[0].replace("'", "")

print(x)
print(y)
print(xa)
print(ya)
print(r2)

# add r2 to the plot left
plt.title('R2 = ' + str(r2), loc='left')
plt.plot(x, y,'*b', xa, ya, '-r');
plt.show()