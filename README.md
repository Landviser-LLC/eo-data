# Earth Observations for Crop Performance (Phenotype) Prediction
private repo made public after the work on the EU HORIZON20 PARSEC grant was completed (2020-2021). Sensitive trial information and stale branches were removed. This is a Python-based project dealing with spatial-temporal geographical datasets. Exploring the scientific concept of GxE (Genotype x Environment interaction). Some initial work was done in 2007 by Larisa Golovko, then at RiceTec Inc see 

## Git collab ground rules 

If you just started using GitHub, some ground rules. Assuming Win OS, for Mac - adjust accordingly. 
Install VS Code (recommended, can use other code editors but stay away from Anaconda, we would use **pip install** in our project). Install Git (Mac has it) from https://git-scm.com/book/en/v2/Getting-Started-Installing-Git. Install Python 3 (this repo would not work for Python 2) - Mac has Python 2 by default installed, make sure you switch to Python 3 if on Mac (and ALWAYS use a separate Virtual Environment for each project, that will save you some headaches later on;).
- Clone the repo to your machine:
~~~
git clone https://github.com/Landviser-LLC/eo-data.git. #[url of this repo]
~~~
- Create new local branch for your work and switch to it:
~~~
git checkout -b branchname    # anything you want, but identifying YOU
~~~
- work on your local branch, use commands
~~~
git add [file]  # file modified
git status   # to check for commits and changes
git commit -m "something about what was done on this commit - changes etc"
~~~
- when done, push your branch back to this repo using
~~~
git push origin
~~~
then submit pull request here on GitHub for others to review and approve the merge of your branch with **master**. You can then delete your branch here or keep for your continued work. When you return to project after awhile, always do pull master/branch from here using
~~~
git pull origin    # this is on your local terminal when navigated to the project folder, 
                   # also depends on which branch are you - switch to master to pull master updates
~~~


## Set local coding environment 

Assuming you installed Python, VS Code (or other IDE), Git and cloned repo as described above, checked out you branch. In the terminal (PS - Power Shell)
check which version of Python you have on your PC by typing **py -0** make sure you are on Python 3.8 or 3.9 (latest).
~~~
py -0
Installed Pythons found by C:\Windows\py.exe Launcher for Windows
 -3.9-64 *
 -3.8-64
 -3.6-64
 -2.7-32
 ~~~

 Install Virtual Environment for the Project - you can use exactly the same name for your environment, repo is setup not to pull files in the environment - they are specific to your machine, no use to share those. If you name your environment differently, it is ok, just setup **.gitignore** file yourself for it ;) so, type
 ~~~
 python -m venv .env39eo
 ~~~
 Finally, activate your coding environment by typing
 ~~~
 .env39eo/scripts/activate
 ~~~
 Notice how the prompt changed showing that you are in your Python environment - with core Python modules copied into environment folder and activated
 ~~~
 (.env39eo) PS C:\Users\laris\OneDrive\PY3\eo_crops> 
 ~~~

 ## Installing Python Modules for the project

 The modules used in the project are listed in the file **requirements.txt** type the following to install all
 ~~~
 pip install -r requirements.txt
 ~~~
 Now you should have no problem using Jupyter Notebooks and Python files in this repo. If in the course of your development, you need an additional module you would **pip install [module]** do not forget to add it in **requirements.txt** so others (or yourself) working after you can quickly reinstall all modules in the repo.

 ## That's All for Now! Welcome to Landviser's Team! Happy Coding 
