print("cfg")
with open("dir_cfg.ini") as f:
    lines = f.readlines()
    dictx = {}
    dictx["name"] = lines[0].split('=')[0].strip()
    dictx["srcDir"] = lines[1].split('=')[0].strip()
    dictx["dataDir"] = lines[1].split('=')[0].strip()
    for k in dictx:
        print(k, dictx[k])
        # haha pp