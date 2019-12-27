# calico-policy-lifecycle

![](https://github.com/bikram20/calico-policy-lifecycle/workflows/Validate/badge.svg?branch=team1)
[![Build Status](https://travis-ci.org/bikram20/calico-policy-lifecycle.svg?branch=master)](https://travis-ci.org/bikram20/calico-policy-lifecycle)

https://medium.com/@bikramgupta/in-part-1-of-gitops-series-we-reviewed-the-need-for-using-gitops-for-calico-policies-and-how-to-660aa6b5e4c9


![Flow Diagram](flowchart.jpeg?raw=true)

# To use the scripts
- Use policygenerator script for generating calico network policies from metadata.
- Copy over the generated policy under policytests folder. Run your policy governance checks in CI. The example here uses Github Actions.
