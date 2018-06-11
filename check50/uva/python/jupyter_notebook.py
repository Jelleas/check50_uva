import check50
import check50.internal
import subprocess

def convert_notebook(name):
    path = f"{check50.internal.run_dir}/{name}"

    if subprocess.call(['jupyter', 'nbconvert', '--to', 'script', path]) != 0:
        raise check50.Failure(f"Could not convert {name} to a .py script")

    path = path.replace(".ipynb", ".py")

    # remove all magic lines from notebook
    with open(path, "r") as f:
        lines = f.readlines()
    with open(path, "w") as f:
        f.write("".join([l for l in lines if "get_ipython" not in l]))
