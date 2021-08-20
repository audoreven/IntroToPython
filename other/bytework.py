import base64

TRANSACTION_BYTE_COUNT = 10
TRANSACTION_BYTE_PADDING = b''.join([b'0']*TRANSACTION_BYTE_COUNT)

# sequenceNumber = bytearray(b'')
# transactionId = bytearray(b'')


def function(sequenceNumber, transactionId) -> bytearray:
    """
    creating byte array joining transaction id with sequence number with padding
    :return: transaction and sequence number with padding
    """
    padding = TRANSACTION_BYTE_COUNT - len(transactionId)
    bytearr = TRANSACTION_BYTE_PADDING[:padding] if padding > 0 else bytearray(b'')

    # join the arrays
    return b''.join([bytearr, transactionId, sequenceNumber])


def func(seq_num: int, trans_id: str) -> bytearray:
    transactionId = bytes(trans_id.split(".")[-1].encode('utf-8'))

    padding = TRANSACTION_BYTE_COUNT - len(transactionId)
    bytearr = TRANSACTION_BYTE_PADDING[:padding] if padding > 0 else bytearray(b'')

    return b''.join([bytearr, transactionId, seq_num.to_bytes(5, 'big')])


def decode(string) -> bytes:
    return base64.b64decode(string.encode('utf-8'))

#sequenceNumber.append(48)
"""
sequenceNumber.append(53)
sequenceNumber.append(69)
sequenceNumber.append(55)
sequenceNumber.append(84)
sequenceNumber.append(65)
sequenceNumber.append(89)
sequenceNumber.append(48)
"""
# sequenceNumber = bytearray([53, 69, 55, 84, 65, 89, 48])
# transactionId.append(86)
# transactionId.append(86)
test = bytearray(b'00V5E7TAY0')

encoded_str = base64.b64encode(test).decode('utf-8')

print(encoded_str)

test1_tid = decode("AABk+wAGxYcASA==")
test1_sn = decode("AABk+wAGxccArQ==")

test2_tid = decode("AABk+wAGyhMAhw==")
test2_sn = decode("AABk+wAGyosAOg==")

test3_tid = decode("AABk+wAGyhMAiQ==")
test3_sn = decode("AABk+wAGyosAOg==")

print(test3_tid)
print(test3_sn)

test2_res = function(test2_tid, test2_sn)
test3_res = function(test3_tid, test3_sn)

print("Test Data 1: ", function(test1_tid, test1_sn))

print("Test Data 2: ", test2_res)

print("Test Data 3: ", test3_res)

print(test3_res < test2_res)


# bytesarray = function()
seq = 1168140

print(func(seq, "000020"))
print(func(seq, "000020") > func(10000000, "000020"))


"""

1
"__$seqval": "AABk+wAGxYcASA==",
"__$start_lsn": "AABk+wAGxccArQ==",

2
"__$seqval": "AABk+wAGyhMAhw==",
"__$start_lsn": "AABk+wAGyosAOg==",

3
"__$seqval": "AABk+wAGyhMAiQ==",
"__$start_lsn": "AABk+wAGyosAOg==",

4
"__$seqval": "AABk+wAA2X4AEw==",
"__$start_lsn": "AABk+wAA2X4AaA==",

"""

