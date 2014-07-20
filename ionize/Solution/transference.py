def transference(obj):
    """Return the fraction of charge carried by each of the ions as a list.

    Should not precisely add to 1, because some charge is carried by protons
    and hydroxyls.
    """
    T = [0] * len(obj.ions)
    for i in range(len(T)):
        T[i] = (obj.ions[i].molar_conductivity(obj.pH, obj.I) *
                obj.concentrations[i])

    T = [tp / obj.conductivity() for tp in T]
    return T