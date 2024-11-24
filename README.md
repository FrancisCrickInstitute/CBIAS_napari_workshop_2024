<p align="center">
  <img width="25%" src="./docs/CRICK_Primary_Logo_CMYK High res.png" alt="Crick Logo">
</p>

# CBIAS napari workshop 2024
CBIAS napari workshop 2024 - run as part of the Crick Bioimage Analysis Symposium 2024

27-28 November 2024 <br>
The Francis Crick Institute

[https://www.crick.ac.uk/whats-on/cbias-napari-workshop-2024](https://www.crick.ac.uk/whats-on/cbias-napari-workshop-2024)

This training is developed and delivered by [Rocco D’Antuono](https://github.com/RoccoDAnt) (the Francis Crick Institute), [Giulia Paci](https://github.com/giuliapaci) (University College London) and [Marie Held](https://github.com/Marien-kaefer) (the University of Liverpool). Additional speakers include [Ana Stojiljkovic](https://github.com/StojiljkovicVetAna) (University of Bern), [Sebastian Gonzalez Tirado](https://github.com/sebgoti) (Heidelberg University), [Cameron Shand](https://github.com/sea-shunned) (the Francis Crick Institute) and [Graham Ross](https://github.com/grahamross123) (the Francis Crick Institute).

We are kindly helped in the organization of the workshop by the Crick External Training team, Lorenza Giannella and Erdal Dogan.

This training provides fee waivers offered thank to the support of the [Chan Zuckerberg Initiative](https://chanzuckerberg.com/)

# Installation of the software
During the workshop we will extensively try and retry the software installation with conda environments, however to gain some practice and proceed smoothly to more interesting topics, please proceed with the following homework before the workshop

1. Install Anaconda Navigator
2. Install napari within conda prompt

Please make sure to have at least 10-15 GB free on the pc you will bring with you for participating in the workshop. Please let us know well in advance if you cannot bring a pc with you, we might be able to get a loan, however this is not guaranteed and you might risk to have no pc to follow along.

### 1. Install Anaconda Navigator
This is a method that use the graphical user interface to download and install Anaconda Navigator.
Please visit https://docs.anaconda.com/ and click on the green button "Download Anaconda". You will be asked to provide an email address and will receive the link to the download page, where you will choose the version for your OS.

Before installing Anaconda Navigator, please identify a folder in your computer over which you have full permission of read and write file: we will create and update many times conda environments, this means that the software will install and remove files all the times.

### 2. Install napari within conda prompt
The successful installation of Anaconda Navigator will make available an app called "Anaconda prompt". Thsi is the terminal that we will use to create and work with conda environments.

a) Update conda, by typing the following line and pressing Enter.
```
conda update -n base -c conda-forge conda
```

b) create a new environment with a meaningful name: substitute with your choice the string "mymeaningfulname". E.g. "cbias-workshop-env". Please do not simplify with "napari-env", as half of the tutorial use that and you might risk to overwrite a previous environment which contain packages used in previous analyses.

```
conda create -n mymeaningfulname-env python=3.12
```

c) activate the new environment

```
conda activate mymeaningfulname-env
```
You should notice a change in the prompt where the name base at the beginning of the prompt has been changed to "mymeaningfulname-env". This confirms that it is safe to install new packages, as you are not altering the base environment (safe choice is not touch "base").

d) install napari

```
conda install -c conda-forge napari pyqt
```

e) check that napari opens
At this point, if no error appears in the terminal as result of the operations above, you are ready to open napari executing
```
napari
```
### Create a conda environment with a recipe
If a working environment cannot be created through the commands above, the following recipe can be used to create an environment with napari
a) Download the file [cbias2024-napari-env.yml](https://github.com/FrancisCrickInstitute/CBIAS_napari_workshop_2024/tree/main/envs/cbias2024-napari-env.yml) into a local folder

b) use the Anaconda prompt to navigate to the local folder and execute
```
conda env create -f cbias2024-napari-env.yml
```
This should create an environment with the same name of the .yml file unless otherwise specified.

c) check that napari opens
At this point, if no error appears in the terminal as result of the operations above, you are ready to open napari executing
```
napari
```
