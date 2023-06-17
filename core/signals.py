from django.db.models.signals import post_save
from django.dispatch import receiver
from core.tasks import check_loan
from core.models import Proposta


@receiver(post_save, sender=Proposta)
def check(sender, instance=None, **kwargs):

    # check is first save obj
    if kwargs['created']:
        # send task check
        check_loan.s(
            instance.id,
            instance.cpf,
            instance.nome
        ).apply_async(countdown=0.2)
