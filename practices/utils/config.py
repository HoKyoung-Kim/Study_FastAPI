from pydantic_settings import BaseSettings

class MySQLSettings(BaseSettings):
    url: str
    host: str
    port: int
    user: str
    password: str
    name: str

    class Config:
        env_prefix = "MYSQL_"
        env_file = '.env'

        '''
        fields = {
            'm
        }
        '''
settings = MySQLSettings()