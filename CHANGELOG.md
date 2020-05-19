# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2020-05-19
### Added
- Whitelist option to keep files when using `sysctl_d_clear: true`

### Changed
- Correct required Ansible version
- Clean up

## [1.2.0] - 2020-03-10
### Changed
- Remove `jmespath` dependency
- Rename option `systemctl_clear_configurations` to `sysctl_d_clear`

## [1.1.0] - 2020-03-08
### Added
- Option `sysctl_d_clear` to remove all left over configurations in `/etc/sysctl.d`

## [1.0.1] - 2020-02-07
### Changed
- Formatted code

## [1.0.0] - 2020-02-03
### Added
- First version of the role
