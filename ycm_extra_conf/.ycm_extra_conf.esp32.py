import os
import ycm_core

flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-ferror-limit=10000',
    '-DNDEBUG',
    '-std=gnu99',
    '-xc',
    '-isystem/usr/include',
]



# Add the paths for the ESP-IDF framework
esp_idf_path = os.environ['IDF_PATH']
componets = os.path.join(esp_idf_path, 'components')

flags.extend([
    '-I' + os.path.join(esp_idf_path, 'components'),
    '-I' + os.path.join(esp_idf_path, 'components', 'esp_common','include'),
    # Add more include paths as needed
])



def find_headders(base_path):
    """TODO: Docstring for find_headders.
    :returns: None

    """
    headder_dirs = []
    if not os.path.exists(base_path):
        return
    for root,dirs,files in os.walk(base_path):
        if 'include' in dirs:
            headder_dirs.append(os.path.join(root, 'include'))
        else:
            for file in files:
                if file.endswith('.h') or file.endswith('.hpp'):
                    absroot = os.path.abspath(root)
                    if absroot not in headder_dirs:
                        headder_dirs.append(absroot)
    for path in headder_dirs:
        flags.append('-I' + path)

def Settings( **kwargs ):
    find_headders(componets)
    return {
        'flags': flags,
        'do_cache': True
    }
