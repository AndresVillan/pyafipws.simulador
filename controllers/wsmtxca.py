# coding: utf8
# try something like
def index(): return dict(message="hello from wsmtxca.py")


from gluon.tools import Service
service = Service(globals())

@service.soap('dummy',
    returns={'dummyResponse' : {u'appserver': unicode, u'dbserver': unicode, u'authserver': unicode}}, 
    args={})
def dummy(): 
    "Metodo dummy para verificacion de funcionamiento"
    db.request.insert(method='dummy')
    return {u'appserver': 'OK', u'dbserver': 'OK', u'authserver': 'OK'}
 
@service.soap('FECAESolicitar',
    returns={'FECAESolicitarResult': {
        'FeCabResp': {'Cuit': long, 'PtoVta': int, 'CbteTipo': int, 
                      'FchProceso': str, 'CantReg': int, 'Resultado': unicode, 
                      'Reproceso': unicode}, 
        'FeDetResp': [{'FECAEDetResponse': 
            {'Concepto': int, 'DocTipo': int, 'DocNro': long, 
             'CbteDesde': long, 'CbteHasta': long, 'CbteFch': unicode, 
             'CAE': str, 'CAEFchVto': str,
             'Resultado': str, 
             'Observaciones': [{'Obs': {'Code': int, 'Msg': unicode}}]}}], 
         'Events': [{'Evt': {'Code': int, 'Msg': unicode}}], 
         'Errors': [{'Err': {'Code': int, 'Msg': unicode}}]}},
    args={
        'Auth': {'Token': str, 'Sign': str, 'Cuit': str},
        'FeCAEReq': {
            'FeCabReq': {'CantReg': int, 'PtoVta': int, 'CbteTipo': int},
            'FeDetReq': [{'FECAEDetRequest': {
                'Concepto': int,
                'DocTipo': int,
                'DocNro': long,
                'CbteDesde': long,
                'CbteHasta': long,
                'CbteFch': str,
                'ImpTotal': float,
                'ImpTotConc': float,
                'ImpNeto': float,
                'ImpOpEx': float,
                'ImpTrib':  float,
                'ImpIVA': float,
                'FchServDesde': str,
                'FchServHasta': str,
                'FchVtoPago': str,
                'MonId': str,
                'MonCotiz': float,
                'CbtesAsoc': [
                {'CbteAsoc': {'Tipo': int, 'PtoVta': int, 'Nro': long}}
                ],
                'Tributos': [
                {'Tributo': {
                    'Id': int, 
                    'Desc': unicode,
                    'BaseImp': float,
                    'Alic': float,
                    'Importe': float,
                    }}
                ],
                'Iva': [ 
                {'AlicIva': {
                    'Id': int,
                    'BaseImp': float,
                    'Importe': float,
                    }}
                ],
                }
            }]
        }})
def cae_solicitar(Auth, FeCAEReq): 
    "Solicitud de Codigo de Autorizacion Electronico (CAE)"
    FeCabReq = FeCAEReq['FeCabReq']
    FeDetReq = FeCAEReq['FeDetReq']
    db.request.insert(method='cae_solicitar', args=repr({'Auth': Auth, 'FeCAEReq': FeCAEReq}))
    return {
        'FeCabResp': {'Cuit': Auth['Cuit'], 
                      'PtoVta': FeCabReq['PtoVta'], 'CbteTipo': FeCabReq['CbteTipo'], 
                      'CantReg': FeCabReq['CantReg'], 
                      'FchProceso': "20101006", 
                      'Resultado': "A", 
                      'Reproceso': "N"}, 
        'FeDetResp': [{'FECAEDetResponse': 
            {'Concepto': f['FECAEDetRequest']['Concepto'], 
             'DocTipo': f['FECAEDetRequest']['DocTipo'], 'DocNro': f['FECAEDetRequest']['DocNro'], 
             'CbteDesde': f['FECAEDetRequest']['CbteDesde'], 'CbteHasta': f['FECAEDetRequest']['CbteHasta'], 
             'CAE': "123456789012345",
             'CbteFch': f['FECAEDetRequest']['CbteFch'], 
             'CAEFchVto': f['FECAEDetRequest']['CbteFch'], 
             'Resultado': "A", 
             'Observaciones': [{'Obs': {'Code': 00, 'Msg': "Todo bien"}}]}} 
                  for f in FeDetReq], 
         'Events': [{'Evt': {'Code': 0, 'Msg': 'Esto es una SIMULACION!!!'}}], 
         'Errors': [{'Err': {'Code': 10001, 'Msg': 'Datos no validos - simulados'}}]}

def call():
    response.title = u"Simulador Factura Electronica"
    response.subtitle = u"Simil Servicios Web AFIP Argentina"
    return service()
