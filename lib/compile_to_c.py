import shlex
import subprocess

def get_cflags():
    return shlex.split(subprocess.check_output(['python3-config', '--cflags']).decode().strip('\n'))

def get_ldflags():
    return shlex.split(subprocess.check_output(['python3-config', '--ldflags']).decode().strip('\n'))

def compile_to_c(c_string: str, name: str):
    with subprocess.Popen(
        ['gcc', '-o', name, '-x', 'c', '-', *get_cflags(), *get_ldflags(), '-lpython3.10'], 
        stdin=subprocess.PIPE,
        text=True
    ) as proc:
        proc.communicate(input=c_string)