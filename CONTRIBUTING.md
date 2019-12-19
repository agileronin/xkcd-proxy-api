# Contributor's Guide

Thanks for your interest in the project! We welcome pull requests from developers of all skill levels. To get started, simply fork the master branch on GitHub to your personal account and then clone the fork into your development environment.

The core project maintainers are:

* Gregory Mundy, Project Lead (**agileronin** on GH, and **graygoree** and Twitter)

Feel free to reach out if you have any questions, or just need a little help getting started. Please note that all contributors and maintainers of this project are subject to our [Code of Conduct][coc].

### Pull Requests

Before submitting a pull request, please ensure you have added or updated tests as appropriate, and that all existing tests still pass with your changes. Please also ensure that your coding style follows PEP 8.

#### Reviews

The creators of this project believe in developing high quality software that is stable and reliable, no matter how trivial the project may be.
Therefore, we invest a lot of time in carefully reviewing PRs and working with contributors to ensure that every patch merged into the master branch is correct, complete, performant, well-documented, and appropriate.

Project maintainers review each PR for the following:

- [ ] **Design.** Does it do the right thing? Is the end goal well understood and correct?
- [ ] **Correctness.** Is the logic correct? Does it behave correctly according to the goal of the feature or bug fix?
- [ ] **Fit.** Is this feature or fix in keeping with the spirit of the project? Would this idea be better implemented as an add-on?
- [ ] **Standards.** Does this change align with approved or standards-track RFCs, de-facto standards, and currently accepted best practices?
- [ ] **Tests.** Does the PR implement sufficient test coverage in terms of value inputs, Python versions, and lines tested?
- [ ] **Compatibility.** Does it work across all supported Python versions and operating systems?
- [ ] **Performance.** Will this degrade application performance? Are there opportunities to optimize the implementation?
- [ ] **Docs.** Does this impact any existing documentation or require new documentation? If so, does this PR include the aforementioned docs, and is the language friendly, clear, helpful, and grammatically correct with no misspellings? Do all docstrings conform to Google style ala [sphinx.ext.napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html)?
- [ ] **Dependencies.** Does this PR bring in any unnecessary dependencies that would prevent us from keeping the application lean and mean, jeopardize the reliability of the project, or significantly increase security risks?

### Test coverage

Pull requests must maintain 100% test coverage of all code branches. This helps ensure the quality of the application.

### Code style rules

* Docstrings are required for classes, attributes, methods, and functions.
* Docstrings should utilize the [napolean style][docstrings] in order to make them read well, regardless of whether they are viewed through `help()` or on [Read the Docs][rtd].
* Please try to be consistent with the way existing docstrings are formatted. In particular, note the use of single vs. double backticks as follows:
    * Double backticks
        * Inline code
        * Variables
        * Types
        * Decorators
    * Single backticks
        * Methods
        * Params
        * Attributes
* Format non-trivial comments using your GitHub nick and one of these prefixes:
    * TODO(riker): Damage report!
    * NOTE(riker): Well, that's certainly good to know.
    * PERF(riker): Travel time to the nearest starbase?
    * APPSEC(riker): In all trust, there is the possibility for betrayal.
* When catching exceptions, name the variable `ex`.
* Use whitespace to separate logical blocks of code and to improve readability.
* No single-character variable names except for trivial indexes when looping,
or in mathematical expressions implementing well-known formulas.
* Heavily document code that is especially complex and/or clever.
* When in doubt, optimize for readability.

### Commit Message Format

Falcon's commit message format uses [AngularJS's style guide][ajs], reproduced here for convenience, with some minor edits for clarity.

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

No line may exceed 100 characters. This makes it easier to read the message on GitHub as well as in various git tools.

#####  Type
Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **refactor**: A code change that neither fixes a bug or adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

##### Scope
The scope could be anything specifying place of the commit change. For example: `$location`, `$browser`, `$compile`, `$rootScope`, `ngHref`, `ngClick`, `ngView`, etc...

##### Subject
The subject contains succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize first letter
* no dot (.) at the end

##### Body
Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes"The body should include the motivation for the change and contrast this with previous behavior.

##### Footer
The footer should contain any information about **Breaking Changes** and is also the place to reference GitHub issues that this commit **Closes**.

[ajs]: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines
[docstrings]: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google-style-python-docstrings
[rtd]: https://readthedocs.org/
[coc]: https://github.com/agileronin/repository-template/blob/master/CODE_OF_CONDUCT.md
