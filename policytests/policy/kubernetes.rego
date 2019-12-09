package kubernetes

is_networkpolicy {
  input.kind = "NetworkPolicy"
}

is_globalnetworkpolicy_selector_all {
  input.kind = "GlobalNetworkPolicy"
  contains(input.spec.namespaceSelector, "all()")
}

is_globalnetworkset {
  input.kind = "GlobalNetworkSet"
}
