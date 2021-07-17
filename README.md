# Poetry Namespace Packaging Test

A demo repository including:

* Transitive path dependencies in develop mode:
  - `foo-platform-common` -> {`foo-core`}
  - `foo-platform-api` -> {`foo-core`, `foo-platform-common`}
* Implicit (native) namespace packaging with heterogeneous levels of nesting:
  - `foo` prefix shared across all 3 packages
  - `foo.platform` prefix shared across 2 packages
