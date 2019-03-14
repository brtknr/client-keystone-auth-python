# client-keystone-auth.py

Also includes a sample `.kubeconfig` file.

Ensure that you `export KUBECONFIG=~/.kubeconfig`.

## Python client

    $ time ./client-keystone-auth.py

    real    0m0.535s
    user    0m0.371s
    sys     0m0.085s

## Golang client

    $ time ./client-keystone-auth

    real    0m0.161s
    user    0m0.059s
    sys     0m0.014s
