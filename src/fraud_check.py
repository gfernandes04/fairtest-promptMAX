def fraud_check(user):
    if user.country != "Brazil":
        return True  
    return False

