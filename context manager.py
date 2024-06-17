import sys
from contextmanager import contextmanager

def usage():
    """Prints usage instructions when insufficient arguments are provided."""
    print(f"Usage: {sys.argv[0]} OUTFILE INFILEs")
    exit(1)

if len(sys.argv) < 3:
    usage()

outfile = sys.argv[1]
infiles = sys.argv[2:]

@contextmanager
def myopen(outfile, *infiles):
    """Efficiently opens the output and input files for reading/writing."""
    out_fh = open(outfile, 'w')
    try:
        input_fhs = [open(filename, 'r') for filename in infiles]
        yield out_fh, input_fhs
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        for fh in input_fhs:
            fh.close()
        out_fh.close()

with myopen(outfile, *infiles) as (out_fh, input_fhs):
    while True:
        row = []  # Use a list for efficient row construction
        any_data = False  # Track if any data was read

        for infh in input_fhs:
            line = infh.readline().rstrip("\n")  # Remove trailing newline
            if line:
                any_data = True
                row.append(line)  # Append line directly to the list
            else:
                break  # Break from inner loop if EOF is reached for a file

        if any_data:  # Only write a row if data was read from at least one file
            out_fh.write(','.join(row))
            out_fh.write('\n')

        if not any_data:
            break  # Break from outer loop if no data is read from any files

print(f"Successfully combined data into '{outfile}'.")
