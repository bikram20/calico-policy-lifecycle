package main

import data.kubernetes

name = input.metadata.name

deny[msg] {
  kubernetes.is_networkpolicy
  not input.spec.order > 500

  msg = sprintf("You must specify an order number > 500 for your networkpolicy  %s", [name])
}

deny[msg] {
  kubernetes.is_globalnetworkpolicy_selector_all

  msg = sprintf("You are trying to apply a policy cluster-wide and not allowed to do so. Please use networkpolicy for %s", [name])
}
