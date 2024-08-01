# -*- coding: utf-8 -*-
"""import os
import tempfile
from chaosext.actions import create_local_file

def test_create_local_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as tmp:
        file_path = tmp.name
        file_content = "Hello, World!"
        create_local_file(file_path, file_content)
        assert os.path.exists(file_path)
        with open(file_path, 'r') as f:
            assert f.read() == file_content
def test_create_local_file_with_non_existent_dir():
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, 'ubdir', 'test_file.txt')
        file_content = 'This is a test file.'

        created_file_path = create_local_file(file_path, file_content)

        assert os.path.exists(created_file_path)
        with open(created_file_path, 'r') as f:
            assert f.read() == file_content
"""

