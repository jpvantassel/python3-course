# Checklist for Releasing a Python Project

> Joseph P. Vantassel, [jpvantassel.com](https://www.jpvantassel.com/)

[![License](https://img.shields.io/badge/license-CC--By--SA--4.0-brightgreen.svg)](https://github.com/jpvantassel/python3-course/blob/main/LICENSE.md)

## General Procedure

1. __Commit last code change to `dev` branch.__
2. __Check GitHub `README.md`.__ Check to ensure new features are included in the
projects description. Consider adding new interesting figures.
3. __Check all `examples`__ provided in the repository. This should include
re-running all example notebooks and recreating all figures presented in the
repositories `README.md`.
4. __Check the version number__ has been appropriately incremented. Note that the
version number should be "single-sourced" throughout the entire package.
5. __Commit any changes__, note then as having been completed in preparation for
release.
6. __Run tests locally__ using `tox`, this should result in a sucessful test. If
any of the tests fail, make the appropriate changes and repeat the steps listed
above to confirm the changes to fix the broken test did not have any adverse
effects.
7. __Push code following successful local test.__
8. __Confirm CircleCI build was successful.__ Make any changes necessary to
ensure successful CircleCI build and repeat the steps listed above.
9. __Open pull request__ from `dev` to `main` GitHub branch.
10. __Wait for LGTM, CircleCI, and Codecov to comment on pull request.__
11. __Fix any issues__ and repeat the procedure above. If several issues are
raised prefer to delay the pull request rather than pushing ahead. Once the
issues have been fixed repeat the process above.
12. __Close pull request to merge `dev` into `main`__.
13. __Change local branch to `main` and publish package to PyPI__. Remember
to `git pull` on your local machine in ensure `main` is consistent with the
remote branch.
14. __Add annotated git tag with version number__ and push to GitHub. Making a
tag is useful for posterity as well as easily creating a formal release.
15. __Make formal release on GitHub__ using the created tag. In the release
notes describe what changes have been made using a short bulleted list.
