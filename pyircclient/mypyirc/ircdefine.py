"""
Copyright (c) 2012, Thomas Recouvreux
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

#####
## <PREFIX_CMD><IRC_CMD><SEP><ARG1><SEP><ARG2>
#####
SEP					= " "
PREFIX_CMD			= "."

CANAL_ERRORS		= "#errors"

"""
1 - Black
2 - Navy Blue
3 - Green
4 - Red
5 - Brown
6 - Purple
7 - Olive
8 - Yellow
9 - Lime Green
10 - Teal
11 - Aqua Light
12 - Royal Blue
13 - Hot Pink
14 - Dark Gray
15 - Light Gray
16 - White
"""
IRCCOLORS = {}
IRCCOLORS['white']			= '0'
IRCCOLORS['black']			= '1'
IRCCOLORS['blue']			= '2'
IRCCOLORS['green']			= '3'
IRCCOLORS['pink']			= '4'
IRCCOLORS['red']			= '5'
IRCCOLORS['purple']			= '6'
IRCCOLORS['brown']			= '7'
IRCCOLORS['yellow']			= '8'
IRCCOLORS['lime_green']		= '9'
IRCCOLORS['teal']			= '10'
IRCCOLORS['aqua_light']		= '11'
IRCCOLORS['royal_blue']		= '12'
IRCCOLORS['hot_pink']		= '13'
IRCCOLORS['dark_gray']		= '14'
IRCCOLORS['light_gray']		= '15'
IRCCOLORS[None]				= ''
COLOR_MARKER				= chr(3)
BOLD_MARKER					= chr(2)


