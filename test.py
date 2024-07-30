from lib.compile_to_c import compile_to_c
from lib.encoder import encode

if __name__ == '__main__':
    c_string = encode('sample.py')
    compile_to_c(c_string, 'outfile')