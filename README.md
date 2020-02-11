# cookiecutter-script

[Cookiecutter](https://cookiecutter.rtfd.io) template to generate a bash
script project layout.

## Layout

This repository provides the following file tree layout:

```
script/
├── docs
│   ├── requirements.txt
│   ├── source
│   │   ├── api
│   │   │   ├── scripts
│   │   │   │   └── script.inc
│   │   │   └── scripts.inc
│   │   ├── api.rst
│   │   ├── author.rst
│   │   ├── compatibility.rst
│   │   ├── conf.py
│   │   ├── description.rst
│   │   ├── index.rst
│   │   ├── license.rst
│   │   ├── links.rst
│   │   ├── parameters
│   │   │   └── help.inc
│   │   ├── parameters.rst
│   │   ├── _static
│   │   │   └── .gitkeep
│   │   ├── uml.rst
│   │   └── usage.rst
│   └── uml
│       └── flow.mmd
├── docthis.sh
├── .gitignore
├── img
│   ├── author.png
│   ├── avatar.png
│   └── flow.png
├── LICENSE
├── README.rst
├── .readthedocs.yml
├── script.sh
└── tests
    └── script.bats
```

## Usage

Install *Cookiecutter*:

```
python3 -m pip install cookiecutter
```

Generate the project using *Cookiecutter*:

```
cookiecutter https://github.com/cslucr/cookiecutter-script.git
```

## License

GPL 3. See the
[LICENSE](https://git.beta.ucr.ac.cr/cslucr/plantillas/cookiecutter-script/raw/master/LICENSE)
file for more details.

## Links

  - [Github repository](https://github.com/cslucr/cookiecutter-script).
  - [Gitlab repository](https://git.beta.ucr.ac.cr/cslucr/plantillas/cookiecutter-script).

## Author Information

[![cslucr](https://git.beta.ucr.ac.cr/cslucr/plantillas/cookiecutter-script/raw/master/img/author.png)](https://git.beta.ucr.ac.cr/cslucr)

Comunidad de Software Libre de la Universidad de Costa Rica
