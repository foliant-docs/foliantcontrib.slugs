# Slugs Extension

Slugs is an extension for Foliant to generate custom slugs from arbitrary lists of values.

It resolves `!slug` and `!date` YAML tags in the project config.

The list of values after the ``!slug`` tag is replaced with the string that joins these values using ``-`` delimeter. Spaces (` `) in the values are replaced with underscores (`_`).

The value of the node that contains the `!date` tag is replaced with the current local date.

## Installation

```bash
$ pip install foliantcontrib.slugs
```

## Usage

Config example:

```yaml
title: &title My Awesome Project
version: &version 1.0
slug: !slug
    - *title
    - *version
    - !date
```

Example of the resulting slug:

```
My_Awesome_Project-1.0-2018-05-10
```

Note that backends allow to override the top-level slug, so you may define different custom slugs for each backend:

```yaml
backend_config:
    pandoc:
        slug: !slug
            - *title
            - *version
            - !date
    mkdocs:
        slug: my_awesome_project
```
