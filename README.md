ionize
=====
A unified Python module for calculating buffer properties.

**ionize** calculates the properties of individual ionic species in
aqueous solution, as well as aqueous solutions containing arbitrary
sets of ions.

The **ionize** model is based on techniques previously demonstrated by
[Peakmaster][peakmaster], [Spresso][Spresso], and [STEEP][STEEP]. The **ionize**
model takes into account pH, ionic strength, and temperature effects, including
the  most up-to-date temperature model published in STEEP. The **ionize** object
classes make these techniques directly accessible as a backend for simulations
written in python.

Tutorial
--------
Want to use **ionize**? Read the [tutorial][tutorial], written in ipython
notebook.

ionize Components
-----------------
**ionize** is composed of three main components:

###The Ion Class
The core of **ionize** is the **Ion** class, which  represents a single ionic
species. An ion contains a name, a set of ionization states, and an optional
temperature parameter. Each ionization state contains a charge, a pKa, and
an absolute mobility. An ionization  state may also include values for
&Delta;H and &Delta;Cp of ionization to improve the accuracy of temperature
correction.

###The Solution Class
The **Solution** class is used to represent an aqueous solution containing any
number of ionic species. A **Solution** contains a list of **Ion** objects, and
a second list containing the concentrations of each species. **Solution** can
also take an optional temperature parameter. **Solution** solves for pH,
iteratively accounting for the ionic strength. The ionic strength and pH are
used to calculate the properties of the **Ions**, and bulk properties of the
solution such as conductivity.

###The ionize Database
**ionize** also contains its own database, containing the combined entries of
the Spresso and STEEP databases. This database can be accessed through the
**load_ion**() and **search_ion**() functions.


[peakmaster]: http://web.natur.cuni.cz/gas/ "Peakmaster"
[Spresso]: http://stanfordspresso.blogspot.com/ "Spresso"
[STEEP]: http://microfluidics.stanford.edu/download/ "STEEP"
[tutorial]: http://nbviewer.ipython.org/github/lewisamarshall/ionize/blob/master/tutorial.ipynb  "ionize Tutorial"