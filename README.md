<!--
## <b> Code-Translation-CodeNet</b>

The goal of Code-Translation is to translate a program written in Python to C++. This can be highly valuable in many respects such as, migrating ancient systems to newer ones or learning new programming languages. 

## Table of Contents

   * [Introduction](#introduction)
      * [Potential use cases](#potential-use-cases)
      * [Usability](#usability)
   * [Models and experiments](#models-and-experiments)
   * [Relevant links](#relevant-links)
   * [Dataset overview](#dataset-overview)
   

## Introduction

## Dataset overview
Code-Translation is a completely open source project, including its dataset. We will use Project CodeNet from IBM. 
-->
<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->
# Code-Translation-CodeNet Documentation

<!-- PROJECT LOGO -->
<p align="center">
  <a href="">
    <img src="https://github.com/tenzin-g/Code-Translation-CodeNet/blob/main/Logo/[ct] .svg" alt="Team/Project logo" width="200" height="200">
  </a>

  <h3 align="center">RCOS Project</h3>

  <p align="center">
    Open Source 
    <br />
    <a href="https://github.com/tenzin-g/Code-Translation-CodeNet/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/tenzin-g/Code-Translation-CodeNet/issues">Report Bug</a>
    ·
    <a href="https://github.com/tenzin-g/Code-Translation-CodeNet/pulls">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Technical Research](#technical-research)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project
The goal of Code-Translation is to translate a program written in Python to C++. This can be highly valuable in many respects such as migrating ancient systems to newer ones or learning new programming languages. Here, we are exploring the technologies surrounding NLP and seeing how pre-existing ML frameworks can help us achieve our goal of code translation. 


### Built With

We are still in the early stages of development so this list will be evolving as this project progresses. 

#### Development Toolkit:

- [VS Code](https://code.visualstudio.com/) (IDE)
- [AIMOS](https://docs.cci.rpi.edu/Slurm/) (Supercomputer Server) 
- [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) (Interactive Computing)
- [Ubuntu](https://help.ubuntu.com/) (Linux Distribution)

#### Project Board:
- [Mural](https://www.mural.co/) (Digital Collaboration)

<!-- Technical Research -->

## Technical Research

The Code-Translation-CodeNet team decided to explore various ML frameworks, specifically targetting natural langauge processing, to help get our project started. Below are the links to the frameworks we have decideded to focus on. There are descriptions of each and how we plan to integrate them in the Code-Translation-CodeNet wiki!

- [OpenNMT](https://opennmt.net/OpenNMT-py/quickstart.html#step-1-prepare-the-data)
- [GloVe](https://nlp.stanford.edu/projects/glove/)
- [BERT](https://github.com/tenzin-g/Code-Translation-CodeNet/blob/main/Copy_of_BERT_Word_Embeddings_v2.ipynb)


<!-- Getting Started -->

## Getting Started

Here are some simple instructions on how to set up the project locally. 

### Prerequisites

- Make sure you have the latest version of Python installed on your device, along with your IDE of choice. 
- For Windows Devices, have a WSL (ubuntu) ready. 
- For jupyter notebooks, Google Colab is fine. A google account is needed. 

#### OpenNMT
(full instructions are linked above)
- upgrade pip

```sh
pip install --upgrade pip
```

- Install OpenNMT

```sh
pip install OpenNMT-py
```

#### BERT
(full instructions are linked above)
- Install transformers

```sh
pip install transformers
```

- Import pytorch

```sh
import torch
```

 - Import pretrained BERT model and BERT tokenizer 
 
 ```sh
 from transformers import BertTokenizer, BertModel
```
 - Import matplotlib
 
 ```sh
 import matplotlib.pyplot as plt
```

## Usage

Code-Translation-CodeNet is most useful for system migration; specifically in respects to migration from an archaic system to a modern alternative. Along with this, because our dataset (CodeNet) utilizes very basic files, this project can be used for educational purposes. Here are examples of files from CodeNet, where a beginner programmer can potentially use to help translate from language to another. 
<p align="center">

![codeNetEx](https://user-images.githubusercontent.com/84874177/204444053-cca3f008-9e0b-4727-970b-6b82ca78a862.png)

</p>


<!-- ROADMAP -->

## Roadmap

(full outline can be found on our mural linked above)

- Find keywords from Python and C++
- Research ML Frameworks to employ in our model 
- Integrate frameworks to fit our desired output 
- Test out results 

<!-- Contact -->
## Contact

**Project Lead:** [Tenzin Ghongwatsang](mailto:ghongt@rpi.edu)

**Project Lead:** [Anisha Halwai](mailto:halwaa@rpi.edu)

<!-- Acknowledgements -->
## Acknowledgements

Huge shoutout to RCOS and Professor Turner. This project only started because of this class and the Code-Translation-CodeNet team is grateful for the support! 
