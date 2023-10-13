from discord_BaseCase import discord_BaseCase

class TestAddMonthlyBudget(discord_BaseCase):
    def test_add_monthly_budget_valid(self):
        """
        Asserts when add_monthly_budget is given a float value
        """
        assert self.user.monthly_budget == 0
        amount = 10.00
        self.user.add_monthly_budget(amount, 2)
        assert self.user.monthly_budget == amount

    def test_add_monthly_budget_invalid(self):
        """
        Asserts when add_monthly_budget is given 0
        """
        assert self.user.monthly_budget == 0
        amount_valid = 10.00
        self.user.add_monthly_budget(amount_valid, 2)
        assert self.user.monthly_budget == amount_valid
        amount = 0.00
        self.user.add_monthly_budget(amount, 2)
        assert self.user.monthly_budget == amount_valid
