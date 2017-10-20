print("cfg")
with open("dir_cfg.ini") as f:
    lines = f.readlines()
    dictx = {}
    dictx["name"] = lines[0].split('=')[1].strip()
    dictx["srcDir"] = lines[2].split('=')[1].strip()
    dictx["dataDir"] = lines[3].split('=')[1].strip()
    for k in dictx:
        print(k, dictx[k])
        # haha pp