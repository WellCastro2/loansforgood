import requests


class LoanProcessor:
    """
    Classe responsável por enviar solicitações de empréstimo para o serviço.

    Methods:
        post_loan(document, name):
            Envia uma solicitação POST para a URL de processamento de empréstimo,
            preenchendo os campos "document" e "name" com os valores fornecidos.

            Args:
                document (str): Número do documento do cliente.
                name (str): Nome do cliente.
    """
    @staticmethod
    def post_loan(document, name):
        url = 'https://loan-processor.digitalsys.com.br/api/v1/loan/'

        data = {
            'document': document,
            'name': name
        }

        response = requests.post(url, data=data)
        response_data = response.json()

        return response_data.get('approved')
