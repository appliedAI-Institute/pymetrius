import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.include_readthedocs_yaml}}" != "y":
    remove(".readthedocs.yaml")


return_code = os.system("""
echo "Initializing your new project in in $(pwd). This might take a while"
git init
git remote origin https://gitlab.aai.lab/{{cookiecutter.gitlab_project_path}}
echo "Creating and activating venv"
python{{cookiecutter.python_version}} -m venv ./venv
. venv/bin/activate
echo "Installing formatter"
pip install black pre-commit
echo "Performing Initial formatting"
black .
echo "Setting git hooks"
pre-commit install
pre-commit autoupdate
echo "Initial commit"
git add . && git commit -m "Initial commit by python_library_template"
git branch develop && git checkout develop
echo "Installing {{cookiecutter.project_name}} in editable mode into venv"
pip install -e .
echo "Running the sample script"
python scripts/run_sample.py
echo "A virtual environment for your project has been created in $(pwd)/venv.\
 The library was installed there in editable mode."
""")
