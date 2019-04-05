# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

flags = [
        '-Wall',
        '-Wextra',
        '-Werror',
        '-Wc++98-compat',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-DNDEBUG',
        # You 100% do NOT need -DUSE_CLANG_COMPLETER in your flags; only the
        # YCM
        # source code needs it.
        '-DUSE_CLANG_COMPLETER',
        # THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't
        # know which
        # language to use when compiling headers. So it will guess. Badly. So
        # C++ headers will be compiled as C headers. You don't want that so ALWAYS
        # specify a "-std=<something>".
        # For a C project, you would set this to something like 'c99' instead
        # of 'c++11'.
        #'-std=c++0x',  # Uncomment for C++
        '-std=gnu99',   # Uncomment for gnu C  (Works best on linux)
        #'-std=c99',     # Uncomment for Ansi C 99
        # ...and the same thing goes for the magic -x option which specifies
        # the language that the files to be compiled are written in. This is mostly
        # relevant for c++ headers.
        # For a C project, you would set this to 'c' instead of 'c++'.
        #'-x', 'c++',
        '-x', 'c',
        #Here are the libraries for the RaspberryPi2 or 3:
        #THIS IS THE MONEY MAKER:
        #'-isystem', '/usr/include/c++/{}/'.format(''.join(max(os.listdir('/usr/include/c++/')))),
        #'-isystem', '/usr/include/c++/{}/x86_64-pc-linux-gnu'.format(''.join(max(os.listdir('/usr/include/c++/')))),
        #'-isystem', '/usr/include/c++/{dir}/x86_64-pc-linux-gnu'.format(dir=''.join(max(os.listdir('/usr/include/c++/')))),
        #'-isystem', '/usr/include/c++/{}/backward'.format(''.join(max(os.listdir('/usr/include/c++/')))),
        #'-isystem', '/usr/include/c++/7.3.1/backward',
        '-isystem', '/usr/include/clang/',
        '-isystem', '/usr/lib/clang/{}/include'.format(''.join(os.listdir('/usr/lib/clang/')[:][0])),
        '-isystem', '/usr/local/include',
        '-isystem', '/usr/include',
        #'-isystem', '/opt/ros/kinetic/',
        #'-isystem', '/opt/ros/kinetic/include/',
        #'-isystem', '/home/nvidia/mast/devel/include/',
        # For other target architectures i.e avr and arm
        #'-isystem', '/usr/lib/gcc/avr/{}/'.format(''.join(os.listdir('/usr/lib/gcc/avr/')[:][0])),
        #'-isystem', '/usr/bin/../lib/gcc/arm-linux-gnueabihf/4.9/include',
        #'-isystem', '/usr/include/arm-linux-gnueabihf',
        '-I', '.'
]


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.C', '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.H', '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }



