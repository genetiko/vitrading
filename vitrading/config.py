from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="VITRADING",
    settings_files=['settings.yaml', '.secrets.yaml'],
)
