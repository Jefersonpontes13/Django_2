from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), min_length=5)

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n\nE-mail: {email}\n\nAssunto: {assunto}\n\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail de Contato - Django_2 System',
            body=conteudo,
            from_email='jeferson.dev.testes@gmail.com',
            to=['jeferson.dev.testes@gmail.com', ],
            headers={'Reply-To': email}
        )
        mail.send()
