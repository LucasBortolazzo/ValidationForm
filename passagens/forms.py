from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classes
from passagens.validacao import *
import collections
from passagens.models import *

class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)                

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe da viagem', 
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

        #data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)                

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')

        lista_de_erros = collections.defaultdict(list)

        validar_numero('origem', origem, lista_de_erros)
        validar_numero('destino', destino, lista_de_erros)
        validar_origem_destino_iguais('origem', origem, destino, lista_de_erros)

        for key, value in lista_de_erros.items():
            for item in value:      
                print(f'campo: {key} validação: { item }')          
                self.add_error(key, item)

        return self.cleaned_data   

class Pessoaform(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']

                            
 