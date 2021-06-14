import os
import time
import subprocess
import random
import sys
import json
import glob
import readline
import requests
## CODED BY 81L1NM1Y0R from Qairex Studio
os.system("clear")
version = "0.3"
banner =[f"""
       ....             .       .x+=:.                                      ..
   .xH888888Hx.        @88>    z`    ^%                                   dF
 .H8888888888888:      %8P        .       <88888X   '?8  ''888E` x88:  `)8b.   X888  888X '888>   888R I888>  beWE "888L
 `:..:`888888>    8>   888E  8888N=*8888   X888  888X '888>   888R I888>  888E  888E
        `"*88     X    888E   %8"    R88   X888  888X '888>   888R I888>  888E  888E
   .xHHhx.."      !    888E    @8Wou 9%    X888  888X '888>  u8888cJ888   888E  888F
  X88888888hx. ..!     888&  .888888P`    "*88%""*88" '888!`  "*888*P"   .888N..888
 !   "*888888888"      R888" `   ^"F        `~    "    `"`      'Y"       `"888*""
        ^"***"`         ""                                                   ""
                                                TEST VERSION v.{version}

"""]
path = ""
def checking_update():
        os.sys.stdout.flush()
        os.sys.stdout.write("Checking Update...")
        os.sys.stdout.flush()
        req = requests.get("https://raw.githubusercontent.com/QairexStudio/dismod/main/main.py")
        if req.text.find('version = "{0}"'.format(version)) == -1:
            while True:
                os.sys.stdout.write("\rDo you want to update dismod? [Y/N]:")
                os.sys.stdout.flush()
                upda = input().lower()
                if "y" in upda or upda.startswith("y"):
                    os.sys.stdout.write("\rUpdating package...")
                    os.sys.stdout.flush()
                    test = os.system("which git")
                    os.system("clear")
                    os.sys.stdout.write("\rUpdating package...")
                    os.sys.stdout.flush()
                    if test != 0:
                        os.sys.stdout.flush()
                        os.sys.stdout.write("\rError! Install git package...")
                        os.sys.stdout.flush()
                        break
                        return
                    time.sleep(1)
                    break
                    return
                if "n" in upda or upda.startswith("n"):
                    os.sys.stdout.flush()
                    os.sys.stdout.write("\rUpdate canceled!")
                    os.sys.stdout.flush()
                    time.sleep(1)
                    break
                    return
                os.sys.stdout.flush()
                os.sys.stdout.write("\rWrong answer!")
                time.sleep(1)
        os.sys.stdout.write("\rNothing to update!")
        time.sleep(1)
        os.system("clear")

def start_animation():
    for t in random.choice(banner):
        time.sleep(0.00114)
        print(t, end='')
