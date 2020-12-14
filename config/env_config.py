import decouple

class EnvConfig:
    def __init__(self):
        self.aws_access_key_id = decouple.config("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = decouple.config("AWS_SECRET_ACCESS_KEY")


env_config = EnvConfig()
