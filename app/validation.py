from datetime import datetime, timedelta


class CreditCardValidator:
    @staticmethod
    def is_valid_exp_date(exp_date):
        try:
            exp_date = datetime.strptime(exp_date, "%m/%Y")
            return exp_date >= datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            return False

    @staticmethod
    def is_valid_holder(holder):
        return len(holder) > 2

    @staticmethod
    def is_valid_card_number(number):
        from creditcard import CreditCard
        cc = CreditCard(number)
        cc.is_valid()

    @staticmethod
    def is_valid_cvv(cvv):
        return cvv.isdigit() and 3 <= len(cvv) <= 4

    @staticmethod
    def format_exp_date(exp_date):
        try:
            exp_date = datetime.strptime(exp_date, "%m/%Y")
            last_day_of_month = (exp_date.replace(day=1, month=exp_date.month % 12 + 1,
                                                  year=exp_date.year + exp_date.month // 12) - timedelta(days=1)).day
            return exp_date.strftime("%Y-%m-") + str(last_day_of_month)
        except ValueError:
            return None
