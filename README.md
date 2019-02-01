# pyWSArchiPRO
Protocollazioni e recupero Documenti da WSArchiPRO con Python

## Installazione
````
pip install git+https://github.com/UniversitaDellaCalabria/pyWSArchiPRO
````

## Esempio di Protocollazione
````
from protocollo_ws.protocollo import Protocollo
wsclient = Protocollo(wsdl_url=PROT_URL,
                      username=PROT_LOGIN,
                      password=PROT_PASSW,
                      aoo=PROTOCOLLO_AOO,
                      anno=2018, numero=234234)
# recupera
wsclient.get()

# salva i files in locale
wsclient.dumpfiles()

# renderizza il documento che descrive il flusso di protocollazione (dataXML)
wsclient.render_dataXML()

````

## Esempio avanzato con generalizzazione classe in Django settings.py

In django settings.py
````
# quale classe utilizzare per instanziare un oggetto, può dunque essere customizzato
CLASSE_PROTOCOLLO = 'protocollo_ws.protocollo'

PROT_DOC_ENCODING = 'utf-8'
PROT_MAX_LABEL_LENGHT = 49
# most common oracle wildcard chars
PROT_UNALLOWED_CHARS = ['&', '(', ')', ',', '?', '!', '{', '}', '\\', '[', ']',
                        '-', ':', '~', '|', '$', '<', '>', '*', '%', '_', ';']

PROT_TEMPLATE_PATH = 'protocollo_ws/xml_templates'
CREAZIONE_FASCICOLO_XML_PATH = '{}/generalizzati/creazione_fascicolo_peo.xml'.format(PROT_TEMPLATE_PATH)
TEMPLATE_FLUSSO_ENTRATA_DIPENDENTE_PATH='{}/unical/peo_flusso_entrata.xml_precompilato.j2'.format(PROT_TEMPLATE_PATH)
ALLEGATO_EXAMPLE_FILE='{}/esempi/sample.pdf'.format(PROT_TEMPLATE_PATH)

# PROTOCOLLO, questi valori possono variare sulla base di come
# vengono istruite le pratiche all'interno del sistema di protocollo di riferimento
PROTOCOLLO_FASCICOLO_DEFAULT = '3'
PROTOCOLLO_TITOLARIO_DEFAULT = '9095'
PROTOCOLLO_CODICI_TITOLARI = (
                               ('9095','7.1'),
                             )

PROTOCOLLO_AOO = 'AOO1'

# PRODUCTION USE
PROT_URL = 'http://url/protservice?wsdl'
PROT_LOGIN = 'USERLOGIN'
PROT_PASSW = 'USERPASS'
````

#### Protocollare, esempio in Django
````
from django.conf import settings
from django.utils import timezone
from io import BytesIO

peo_dict = {'aoo': settings.PROTOCOLLO_AOO,
            'oggetto':'Partecipazione {} - {}'.format(bando, dipendente),
             # Variabili
            'matricola_dipendente': dipendente.matricola,
            'denominazione_persona': ' '.join((dipendente.nome,
                                               dipendente.cognome,)),

            # attributi creazione protocollo
            'id_titolario': bando.protocollo_cod_titolario, # settings.PROTOCOLLO_TITOLARIO_DEFAULT,
            'fascicolo_numero': bando.protocollo_fascicolo_numero, # settings.PROTOCOLLO_FASCICOLO_DEFAULT,
            'fascicolo_anno': timezone.localtime().year,

            'wsdl_url' : settings.PROT_URL,
            'username' : settings.PROT_LOGIN,
            'password' : settings.PROT_PASSW}

protclass = __import__(settings.CLASSE_PROTOCOLLO, globals(), locals(), ['*'])
wsclient = protclass.Protocollo(**peo_dict)

docPrinc = BytesIO()
docPrinc.write(download_domanda_pdf(request, bando_id, domanda_bando_id).content)
docPrinc.seek(0)
wsclient.aggiungi_docPrinc(docPrinc,
                           nome_doc="domanda_{}_{}.pdf".format(dipendente.matricola,
                                                               bando),
                           tipo_doc='Partecipazione {} - {}'.format(bando, dipendente))

for modulo in domanda_bando.modulodomandabando_set.all():
    allegato = BytesIO()
    allegato.write(download_modulo_inserito_pdf(request, bando_id, modulo.pk).content)
    allegato.seek(0)
    wsclient.aggiungi_allegato(nome="domanda_{}_{}-{}.pdf".format(dipendente.matricola,
                                                                  bando,
                                                                  modulo.pk),
                               descrizione='{} - {}'.format(modulo.descrizione_indicatore.id_code,
                                                            modulo.get_identificativo_veloce()),
                               fopen=allegato)
# print(wsclient.is_valid())
# print(wsclient.render_dataXML())
prot_resp = wsclient.protocolla()
````

## Scaricare tutte le domande protocollate relative ad un bando PEO
````
import datetime
import os

from django.conf import settings
from domande_peo.models import *
from gestione_peo.models import Bando
from protocollo_ws.protocollo import Protocollo


df = '%d/%m/%Y'
bando = Bando.objects.filter(slug='peo-2018').last()

auth_dict = {'wsdl_url' : settings.PROT_URL,
             'username' : settings.PROT_LOGIN,
             'password' : settings.PROT_PASSW,
             'aoo'      : settings.PROTOCOLLO_AOO}

ws_client = Protocollo(**auth_dict)

for i in DomandaBando.objects.filter(bando=bando):
    print(i)
    if not i.is_protocollata():
        print(i, 'non protocollata')
        continue
    ws_client.numero = i.numero_protocollo
    ws_client.anno = 2018
    destdir = '/tmp/peo-2018/{}'.format(i.dipendente.__str__().replace(' ', '_'))
    os.mkdir(destdir)
    ws_client.dump_files(destdir)
````

## test veloce
````
from pyWSArchiPRO.protocollo import test
test()
````
