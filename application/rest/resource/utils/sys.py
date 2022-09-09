import os
import shutil
import tempfile

from flask import request
from marshmallow.exceptions import ValidationError


def get_file(filename: str, *mimetypes: str):
    if filename not in request.files:
        raise ValidationError({filename: 'missing required file'})

    file = request.files[filename]

    if file.content_type not in mimetypes:
        raise ValidationError({
            filename: f'invalid mime type {file.content_type}. '
                      f'It has to be {mimetypes}'
        })

    return file


def make_dir(dirname: str):
    if os.path.exists(dirname):
        shutil.rmtree(dirname, ignore_errors=True)

    os.mkdir(dirname)


def make_tmp_dir(dir_prefix: str):
    return tempfile.mkdtemp(prefix=dir_prefix)


def rm_dir(dirname: str):
    shutil.rmtree(dirname, ignore_errors=True)
