# value contains policy parameters. createpolicy will generate a json and dump it as YAML
def createcalicopolicy(value):
    basepol = {}
    #basepol['apiVersion'] = 'projectcalico.org/v3'
    basepol['apiVersion'] = 'crd.projectcalico.org/v1'
    basepol['kind'] = value['ObjectType']


    basepol['metadata'] = {}
    basepol['metadata']['annotations'] = dict(source='Policy enforced by <REF> cybersecurity')
    basepol['metadata']['name'] = value['PolicyName']
    if value['ObjectType'] == 'NetworkPolicy':
        if value['PolicyNamespace'] != '':
            basepol['metadata']['namespace'] = value['PolicyNamespace']
   
    basepol['spec'] = {}

    if value['PolicyOrder'] != '': 
        basepol['spec']['order'] = value['PolicyOrder']

    if value['ObjectType'] == 'GlobalNetworkPolicy':
        if value['AppliesToNamespaceSelector'] != '':
            basepol['spec']['namespaceSelector'] = value['AppliesToNamespaceSelector']

    if value['AppliesToSelector'] != '':
        basepol['spec']['selector'] = value['AppliesToSelector']

    if value['AppliesToSvcActSelector'] != '':
        basepol['spec']['serviceAccountSelector'] = value['AppliesToSvcActSelector']
   
    if value['Direction'] != []:
        basepol['spec']['types'] = value['Direction']

    for direction in value['Direction']:
        if direction == 'Ingress' and value['INGRESS'] != None:
            basepol['spec']['ingress'] = [None] * len(value['INGRESS'])
            #print(basepol['spec']['ingress'])
            i=0
            while i < len(value['INGRESS']):
                basepol['spec']['ingress'][i] = {}
                basepol['spec']['ingress'][i]['source'] = {}
                basepol['spec']['ingress'][i]['destination'] = {}
                basepol['spec']['ingress'][i]['source']['serviceAccounts'] = {}
        
                if value['INGRESS'][i]['IngressAction'] != '':
                    basepol['spec']['ingress'][i]['action'] = value['INGRESS'][i]['IngressAction']
                if value['INGRESS'][i]['IngressSourceSelector'] != '':
                    basepol['spec']['ingress'][i]['source']['selector'] = value['INGRESS'][i]['IngressSourceSelector']
                if value['INGRESS'][i]['IngressSourceNamespace'] != '':
                    basepol['spec']['ingress'][i]['source']['namespaceSelector'] = value['INGRESS'][i]['IngressSourceNamespace']
                if value['INGRESS'][i]['IngressSourceServiceAccount'] != '':
                    basepol['spec']['ingress'][i]['source']['serviceAccounts']['selector'] = value['INGRESS'][i]['IngressSourceServiceAccount']
                if value['INGRESS'][i]['IngressPort'] != '':
                    basepol['spec']['ingress'][i]['destination']['ports'] = value['INGRESS'][i]['IngressPort']
                if value['INGRESS'][i]['IngressProtocol'] != '':
                    basepol['spec']['ingress'][i]['protocol'] = value['INGRESS'][i]['IngressProtocol']
                i=i+1
        
        if direction == 'Egress' and value['EGRESS'] != None:
            basepol['spec']['egress'] = [None] * len(value['EGRESS'])
            #print(basepol['spec']['egress'])
            i=0
            while i < len(value['EGRESS']):
                basepol['spec']['egress'][i] = {}
                basepol['spec']['egress'][i]['destination'] = {}
                basepol['spec']['egress'][i]['destination']['serviceAccounts'] = {}

                if value['EGRESS'][i]['EgressAction'] != '':
                    basepol['spec']['egress'][i]['action'] = value['EGRESS'][i]['EgressAction']
                if value['EGRESS'][i]['EgressDestinationSelector'] != '':
                    basepol['spec']['egress'][i]['destination']['selector'] = value['EGRESS'][i]['EgressDestinationSelector']
                if value['EGRESS'][i]['EgressDestinationNamespace'] != '':
                    basepol['spec']['egress'][i]['destination']['namespaceSelector'] = value['EGRESS'][i]['EgressDestinationNamespace']
                if value['EGRESS'][i]['EgressDestinationServiceAccount'] != '':
                    basepol['spec']['egress'][i]['destination']['serviceAccounts']['selector'] = value['EGRESS'][i]['EgressDestinationServiceAccount']
                if value['EGRESS'][i]['EgressPort'] != '':
                    basepol['spec']['egress'][i]['destination']['ports'] = value['EGRESS'][i]['EgressPort']
                if value['EGRESS'][i]['EgressProtocol'] != '':
                    basepol['spec']['egress'][i]['protocol'] = value['EGRESS'][i]['EgressProtocol']
                i=i+1

    return basepol

