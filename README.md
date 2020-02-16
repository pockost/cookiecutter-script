# cookiecutter-script

[Cookiecutter](https://cookiecutter.rtfd.io) template to generate a bash
script project layout.

## Usage

Install *Cookiecutter*:

```
python3 -m pip install cookiecutter
```

Generate the project using *Cookiecutter*:

```
cookiecutter https://github.com/cslucr/cookiecutter-script.git
```

## Layout

This repository provides the following file tree layout:

```
script/
├── doc
│   ├── requirements.txt
│   ├── source
│   │   ├── api
│   │   │   ├── script
│   │   │   │   └── script.inc
│   │   │   └── script.inc
│   │   ├── api.rst
│   │   ├── author.rst
│   │   ├── compatibility.rst
│   │   ├── conf.py
│   │   ├── description.rst
│   │   ├── index.rst
│   │   ├── license.rst
│   │   ├── link.rst
│   │   ├── parameter
│   │   │   └── help.inc
│   │   ├── parameter.rst
│   │   ├── _static
│   │   │   └── .gitkeep
│   │   ├── uml.rst
│   │   └── usage.rst
│   └── uml
│       └── flow.mmd
├── docthis.sh
├── .gitignore
├── .gitlab
│   └── issue_templates
│       ├── Bug.md
│       └── Feature.md
├── .gitlab-ci.yml
├── img
│   ├── author.png
│   ├── avatar.png
│   └── flow.png
├── LICENSE
├── README.rst
├── .readthedocs.yml
├── script.sh
├── test
│   └── script.bats
├── testme.sh
└── .travis.yml
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
