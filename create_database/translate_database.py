from math import copysign
import shelve
from load_steep_db import load_steep_db


def make_database():
    """Make the ionize database.

    The ionize database is drawn from the STEEP and Spresso databases. These old
    database files are housed in csv files. These databases are translated,
    combined, and housed in a shelve database.

    Note that the shelve backend is different for OSX and Windows, so separate
    shelves are created for each system.
    """

    # Open the files from the spresso database.
    z = open('create_database/z.csv', 'r')
    namelist = open('create_database/name.csv', 'r')
    pKalist = open('create_database/pKa.csv', 'r')
    mobilitylist = open('create_database/mobility.csv', 'r')

    # z is a fixed list that the other parameters are compared to.
    z = map(int, z.readline().split(','))

    # Call a separate function to open the steep db.
    steep_db = load_steep_db()

    # Initialize the ion dictionary.
    ion_dict = dict()
    n_steep = 0
    steep_common = []
    for idx, name in enumerate(namelist):
        # get name
        name = name.rstrip().lower()

        # check to see if the ion is in the steep database.
        if name in steep_db.keys():
            n_steep += 1
            steep_common.append(name)
            dH = steep_db[name][3]
            if steep_db[name][4]:
                dCp = steep_db[name][4]
        else:
            dH = None
            dCp = None

        # Get pKa lists
        pKa = pKalist.readline()
        pKa = pKa.rstrip().split(',')

        # Get mobility lists
        mobility = mobilitylist.readline()
        mobility = mobility.rstrip().split(',')

        # print name, pKa, mobility
        state = [[], [], [], dH, dCp]
        for i in range(len(z)):
            if not pKa[i] == 'NaN':
                state[0].append(z[i])
                state[1].append(float(pKa[i]))
                state[2].append(copysign(float(mobility[i]), z[i])*1e-9)

        # If steep parameters were added, but the length was different,
        # pad the parameters.
        if state[3] and len(state[3]) < len(state[2]):
            state[3].append(0)
        if state[4] and len(state[4]) < len(state[2]):
            state[4].append(0)

        # Add the result to the ion dictionary.
        ion_dict[name] = state

    # boric acid is uniquely in the STEEP database but not the Spresso database
    # add manually.
    ion_dict['boric acid'] = steep_db['boric acid']
    n_steep += 1
    steep_common.append('boric acid')

    ions = shelve.open('ionize/ions_shelve')
    ions.update(ion_dict)
    ions.close()

    print len(ion_dict), 'ions in database'
    print n_steep, 'ions from steep'

    # Check to make that all of the entries in the steep db were added
    for name in steep_db.keys():
        if name not in steep_common:
            print name, 'in Steep database not added'

    # make sure that the length of dCp is the same as the length of z
    for ion in sorted(ion_dict.keys()):
        if ion_dict[ion][3]:
            if len(ion_dict[ion][3]) != len(ion_dict[ion][0]):
                print ion, ion_dict[ion]

if __name__ == "__main__":
    make_database()