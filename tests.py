#!/usr/bin/python3
import subprocess

def compile(c_file):
    try:
        out = subprocess.check_output(["gcc", c_file], cwd="rendu/%s" % c_file.split(".")[0])
        if out == "".encode():
            return True
        return False
    except Exception:
        return False

def inter():
    if compile("inter.c") == True:
        test1 = subprocess.check_output(["./a.out", "padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"] , cwd="rendu/inter")
        test2 = subprocess.check_output(["./a.out", "ddf6vewg64f", "gtwthgdwthdwfteewhrtag6h4ffdhsd"] , cwd="rendu/inter")
        test3 = subprocess.check_output(["./a.out", "nothing", "This sentence hides nothing"] , cwd="rendu/inter")
        test4 = subprocess.check_output(["./a.out"] , cwd="rendu/inter")

        if test1 == "padinto\n".encode() and test2 == "df6ewg4\n".encode() and test3 == "nothig\n".encode() and test4 == "\n".encode():
            return True
        else:
            return False
    else:
        return "something went wrong compiling your code!"

def union():
    compile("union.c")

def ft_printf():
    pass

def gnl():
    pass
