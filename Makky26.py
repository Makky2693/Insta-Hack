import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))