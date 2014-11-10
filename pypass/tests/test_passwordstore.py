#
#    Copyright (C) 2014 Alexandre Viau <alexandre@alexandreviau.net>
#
#    This file is part of python-pass.
#
#    python-pass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-pass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-pass.  If not, see <http://www.gnu.org/licenses/>.
#

import unittest
import os
import shutil
import tempfile

from pypass.passwordstore import PasswordStore


class TestPasswordStore(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()

        # .gpg_id file
        with open(os.path.join(self.dir, '.gpg-id'), 'w') as gpg_id_file:
            gpg_id_file.write('5C5833E3')

    def tearDown(self):
        shutil.rmtree(self.dir)

    def test_init(self):
        store = PasswordStore(self.dir)
        self.assertEqual(store.gpg_id, '5C5833E3')
        self.assertFalse(store.uses_git)
        self.assertEqual(self.dir, store.path)
