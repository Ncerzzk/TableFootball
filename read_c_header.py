
import re
import unittest

class C_Enum:
    def __init__(self,str):
        self.contents=str
        if self.contents.find(",")<0:
            self.startnum=0
        else:
            result=re.findall(r"\S+\s*=(.+?)\s*,",self.contents)
            if len(result)!=0:
                self.startnum=int(result[0].strip())
            else:
                self.startnum=0


    def get(self,item_name):
        pattern=re.compile(r"%s\s*=(.+?)\s*,"%item_name)
        result=re.findall(pattern,self.contents)

        if len(result)==0:
            result=self.contents.split(",")
            for index,item in enumerate(result):
                if item.strip() == item_name:
                    return index+self.startnum
        else:
            return int(result[0].strip())


class C_Header:
    def __init__(self,filename):
        self.contents=None
        with open(filename,"r") as f:
            self.contents=f.read()
        self.enum_types=self.get_enum_types()

    def get_enum_types(self):
        ss =re.compile(r"typedef\s+enum\s*{(.+?)}\s*(\S+);",re.DOTALL)
        result=re.findall(ss,self.contents)
        dic={}
        for i in result:
            dic[i[1]]=C_Enum(i[0])
        return dic

    def get_enum(self,name):
        return self.enum_types[name]


class C_Enum_Test(unittest.TestCase):
    def test_funcs(self):
        header = C_Header("datatypes.h")
        self.assertEqual(len(header.enum_types),49)
        self.assertEqual(header.get_enum("BATTERY_TYPE").get("BATTERY_TYPE_LEAD_ACID"),2)
        self.assertEqual(header.get_enum("mc_state").get("MC_STATE_FULL_BRAKE"),3)

