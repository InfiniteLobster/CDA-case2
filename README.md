# CDA-case2

This is the repository for case 2 project for [02582 Computational Data Analysis](https://kurser.dtu.dk/course/02582) course from [DTU](https://www.dtu.dk/).

The project goal was to investiagate how much information about the emotional state induced by the experiment (resting vs competing) is actually present in the extracted features. We used a lower-dimension representation of the given data (not shared publicly) in our exploration. We chose to separate each element of project work into different folders (located in 'src' folder). In each folder there is at least a Jupyter notebook with all performed steps.  An additional python file might also be present for the purpose of putting some repeating code out of the notebook to improve interpretability.

Src folders:
- Pre-processing: In this folder data analyses, to determine pre-processing steps, was performed. Due to the used structure of scikit-learn code and the goal of keeping the code logic clear(interpretability and reproductability) the pre-processing itself is not performed at this point. Only properties of data are checked to find out what pre-processing and with which method would be needed for the further analyses.
- PCA: in this folder Principal Component Analysis (PCA) and sparse PCA (sPCA) are done to get low-dimensional view of the sensor data. Scikit-learn was used for those operations.
- CCA-PLS: in this folder Partial Least Squares (PLS) regression and Canonical Correlation Analysis (CCA) were performed. The goal in this section was to investiagte the connection between sensor data and self-reported emotional state in lower dimensions. Here as well, Scikit-learn was used for those operations.

[Uv](https://docs.astral.sh/uv/) is used as virtual environment (libraries/packages) manager. The project was tested on a few Windows machines, and dependencies worked as expected. Only "uv sync" (see Installation) command was needed to construct needed virtual environment for repository run.

## Cookiecutter template

In the creation of project structure this [cookiecuter template](https://github.com/InfiniteLobster/cookiecutter-ml-project) was used.

## Installation
To use this GitHub repository it first needs to be cloned locally as follows (standard code for git repository cloning):
```bash
git clone https://github.com/InfiniteLobster/CDA-case2
```
After the cloning, the virtual environment needs to be configured. In this project [uv](https://docs.astral.sh/uv/) is used for this purpose. With it installed on the machine following code needs to be executed for this purpose  (standard code for uv):
```bash
uv sync
```
## Requirements
* [git](https://git-scm.com/)
* [uv](https://docs.astral.sh/uv/)
* python version: 3.12
## Authors
*  [InfiniteLobster](https://github.com/InfiniteLobster)
* [RupakKadhare15](https://github.com/RupakKadhare15)
* [yukthadabke](https://github.com/yukthadabke)
## Version

1.0.0 (Created: 2026-04-20)

## License

MIT License

