# Codar: Code Architecture System
A command-line tool for auditing and understanding your codebase i.e. a radar for your code.

## Features

Codar offers a couple of very useful terminal commands to help you analyze your repository:

| Feature       | Description                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| `codar report` | Export a full audit/report of the codebase, ideally with visual graphs and summaries.                           |
| `codar stats`  | Show code metrics: LOC, comments, whitespace ratio, churn, test coverage, etc.                                  |
| `codar graph`  | Output call graph, class hierarchy, and module dependencies (e.g. to `.dot`, `.svg`, or terminal).              |
| `codar dead`  | Identify dead code, duplicated logic, or overly complex parts.                                                  |

Additionally, Codar ...
+ ingores files and directories specified in `.gitignore` and `.codarignore` (where you can optionally ignore gitignore)


## Install

Get started with:
```bash
pip install git+https://github.com/QuentinWach/codar.git
```



