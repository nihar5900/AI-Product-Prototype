def process_encode(fet, encoder):
    return encoder.transform([fet])[0]

def encode_YN(x):
    if x == 'Yes':
        return 1
    else:
        return 0
