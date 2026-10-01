from ps4b import Message, PlaintextMessage, EncryptedMessage

test = PlaintextMessage("This test!")
print(test.apply_pad([1,-4,0,15,0,2,2,-20,-100,-300]))


print(test.generate_pad())

test2 = EncryptedMessage("?hjK4")
print(test2.decrypt_message([1,1,1,1,1]))







