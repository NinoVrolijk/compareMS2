# compareMS2

This project concerns the compareMS2 software for molecular phylogenetics by direct comparison of tandem mass spectra, and the associated generation of distance matrices and novel compareMS2GUI graphical user interface.

## Getting Started

This file is dedicated to getting the user started with the compareMS2Gui. The readme.md consist of system prerequisites and various instructions.

### Prerequisites

The programs and libraries that need to be installed to run the CompareMS2Gui software.

```
- Python 3. available from https://www.python.org/downloads/
- ETE3 Toolkit.
- Pyqt5.
```

### Installing
Series of step to make the system ready for the software.

#### Windows
```
1. Visit https://www.python.org/downloads/
2. Download python version 3. for Windows.
3. Open the cmd.
4. Type : pip install PyQt5
5. Type : pip install Ete3
6. Install and run the CompareMS2Gui.exe
Now you have all required programs and libraries present.
```

#### MacOS
```
until finished
```

## Using the software.
The Gui consist of 3 distinct components.
  1. Introduction screen.
  2. Main input screen.
  3. Phylogenetic tree analysis screen.
The introduction screen contains information about the compareMS2Gui. The main input screen is the central screen of the Gui. This is where the user can specify various parameters for the CompareMS2 algorithm. These parameters are used to create the phylogenetic tree. This tree is visualized in the final screen. The tree analysis screen gives the user real-time feedback on the progression of the analysis. When the tree is completed the Gui colors each seperate leaf, this is an quality control step. The colors range from green (high quality) to red (low quality).


## Authors

* **Nino Vrolijk** - *N.V* - https://github.com/NinoVrolijk
* **Magnus Palmblad** - *N.M.P* - https://github.com/magnuspalmblad

## Acknowledgments

* https://github.com/lex8erna/UPGMApy provided the UPGMA algorithm that was used to create the phylogenetic tree that is visualized in the gui.
