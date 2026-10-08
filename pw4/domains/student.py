import math
import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def set_mark(self, c_id, score):
        self.marks[c_id] = math.floor(score * 10) / 10.0

    def get_gpa(self, courses):
        c_dict = {c.id: c.credits for c in courses}
        m_list = [self.marks[cid] for cid in self.marks if cid in c_dict]
        c_list = [c_dict[cid] for cid in self.marks if cid in c_dict]

        if not c_list or sum(c_list) == 0:
            return 0.0
        return float(np.sum(np.array(m_list) * np.array(c_list)) / np.sum(c_list))
