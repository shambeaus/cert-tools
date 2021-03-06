import pprint

output = '''Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            01:e3:a9:30:1c:fc:72:06:38:3f:9a:53:1d
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: OU=GlobalSign Root CA - R2; O=GlobalSign; CN=GlobalSign
        Validity
            Not Before: Jun 15 00:00:42 2017 GMT
            Not After : Dec 15 00:00:42 2021 GMT
        Subject: C=US; O=Google Trust Services; CN=Google Internet Authority G3
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ca:52:4b:ea:1e:ff:ce:24:6b:a8:da:72:18:68:
                    d5:56:5d:0e:48:5a:2d:35:09:76:5a:cf:a4:c8:1c:
                    b1:a9:fe:53:89:fb:ad:34:ff:88:5b:9f:bb:e7:e8:
                    00:01:dc:35:73:75:03:ad:b3:b1:b9:a4:7d:2b:26:
                    79:ce:15:40:0a:ef:51:b8:9f:32:8c:7c:70:86:52:
                    4b:16:fe:6a:27:6b:e6:36:7a:62:50:d8:df:9a:89:
                    cc:09:29:eb:4f:29:14:88:80:0b:8f:38:1e:80:6a:
                    18:7c:1d:bd:97:3b:78:7d:45:49:36:4f:41:cd:a2:
                    e0:76:57:3c:68:31:79:64:c9:6e:d7:51:1e:66:c3:
                    a2:64:2c:79:c0:e7:65:c3:56:84:53:5a:43:6d:cb:
                    9a:02:20:d2:ef:1a:69:d1:b0:9d:73:a2:e0:2a:60:
                    65:50:31:cf:fb:b3:2f:bf:11:88:40:2e:b5:49:10:
                    0f:0a:6e:dc:97:fa:bf:2c:9f:05:39:0b:58:54:af:
                    06:96:e8:c5:8e:01:16:bc:a8:1a:4d:41:c5:93:91:
                    a2:1e:a1:8b:f2:fe:c1:88:24:49:a3:47:4b:c5:13:
                    01:dd:a7:57:12:69:62:2b:eb:fe:20:ef:69:fb:3a:
                    a5:f0:7e:29:ee:ed:96:16:f7:b1:1f:a0:e4:90:25:
                    e0:33
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature, Certificate Sign, CRL Sign
            X509v3 Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Subject Key Identifier:
                77:C2:B8:50:9A:67:76:76:B1:2D:C2:86:D0:83:A0:7E:A6:7E:BA:4B
            X509v3 Authority Key Identifier:
                keyid:9B:E2:07:57:67:1C:1E:C0:6A:06:DE:59:B4:9A:2D:DF:DC:19:86:2E

            Authority Information Access:
                OCSP - URI:http://ocsp.pki.goog/gsr2

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.pki.goog/gsr2/gsr2.crl

            X509v3 Certificate Policies:
                Policy: 2.23.140.1.2.2
                  CPS: https://pki.goog/repository/

    Signature Algorithm: sha256WithRSAEncryption
         1c:b7:89:96:e4:53:ed:bb:ec:db:a8:32:01:9f:2c:a3:cd:6d:
         ad:42:12:77:b3:b8:e6:c9:03:52:60:20:7b:57:27:c6:11:b5:
         3f:67:0d:99:2c:5b:5a:ca:22:0a:dd:9e:bb:1f:4b:48:3f:8f:
         02:3d:8b:21:84:45:1d:6d:f5:ff:ac:68:89:cd:64:e2:d6:d6:
         5e:40:c2:8e:2a:f7:ef:14:d3:36:a4:40:30:f5:32:15:15:92:
         76:fb:7e:9e:53:ea:c2:76:fc:39:ad:88:fe:66:92:26:e9:1c:
         c4:38:cd:49:fa:43:87:f0:5d:d6:56:4d:81:d7:7f:f1:c2:dd:
         b0:4d:fe:c3:2a:6e:7c:9f:6e:5c:ed:62:42:99:e1:f7:36:ee:
         14:8c:2c:20:e3:46:97:5a:77:03:c0:a0:c6:4a:88:fd:40:22:
         87:72:5a:18:ea:9c:a5:c7:5a:08:8c:e4:05:a4:7d:b9:84:35:
         5f:89:36:56:0e:40:3d:12:e8:bb:35:72:ed:af:08:56:4e:b0:
         bb:2e:a9:9b:e4:fb:1d:3e:0b:63:c8:9b:4b:91:44:66:57:c0:
         14:b4:96:f0:dc:2c:57:3f:52:04:ad:95:aa:7d:4d:d0:f2:0c:
         9f:9c:40:e8:d6:55:73:ba:3c:df:90:cb:00:5b:21:11:67:c2:
         ed:32:1e:de'''


def parse_cert_content(output):
    result = {}
    outputsplit = output.splitlines()

    for i, line in enumerate(outputsplit):
        if 'version' in line.lower():
            result['version'] = line.strip().split(' ')[1]
        if 'not before' in line.lower():
            result['start_date'] = line.strip()[12:]
        if 'not after' in line.lower():
            result['expire_date'] = line.strip()[12:]
        if 'serial number' in line.lower():
            result['serial'] = outputsplit[i + 1].strip()
    pprint.pprint(result)


parse_cert_content(output)
