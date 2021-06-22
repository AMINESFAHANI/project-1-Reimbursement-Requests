class Manager:
    def __init__(self, m_id: int = 0, m_name: str = "", m_username: str = "", m_password: str = ""):
        self.m_id = m_id
        self.m_name = m_name
        self.m_username = m_username
        self.m_password = m_password


    def __str__(self):
        return f"m_id={self.m_id},m_name={self.m_name},m_password = {self.m_password},m_username={self.m_username}"

    def serialized(self) -> dict:
        return {"mId": self.m_id, "mName": self.m_name, "mPassword": self.m_password, "mUsername": self.m_username}

    @staticmethod
    def deserialized(dic: dict):
        manager = Manager()
        manager.m_id = dic["mId"]
        manager.m_name = dic["mName"]
        manager.m_password = dic["mPassword"]
        manager.m_username = dic["mUsername"]
        return manager
