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
filesize = {}
for dat in data:
    dat = dat.split()
    #print(current_dir)
    if cd == 1:
        if dat[0] == "$":
            if dat[1] == "cd" and dat[2] != "..":
                current_dir.append(dat[2])
                dirs = current_dir[-1]
                file_sys[dat[2]] = file_sys.get(dat[2], [])
                file_sys_size[dat[2]] = file_sys_size.get(dat[2])
            elif dat[1] == "cd" and dat[2] == "..":
                cd += 1
                continue
            elif dat[1] == "ls":
                print("list")
        else: 
            if dat[0] == 'dir':
                file_sys[dat[1]] = file_sys.get(dat[1], [])
                insert = dat[1]
                file_sys[dirs] += [insert]
                         
    else:
        if dat[0] == "$":
            if dat[1] == "cd" and dat[2] == "..":
                cd += 1
                continue
            elif dat[1] == "cd" and dat[2] != "..":
                dirs = current_dir[-cd]
                current_dir = current_dir[:(-cd+1)]
                current_dir.append(dat[2])
                cd = 1
                #print(current_dir)
            elif dat[1] == "ls":
                print("list2")
        elif dat[0] == "dir":
            print("hi")
        
        else: 
            print("else")
            break

print(file_sys)


