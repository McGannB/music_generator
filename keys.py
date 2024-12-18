def get_key(root, key_type):
    key = [root]
    i = 1
    while len(key) < 7:
        match key_type:
            case 1: #major
                if i == 3:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 2: #natural minor
                if i == 2 or i == 5:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 3: #harmonic minor
                if i == 2 or i == 5:
                    key.append(key[i-1] + 1)
                elif i == 6:
                    key.append(key[i-1] + 3)
                else:
                    key.append(key[i-1] + 2)
            case 4: #dorian mode
                if i == 2 or i == 6:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 5: #mixolydian mode
                if i == 3 or i == 6:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 6: #lydian mode
                if i == 4:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 7: #phrygian mode
                if i == 1 or i == 5:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
            case 8: #locrian mode
                if i == 1 or i == 4:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)

        i += 1
    return key