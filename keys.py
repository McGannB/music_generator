def get_key(root, key_type):
    key = [root]
    i = 1
    match key_type:
        case 1: #major
            while len(key) < 7:
                if i == 3:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 2: #natural minor
            while len(key) < 7:
                if i == 2 and i == 5:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 3: #harmonic minor
            while len(key) < 7:
                if i == 2 or i == 5:
                    key.append(key[i-1] + 1)
                elif i == 6:
                    key.append(key[i-1] + 3)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 4: #dorian mode
            while len(key) < 7:
                if i == 2 or i == 6:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 5: #mixolydian mode
            while len(key) < 7:
                if i == 3 or i == 6:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 6: #lydian mode
            while len(key) < 7:
                if i == 4:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 7: #phrygian mode
            while len(key) < 7:
                if i == 1 or i == 5:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key
        case 8: #locrian mode
            while len(key) < 7:
                if i == 1 or i == 4:
                    key.append(key[i-1] + 1)
                else:
                    key.append(key[i-1] + 2)
                i += 1
            return key