def main():
        global path, plug
        commands, keys, com, plug_com, config, ats, asa, bass, c, yasa, j, z, bam = [], [], 0, [], {}, [""], [], [], 1, [], 0, 0, []
        plugins = os.path.join(os.getcwd(), "modules")
        for i in os.listdir(plugins):
            if not os.path.isfile(i):
                commands.append(i)
        plugin_command = {"run": "Execute script", "set": "Set variable", "restart": "Reset config", "config": "Show config"}
        for l in plugin_command.keys():
            plug_com.append(l)
        komut = {"load": "Load module", "help": "Show this help menu", "clear": "clear screen", "back": "Return from module", "banner": "Show random banner", "exit": "Exit the dismod", "restart": "Reset all configs", "modules": "Show all modules", "update": "Update dismod"}
        for t in komut.keys():
            keys.append(t)
        command = input(str(path) + ">>>")
        if len(path) > 0:
            if plug_com[0] in command.lower():
                if not os.path.exists(plugins + "/" + str(plug) + "/" + "installed.txt"):
                    os.sys.stdout.write("Checking dependencies file...")
                    os.sys.stdout.flush()
                    contin = False
                    try:
                        with open(plugins + "/" + str(plug) + "/" + "requirements.txt", "r") as test:
                            best = test.read().splitlines()
                        if not os.path.exists(plugins + "/" + str(plug) + "/" + "requirements.txt"):
                            os.sys.stdout.write("\rNot found dependencies file!")
                            contin = True
                        if not contin:
                            os.sys.stdout.write("\rChecking dependencies...")
                            os.sys.stdout.flush()
                            os.sys.stdout.write("Installing Dependencies...")
                            os.sys.stdout.flush()
                            for t in best:
                                os.system("pip install {0}".format(t))
                            os.sys.stdout.write("\r Installed Dependencies!")
                            with open(plugins + "/" + str(plug) + "/" + "installed.txt", "w") as test:
                                test.write("1")
                    except:
                        print("something went wrong")
                        print("Please install dependencies with manually!")
                        for t in best:
                            print(t)
                os.sys.stdout.flush()
                os.sys.stdout.write("\rLoading module...")
                with open(plugins + "/" + str(plug) + "/" + "config.json", "r") as test:
                    best = json.loads(test.read())
                for b in best.items():
                    asa.append(b)
                    c += 1
                for k in range(0, c, 2):
                    bass.append(asa[:k])
                for atmaca in bass:
                    if len(atmaca) == 0:
                        continue
                    bam.append(atmaca[z][1])
                    z += 2
                os.system("python3 " + plugins + "/" + str(plug) + "/" + "main.py {}".format(' '.join(bam)))
                print("Loaded module!")
                c, z = 1, 0
                asa.clear()
                bass.clear()
                return
            if plug_com[1] in command.lower():
                data = command.lower().split()
                for t in data:
                    if len(t) == 0:
                        data.remove(t)
                if len(data) < 3:
                    print("""USAGE:
                            set variable value""")
                    return
                with open(str(plugins) + "/" + str(plug) + "/" + "config.json", "r") as con:
                    tata = json.loads(con.read())
                for t in tata.items():
                    bass.append(t)
                    c += 1
                for k in range(0, c, 2):
                    bam.append(bass[:k])
                for lan in bam:
                    if len(lan) == 0:
                        continue
                    asa.append(lan[len(lan) -2][0])
                att = []
                for t in asa:
                    if t in data:
                        comma = command.replace("set", "", 1).replace(t, "", 1).strip()
                        tata[t] = comma
                        att.append(True)
                    else:
                        att.append(False)
                if not True in att:
                    print("Variable not found!")
                    return
                with open(str(plugins) + "/" + str(plug) + "/" + "config.json", "w") as test:
                    test.write(json.dumps(tata))
                return
            if plug_com[2] in command.lower():
                with open(str(plugins) + "/" + str(plug) + "/" + "config.json", "r") as best:
                    bat = json.loads(best.read())
                for t in bat:
                    if t.lower() == "description":
                        continue
                    bat[t] = ""
                kata = json.dumps(bat)
                with open(str(plugins) + "/" + str(plug) + "/" + "config.json", "w") as test:
                    test.write(kata)
                return
            if plug_com[3] in command.lower():
                with open(str(plugins) + "/" + str(plug) + "/" + "config.json", "r") as get:
                    tata = json.loads(get.read())
                for b in tata.items():
                    asa.append(b)
                    c += 1
                for k in range(0, c, 2):
                    bass.append(asa[:k])
                for t in bass:
                    if len(t) == 0:
                        continue
                    j += 2
                    ats[0] = """
===== VARIABLE =========== VALUE ============= DESCRIPTION ======
-----------------------------------------------------------------
    {0}              {1}                    {2}
                """.format(t[z][0], t[z][1], t[len(t) -1][1])
                    print(ats[0])
                    z += 2
                print()
                print(asa[j][1])
                print()
                return
        try:
            com = subprocess.call(command.lower(), stderr=subprocess.STDOUT)
        except:
            pass
        if keys[0] in command.lower():
            ham = False
            for t in commands:
                if t in command.lower():
                    plug = str(t)
                    path = "module > " + str(t) + " "
                    ham = True
            if not ham:
                print("Not found module!")
                return
            return
        if keys[1] in command.lower():
            for help in komut.items():
                print("""----------------------->>
                {0}: {1}
                """.format(help[0], help[1]))
            return
        if keys[2] in command.lower():
            os.system("clear")
            print(random.choice(banner))
            return
        if keys[3] in command.lower():
            path = ""
            return
        if keys[4] in command.lower():
            print(random.choice(banner))
            return
        if keys[5] in command.lower():
            print("Bye! Bye! :)")
            exit()
        if keys[6] in command.lower():
            for t in glob.glob("modules/*"):
                if os.path.isdir(t):
                    with open(str(t) + "/" + "config.json", "r") as test:
                        tata = json.loads(test.read())
                    c = 1
                    for item in tata.items():
                        bam.append(item)
                        c += 1
                    for i in range(0, c, 2):
                        bass.append(bam[:i])
                    for l in bass:
                        if len(l) == 0:
                            continue
                        tata[l[len(l) -2][0]] = ""
                    with open(str(t) + "/" + "config.json", "w") as wri:
                        wri.write(json.dumps(tata))
                    bam.clear()
                    bass.clear()
            return
        if not command.lower() in keys and com != 0:
            print("Wrong command. Type help to see the list of commands!")
            return
        if keys[7] in command.lower():
            print("                 Module list:")
            for t in commands:
                print(t)
            return
        if keys[8] in command.lower():
            checking_update()


if not os.geteuid() == 0:
    print("You \033[4;49;91mMust\033[0m be \033[1;49;37mroot!\033[0m")
else:
    start_animation()
    while True:
        main()
