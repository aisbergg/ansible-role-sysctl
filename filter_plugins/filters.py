class FilterModule(object):
    def filters(self):
        return {
            'config_path': self.config_path,
            'excess_configs': self.excess_configs
        }

    def config_path(self, config):
        assert isinstance(config, dict)
        return "/etc/sysctl.d/{}-{}.conf".format(config.get("order", "00"), config.get("file"))

    def excess_configs(self, files_stat, sysctl_d):
        existing_configs = set([stat["path"] for stat in files_stat])
        new_configs = set([self.config_path(s) for s in sysctl_d])
        return list(existing_configs - new_configs)
