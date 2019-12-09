def createcaliconetworkset(value):
   
    baseset = {}

    baseset['apiVersion'] = 'projectcalico.org/v3'
    baseset['kind'] = value['ObjectType']
    baseset['metadata'] = {}
    baseset['metadata']['annotations'] = dict(source='Policy auto-generated by <REF>')
    baseset['metadata']['name'] = value['NetworkSetName']

    baseset['metadata']['labels'] = value['Labels']
   
    baseset['spec'] = {}

    if 'CIDR' in value.keys():
        baseset['spec']['nets'] = value['CIDR']
    if 'Domains' in value.keys():
        baseset['spec']['allowedEgressDomains'] = value['Domains']

    return baseset

