import re
import pytest
class change_calculater:
    def __init__(self,presented_amount,product_price):
        self.presented_amount=presented_amount
        self.product_price=product_price
        self.denom={"Dollars":{"Denomination":
    ["1¢","5¢","10¢","25¢","50¢","$1","$2","$5","$10","$20","$50","$100","$200"],
    "Convertor":{"$":100,"¢":1},"minimum_currency":"¢","min_val":1
              
              }
}


    def get_change(self):
        output_dict={}
        currency_type=""
        if '$' in self.presented_amount:
            currency_type="Dollars"
            pr_amount=float(self.presented_amount.replace("$",""))
            prod_amt=float(self.product_price.replace("$",""))
        elif 'Rs' or 'rs' in self.presented_amount:
            currency_type="Rupees"
            pr_amount=float(self.presented_amount.replace("Rs",""))
            prod_amt=float(self.product_price.replace("Rs",""))
        else:
            return "Coming soon"
        settings={}
        denomination_dict={}
        if currency_type in self.denom:
            settings=self.denom[currency_type]
            for i in settings["Denomination"]:
                dig=int(re.findall("\d+",i)[0])
                curr=re.sub("\d+", "", i)
                if curr in settings["Convertor"]:
                    dig*=settings["Convertor"][curr]
                    denomination_dict[dig]={"orig_val":i}


        nd={}
        for key in reversed(sorted(denomination_dict)):
            nd[key] = denomination_dict[key]


        # nominals = [1000, 500, 100, 50, 20, 5, 1,.3,.1]
        nominals = nd
        change_upper=100
        amount = float(pr_amount-prod_amt)
        amount*=change_upper
        output = {}
        result={}
        result['currency']=currency_type
        result['amount']=pr_amount
        result['price']=prod_amt
        result['change']=pr_amount-prod_amt
        for n in nominals:
            output[n] = amount // n
            amount %= n
        for k, v in output.items():
            if v>0:
                # print(f'{denomination_dict[k]["orig_val"]} * {int(v)}')
                result[denomination_dict[k]["orig_val"]]= int(v)
        return result       
price_amount=input("Enter the prced amount= ")
product_price=input("enter the product price=")
obj=change_calculater(price_amount,product_price)
print(obj.get_change())
