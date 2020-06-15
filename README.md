# compareMS2 and compareMS2GUI

This is the official repository for the GUI version of compareMS2 software suite. compareMS2 is a tool for molecular phylogenetics (or phyloproteomics) by direct comparison of tandem mass spectra, with associated software for generation of distance matrices in several formats. compareMS2GUI provides a graphical user interface for running the compareMS2 pipeline in batch mode while providing real-time feedback and quality control to the user.

## Getting Started

This README document described how to get started with compareMS2GUI, including system prerequisites and various instructions.

### Prerequisites

Minimum system prerequisites to run the compareMS2GUI:

* At least 53 MB free hard drive space
* At least N GB of RAM

### Installing

Follow these steps to install and run compareMS2GUI:

#### Windows

1. Download compareMS2GUI zip file
2. Navigate inside the zip file to dist/compareMS2Gui/compareMS2GUI.exe
3. Run compareMS2GUI.exe
4. OPTIONAL: Create a shortcut of the compareMS2GUI.exe file to the desktop

#### Linux

1.
2.
3.

## Using the software

The GUI consists of three windows:

1. An introduction splash screen with version information
2. The main control window
3. A custom phylogenetic tree visualization for quality control (while running)

The introduction window contains information about compareMS2GUI. The main control window is where the user can specify parameters for the compareMS2 and compareMS2_to_distance_matrices algorithms. These parameters are also used to create the phylogenetic tree. This tree is visualized in a third window during the analysis, giving the user real-time feedback on the progression of the analysis. When the tree is completed, the GUI updates the colors each seperate leaf according to the number of tandem mass spectra in each dataset, ranging from green (within 80% of the largest dataset in the input, indicating high quality) to red (below 20%, suggesting the dataset is of low quality or contains less information). The QC information is written to the parswise comparisons by compareMS2, and can be replaced by any other QC metric.

As with the command-line version, compareMS2GUI outputs files in MEGA, NEXUS and other formats, for further phylogenetic analysis and visualization. The UPGMA tree built in real time by compareMS2GUI is primarily meant to monitor the progress and provide early quality control, allowing the user to interrupt the process if the results do not look like expected or the parameters may have been wrong.


## Authors

* **Nino Vrolijk** - *N.V.* - https://github.com/NinoVrolijk
* **Magnus Palmblad** - *M.P.* - https://github.com/magnuspalmblad

## Acknowledgments

* https://github.com/lex8erna/UPGMApy provided the UPGMA algorithm that was used to create the phylogenetic tree that is visualized in the GUI.
