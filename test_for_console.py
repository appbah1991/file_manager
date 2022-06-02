import shutil
import os
import sys

def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)

def test_copy_file_or_directory(name):
    result = []
    include = False
    for item in os.listdir():
        result.append(item)
    for dirpath, dirnames, filenames in os.walk("."):
        for dirname in dirnames:
            result.append(os.path.join(dirname))
    if name in result:
        include = True
    assert include == True
test_copy_file_or_directory(name = 'bank_prog.py')

###############

def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result
def test_filenames():
    assert filenames() == ['adfasdf', 'bank_prog.py', 'main.py', 'test_for_console.py', 'test_python.py', 'victory.py']
test_filenames()

################
def author_info():
    return 'Leonid Orlov'
def test_author_info():
    assert author_info() == 'Leonid Orlov'
test_author_info()

################
def quit():
    sys.exit(0)

def test_exit(mymodule = quit()):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
            mymodule.will_exit_somewhere_down_the_stack()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 42
test_exit()