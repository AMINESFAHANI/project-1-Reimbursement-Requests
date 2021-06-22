class Employee:
    def __init__(self, e_id: int = 0, e_name: str = "", e_username: str = "", e_password: str = ""):
        self.e_id = e_id
        self.e_name = e_name
        self.e_username = e_username
        self.e_password = e_password


    def __str__(self):
        return f"e_id={self.e_id},e_name={self.e_name},e_password = {self.e_password},e_username={self.e_username}"

    def serialized(self) -> dict:
        return {"eId": self.e_id, "eName": self.e_name, "ePassword": self.e_password, "eUsername": self.e_username}

    @staticmethod
    def deserialized(dic: dict):
        employee = Employee()
        employee.e_id = dic["eId"]
        employee.e_name = dic["eName"]
        employee.e_password = dic["ePassword"]
        employee.e_username = dic["eUsername"]
        return employee
