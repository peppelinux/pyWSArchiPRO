Flusso con Persona e non Dipendente

```
# XML flusso
PROTOCOL_XML = """<Segnatura xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<Intestazione>
<Oggetto>{oggetto}</Oggetto>
<Identificatore>
<CodiceAmministrazione>UNICAL</CodiceAmministrazione>
<CodiceAOO>{aoo}</CodiceAOO>
<Flusso>E</Flusso>
</Identificatore>
<Mittente>

<Dipendente id="{matricola_dipendente}">
<Denominazione>{denominazione_persona}</Denominazione>
</Dipendente>

<Studente id="{matricola_studente}">
<Denominazione>{denominazione_persona}</Denominazione>
</Studente>

<Persona id="{id_persona}">
<Nome>{nome_persona}</Nome>
<Cognome>{cognome_persona}</Cognome>
<Denominazione>{denominazione_persona}</Denominazione>
</Persona>

</Mittente>
<Destinatario>
<Amministrazione>
<Denominazione>UNICAL</Denominazione>
<CodiceAmministrazione>UNICAL</CodiceAmministrazione>
<IndirizzoTelematico tipo="smtp">amministrazione@pec.unical.it</IndirizzoTelematico>
<UnitaOrganizzativa id="{uo_id}"/>
</Amministrazione>
</Destinatario>
<Classifica>
<CodiceTitolario>{id_titolario}</CodiceTitolario>
</Classifica>
<!--  Informazioni sul fascicolo  -->
<Fascicolo numero="{fascicolo_numero}" anno="{fascicolo_anno}"/>
</Intestazione>
<Descrizione>
<Documento id="1" nome="{nome_doc}">
<DescrizioneDocumento>{nome_doc}</DescrizioneDocumento>
<TipoDocumento>{tipo_doc}</TipoDocumento>
</Documento>
<Allegati>
<!-- Allegati -->
</Allegati>
</Descrizione>
<ApplicativoProtocollo nome="ArchiPRO">
<Parametro nome="agd" valore="{agd}"/>
<Parametro nome="uo" valore="{uo}"/>
</ApplicativoProtocollo>
</Segnatura>
```

Adotteremmo sempre {id_persona} anche per Dipendente e Studente.
Faremmo come per gli allegati un template da inserire in base al tipo, purtroppo non basta generalizzare con {id_persona} perchè i tag xml sono differenti.

````
<Mittente>

<Dipendente id="{matricola_dipendente}">
<Denominazione>{denominazione_persona}</Denominazione>
</Dipendente>

<Studente id="{matricola_studente}">
<Denominazione>{denominazione_persona}</Denominazione>
</Studente>

<Persona id="{id_persona}">
<Nome>{nome_persona}</Nome>
<Cognome>{cognome_persona}</Cognome>
<Denominazione>{denominazione_persona}</Denominazione>
</Persona>

</Mittente>
````
