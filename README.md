# Poetry Namespace Packaging Test

This is a demo repository including:

* Transitive path dependencies in develop mode:
  - `foo-platform-common` -> {`foo-core`}
  - `foo-platform-api` -> {`foo-core`, `foo-platform-common`}
* Implicit (native) namespace packaging with heterogeneous levels of nesting:
  - `foo` prefix shared across all 3 packages
  - `foo.platform` prefix shared across 2 packages

## To run stuff

Try `cd foo-platform-api && poetry install && poetry run pytest .`. You should see a failing test assertion along with
some captured stdout indicating that packaging and imports worked as expected.

You might also try to change a print statement in either `foo-core` or `foo-platform-common` and rerun the tests to see
that indeed the output changes in response to the current state of the code in your local repository.
