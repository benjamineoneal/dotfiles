#!/usr/bin/env python3

"""
DESCRIPTION

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details. You
should have received a copy of the GNU General Public License along with this
program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Benjamin O'Neal"
__authors__ = ["Benjamin O'Neal", "Another", "etc"]
__contact__ = "benjaminoneal1989@gmail.com"
__copyright__ = "Copyright YEAR, Benjamin O'Neal"
__credits__ = ["Another", "Another", "etc"]
__date__ = "yyyy/mm/dd"
__deprecated__ = "false"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Prototype" # Needs to be Prototype, Development, or Production
__version__ = "0.0.1"

import sys
import os

# Get scriptname as variable
sriptName = os.path.basename(__file__)

def showUsage():
    print(f"Usage: {scriptName} filename")
    print("Options:")
    print("  --help, -h     Show this usage information")
    print("  --verbose, -v  Print additional details during execution.")

# Check for help flag
if "--help" in sys.argv or "-h" in sys.argv:
    showUsage()

# Check for verbose flag
verbose = "--verbose" in sys.argv or "-v" in sys.argv

# Example verbose message to add to step
# if verbose:
    # print(f"Logging Info.")
