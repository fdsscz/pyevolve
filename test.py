import subprocess;
import os
n = 5;
filename = 'pyevolve.ap'
for i in range(n,n+10):
	path = "/kern3.16_base/dbserver-sdc1-ext4-run-" + str(i);
	path = path.replace("/","\/")
	subprocess.call(['sed', '-i', "s/VAR BASE_RESULTS_DIR\=[^ ]*/VAR BASE_RESULTS_DIR\="+path+"/g", filename])
	subprocess.call(["auto-pilot", "py_main.ap"], stdout=open(os.devnull,'w'), stderr=subprocess.STDOUT)
