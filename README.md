# compareMS2

This project concerns the compareMS2 software for molecular phylogenetics by direct comparison of tandem mass spectra, and the associated generation of distance matrices and novel compareMS2GUI graphical user interface providing real-time feedback and quality control.

## Getting Started

This file is dedicated to getting the user started with the compareMS2GUI. The README.md consist of system prerequisites and various instructions.

### Prerequisites

The programs and libraries that need to be installed to run the compareMS2GUI software.

```
- Python 3. available from https://www.python.org/downloads/
- ETE3 Toolkit.
- Pyqt5.
```

### Installing
Series of steps to make the system ready for the software.

#### Windows
```
1. Visit https://www.python.org/downloads/
2. Download python version 3. for Windows.
3. Open cmd and navigate to the CompareMS2 folder.
4. Type : pip install PyQt5
5. Type : pip install Ete3
6. Type : pip install pyinstaller
7. Type : pyinstaller initializer.py
Now you should have all required programs and libraries present.
```

#### MacOS
```
until finished
```

## Using the software.
The GUI consists of 3 distinct components, or screens:
  1. An introduction screen
  2. The main input screen
  3. A phylogenetic tree analysis screen \n
The introduction screen contains information about compareMS2GUI. The main input screen is the central screen of the GUI. This is where the user can specify various parameters for the compareMS2 algorithm. These parameters are used to create the phylogenetic tree. This tree is visualized in the final screen. The tree analysis screen gives the user real-time feedback on the progression of the analysis. When the tree is completed the GUI updates the colors each seperate leaf. By default, the colors indicate the number of tandem mass spectra in the dataset, ranging from green (within 80% of the largest dataset in the input, indicating high quality) to red (below 20%, suggesting the dataset is of low quality or contains less information).

As with the command-line version, compareMS2GUI outputs files in MEGA and other formats, for further phylogenetic analysis and visualization. The UPGMA tree built in real time by compareMS2GUI is primarily meant to monitor the progress and provide early quality control, allowing the user to interrupt the process if the results do not look like expected or the parameters may have been wrong.


## Authors

* **Nino Vrolijk** - *N.V* - https://github.com/NinoVrolijk
* **Magnus Palmblad** - *M.P* - https://github.com/magnuspalmblad

## Acknowledgments

* https://github.com/lex8erna/UPGMApy provided the UPGMA algorithm that was used to create the phylogenetic tree that is visualized in the GUI.
