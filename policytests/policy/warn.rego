package main

import data.kubernetes


name = input.metadata.name

warn[msg] {
  kubernetes.is_globalnetworkset
  msg = sprintf("You should use networkset for %s. Globalnetworkset is meant to be used for cluster wide resources.", [name])
}
