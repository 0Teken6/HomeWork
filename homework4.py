class SavingAccount: pass

class CheckingAccount: pass

class BankAccount(SavingAccount, CheckingAccount): pass

class Stock: pass

class Bond: pass

class Security(Stock, Bond): pass

class RealEstate: pass

class Insurableltem(RealEstate, BankAccount): pass

class Asset(BankAccount, RealEstate, Security): pass

class InterestBearingItem(BankAccount, Security): pass