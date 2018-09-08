#!/usr/bin/env python
"""
This project is being developed by Kexin Huang & Dewei Liu who are the best friends in the world, since 14 Aug 2018!

(c) 2018 - All rights reserved.

The copyright to the computer program herein is the property
of Kexin Huang & Dewei Liu. The programs may be used and/or copied only with
the written permission from Kexin Huang & Dewei Liu or in accordance with the
terms and conditions stipulated in the agreement/contract under
which the program(s) have been supplied.
********************************************************************
Name    : BestFriends
Purpose : Hunting jobs
********************************************************************
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "BestFriends.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

