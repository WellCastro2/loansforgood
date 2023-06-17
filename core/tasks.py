from celery import task

from core.models import Proposta
from core.services.loan import LoanProcessor


@task(name='check_loan')
def check_loan(id, document, name):

    approved = LoanProcessor.post_loan(document, name)

    obj = Proposta.objects.get(id=id)

    obj.status = Proposta.NEGADO if not approved else Proposta.ANALISE
    obj.finalizada = True if not approved else False
    obj.save()

    return True
