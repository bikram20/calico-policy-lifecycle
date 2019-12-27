#!/usr/bin/env python3

import sys
import click
import yaml
import logging
import click_log

from policy_generator.validateinput import validate_input_networkpolicy, validate_input_networkset
from policy_generator.createpolicy import create_calico_policy
from policy_generator.createnetworkset import create_calico_networkset

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

@click.command()
@click.option('-i', '--policydata', help='Path to the file containing policy meta information.')
@click.option('-o', '--outputfile', default='generatedpolicy.yaml', 
              help='Output filename to write the YAML policy into. Existing file will be overwritten! Default is generatedpolicy.yaml')
@click_log.simple_verbosity_option(logger)
def generate_calico_policy(policydata, outputfile):

    # validate metadata file for reading
    try:
        customvalues = yaml.safe_load_all(open(policydata))
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to open file, exiting. Please make sure to provide a valid policy data file.'
                        'Use --help for argument information')
    
    # clean the policyfilename content as you open for writing
    try:
        f_writefile = open(outputfile, 'w')
    except Exception as e:
        logger.error(e)
        raise Exception('Unable to write to file, exiting. Please make sure to provide a valid policy outfile.')

    logger.info("Reading from %s and will write the policy into %s" % (policydata, outputfile))

    for value in customvalues:
        if value and (value['ObjectType'] == 'NetworkPolicy' or value['ObjectType'] == 'GlobalNetworkPolicy'):
            if not validate_input_networkpolicy(value): raise Exception("Invalid input format. Value provided: %s" % value)
            rewrittenpolicy = create_calico_policy(value)
            yaml.safe_dump(rewrittenpolicy, f_writefile)
            f_writefile.write("\n---\n\n")
            logger.debug(yaml.dump(rewrittenpolicy))
        if value and (value['ObjectType'] == 'GlobalNetworkSet'):
            if not validate_input_networkset(value): raise Exception("Invalid input format. Value provided: %s" % value)
            rewrittennetworkset = create_calico_networkset(value)
            yaml.safe_dump(rewrittennetworkset, f_writefile)
            f_writefile.write("\n---\n\n")
            logger.debug(yaml.dump(rewrittennetworkset))
        logger.debug(value)
    
    logger.info("Generated calico policy written into file %s" % (outputfile))

def main(args=None):
    return generate_calico_policy()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
