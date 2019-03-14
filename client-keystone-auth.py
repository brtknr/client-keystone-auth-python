#!/usr/bin/env python
import openstack as sdk
import json
cloud = sdk.connect()
print(json.dumps({
        "apiVersion": "client.authentication.k8s.io/v1beta1",
        "kind": "ExecCredential",
        "status": {
                "token": cloud.auth_token,
                #"expirationTimestamp": "2019-03-14T13:00:16.525539Z"
        }
}, indent=4))
