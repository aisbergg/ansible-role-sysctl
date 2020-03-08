class FilterModule(object):
    def filters(self):
        return {
            'config_path': self.config_path,
        }

    def config_path(self, config):
        assert isinstance(config, dict)
        return "/etc/sysctl.d/{}-{}.conf".format(config.get("order", "00"), config.get("file"))
