'''OpenGL extension AMD.sample_positions

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.sample_positions to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism to explicitly set sample positions for a
	FBO with multi-sampled attachments. The FBO will use identical sample locations
	for all pixels in each attachment. This forces TEXTURE_FIXED_SAMPLE_LOCATIONS
	to TRUE if a multi-sampled texture is specified using TexImage2DMultisample
	or TexImage3DMultisample. That is, using GetTexLevelParameter to query
	TEXTURE_FIXED_SAMPLE_LOCATIONS will always return TRUE if the mechanism is
	explicitly used to set the sample positions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/sample_positions.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.sample_positions import *
from OpenGL.raw.GL.AMD.sample_positions import _EXTENSION_NAME

def glInitSamplePositionsAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION