# Slugs Extension

Slugs is an extension for Foliant to generate custom slugs from arbitrary lists of values.

It resolves `!slug`, `!date`, `!version`, and `!commit_count` YAML tags in the project config.

The list of values after the `!slug` tag is replaced with the string that joins these values using `-` delimeter. Spaces (` `) in the values are replaced with underscores (`_`).

The value of the node that contains the `!date` tag is replaced with the current local date.

The list of values after the `!version` tag is replaced with the string that joins these values using `.` delimeter.

The value of the node that contains the `!commit_count` tag is replaced by the number of commits in the current Git repository.

## Installation

```bash
$ pip install foliantcontrib.slugs
```

## Usage

### Slug

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

### Version

Config example:

```yaml
version: !version [1, 0, 5]
```

Resulting version:

```
1.0.5
```

If you wish to use the number of commits in the current branch as a part of your version, add the `!commit_count` tag:

```yaml
version: !version
    - 1
    - !commit_count
```

Resulting version:

```
1.85
```

The `!commit_count` tag accepts two arguments:

* name of the branch to count commits in;
* correction — a positive or negative number to adjust the commit count.

Suppose you want to bump the major version and start counting commits from the beginning. Also you want to use only number of commits in the `master` branch. So your config will look like this:

```yaml
version: !version
    - 2
    - !commit_count master -85
```

Result:

```
2.0
```
