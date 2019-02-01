# win-chrk4d7tc85 must be resolved in /etc/hosts or DNS
PROT_DOC_ENCODING = 'utf-8'
PROT_MAX_LABEL_LENGHT = 49
# most common oracle wildcard chars
PROT_UNALLOWED_CHARS = ['&', '(', ')', ',', '?', '!', '{', '}', '\\', '[', ']',
                        '-', ':', '~', '|', '$', '<', '>', '*', '%', '_', ';']

PROT_TEMPLATE_PATH = 'protocollo_ws/xml_templates'
CREAZIONE_FASCICOLO_XML_PATH = '{}/generalizzati/creazione_fascicolo_peo.xml'.format(PROT_TEMPLATE_PATH)
TEMPLATE_FLUSSO_ENTRATA_DIPENDENTE_PATH='{}/unical/peo_flusso_entrata.xml_precompilato.j2'.format(PROT_TEMPLATE_PATH)
ALLEGATO_EXAMPLE_FILE='{}/esempi/sample.pdf'.format(PROT_TEMPLATE_PATH)

# Flusso entrata per dipendenti
# mittente persona fisica come dipendente, destinatario Unical
parametri_ws_archipro_tmpl = '<Parametro nome="{nome}" valore="{valore}" />'
# parametri_ws_archipro = [{'nome': 'agd', 'valore': '483'},
                         # {'nome': 'uo', 'valore': '1231'}]

# PROTOCOLLO, questi valori possono variare sulla base di come
# vengono istruite le pratiche all'interno del sistema di protocollo di riferimento
PROTOCOLLO_FASCICOLO_DEFAULT = '3'
PROTOCOLLO_TITOLARIO_DEFAULT = '9095'
PROTOCOLLO_CODICI_TITOLARI = (
                               ('9095','7.1'),
                             )

PROTOCOLLO_AOO = 'AOO55' # test
# PROTOCOLLO_AOO = 'AOO1' # produzione

# PRODUCTION USE
PROT_URL = 'http://PROT_URL?wsdl'
PROT_LOGIN = 'UT_PROTO_WS'
PROT_PASSW = 'UT_PROTO_WS'

# TEST USE
PROT_URL = 'http://PROT_URL?wsdl'
PROT_LOGIN = 'UT_PROTO_WS'
PROT_PASSW = 'UT_PROTO_WS'
