class Rr:
    def __init__(self, rr_id: int = 0, rr_amount: int = 0, rr_reason: str = "", rr_status: str = "pending", rr_e_id: int = 0):
        self.rr_id = rr_id
        self.rr_amount = rr_amount
        self.rr_reason = rr_reason
        self.rr_status = rr_status
        self.rr_e_id = rr_e_id

    def __str__(self):
        return f"rr_id={self.rr_id},rr_amount={self.rr_amount},rr_reason = {self.rr_reason},rr_status={self.rr_status}, rr_e_id={self.rr_e_id}"

    def serialized(self) -> dict:
        return {"rrId": self.rr_id, "rrAmount": self.rr_amount, "rrReason": self.rr_reason, "rrStatus": self.rr_status, "rrEId": self.rr_e_id}

    @staticmethod
    def deserialized(dic: dict):
        rr = Rr()
        rr.rr_id = dic["rrId"]
        rr.rr_amount = dic["rrAmount"]
        rr.rr_reason = dic["rrReason"]
        rr.rr_status = dic["rrStatus"]
        rr.rr_e_id = dic["rrEId"]
        return rr
