
Starting from env create to all packages install and run matminer : all things
will be documented over here

1. create env:
             conda create -n matminer python=3.9

2. Go to where you want to download the matminer package
        go to matminer github----copy code ---- git clone pest where you want to
 download

3. Activate matminer envs: conda activate matminer

4. Go to where you downloaded the package matminer and install it

5.        pip install -e .  # This ype of installation allows you to et the acess of changes you could make in side any code file inside this package

6. Now inside matminer install the following packages using pip
    
    pip install ipython
    
    pip install ipywidgets
    
    pip install ipykernel

    pip install mp-api
    
    pip install phonopy

7. Check this site for different packages

        https://pypi.org/project/ipykernel/

  Use pip check command
8.

        Things which are uninstall during my mistake : I was installing matminer in base 

        (base) thsim2@thsim2:~/code/ML/matminer$ pip install -e .
Obtaining file:///home/thsim2/code/ML/matminer
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
    Preparing wheel metadata ... done
Collecting scikit-learn~=1.3
  Downloading scikit_learn-1.4.1.post1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.2 MB)
     |████████████████████████████████| 12.2 MB 4.5 MB/s 
Requirement already satisfied: monty>=2023 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matminer==0.9.3.dev1) (2023.11.3)
Requirement already satisfied: numpy<2,>=1.23 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matminer==0.9.3.dev1) (1.26.3)
Requirement already satisfied: pymongo~=4.5 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matminer==0.9.3.dev1) (4.6.1)
Requirement already satisfied: pymatgen>=2023 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matminer==0.9.3.dev1) (2023.12.18)
Collecting requests~=2.31
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting sympy~=1.11
  Using cached sympy-1.12-py3-none-any.whl (5.7 MB)
Collecting pandas<3,>=1.5
  Downloading pandas-2.2.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.0 MB)
     |████████████████████████████████| 13.0 MB 56.7 MB/s 
Collecting tqdm~=4.66
  Downloading tqdm-4.66.2-py3-none-any.whl (78 kB)
     |████████████████████████████████| 78 kB 1.7 MB/s 
Requirement already satisfied: python-dateutil>=2.8.2 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pandas<3,>=1.5->matminer==0.9.3.dev1) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pandas<3,>=1.5->matminer==0.9.3.dev1) (2021.3)
Collecting tzdata>=2022.7
  Downloading tzdata-2024.1-py2.py3-none-any.whl (345 kB)
     |████████████████████████████████| 345 kB 102.5 MB/s 
Requirement already satisfied: networkx>=2.2 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (2.7.1)
Requirement already satisfied: ruamel.yaml>=0.17.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (0.17.21)
Requirement already satisfied: spglib>=2.0.2 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (2.2.0)
Requirement already satisfied: palettable>=3.1.1 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (3.3.0)
Requirement already satisfied: scipy>=1.5.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (1.11.4)
Requirement already satisfied: joblib in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (1.1.0)
Requirement already satisfied: plotly>=4.5.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (5.6.0)
Requirement already satisfied: matplotlib>=1.5 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (3.5.1)
Requirement already satisfied: pybtex in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (0.24.0)
Requirement already satisfied: uncertainties>=3.1.4 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (3.1.7)
Requirement already satisfied: tabulate in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymatgen>=2023->matminer==0.9.3.dev1) (0.8.9)
Requirement already satisfied: packaging>=20.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (21.3)
Requirement already satisfied: kiwisolver>=1.0.1 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (1.3.2)
Requirement already satisfied: fonttools>=4.22.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (4.25.0)
Requirement already satisfied: pillow>=6.2.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (9.0.1)
Requirement already satisfied: cycler>=0.10 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (0.11.0)
Requirement already satisfied: pyparsing>=2.2.1 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from matplotlib>=1.5->pymatgen>=2023->matminer==0.9.3.dev1) (3.0.4)
Requirement already satisfied: tenacity>=6.2.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from plotly>=4.5.0->pymatgen>=2023->matminer==0.9.3.dev1) (8.0.1)
Requirement already satisfied: six in /home/thsim2/anaconda3/lib/python3.9/site-packages (from plotly>=4.5.0->pymatgen>=2023->matminer==0.9.3.dev1) (1.16.0)
Requirement already satisfied: dnspython<3.0.0,>=1.16.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pymongo~=4.5->matminer==0.9.3.dev1) (2.4.2)
Requirement already satisfied: idna<4,>=2.5 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from requests~=2.31->matminer==0.9.3.dev1) (3.3)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from requests~=2.31->matminer==0.9.3.dev1) (1.26.9)
Requirement already satisfied: charset-normalizer<4,>=2 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from requests~=2.31->matminer==0.9.3.dev1) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from requests~=2.31->matminer==0.9.3.dev1) (2021.10.8)
Requirement already satisfied: ruamel.yaml.clib>=0.2.6 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from ruamel.yaml>=0.17.0->pymatgen>=2023->matminer==0.9.3.dev1) (0.2.7)
Requirement already satisfied: threadpoolctl>=2.0.0 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from scikit-learn~=1.3->matminer==0.9.3.dev1) (2.2.0)
Collecting joblib
  Downloading joblib-1.3.2-py3-none-any.whl (302 kB)
     |████████████████████████████████| 302 kB 65.6 MB/s 
Requirement already satisfied: mpmath>=0.19 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from sympy~=1.11->matminer==0.9.3.dev1) (1.2.1)
Requirement already satisfied: future in /home/thsim2/anaconda3/lib/python3.9/site-packages (from uncertainties>=3.1.4->pymatgen>=2023->matminer==0.9.3.dev1) (0.18.2)
Requirement already satisfied: latexcodec>=1.0.4 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pybtex->pymatgen>=2023->matminer==0.9.3.dev1) (2.0.1)
Requirement already satisfied: PyYAML>=3.01 in /home/thsim2/anaconda3/lib/python3.9/site-packages (from pybtex->pymatgen>=2023->matminer==0.9.3.dev1) (6.0)
Installing collected packages: tzdata, tqdm, sympy, requests, pandas, joblib, scikit-learn, matminer
  Attempting uninstall: tqdm
    Found existing installation: tqdm 4.64.0
    Uninstalling tqdm-4.64.0:
      Successfully uninstalled tqdm-4.64.0
  Attempting uninstall: sympy
    Found existing installation: sympy 1.10.1
    Uninstalling sympy-1.10.1:
      Successfully uninstalled sympy-1.10.1
  Attempting uninstall: requests
    Found existing installation: requests 2.27.1
    Uninstalling requests-2.27.1:
      Successfully uninstalled requests-2.27.1
  Attempting uninstall: pandas
    Found existing installation: pandas 1.4.2
    Uninstalling pandas-1.4.2:
      Successfully uninstalled pandas-1.4.2
  Attempting uninstall: joblib
    Found existing installation: joblib 1.1.0
    Uninstalling joblib-1.1.0:
      Successfully uninstalled joblib-1.1.0
  Attempting uninstall: scikit-learn
    Found existing installation: scikit-learn 1.0.2
    Uninstalling scikit-learn-1.0.2:
      Successfully uninstalled scikit-learn-1.0.2
  Running setup.py develop for matminer
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
conda-repo-cli 1.0.4 requires pathlib, which is not installed.
Successfully installed joblib-1.3.2 matminer-0.9.3.dev1 pandas-2.2.1 requests-2.31.0 scikit-learn-1.4.1.post1 sympy-1.12 tqdm-4.66.2 tzdata-2024.1



