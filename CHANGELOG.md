# Changelog

All notable changes to this project will be documented in this file.

- [3.0.0 (2021-10-12)](#300-2021-10-12)
- [2.1.0 (2020-06-10)](#210-2020-06-10)
- [2.0.0 (2020-06-10)](#200-2020-06-10)
- [1.3.0 (2020-05-19)](#130-2020-05-19)
- [1.2.0 (2020-03-10)](#120-2020-03-10)
- [1.1.0 (2020-03-08)](#110-2020-03-08)
- [1.0.1 (2020-02-07)](#101-2020-02-07)

---

<a name="3.0.0"></a>
## [3.0.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v2.1.0...v3.0.0) (2021-10-12)

### Bug Fixes

- correctly use boolean test
- correct Ansible version requirement

### CI Configuration

- add Github action for automatic releases

### Chores

- update changelog
- update development configs
- use google as yapf base style
- **.ansible-lint:** update linter config
- **.pre-commit-config.yaml:** bump pre-commit hook versions
- **CHANGELOG.md:** update changelog
- **CHANGELOG.md:** update changelog
- **CHANGELOG.md:** update changelog
- **CHANGELOG.tpl.md:** update changelog template
- **requirements.yml:** add role requirements

### Code Refactoring

- drop support for Ansible < 2.10
- clean up

### Documentation

- add 'required' note

### Features

- ensure the rendered templates change everytime
- link /etc/sysctl.conf to /etc/sysctl.d/99-sysctl.conf
- rename `variables` to `parameters`
- add 'sysctl_d_clear_whitelist' option
- rename sysctl_clear_configurations option and remove jmespath dependency
- add option sysctl_clear_configurations


<a name="2.1.0"></a>
## [2.1.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v2.0.0...v2.1.0) (2020-06-10)

### Chores

- **CHANGELOG.md:** update changelog


<a name="2.0.0"></a>
## [2.0.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v1.3.0...v2.0.0) (2020-06-10)

### Bug Fixes

- correctly use boolean test


<a name="1.3.0"></a>
## [1.3.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v1.2.0...v1.3.0) (2020-05-19)

### Bug Fixes

- correct Ansible version requirement

### Code Refactoring

- clean up


<a name="1.2.0"></a>
## [1.2.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v1.1.0...v1.2.0) (2020-03-10)

### Chores

- **CHANGELOG.md:** update changelog


<a name="1.1.0"></a>
## [1.1.0](https://github.com/aisbergg/ansible-role-sysctl/compare/v1.0.1...v1.1.0) (2020-03-08)

### Features

- add option sysctl_clear_configurations


<a name="1.0.1"></a>
## [1.0.1]() (2020-02-07)

Initial Release
