# Chaos Toolkit (ChaosToken)

[![Version](https://img.shields.io/pypi/v/chaostoolkit-my-extension.svg)](https://img.shields.io/pypi/v/chaostoolkit-lib.svg)
[![License](https://img.shields.io/pypi/l/chaostoolkit-my-extension.svg)](https://img.shields.io/pypi/l/chaostoolkit-lib.svg)

[![Build, Test, and Lint](https://github.com/chaostoolkit/chaostoolkit-extension-template/actions/workflows/build.yaml/badge.svg)](https://github.com/chaostoolkit/chaostoolkit-extension-template/actions/workflows/build.yaml)
[![Python versions](https://img.shields.io/pypi/pyversions/chaostoolkit-my-extension.svg)](https://www.python.org/)


## Install

This package requires Python 3.7+

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install git+https://github.com/deceptiveChaos/chaosToken.git
```


## Usage

<Explain your probes and actions usage from the experiment.json here>

To use the probes and actions from this package, add the following to your experiment file:
```json
{
    "type": "action",
    "name": "deploy-token",
    "provider": {
        "type": "python",
        "module": "chaosext.actions",
        "func": "send_files_to_host",
        "arguments": {
            "folder_path": "fake_files",
            "host": "192.168.163.128",
            "username": "kali",
            "password": "kali",
            "remote_folder": "Home",
            "remote_subfolder": ["Desktop","Documents","Downloads"]
        }
      }
    }
```

```json
{
      "type": "action",
      "name": "deploy-token",
      "provider": {
        "type": "python",
        "module": "chaosext.actions",
        "func": "send_files_to_hosts",
        "arguments": {
          "folder_path": "fake_files",
          "hosts": [
            {
              "host": "192.168.163.129",
              "username": "kali",
              "password": "kali",
              "remote_folder": "Home",
              "remote_subfolder": ["Desktop","Documents","Downloads"]
            },
            {
              "host": "192.168.163.128",
              "username": "kali",
              "password": "kali",
              "remote_folder": "Home",
              "remote_subfolder": ["Desktop","Documents","Downloads"]
            }
          ]
        }
      }
    }
```

Please explore the code to see existing probes and actions.

## Configuration

<Specify any extra configuration your extension relies on here>
Users would need to store the tokens in their own folder and use that folder in "folder_path".

## Test

To run the tests for the project execute the following:

```
$ pdm run test
```

### Formatting and Linting

We use a combination of [`black`][black], [`ruff`][ruff], and [`isort`][isort]
to both lint and format this repositories code.

[black]: https://github.com/psf/black
[ruff]: https://github.com/astral-sh/ruff
[isort]: https://github.com/PyCQA/isort

Before raising a Pull Request, we recommend you run formatting against your
code with:

```console
$ pdm run format
```

This will automatically format any code that doesn't adhere to the formatting
standards.

As some things are not picked up by the formatting, we also recommend you run:

```console
$ pdm run lint
```

To ensure that any unused import statements/strings that are too long, etc.
are also picked up.

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [black][blackstyle] code style, sprinkling with tests and submit a PR for
review.

[blackstyle]: https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html

To contribute to this project, you will also need to install [pdm][].

[pdm]: https://pdm.fming.dev/latest/
