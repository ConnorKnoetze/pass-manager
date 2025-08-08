import sys, os, subprocess

__project_dir = os.path.abspath(os.path.dirname(__file__))
__app_dir = os.path.join(__project_dir, "app")

def main():
    print(__app_dir)
    subprocess.run("python " + os.path.join(__app_dir, "app.py"))


if __name__ == "__main__":
    main()