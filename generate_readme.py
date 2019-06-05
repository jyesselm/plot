import pandas as pd
import numpy as np
import subprocess


def main():
    f = open("README.md", "w")
    f.write("Plot.py examples\n")
    f.write("----------------\n")

    df = pd.read_csv("commands.csv")
    exe = "plot.py "
    for i, row in df.iterrows():
        path = "imgs/examples/"+str(i)+".png"
        args = ""
        if not pd.isnull(row.args):
            args = row.args
        print args
        command = exe + " -csv {csv} -t {type} {args} -o {path}".format(
            csv=row.csv, type=row.type, args=args, path=path)
        subprocess.call(command, shell=True)
        f.write(row.note + "\n")
        f.write("![]({path})".format(path=path))
    f.close()

if __name__ == "__main__":
    main()


