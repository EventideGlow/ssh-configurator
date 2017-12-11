# ssh-configurator



### Tests
Our tests test for the following:
1. Ability to provision based off a local yaml with no changes [test-basic-runs]
2. Ability to configure a server from a remote source [test-remote-source]
3. Ability to correctly reject an unauthenticated remote source [test-http-disallowed]
4. Ability to atomically modify an existing configuration [test-modify-existing]
5. Ability to configure a server from a remote source on server startup [test-remote-source]
6. Ability to remove keys when the remote source no longer specifies the keys’ presence on the server [test-modify-existing]