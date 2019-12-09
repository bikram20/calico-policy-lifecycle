#!/usr/bin/env python3

import yaml
from createpolicy import createcalicopolicy
from createnetworkset import createcaliconetworkset


def main():

    # basefilename for base YAML policy. policyfilename is the output
    datafile = "data.yaml"
    policyfilename = "./generatedcalicopolicy.yaml"
    
    # clean the policyfilename content
    open(policyfilename, 'w').close()
    
    # customvalues has the custom parameters. we will take one document at a time, rewrite the basepolicy, and then dump the base policy to policyfilename
    f_values = open(datafile)
    customvalues = yaml.safe_load_all(f_values)

    # here we do the actual work
    f_writefile = open(policyfilename, 'w')
    for value in customvalues:
        if value and (value['ObjectType'] == 'NetworkPolicy' or value['ObjectType'] == 'GlobalNetworkPolicy'):
            # TBD - validate inputs
            rewrittenpolicy = createcalicopolicy(value)
            yaml.safe_dump(rewrittenpolicy, f_writefile)
            f_writefile.write("\n---\n\n")
            #print(yaml.dump(rewrittenpolicy))
        if value and (value['ObjectType'] == 'GlobalNetworkSet'):
            # TBD - validate inputs
            rewrittennetworkset = createcaliconetworkset(value)
            yaml.safe_dump(rewrittennetworkset, f_writefile)
            f_writefile.write("\n---\n\n")
            #print(yaml.dump(rewrittennetworkset))

    
    
if __name__ == "__main__":
    main()
