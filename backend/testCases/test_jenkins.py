def test_jenkins():
    import jenkins

    server = jenkins.Jenkins('http://192.168.202.128', username="admin", password="1126197eb07ec9dbcc354a41d4abb943a9")
    print(server.build_job("cekai17"))