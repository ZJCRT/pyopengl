'''OpenGL extension EXT.texture_type_2_10_10_10_REV

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.texture_type_2_10_10_10_REV to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_type_2_10_10_10_REV.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.texture_type_2_10_10_10_REV import *
from OpenGL.raw.GLES2.EXT.texture_type_2_10_10_10_REV import _EXTENSION_NAME

def glInitTextureType2101010RevEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION