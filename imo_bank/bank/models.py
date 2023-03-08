from django.db import models
from .constants import TRANSACTION_TYPE, DEPOSIT, TRANSFER, WITHDRAW
from user.models import User

class Account(models.Model):
    account_no = models.PositiveIntegerField(unique=True)
    user = models.OneToOneField(User, verbose_name="usuario", on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    initial_deposit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.account_no)
    
    def transaction(self, type, t_ammount, target=None,):
        if type == DEPOSIT:
            transaction = Transaction.objects.create(
                account=self,
                ammount=t_ammount,
                balance_after_transaction=self.balance+t_ammount,
                transaction_type=TRANSACTION_TYPE[0] 
            )
            transaction.save()
            self.balance += t_ammount
            self.save()
        
        elif type == WITHDRAW:
            transaction = Transaction.objects.create(
                account=self,
                ammount=t_ammount,
                balance_after_transaction=self.balance - t_ammount,
                transaction_type=TRANSACTION_TYPE[1] 
            )
            transaction.save()
            self.balance -= t_ammount
            self.save()

        elif type == TRANSFER:
            # current user
            transaction = Transaction.objects.create(
                account=self,
                ammount=t_ammount,
                balance_after_transaction=self.balance - t_ammount,
                transaction_type=TRANSACTION_TYPE[1] 
            )
            transaction.save()
            self.balance -= t_ammount
            self.save()

            # Target user
            target_user = Account.objects.get(account_no=target)
            transfer = Transaction.objects.create(
                account=target,
                ammount=t_ammount,
                balance_after_transaction=self.balance+t_ammount,
                transaction_type=TRANSACTION_TYPE[0] 
            )
            transfer.save()
            target.balance += t_ammount
            target.save()

        else:
            return 'Tipo de transação inválida'
        
        return transaction

class Transaction(models.Model):
    account = models.ForeignKey(
        Account,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.account_no)

    class Meta:
        ordering = ['timestamp']