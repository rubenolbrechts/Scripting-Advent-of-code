#!/usr/bin/python3

with open("Commands.txt") as f:
    data = f.read()
data = data.split("\n")
data.pop()

file_sys = {}
file_sys_size = {}
current_dir = []
dirs = ""
cd = 1
for dat in data:
    dat = dat.split()
    if cd == 1:
        if dat[0] == "$":
            if dat[1] == "cd" and dat[2] != "..":
                current_dir.append(dat[2])
                dirs = current_dir[-1]
                file_sys[dat[2]] = file_sys.get(dat[2], [])
                file_sys_size[dat[2]] = file_sys_size.get(dat[2], 0)
            elif dat[1] == "cd" and dat[2] == "..":
                cd += 1
                continue
            else:
                continue
        else: 
            if dat[0] == 'dir':
                insert = dat[1]
                file_sys[dirs] += [insert]    
            else:
                file_sys_size[dirs] += int(dat[0])           
    else:
        if dat[0] == "$":
            if dat[1] == "cd" and dat[2] == "..":
                cd += 1
                continue
            elif dat[1] == "cd" and dat[2] != "..":
                dirs = current_dir[-cd]
                current_dir = current_dir[:-cd+1]
                current_dir.append(dat[2])
                cd = 1
            else:
                print("list")
        elif dat[0] == "dir":
            print("hi")
        
        else: 
            print("else")
            
print(file_sys)
print(current_dir)
print(file_sys_size)