def get_chord(scale, key, measure):
    chord = []
    match scale:
        case 1:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return fifth(chord, key)
            elif measure == 2:
                return sixth(chord, key)
            elif measure == 3:
                return fourth(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 2:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return sixth(chord, key)
            elif measure == 2:
                return third(chord, key)
            elif measure == 3:
                return seventh(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 3:
            if measure == 0 or measure == 3:
                return root(chord, key)
            elif measure == 1:
                return fourth(chord, key)
            elif measure == 2:
                return fifth_7(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 4:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return fifth(chord, key)
            elif measure == 2:
                return seventh(chord, key)
            elif measure == 3:
                return fourth(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 5:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return seventh(chord, key)
            elif measure == 2:
                return fourth(chord, key)
            elif measure == 3:
                return fifth(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 6:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return third(chord, key)
            elif measure == 2:
                return second(chord, key)
            elif measure == 3:
                return seventh(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 7:
            if measure == 0:
                return root(chord, key)
            elif measure == 1:
                return fourth(chord, key)
            elif measure == 2:
                return third(chord, key)
            elif measure == 3:
                return second(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None
        case 8:
            if measure == 0 or measure == 3:
                return root(chord, key)
            elif measure == 1:
                return second(chord, key)
            elif measure == 2:
                return third(chord, key)
            else:
                print("Unknown error. Measure was greater than 4.")
                return None


def root(chord, key):
    # First natural chord
    for i in key:
        if key.index(i) == 2 or key.index(i) == 4:
            chord.append(i)
        elif key.index(i) == 0:
            chord.append(i)
            chord.append(i + 12)
    return sorted(chord)

def second(chord, key):
    # Second natural chord
    for i in key:
        if key.index(i) == 1 or key.index(i) == 3 or key.index(i) == 5:
            chord.append(i)
    return sorted(chord)

def third(chord, key):
    # Third natural chord
    for i in key:
        if key.index(i) == 2 or key.index(i) == 4 or key.index(i) == 6:
            chord.append(i)
    return sorted(chord)

def fourth(chord, key):
    # Forth natural chord
    for i in key:
        if key.index(i) == 3 or key.index(i) == 5:
            chord.append(i)
        elif key.index(i) == 0:
            chord.append(i)
            chord.append(i + 12)
    return sorted(chord)


def fifth(chord, key):
    # Fifth natural chord
    for i in key:
        if key.index(i) == 4 or key.index(i) == 6:
            chord.append(i)
        elif key.index(i) == 1:
            chord.append(i)
            chord.append(i + 12)
    return sorted(chord)

def sixth(chord, key):
    # Sixth natural chord
    for i in key:
        if key.index(i) == 0 or key.index(i) == 2:
            chord.append(i)
            chord.append(i + 12)
        elif key.index(i) == 5:
            chord.append(i)
    return sorted(chord)

def seventh(chord, key):
    # Seventh natural chord
    for i in key:
        if key.index(i) == 1 or key.index(i) == 3:
            chord.append(i)
            chord.append(i + 12)
        elif key.index(i) == 6:
            chord.append(i)
    return sorted(chord)

def fifth_7(chord, key):
    # Fifth natural chord
    for i in key:
        if key.index(i) == 4 or key.index(i) == 6:
            chord.append(i)
        elif key.index(i) == 3:
            chord.append(i + 12)
        elif key.index(i) == 1:
            chord.append(i)
            chord.append(i + 12)
    return sorted(chord)